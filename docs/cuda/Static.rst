
.. _Static Inversion:

Static Slip Inversion
======================

Static Source model
-------------------

The finite fault earthquake source models infer the spatial distribution and temporal evolution of coseismic slips at fault plane(s) from the observed surface or subsurface displacements. In the static source model, the spatial distributions of coseismic slips are determined. We model the fault plane(s) as a set of patches; each patch treated as a point source with two orthogonal displacement components, slips along the strike and dip directions. Each slip on the fault plane can be translated into surface deformation, e.g., by the Okada model, which is derived from a Green’s function solution to the elastic half space problem. The observed surface deformation at a given location is the linear combination due to (strike/dip) slips of all patches.

.. note::

   For the static inversion, the patches can be of any shape or area as long as each patch can be treated a single point source. If you plan for a joint static-kinematic inversion, note that the currently implemented kinematic inversion only processes a rectangle fault divided into :math:`n_d \times n_s` square patches.

Therefore, the forward model is a linear model

.. math::

   {\bf d}^{pred} = \mathcal{G}  {\boldsymbol \theta}.

where :math:`{\boldsymbol \theta}` (also denoted as :math:`{\bf m}` in literature) is a vector with :math:`N_{parameters}=2N_{patch}` components, representing the slips along the strike and dip directions for :math:`N_{patch}`-patches; :math:`{\bf d}` is a vector of observed surface deformations (may include vertical and east,north horizontal components) at different locations, with :math:`N_{observation}`-observations; and  :math:`\mathcal{G}` is :math:`2N_{patch} \times N_{observation}` matrix, pre-calculated Green's functions connecting a slip source to an observation location.

A generalized forward model could also include other linear parameters, for example, the InSAR ramp parameters :math:`(a, b, c)`, used to fit the spurious ramp-like displacement fields :math:`a+bx+cy` from InSAR interferograms, where :math:`x` and :math:`y` are the locations of the data in local Cartesian coordinates.


Input files
-----------

For the static inversion, you are required to prepare three input files

* ``data.txt``, the observed data with :math:`N_{observation}` observations, a vector in one row or one column.
* ``cd.txt``, covariance of data representing data errors/uncertainties, prepared in a :math:`N_{observation} \times N_{observation}` matrix (could have off-diagonal terms for correlated errors).  A constant cd could be used if all data are uncorrelated and have the same variance.
* ``green.txt``, the pre-calculated Green's functions, prepared in a :math:`N_{observation} \times N_{parameters}` matrix, with :math:`N_{parameters}` as the leading dimension, i.e., data arranged in row-major as

.. code-block:: none

    Obs1Param1, Obs1Param2, ... Obs1ParamNp
    Obs2Param2, Obs2Param2, ... Obs2ParamNp
    ... ...
    ObsNoParam1, ObsNoParam2, ... ObsNoParamNp

You may use any names for these files but need to specify them in the configuration file.

In addition to plain text inputs, ``.txt``, AlTar 2.0 also accepts binary data format ``.bin``, ``.dat`` or HDF5 files (with suffix ``.h5``). For the raw binary data, the precision should be consistent with the numerical precision desired ``job.gpuprecision``, or otherwise be specified. HDF5 files include the data shape and precision in metadata, which can be easily recognized and automatically converted by AlTar.

There are some software packages which can pre-calculate the Green's functions and/or prepare the input files for AlTar, e.g., `CSI <http://www.geologie.ens.fr/~jolivet/csi/>`__. Please refer to its manual and tutorials for more details.


.. _HDF5 Converter:

HDF5 Converter tool
-------------------

We recommend HDF5 as the input format. A conversion tool ``H5Converter`` is provided if you need to convert any ``.txt`` or ``.bin`` files (e.g., from AlTar 1.1) to ``.h5``.

:Examples:

Convert a text file to hdf5

.. code-block:: bash

    H5Converter --inputs=static.gf.txt

Convert a binary file to hdf5, additional information such as the precision (default=float32) and the shape (default = 1d vector and will be reshaped to 2d in program if needed) of the output can be added by

.. code-block:: bash

    H5Converter --inputs=kinematicG.gf.bin --precision='float32' --shape=[100,11000]

Merge several files into one hdf5, e.g., to prepare the sensitivity kernels for Cp,

.. code-block:: bash

    H5Converter --inputs=[static.kernel.pertL1.txt,static.kernel.pertL2.txt] --output=static.kernel.h5

For help on all available options

.. code-block:: bash

    H5Converter --help


Configurations
--------------

The configuration file for the static inversion appears as

.. code-block :: none

    ; application instance name
    slipmodel:

        ; model to be sampled
        model = altar.models.seismic.cuda.static
        model:

            ; the name of the test case
            case = 9patch

            ; number of patches
            patches = 9

            ; green's function (observations, parameters)
            green = static.gf.h5

            dataobs = altar.cuda.data.datal2
            dataobs:
                observations = 108
                data_file = static.data.h5
                cd_file = static.Cd.h5

            ; list of parametersets
            ; the order should be consistent with the green's function
            psets_list = [strikeslip, dipslip]

            ; define parametersets
            psets:
                strikeslip = altar.cuda.models.parameterset
                dipslip = altar.cuda.models.parameterset

                strikeslip:
                    count = {slipmodel.model.patches}
                    prior = altar.cuda.distributions.gaussian
                    prior.mean = 0
                    prior.sigma = 0.5

                dipslip:
                    count = {slipmodel.model.patches}
                    prep = altar.models.seismic.cuda.moment
                    prep:
                        Mw_mean = 7.3
                        Mw_sigma = 0.2
                        Mu = [30] ; in GPa
                        area = [400] ; patch area in km^2
                    prior = altar.cuda.distributions.uniform
                    prior.support = (-0.5, 20)

        controller:
            sampler = altar.cuda.bayesian.metropolis
            archiver:
                output_dir = results/static ; output directory
                output_freq = 3 ; output frequency in beta steps


        ; run configuration
        job:
            tasks = 1 ; number of tasks per host
            gpus = 1  ; number of gpus per task
            gpuprecision = float32 ; double(float64) or single(float32) precision for gpu computations
            ;gpuids = [0] ; a list gpu device ids for tasks on each host, default range(job.gpus)
            chains = 2**10 ; number of chains per task
            steps = 1000 ; MC burn-in steps for each beta step

We explain each section below.

Application Instance Name
~~~~~~~~~~~~~~~~~~~~~~~~~~

We use a shell command ``slipmodel`` for all seismic slip models, including static and kinematic inversions, which uses ``slipmodel`` as the application instance name. Therefore, please use ``slipmodel`` as the root in the configuration file. By the pyre_ convention, the shell command searches and loads configurations from the file ``slipmodel.pfg`` in current path. If you name your configuration file as ``slipmodel.pfg``,  you may simply run

.. code-block:: bash

    $ slipmodel

to invoke simulations for any slip models.  If you want to name the configuration file as something else, e.g., ``static.pfg``, ``static_mpi.pfg``, or ``Nepal_static.pfg``, you may specify the configuration file from the command line by the ``--config`` option,

.. code-block:: bash

    $ slipmodel  --config=static.pfg


Model
~~~~~~

For static inversion, you need to specify ``model = altar.models.seismic.cuda.static`` (or the CPU version, ``model=altar.models.seismic.static``).

:Attributes:

* ``case``, the directory where all input files are located;
* ``patches``, the number of patches, or point sources;
* ``green``, the file name for the Green's functions, as prepared from the instructions above;
* ``dataobs = altar.cuda.data.datal2``, a component to process the data observations and calculate the data likelihood with L2 norm, with details provided in :ref:`Data Observations`;
* ``psets_list``, and ``psets``, components to describe the parameter sets, with details provided in :ref:`Parameter Sets`.

.. _Data Observations:

Data Observations
~~~~~~~~~~~~~~~~~~

The observed data are handled by a component named ``dataobs``. We use exclusively the L2 norm for the likelihood computation because it accommodates the uncertainty quantification from the data covariance matrix (Cd). Therefore,

.. code-block:: none

    dataobs = altar.cuda.data.datal2
    dataobs:
        observations = 108
        data_file = static.data.h5
        cd_file = static.Cd.h5
        ; cd_std = 1e-2

For the data observations with the data covariance matrix ``datal2``, the following attributes are required

* ``observations``, the number of data observations
* ``data_file``, the name of the file containing the data observations, a vector with ``observations`` elements
* ``cd_file``, the name of the file containing the data covariance,  a matrix with ``observations x observations`` elements
* ``cd_std``, if the data covariance has only constant diagonal elements, you may use this option instead of ``cd_file``.


.. _Parameter Sets:

Parameter Sets
~~~~~~~~~~~~~~~

A parameter set is a group of parameters which share the same prior distributions and are arranged continuously in :math:`{\boldsymbol \theta}`. In static model, we use the following parameter sets ``strikeslip``, ``dipslip``, and optionally, ``ramp`` (you may use any other names for the parameter sets as long as they are intuitive).

The order of the parameter sets in :math:`{\boldsymbol \theta}` is enforced by the attribute ``psets_list``,

.. code-block:: none

    psets_list = [strikeslip, dipslip, ramp]

If the number of patches is 9 and there are 3 InSAR ramp parameters for one set of interferograms. The 21 parameters in
:math:`{\boldsymbol \theta}` are (0-8), strike slips of 9 patches; (9-17), dip slipd of 9 patches; and (18-20), ramp parameters. The order of the parameter sets can be varied, but has to be consistent with that in the Green's function matrix.

:Attributes:

* ``count`` the number of parameters in this set,
* ``prior``, the prior distribution to initialize random samples in the beginning, and compute prior probabilities during the sampling process. See :ref:`Prior Distributions` for choices of priors.
* ``prep`` (optional), a distribution to initialize samples only, while ``prior`` is still used for computing prior probabilities.

:Example:

For dip-slip faults, you may use a ``uniform`` prior to limit the range of dip slips while using a :ref:`Moment Distribution` to initialize samples so that the moment magnitude is consistent with an estimate scale :math:`M_w`.

.. code-block:: none

        dipslip = altar.cuda.models.parameterset
        dipslip:
            count = {slipmodel.model.patches}
            prep = altar.models.seismic.cuda.moment
            prep:
                Mw_mean = 7.3 ; mean moment magnitude scale
                Mw_sigma = 0.2 ; sd for moment magnitude scale
                Mu = 30 ; in GPa
                area = 400 ; patch area in km^2
            prior = altar.cuda.distributions.uniform
            prior:
                support = (-0.5, 20)

Meanwhile, a Gaussian distribution centered at 0 may be used for strike slips

.. code-block:: none

        strikeslip = altar.cuda.models.parameterset
        strikeslip:
            count = {cudastatic.model.patches}
            prior = altar.cuda.distributions.gaussian ; we only need to say gaussian after gpu/cpu code are merged
            prior:
                mean = 0
                sigma = 0.5

since the same ``prior`` is also used to initialize samples, no ``prep`` is needed.

For InSAR ramps, either a uniform or a Gaussian prior can be used

.. code-block:: none

        ramp = altar.cuda.models.parameterset
        ramp:
            count = 3
            prior = altar.cuda.distributions.uniform
            prior.support = (-0.5, 0.5)

If you prefer to use different priors for different patches, for example, to limit the range of slips far away from the hypocenter, you can further divide the strikeslip/dipslip into several parameter sets, such as

.. code-block:: none

    psets_list = [strikeslip_p1-3, strikeslip_p4-6, strikeslip_p7-9, ...]


.. _Moment Distribution:

Moment Distribution
~~~~~~~~~~~~~~~~~~~~

For strike (dip) faults, we may want the generated seismic moment from all strike (dip) slips to be consistent with the estimated moment magnitude scale :math:`M_w`,

.. math::

    M_w = (\log M_0 -9.1)/1.5

:math:`M_0` is the scalar seismic moment, defined by

.. math::

    M_0 = \mu \sum_{p=1}^{N_{patch}}  A_p D_p

where :math:`\mu` is the shear modulus of the rocks involved in the earthquake (in pascals), :math:`A_p` and :math:`D_p` are the area (in square meters) and the slip (in meters) of a patch.

A ``Moment`` distribution is designed to generate random slips for this purpose : it generates a random :math:`M_w` from a Gaussian distribution :math:`M_w \sim N(Mw_{mean}, Mw_{\sigma})`, then distributes the corresponding :math:`M_0/\mu` to different patches with a Dirichlet distribution (i.e., the sum is a constant), and divides the values by the patch area to obtain slips.

:Example:

The Moment distribution is used as a ``prep`` distribution to initialize samples in a parameter set,

.. code-block::

        prep = altar.models.seismic.cuda.moment
        prep:
            Mw_mean = 7.3 ; mean moment magnitude scale
            Mw_sigma = 0.2 ; sd for moment magnitude scale
            Mu = 30 ; in GPa
            area = [400] ; patch area in km^2

:Attributes:

* ``Mw_mean``, the mean moment magnitude scale
* ``Mw_sigma``, the standard deviation of the moment magnitude scale
* ``Mu``, the shear modulus of the rocks (in GPa)
* ``area``, the patch area (in square kilometers). If the areas for all patches are the same, you may input only one value ``area = [400]``. If the areas are different, you may input the list as ``area = [400, 300, 200, 300, ...]``, or ``area_patch_file = area.txt``, i.e., to use a text file as input for patch areas.

Controller
-----------

Please refer to :ref:`Controller` for Bayesian framework configurations, e.g., to use an adaptive MCMC sampler.

Job
----

Please refer to :ref:`Job Management` on details how to deploy AlTar simulation to different platforms.


Output
------

By default, the static inversion simulation outputs results in HDF5 files, see :ref:`H5Recorder` for more details.


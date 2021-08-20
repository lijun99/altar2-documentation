
.. _Static Inversion:

Static Slip Inversion
======================

Static Source model
-------------------

The finite fault earthquake source models infer the spatial distribution and temporal evolution of coseismic slips at fault plane(s) from the observed surface or subsurface displacements.

In the static source model, the spatial distributions of coseismic slips are determined. We model the fault plane(s) as a set of patches; each patch treated as a point source with two orthogonal displacement components, slips along the strike and dip directions. Each slip on the fault plane can be translated into surface deformation, e.g., by the Okada model, which is derived from a Green’s function solution to the elastic half space problem. The observed surface deformation at a given location is the linear combination due to (strike/dip) slips of all patches.

.. note::

   For the static inversion, the patches can be of any shape or area as long as each patch can be treated a single point source. Note that the kinematic inversion currently only supports a rectangle fault divided into :math:`n_{dd} \times n_{as}` square patches. If you plan for a joint static-kinematic inversion, you need to run the static inversion on the square patches as well.

Therefore, the forward model can be expressed as a linear model

.. math::

   {\bf d}^{pred} = \mathcal{G}  {\boldsymbol \theta}.

where :math:`{\boldsymbol \theta}` (also denoted as :math:`{\bf m}` in geophysics literatures) is a vector with :math:`N_{param}=2N_{patch}` components, representing the slips along the strike and dip directions for :math:`N_{patch}` patches; :math:`{\bf d}` is a vector of observed surface deformations (may include vertical and east, north horizontal components) at different locations, with :math:`N_{obs}` observations; and  :math:`\mathcal{G}` is a :math:`2N_{patch} \times N_{obs}` matrix, pre-calculated Green's functions connecting a slip source to a deformation component at an observation location.

A generalized forward model could also include other linear parameters, for example, the InSAR ramp parameters :math:`(a, b, c)`, used to fit the spurious ramp-like displacement fields :math:`a+bx+cy` from InSAR interferograms, where :math:`x` and :math:`y` are the locations of the data in local Cartesian coordinates.


Input
-----

To run the static inversion, in addition to an AlTar configuration file (see next section), you are required to prepare three input files,

:data.txt: the observed data with :math:`N_{obs}` observations, a vector in one row or one column.
:cd.txt: covariance of data representing measurement errors/uncertainties, prepared in a :math:`N_{obs} \times N_{obs}` matrix (could have off-diagonal terms for correlated errors).  A constant could be used (with *cd_std* option) if all data are uncorrelated and have the same variance. Epistemic uncertainties such as elastic heterogeneity and fault geometry uncertainties may also be included, see :ref:`Static Inversion Cp` for more details.
:green.txt: the pre-calculated Green's functions, prepared in a :math:`N_{obs} \times N_{param}` matrix, with :math:`N_{param}` as the leading dimension, i.e., data arranged in row-major as

.. code-block:: none

    G[Obs1][Param1] G[Obs1][Param2] ... G[Obs1][ParamNparam]
    G[Obs2][Param2] G[Obs2][Param2] ... G[Obs2][ParamNparam]
    ... ...
    G[ObsNobs][Param1] G[ObsNobs][Param2] ... G[ObsNobs][ParamNparam]

You may use any other names for these files but need to specify them in the configuration file. These files are arranged under the same directory which can be specified by ``case`` setting in the configuration file.

In addition to plain text inputs with suffix ``.txt``, AlTar 2 also accepts binary data, including

    - Raw binary format with suffix ``.bin`` or ``.dat``. The precision should be consistent with the numerical precision specified by ``job.gpuprecision``. Its size should match the size of the corresponding quantity. For example, the Green's function has in total :math:`N_{obs} \times N_{param}` elements. They will be reshaped by the program.

    - HDF5 files with suffix ``.h5``. HDF5 files are preferred because they include the data shape and precision in metadata. AlTar2 performs the reshaping and precision conversions if necessary.

AlTar2 recognizes the data format automatically by the file suffixes.

There are some software packages which can pre-calculate the Green's functions and/or prepare the input files for AlTar, e.g., `CSI <http://www.geologie.ens.fr/~jolivet/csi/>`__. Please refer to its manual and tutorials for more details.

Configurations
--------------

A configuration file for the static inversion appears as

.. code-block :: none

    ; application instance name
    slipmodel:

        ; model to be sampled
        model = altar.models.seismic.cuda.static
        model:

            ; the name of the test case, also as the directory for input files
            case = 9patch

            ; number of patches
            patches = 9

            ; green's function (observations, parameters)
            green = static.gf.h5

            ; data observations
            dataobs = altar.cuda.data.datal2
            dataobs:
                observations = 108
                data_file = static.data.h5
                cd_file = static.Cd.h5
                ; or use a constant cd
                ; cd_std = 1e-4

            ; list of parameter sets
            ; the order should be consistent with the green's function
            psets_list = [strikeslip, dipslip, ramp]

            ; define parameter sets
            psets:
                strikeslip = altar.cuda.models.parameterset
                dipslip = altar.cuda.models.parameterset
                ramp = altar.cuda.models.parameterset

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

                ramp:
                    count = 3
                    prior = altar.cuda.distribution.uniform
                    prior.support = (-1, 1)

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
~~~~~

For static inversion, you need to specify ``model = altar.models.seismic.cuda.static`` (or the CPU version, ``model=altar.models.seismic.static``).

**Model Attributes**

:case: the directory where all input files are located;
:patches: the number of patches, or point sources;
:green: the file name for the Green's functions, as prepared from the instructions above;
:dataobs: a component to process the data observations and calculate the data likelihood with L2 norm, with details provided in :ref:`Data Observations`;
:psets_lists: a list of parameter sets, the order will be used for many purposes, e.g., enforcing the order of parameters in :math:`\theta`;
:psets: components to describe the parameter sets, with details provided in :ref:`Parameter Sets`.

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

:observations: the number of data observations
:data_file: the name of the file containing the data observations, a vector with ``observations`` elements
:cd_file: the name of the file containing the data covariance,  a matrix with ``observations x observations`` elements
:cd_std: if the data covariance has only constant diagonal elements, you may use this option instead of ``cd_file``.


.. _Parameter Sets:

Parameter Sets
~~~~~~~~~~~~~~~

A parameter set is a group of parameters which share the same prior distributions and are arranged continuously in :math:`{\boldsymbol \theta}`. In static model, we use the following parameter sets ``strikeslip``, ``dipslip``, and optionally, ``ramp`` (you may use any other names for the parameter sets as long as they are intuitive).

The order of the parameter sets in :math:`{\boldsymbol \theta}` is enforced by the attribute ``psets_list``,

.. code-block:: none

    psets_list = [strikeslip, dipslip, ramp]

If the number of patches is 9 and there are 3 InSAR ramp parameters for one set of interferograms. The 21 parameters in
:math:`{\boldsymbol \theta}` are (0-8), strike slips of 9 patches; (9-17), dip slipd of 9 patches; and (18-20), ramp parameters. The order of the parameter sets can be varied, but has to be consistent with that in the Green's function matrix.

For each parameter set, you need to define it as a parameterset, e.g., ``strikeslip = altar.cuda.models.parameterset`` or (``strikeslip = contiguous`` for CPU models). Its attributes include

:count: the number of parameters in this set. ``{slipmodel.model.patches}`` is another way to assign values with pre-defined parameters;
:prior: the prior distribution to initialize random samples in the beginning, and compute prior probabilities during the sampling process. See :ref:`Prior Distributions` for choices of priors.
* ``prep`` (optional), a distribution to initialize samples only. If it is defined, ``prep`` distribution is used to initialize samples while ``prior`` distribution is used for computing prior probabilities. If ``prep`` is not defined, ``prior`` distribution is used for both.

**Example**

For dip-slip faults, you may use a ``uniform`` prior to limit the range of dip slips while using a :ref:`Moment Distribution` to initialize samples so that the moment magnitude is consistent with an estimate scale :math:`M_w`.

.. code-block:: none

        dipslip = altar.cuda.models.parameterset
        dipslip:
            count = {slipmodel.model.patches}
            prep = altar.models.seismic.cuda.moment
            prep:
                Mw_mean = 7.3 ; mean moment magnitude scale
                Mw_sigma = 0.2 ; sd for moment magnitude scale
                Mu = [30] ; in GPa
                area = [400] ; patch area in km^2
            prior = altar.cuda.distributions.uniform
            prior:
                support = (-0.5, 20)

Meanwhile, a Gaussian distribution centered at 0 may be used for strike slips

.. code-block:: none

        strikeslip = altar.cuda.models.parameterset
        strikeslip:
            count = {cudastatic.model.patches}
            prior = altar.cuda.distributions.gaussian
            prior:
                mean = 0
                sigma = 0.5

Since the same distribution is also used to initialize samples, no ``prep`` setting is needed.

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

and define each parameter set by specifying its count and range.

Controller
~~~~~~~~~~

Please refer to :ref:`Controller` for Bayesian framework configurations. You may use this section to choose and customize the ``sampler`` - to process MCMC (e.g, ``altar.cuda.bayesian.metropolis`` or ``altar.cuda.bayesian.adaptivemetropolis``), ``archiver`` - to record the results (default is ``H5Recorder``), and ``scheduler`` - to control the annealing schedule (default is ``COV`` scheduler).

Job
~~~

Please refer to :ref:`Job Management` on details how to deploy AlTar simulation to different platforms, e.g., single GPU,  multiple GPUs on one computer (with mpi), or multiple GPUs distributed in different nodes of a cluster (with mpi and PBS/Slurm scheduler).

Output
------

By default, the static inversion simulation results are stored in HDF5 files, see :ref:`H5Recorder` for more details.

.. _Moment Distribution:

Moment Distribution
-------------------

For strike (dip) faults, we may want the generated seismic moment from all strike (dip) slips to be consistent with the estimated moment magnitude scale :math:`M_w`,

.. math::

    M_w = (\log M_0 -9.1)/1.5

:math:`M_0` is the scalar seismic moment, defined by

.. math::

    M_0 = \mu \sum_{p=1}^{N_{patch}}  A_p D_p

where :math:`\mu` is the shear modulus of the rocks involved in the earthquake (in pascals), :math:`A_p` and :math:`D_p` are the area (in square meters) and the slip (in meters) of a patch.

A ``Moment`` distribution is designed to generate random slips for this purpose : it generates a random :math:`M_w` from a Gaussian distribution :math:`M_w \sim N(Mw_{mean}, Mw_{\sigma})`, then distributes the corresponding :math:`M_0/\mu` to different patches with a Dirichlet distribution (i.e., the sum is a constant), and divides the values by the patch area to obtain slips.

**Example**

The Moment distribution is used as a ``prep`` distribution to initialize samples in a parameter set,

.. code-block:: none

        prep = altar.models.seismic.cuda.moment
        prep:
            Mw_mean = 7.3 ; mean moment magnitude scale
            Mw_sigma = 0.2 ; sd for moment magnitude scale
            Mu = [30] ; in GPa
            area = [400] ; patch area in km^2

**Attributes**

:Mw_mean: the mean value of the moment magnitude scale.
:Mw_sigma: the standard deviation of the moment magnitude scale.
:Mu: the shear modulus of the rocks (in GPa), a list with :math:`N_{patch}` elements. If only one element, the same value will be used for all patches.
:area: the patch area (in square kilometers), also a list with :math:`N_{patch}` elements. If the areas for all patches are the same, you may input only one value ``area = [400]``. If the areas are different, you may input the list as ``area = [400, 300, 200, 300, ...]``, or use a file option below.
:area_patch_file:  a text file as input for patch areas, a vector with :math:`N_{patch}` elements, e.g., ``area_patch_file = area.txt``.
:slip_sign: ``positive`` (default) or ``negative``. By default, the moment distribution generates all positive slips, i.e., the displacement is along the positive axis along the dip or strike direction. If the slips are along the opposite direction, use ``negative`` to generate negative slips.

Note also since ``Mu`` and ``area`` appear as products for each patch, you may also use, e.g., ``Mu=[1]`` and input their products to ``area`` or ``area_patch_file``.


.. _Static Forward Model:

Forward Model Application
-------------------------

When analyzing the results, you may need to run the forward model once for the obtained mean, medium, or MAP model, or a synthetic model, to produce data predictions and compare with data observations. For the static model, it is straightforward: obtain the mean model (vector), read the Green's function (matrix), and perform a matrix-vector multiplication with numpy.

AlTar2 also provides an option to run the forward modeling only instead of the full-scale simulation, with a slightly modified configuration file. Please follow the steps below.

The first step is to prepare a model file, e.g., ``static_mean_model.txt``, including a set of parameters (a vector of :math:`N_{param}` elements), and copy the file to the input directory - the ``case`` directory. To obtain the mean model from the simulations, see :ref:`Static Model Utilities` below.

The second step is to modify the configuration file, e.g, ``static.pfg``, by adding the following settings under ``model`` configuration, (for convenience, we rename it to ``static_forward.pfg``.)

.. code-block:: none

    slipmodel:

        ; model to be sampled
        model = altar.models.seismic.cuda.static
        model:

            ; forward only (True), simulation(set to False)
            forwardonly = True
            ; forward theta input
            theta_input = static_mean_model.txt
            ; forward output file
            forward_output = static_forward_prediction.h5

            ; the name of the test case, also as directory for input files
            case = 9patch

            ... ...
            ; the rest is the same


:forwardonly:  ``True`` for forward modeling only, ``False`` (default) for regular simulations.
:theta_input: the input model file.
:forward_output: the output file including the predicted data in HDF5 format.

You may also need to change the ``job`` configuration since the forward modeling option uses only one GPU (and one thread),

.. code-block:: none

    job:
        tasks = 1 ; number of tasks per host
        gpus = 1  ; number of gpus per task
        gpuprecision = float32 ; double(float64) or single(float32) precision for gpu computations
        ;gpuids = [0] ; a list gpu device ids for tasks on each host, default range(job.gpus)
        ... ...

The third step is to run a different command

.. code-block:: bash

    $ slipmodel.plexus forward --config=static_forward.pfg

Check the generated ``static_forward_prediction.h5`` file for the predicted data from the input model.

Please check the :altar_src:`examples <models/seismic/examples>` directory from the source code for a complete sample.

Actually, you can run the regular simulation with the same configuration file ``static_forward.pfg`` by simply changing ``forwardonly`` to ``False`` (and ``job`` section if needed), by

.. code-block:: bash

    $ slipmodel --config=static_forward.pfg
    # or
    $ slipmodel.plexus sample --config=static_forward.pfg

``slipmodel.plexus`` is a pyre plexus application which supports extra options (panels) compared to the ``slipmodel`` application,

.. code-block:: bash

    $ slipmodel.plexus  #  call about to show application info
    $ slipmodel.plexus about # show application info
    $ slipmodel.plexus sample --config=...  # full simulation, equivalent to slipmodel command
    $ slipmodel.plexus forward --config=... # forward modeling only


.. _Static Model Utilities:

Utilities
---------

We also provide some utilities (in Python) which may be useful to analyze the data or data conversions. Some of scripts may require user modification. Before we can finalize them into standard features, these utilities are currently located at :altar_src:`seismic/examples/utils <models/seismic/examples/utils>` directory of the source code.


.. _HDF5 Converter:

HDF5 Converter tool
~~~~~~~~~~~~~~~~~~~

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


Plot histograms of Bayesian probabilities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You may want to check the distributions of the (log) prior/likelihood/posterior probabilities, which usually a good indication for the simulation performance. The utility is named ``plotBayesian``.

Taking the source code example as an example,

.. code-block:: bash

    # go to the result directory
    cd results/static
    # run plotBayesian for the final step output,
    # which shows the histograms of (log) prior/likelihood/posterior
    ../../utils/plotBayesian
    # to show output from a different beta step
    ../../utils/plotBayesian --step=step_000.h5
    # to change the number of bins for the histogram
    ../../utils/plotBayesian --bin=20

The ``plotBayesian`` utility generates a ``Bayesian_histograms.pdf`` file for the plot.  You may change the script to show the plot on GUI directly or save it to a different format.


Compute the mean model
~~~~~~~~~~~~~~~~~~~~~~

``meanModelStatic.py`` under the ``utils`` directory can be used to compute the mean model of the samples in a given beta step. It also serves as a tool to convert AlTar2 H5 output to AlTar-1.1 H5 output.

.. code-block:: bash

    # go the result directory
    cd results/static
    # run the utility
    python3 ../../utils/meanModelStatic.py

which prints out the mean values and variances of all parameters, as well as saving them to text files. It also converts ``step_final.h5`` to AlTar-1.1 H5 format, ``step_final_v1.h5``.

For a different beta step output, you need to change ``input`` and ``output`` in the script.

The script can also be used for other models, not limited to ``static``: you will just need to change ``psets_list`` to the same as your simulation script.

Compare the data predications and observations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``checkDataPrediction.py`` reads the data predictions from the forward modeling application and compares them with the input data observations. You may need to change the input files in the script.


Convert AlTar2 output to AlTar-1.1 output
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

AlTar2's H5 output differs from AlTar-1.1 H5 output in rearranging the samples in their parameter sets. You may use the ``meanModelStatic.py`` utility above to convert them.









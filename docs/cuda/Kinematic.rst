
.. _Kinematic Inversion:

Kinematic Slip Inversion
=========================

Kinematic Source Model
-----------------------

The kinematic source model studies also the temporal evolution of coseismic slips. The kinematic source model currently implemented in AlTar is formulated as follows.

The fault plane, as a rectangular area, is divided into :math:`N_{dd} \times N_{as}` square patches (dd=down dip, as=along strike), and time is divided into :math:`N_t` intervals. The kinematic slip function :math:`{\bf M}_b({\vec \xi}, t)` (big M) can be in general written as

.. math::

    {\bf M}_b({\vec \xi}, t) = {\bf D}({\vec \xi}) S(t-T_R({\vec \xi}); T_r({\vec \xi})),

where :math:`{\vec \xi}, t` label the patch and time, respectively, and

* :math:`{\bf D}({\vec \xi})` is the coseismic slip vector, also subject to the static source model inversion;
* :math:`T_R({\vec \xi})` is the initial rupture time of each patch, determined by solving the Eikonal equation with a Fast Sweeping algorithm, given the location of the hypocenter :math:`H_0` and the rupture velocity :math:`V_r({\vec \xi})` (assumed to be isotropic and the same within each patch);
* :math:`T_r({\vec \xi})` is the slip duration (rise time) for each patch;
* :math:`S(t, T_r)` is the source time function which is finite only for :math:`t \in [0, T_r]` and integrated to 1: we choose a triangular source time function.

To produce smooth synthetics, we refine each patch into :math:`N_{mesh} \times N_{mesh}` grids when solving the eikonal equation, while dividing each time interval into :math:`N_{pt}` points. :math:`{\bf M}_b({\vec \xi}, t)` are then interpolated and integrated from these finer spatial and temporal meshes.

The predicted observations can be calculated by,

.. math::

    d_{prediction} ({\vec x}, t) = {\cal G}_b({\vec x}, {\vec \xi}; t-t') {\bf M}_b({\vec \xi}, t')

which is a linear model (note that the Eikonal equation is non-linear). Here, :math:`{\cal G}_b({\vec x}, {\vec \xi}; t-t')` (big G) are the kinematic Green's functions relating the source :math:`{\bf M}_b({\vec \xi}, t')` to an observation location at a given time :math:`({\vec x}, t)`. The kinematic Green's functions are pre-calculated as inputs to AlTar. There are some existing software packages for the calculation, e.g., the frequency-wavenumber integration code of `Zhu and Rivera <https://doi.org/10.1046/j.1365-246X.2002.01610.x>`__, or `AXITRA <https://github.com/coutanto/axitra>`__.

In summary, the kinematic inversion uses the following source parameters

- the two components of coseismic slip :math:`{\bf D}({\vec \xi})` (:math:`2\times N_{dd} \times N_{as}` elements),
- the rupture velocity  :math:`V_r({\vec \xi})` (:math:`N_{dd} \times N_{as}` elements),
- the rise time :math:`T_r({\vec \xi})` (:math:`N_{dd} \times N_{as}` elements),
- the location of the hypocenter :math:`{\bf H}_0` (2 elements),

and the forward model

.. math::

    d_{pred} = G( {\bf D}({\vec \xi}), V_r({\vec \xi}),  T_r({\vec \xi}), {\bf H}_0)

is preformed in two steps,

- to obtain :math:`{\bf M}_b({\vec \xi}, t')` from the Eikonal equation sovler,
- to calculate :math:`d_{pred} = {\cal G}_b {\bf M}_b`.


Joint Kinematic-Static Inversion
---------------------------------

Because the slips :math:`{\bf D}({\vec \xi})` are subject to both static and kinematic observations, we in general run static and kinematic models together, by a model ensemble with or without cascading.

The joint Bayesian probability for static and kinematic models can be written as

.. math::

    P({\boldsymbol \theta}_c, {\boldsymbol \theta}_s, {\boldsymbol \theta}_k | {\bf d}_s, {\bf d}_k) = P({\boldsymbol \theta}_c)P({\boldsymbol \theta}_s)P({\boldsymbol \theta}_k) P({\bf d}_s| {\boldsymbol \theta}_c, {\boldsymbol \theta}_s) P({\bf d}_k| {\boldsymbol \theta}_c, {\boldsymbol \theta}_k).

where :math:`{\boldsymbol \theta}_c = [strikeslip, dipslip]` as shared (common) parameters, :math:`{\boldsymbol \theta}_s = [ramp]`, and :math:`{\boldsymbol \theta}_k = [risetime, rupturevelocity, hypocenter]`. The data likelihoods are computed from

* the static model with observations :math:`{\bf d}_s` and the forward model :math:`{\bf d}_s^{pred} = G_s({\boldsymbol \theta}_c, {\boldsymbol \theta}_s)`,
* the kinematic model with :math:`{\bf d}_k` and :math:`{\bf d}_k^{pred} = G_k({\boldsymbol \theta}_c, {\boldsymbol \theta}_k)`.

In the annealing schemes such as CATMIP, we can introduce transitioning distributions

.. math::

    P_{\beta_s, \beta_k} ({\boldsymbol \theta}_c, {\boldsymbol \theta}_s, {\boldsymbol \theta}_k | {\bf d}_s, {\bf d}_k) = P({\boldsymbol \theta}_c)P({\boldsymbol \theta}_s)P({\boldsymbol \theta}_k) [P({\bf d}_s| {\boldsymbol \theta}_c, {\boldsymbol \theta}_s)]^{\beta_s} [P({\bf d}_k| {\boldsymbol \theta}_c, {\boldsymbol \theta}_k)]^{\beta_k}.

where both :math:`\beta_s` and :math:`\beta_k` vary from 0 to 1, either jointly or independently. Depending on how :math:`\beta_s, \beta_k` vary, AlTar supports two schemes:

* In the non-cascading scheme, we set :math:`\beta=\beta_s=\beta_k`, i.e., both increasing at the same pace, while their increment in the COV scheduler is determined by the coefficient of variation of the weights :math:`w = [P({\bf d}_s| {\boldsymbol \theta}_c, {\boldsymbol \theta}_s) P({\bf d}_k| {\boldsymbol \theta}_c, {\boldsymbol \theta}_k)]^{\beta_{m+1}-\beta_m}`.

* In the cascading scheme, we run AlTar twice:

  1.  In the first run, we perform inversion on the static model only, or producing samples of :math:`{\boldsymbol \theta}_c` and :math:`{\boldsymbol \theta}_s` pursuant to the posterior distribution of the static model :math:`P({\boldsymbol \theta}_c, {\boldsymbol \theta}_s | {\bf d}_s) = P({\boldsymbol \theta}_c)P({\boldsymbol \theta}_s) [P({\bf d}_s| {\boldsymbol \theta}_c, {\boldsymbol \theta}_s)]`.

  2. In the second run, we run static and kinematic models together, by setting :math:`\beta_s=1` (``cascaded = True``) and varying :math:`\beta_k` from 0 to 1 (``cascaded = False``). Here, the samples of :math:`{\boldsymbol \theta}_c` and :math:`{\boldsymbol \theta}_s` from the static inversion are used as the initial samples for the joint inversion. The increment of :math:`\beta_k` in the COV scheduler is determined by the coefficient of variation of the weights :math:`w = [P({\bf d}_k| {\boldsymbol \theta}_c, {\boldsymbol \theta}_k)]^{\beta_{k,m+1}-\beta_{k,m}}`.

With the optimized and (usually greatly) reduced search range of :math:`{\boldsymbol \theta}_c` and :math:`{\boldsymbol \theta}_s` in parameter space from the static inversion, the cascaded joint-static-kinematic inversion runs more efficiently than the non-cascading scheme. In general, the cascading scheme is recommended for all model ensembles if there is a computation-intensive model (such as the kinematic model) present.

Configurations (Kinematic Model only)
-------------------------------------

We illustrate the settings of the kinematic model by assuming to run it alone (in practice this is rarely adopted).

An example configuration file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The configuration file (``kinematicg_only.pfg``) for the kinematic model appears as

.. code-block:: none

    ; application instance name
    slipmodel:

        ; model to be sampled
        model = altar.models.seismic.cuda.kinematicg
        model:

            dataobs:
                observations = 14148 ; number of observed data points
                data_file = kinematicG.data.h5
                cd_std = 5.0e-3
                ; or cd_file = kinematicG.cd.h5 if using a file input

            ; fixed model parameters
            ; green's function (2*Ndd*Nas*Nt, observations)
            ; [Nt][2(strike/dip)][Nas][Ndd] with leading dimensions on the right
            green = kinematicG.gf.h5

            Ndd = 3 ; patches along dip
            Nas = 3 ; patches along strike
            Nmesh = 30 ; mesh points for each patch
            dsp = 20.0 ; length for each patch, km
            Nt = 90 ; number of time intervals
            Npt = 2 ; mesh points for each time interval
            dt = 1.0 ; time unit for each interval, second
            ; initial starting time for each patch, in addition to the fast sweeping calculated arrival time
            t0s = [0.0] * {slipmodel.model.patches}

            ; parameters to be simulated
            ; provide a list at first, serving as their orders in theta
            psets_list = [strikeslip, dipslip, risetime, rupturevelocity, hypocenter]

            ; define each parameterset
            psets:
                strikeslip = altar.cuda.models.parameterset
                dipslip = altar.cuda.models.parameterset
                risetime = altar.cuda.models.parameterset
                rupturevelocity = altar.cuda.models.parameterset
                hypocenter = altar.cuda.models.parameterset

                ; variables for patches are arranged along dip direction at first [Nas][Ndd]
                strikeslip:
                    count = {slipmodel.model.patches}
                    prep = altar.cuda.distributions.preset ; load preset samples
                    prep.input_file = theta_cascaded.h5 ; file name
                    prep.dataset = ParameterSets/strikeslip ; dataset name in h5
                    prior = altar.cuda.distributions.gaussian
                    prior.mean = 0
                    prior.sigma = 0.5

                dipslip:
                    count = {slipmodel.model.patches}
                    prep = altar.cuda.distributions.preset
                    prep.input_file = theta_cascaded.h5 ; file name
                    prep.dataset = ParameterSets/dipslip ; dataset name in h5
                    prior = altar.cuda.distributions.uniform
                    prior.support = (-0.5, 20.0)

                risetime:
                    count = {slipmodel.model.patches}
                    prior = altar.cuda.distributions.uniform
                    prior.support = (10.0, 30.0)

                rupturevelocity:
                    count = {slipmodel.model.patches}
                    prior = altar.cuda.distributions.uniform
                    prior.support= (1.0, 6.0)

                ; along strike(first), dip directions
                ; could be separated into 2 for dip and strike direction
                hypocenter:
                    count = 2
                    prior = altar.cuda.distributions.gaussian
                    prior.mean = 20.0
                    prior.sigma = 5.0


Parameter Sets
~~~~~~~~~~~~~~

The parameter sets or ``psets`` for the kinematic models are ``psets_list = [strikeslip, dipslip, risetime, rupturevelocity, hypocenter]``.

- The names the parameter sets can be changed per your preference, e.g., ``strike_slip``, ``StrikeSlip``.  But the order of the parameter sets must be preserved because the forward model uses the order to map appropriate parameters. ``strikeslip`` and ``dipslip`` may be switched as long as their order is consistent with the Green's functions.

- ``strikeslip`` and ``dipslip`` are two components of the cumulative slip displacement. If you prefer to load their initial samples from the static inversion results, use the ``altar.cuda.distributions.preset`` distribution for ``prep``. Only ``HDF5`` format is accepted and therefore, its dataset name ``prep.dataset=ParameterSets/strikeslip`` is also required. If you choose to generate samples from a given distribution, e.g., gaussian/moment scale distributions, please follow the static inversion example to set their ``prep`` and ``prior`` distributions.

- ``risetime`` and ``rupturevelocity`` are rupture duration and velocities for each patch. As they are positive, usually uniform or truncated gaussian distributions are used as their priors.

-  ``strikeslip``, ``dipslip``, ``risetime`` and ``rupturevelocity`` are defined for each patch and their counts are the same as the number of patches. The sequence of patches is arranged as, for :math:`N_{dd} \times N_{as}` patches,  :math:`(as_0, dd_0), (as_0, dd_1), ... (as_0, dd_{Ndd-1}), (as_1, dd_0), ..., (as_{Nas-1}, dd_{Ndd-1})`. Or ``dd`` is the leading dimension.

- ``hypocenter`` is the location of the hypocenter measured from the **CENTER** of the :math:`(as_0, dd_0)` patch (note that it's not the origin or the corner), in unit of kilometers. If the distances along dip and strike directions are different, you may separate them as ``hypo_dd`` and ``hypo_as``, with ``dd`` being first.

Input files
~~~~~~~~~~~

The kinematic model requires the following input files

- ``green`` as the kinematic Green's functions, with the ``shape=(2*Ndd*Nas*Nt, observations)``. The ``observations`` is the number of observed data points, and is the leading dimension. ``[Nt][2(strike/dip)][Nas][Ndd]`` labels the spatial-temporal source displacements with leading dimensions on the right (or which comes first):

::

  (t=0, strike, as_0, dd_0, obs_0), (t=0, strike, as_0, dd_0, obs_1), ..., (t=0, strike, as_0, dd_0, obs_{Nobs-1})
  (t=0, strike, as_0, dd_1, obs_0), (t=0, strike, as_0, dd_1, obs_1), ..., (t=0, strike, as_0, dd_1, obs_{Nobs-1})
  ... ...
  (t=0, strike, as_0, dd_{Ndd-1}, obs_0), (t=0, strike, as_0, dd_{Ndd-1}, obs_1), ...,  (t=0, strike, as_0, dd_{Ndd-1}, obs_{Nobs-1})
  (t=0, strike, as_1, dd_0, obs_0), (t=0, strike, as_1, dd_0, obs_1), ..., (t=0, strike, as_1, dd_0, obs_{Nobs-1})
  ... ...
  (t=0, strike, as_{Nas-1}, dd_{Ndd-1}, obs_0), (t=0, strike, as_{Nas-1}, dd_{Ndd-1}, obs_1), ..., (t=0, strike, as_{Nas-1}, dd_{Ndd-1}, obs_{Nobs-1})
  (t=0, dip, as_0, dd_0, obs_0), (t=0, dip, as_0, dd_0, obs_1), ..., (t=0, dip, as_0, dd_0, obs_{Nobs-1})
  ... ...
  (t=0, dip, as_{Nas-1}, dd_{Ndd-1}, obs_0), (t=0, dip, as_{Nas-1}, dd_{Ndd-1}, obs_1), ..., (t=0, dip, as_{Nas-1}, dd_{Ndd-1}, obs_{Nobs-1})
  (t=1, strike, as_0, dd_0, obs_0), (t=1, strike, as_0, dd_0, obs_1), ..., (t=1, strike, as_0, dd_0, obs_{Nobs-1})
  ... ...
  (t={Nt-1}, dip, as_{Nas-1}, dd_{Ndd-1}, obs_0), (t={Nt-1}, dip, as_{Nas-1}, dd_{Ndd-1}, obs_1), ..., (t={Nt-1}, dip, as_{Nas-1}, dd_{Ndd-1}, obs_{Nobs-1})

  You need to follow the above order when preparing the Green's functions as it's the order how big-M is arranged in the forward model.

- ``dataobs.data_file``, with 1d vector of observed data.

- ``dataobs.cd_file`` for the data covariance matrix with ``shape=(observations, observations)``. If not available, a constant ``dataobs.cd_std`` may be used instead.

The input files can be a text file (.txt), a raw binary (.bin or .dat) or an HDF5 (.h5) file, with its format recognized by the file suffix.


Configurations (Joint inversion)
--------------------------------

The configuration for the joint kinematic-static inversion (``kinematicg.pfg``) appears as

.. code-block:: none

    model = altar.models.seismic.cuda.cascaded
    model:
        ; parameters to be simulated (priors)
        ; provide a list at first, serving as their orders in theta
        psets_list = [strikeslip, dipslip, ramp, risetime, rupturevelocity, hypocenter]
        ; define parametersets
        psets:
            ; define the prior for each parameter set
            ; use preset prior to load samples from static inversion for cascading scheme
            ; or use regular priors for non-cascading scheme
            strikeslip = ... ...
            dipslip = ... ...
            ... ...

        ; the model ensemble
        models:
            static = altar.models.seismic.cuda.static
            kinematic = altar.models.seismic.cuda.kinematicg

            static:
                cascaded = True ; or False for non-cascading scheme
                psets_list = [strikeslip, dipslip, ramp]
                ; other static model configurations
                ... ...

            kinematic:
                cascaded = False ; default setting for model
                psets_list = [strikeslip, dipslip, risetime, rupturevelocity, hypocenter]
                ; other kinematic model configurations
                ... ...

Here, the main model is a model ensemble ``altar.models.seismic.cuda.cascaded``, while its embedded-models ``[static, kinematic]`` listed as elements of the attribute ``models`` (a dict).

The parametersets are properties of the main model and are processed by the main model for sample initializations and prior probability computations. Each embedded-model only requires a ``psets_list`` attribute to extract a sub set of parameters from ``model.psets`` for its own forward modelling, with the data likelihood computed with respect to its own data observations. The main model collects the data likelihood from all embedded models and assembles them into the Bayesian posterior.

The configuration for each embedded model will be the same as when running it independently, except for an extra flag ``cascaded`` (default=False) to control the cascading scheme.

For the non-cascading scheme with :math:`\beta_s = \beta_k = \beta` varying from 0 to 1, set

.. code-block:: none

    static:
        cascaded=False
    kinematic:
        cascaded=False

while for the cascading scheme with :math:`\beta_s =1`, and  :math:`\beta_k = \beta` varying from 0 to 1, after running the static inversion,

.. code-block:: none

    static:
        cascaded=True
    kinematic:
        cascaded=False

Examples
--------

The examples for the joint static and kinematic inversion are available at :altar_src:`models/seismic/examples <models/seismic/examples>`. Input files for both static and kinematic models are stored under the ``9patch`` directory.

Cascading Scheme
~~~~~~~~~~~~~~~~~

The first step is to run the static inversion only:

.. code-block:: bash

    $ slipmodel --config=static.pfg

Please refer to :ref:`Static Inversion` for more details.

The results are saved in the directory ``results/static`` specified by the config ``controller.archiver.output_dir``, which include HDF5 files for all or selected annealing steps. The final step (:math:`\beta=1`) results are saved in ``step_final.h5``. Copy that file to ``9patch`` directory so that the final samples of strike/dip slips serve as initial samples for the joint inversion:

.. code-block:: bash

    $ cp results/static/step_final.h5 9patch/theta_cascaded.h5

Please also note that the number of chains ``job.chains`` in the static inversion should be the same or larger than that of the joint inversion so that there are enough samples available.

We now can run the joint static-kinematic inversion,

.. code-block:: bash

    $ slipmodel --config=kinematicg.pfg

The results for the jointly inversion will be saved to ``results/cascaded``, or any other directory by changing ``controller.archiver.output_dir`` in ``kinematicg.pfg``.

Non-cascading Scheme
~~~~~~~~~~~~~~~~~~~~~

For the non-cascading scheme, you don't need the step to run static inversion.

You may edit the ``kinematicg.pfg`` file (or make a copy at first),

- change the ``static.cascaded`` to ``False``;
- change the ``prep`` distributions for ``strikeslip``, ``dipslip``, and ``ramp`` from ``preset`` to appropriate distributions, e.g., copying them from ``static.pfg`` file.
- change the output directory ``controller.archiver.output_dir`` to, e.g., ``results/non-cascaded``.

Then run the joint inversion:

.. code-block:: bash

    $ slipmodel --config=kinematicg.pfg

In general, the non-cascading takes long iterations to converge and therefore is slower than the cascading scheme.

Please refer to the :ref:`AlTar Framework` for the Bayesian MCMC framework options and job/output controls. For example, the Adaptive Metropolis Sampler in general has better performance than the fixed-length Metropolis Sampler, which can be selected by setting ``sampler=altar.cuda.bayesian.adapativemetropolis`` in the configuration file.


Forward Model Application (new version)
---------------------------------------

It is essentially the same as the :ref:`Static Forward Model`. The predicted data from both static and kinematic models, as well as the bigM, will be saved to one ``forward_prediction.h5`` file. An example is available at :altar_src:`examples/kinematicg_forward.pfg <models/seismic/examples/kinematicg_forward.pfg>`.


Forward Model Application (old version)
---------------------------------------

When analyzing the results, you may need to run the forward model once for the obtained mean-model or any set of parameters, to produce data predictions in comparison with data observations. Since the kinematic forward model is not straightforward, we provide an additional application for running the forward model only, named ``kinematicForwardModel``.

An example configuration file is available as ``examples/kinematicg_forward_oldversion.pfg``. You may use the ``model`` configuration copied from ``kinematicg.pfg``, with extra settings

.. code-block:: none

    ; theta input
    theta_input = kinematicG_synthetic_theta.txt

    ; output h5 file name
    ; data prediction is 1d vector with dimension observations
    data_output = kinematicG_synthetic_data.h5
    ; Mb is 1d vector arranged as [Nt][2(strike/dip)][Nas][Ndd] with leading dimensions on the right
    mb_output = kinematicG_sythetic_mb.h5


where ``theta_input`` is the input of a mean model or any synthetic model, and ``data_out`` and ``mb_output`` are output file names for the data predictions and the big M (you can create an animation from it to observe the rupture process).

The forward model application may be run as

.. code-block:: bash

    $ kinematicForwardModel --config=kinematicg_forward.pfg

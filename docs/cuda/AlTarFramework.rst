.. _AlTar Framework:

###############
AlTar Framework
###############

Application
============

*See API Reference:* :mod:`altar.shells.application`

An AlTar application is the *root* component which integrates all the components in AlTar.  The main components of an AlTar application are as follows.

.. py:class:: Application(altar.application, family="altar.shells.application")

    .. py:attribute:: controller = altar.bayesian.controller()

        :value: altar.bayesian.Annealer (default)
        :description: the MCMC simulation processor, *Annealer* for CATMIP algorithm;

    .. py:attribute:: model = altar.models.model()

        :value: altar.models.linear(), altar.models.cuda.static(), ...
        :description: performs the forward modelling and computes the Bayesian probability densities: the prior, the data likelihood and the posterior;

    .. py:attribute:: job = altar.simulations.run()

        :description: manages the simulation size and job deployment;

    .. py:attribute:: rng = altar.simulations.rng()

        :description: the random number generator shared by all processes;

    .. py:attribute:: monitors = altar.properties.dict(schema=altar.simulations.monitor())

        :description: a collection of event handlers, such as reporter, profiler.

An AlTar application executes the simulation by defining a required ``main`` entry point:

.. code-block:: python

    @altar.export
    def main(self, *args, **kwds):
        """
        The main entry point
        """

        # initialize various components
        self.job.initialize(application=self)
        self.rng.initialize()
        self.controller.initialize(application=self)
        self.model = self.model.initialize(application=self)
        # sample the posterior distribution
        return self.model.posterior(application=self)

which initializes different components and invokes the ``model.posterior`` to perform the MCMC sampling.

An AlTar application is also the engager of the pyre framework, as inherited from ``pyre.application`` or ``pyre.plexus``, which performs

    - registering all protocols and components in a database;

    - reading/loading configuration files;

    -  instantiating all components into *regular* Python objects;

    - invoking the proper shell (MPI, SLURM) to deploy the job.

.. _Controller:

Controller/Annealer
===================
*See API Reference:* :mod:`altar.bayesian.Annealer`

A Bayesian controller uses an annealing schedule and MCMC to approximate the posterior distribution of a model. The current Annealer uses exclusively the CATMIP algorithm (more controllers implementing other algorithms will be added to a future release). It includes the following configurable components

    * ``sampler = altar.bayesian.sampler()``, the MCMC sampler. The default is a ``Metropolis`` sampler with fixed chain length based on Metropolis-Hastings algorithm. Another sampler implemented is ``AdaptiveMetropolis`` which targets a fixed acceptance ratio and varies the chain length targeting a fixed effective sample size.
    * ``scheduler = altar.bayesian.scheduler()``, the generator of the annealing schedule. The default and currently only implemented scheduler is based on the Coefficient of Variance (COV) of the data likelihood densities.
    * ``dispatcher = altar.simulations.dispatcher(default=Notifier)``, currently only serves the purpose of profiling.
    * ``archiver = altar.simulations.archiver(default=Recorder)``, the archiver of simulation state. The default recorder saves the simulation state to HDF5 files.

and another component determined at runtime from the job configurations,

    * ``worker`` (AnnealingMethod): as AlTar simulations can be performed with either single thread or multiple threads, on CPUs or GPUs, the Controller uses different workers where various deployment-dependence procedures are differentiated. For example, the multiple thread processor, ``MPIAnnealing`` needs to include additional procedures to collect/distribute samples for all threads.

The Annealer's behaviors include

    * ``deduceAnnealingMethod`` which uses the job configuration to determine the worker.
    * ``posterior`` which defines the MCMC procedures with an annealing schedule.


Worker/AnnealingMethod
----------------------
*See API Reference:*  :mod:`altar.bayesian.AnnealingMethod`

A worker(AnnealingMethod) defines each procedure of annealing which may be platform dependent. There are three types of workers:

    - ``SequentialAnnealing``, a single thread CPU processor
    - ``CUDAAnnealing``, a single thread GPU processor
    - ``MPIAnnealing``, a multiple thread processor which uses SequentialAnnealing(CPU) or CUDAAnnealing(GPU) as slave workers.

    Each worker also keeps a set of simulation state data, such as ``beta`` (the inverse temperature), ``theta`` (the random samples), ``prior/data/posterior`` (the Bayesian densities), in an object ``CoolingStep``.

Worker is not directly user configurable; it is determined automatically by the job configuration.

Sampler
-------
*See API Reference:*  :mod:`altar.bayesian.Sampler`

Starting with :math:`N_s` number of chains/samples (processed in parallel), a sampler performs MC updates of the samples pursuant to a given distribution for several steps (length of the chain). For finite :math:`\beta`, the target distribution is the transient distribution :math:`P_m({\boldsymbol \theta}|{\bf d}) = P({\boldsymbol \theta}) P({\bf d}|{\boldsymbol \theta})^{\beta_m}`, while the sampling serves as a burn-in process. When :math:`\beta=1` is reached, the sampler samples the posterior distribution :math:`P({\boldsymbol \theta}|{\bf d})`.

The default sampler is a CPU ``Metroplis`` sampler. To use other samplers, e.g., for CUDA simulations, users need to specify it in the controller block of the configuration file

.. code-block:: none

    ApplicationInstance:
        controller:
            sampler = altar.cuda.bayesian.metropolis
            sampler:
                ; sampler attributes
                ... ...

Metropolis
~~~~~~~~~~
*See API Reference:*  :mod:`altar.bayesian.Metropolis`

**Algorithm**

* New samples are proposed with a Gaussian kernel,

    .. math::

        {\boldsymbol \theta} ' &=  {\boldsymbol \theta}  + \alpha {\boldsymbol \delta}  \\
        {\boldsymbol \delta} &\sim N(0, {\boldsymbol \Sigma}) \nonumber

    where :math:`{\boldsymbol \Sigma}` is the (weighted) covariance matrix of starting samples (from the previous :math:`\beta` step), and :math:`\alpha` is a scaling factor adjusting the jump distance. In CATMIP, :math:`\alpha` is adjusted by the acceptance rate (from the previous :math:`\beta`-step):

    .. math::

        \alpha = acceptanceWeight * acceptanceRate + rejectionWeight

    Since the acceptance rate varies between 0 and 1, ``rejectionWeight`` and ``rejectionWeight+acceptanceWeight`` offer as the lower and upper limits of the scaling factor :math:`\alpha`.

* Decide whether to accept the proposed samples with the Metropolis–Hastings algorithm.

* Repeat the MC updates for a fixed :math:`N_c`-number of times.

**Configurable attributes**

:scaling: float, the initial value of :math:`\alpha`, default=0.1
:acceptanceWeight, rejectionWeight: float, ratios to adjust the value of :math:`\alpha` during the run, defaults=8/9, 1/9
:steps: integer, the MC update steps in each :math:`\beta`-step (the length of each chain), configured by ``job.steps``.

**Configuration examples**

.. code-block:: none

    ApplicationInstanceName:
        controller:
            sampler = altar.bayesian.metropolis
            sampler:
                scaling = 0.2
                acceptanceWeight = 0.1
                rejectionWeight = 0.9
        ; the length of chains
        job.steps = 2**12


Metropolis (CUDA Version)
~~~~~~~~~~~~~~~~~~~~~~~~~
*See API Reference:*  :mod:`altar.cuda.bayesian.cudaMetropolis`

The CUDA version follows the same procedure as above, but includes more control on the scaling factor.

**Configurable attributes**

:scaling: float; the initial value of :math:`\alpha`; default=0.1
:acceptanceWeight, rejectionWeight: float; ratios to adjust the value of :math:`\alpha` during the run, defaults=8/9, 1/9
:useFixedScaling: bool; if ``True``, the initial ``scaling`` will be used for all :math:`\beta`-steps; default= ``False``
:scalingMin, scalingMax: float; the min/max values of the scaling factor; default=0.01, 1
:steps: integer, the MC update steps in each :math:`\beta`-step (the length of each chain), configured by ``job.steps``.

**Configuration examples**

.. code-block:: none

    ApplicationInstanceName:
        controller:
            sampler = altar.cuda.bayesian.metropolis
            sampler:
                scaling = 0.2
                acceptanceWeight = 0.99
                rejectionWeight = 0.01
                useFixedScaling = False
                scalingMin = 0.1
                scalingMax = 0.5
        ; the length of chains
        job.steps = 2**12

In this example, ``scaling`` is set to 0.2 in the beginning. During the run, ``scaling = acceptanceWeight*R + rejectionWeight``, where :math:`R` is the acceptance rate from the previous :math:`\beta`-step, or ``scaling`` :math:`\in[0.01, 1]`. ``scalingMin`` and ``scalingMax`` further adjust the range as [0.1, 0.5].

AdaptiveMetropolis
~~~~~~~~~~~~~~~~~~
*See API Reference:*  :mod:`altar.cuda.bayesian.cudaAdaptiveMetropolis` (for CUDA only)

**Algorithm**

In an AdaptiveMetropolis sampler, there are a few variations from the Metropolis sampler,

#. After a certain number of MC updates, ``corr_check_steps``, the correlation between the current samples and the initial samples are computed. If the correlation is smaller than a threshold value, ``target_correlation``, or the samples become sufficiently de-correlated, we can stop MC updates for the current :math:`\beta`-step. A ``max_mc_steps`` sets the maximum number of MC updates if the correlation threshold value cannot be achieved.

#. The scaling factor :math:`\alpha` targets an optimal acceptance rate, ``target_acceptance_rate``, with a feedback function

    .. math::

        \alpha_{j+1} = \alpha_j \exp[-gain*(acceptanceRate_j-target\_acceptance\_rate)]

    where :math:`j` labels the :math:`\beta`-step. The initial value is set as

    .. math::

        \alpha_0 = scaling/\sqrt{parameters}

    It is shown that an optimal value for :math:`\alpha` is :math:`2.38/\sqrt{d}`, where :math:`d` is the dimension of parameter space, or ``parameters``.

#. (*New in 2.0.2*) Sometimes, it is useful to use more MC steps when :math:`\beta` is small, or *vice versa*. We introduce a new ``max_mc_steps_stage2`` to be used for the maximum MC steps when :math:`\beta` > ``beta_step2``.


**Configurable Attributes**

:scaling: float, default=2.38,
    initial scaling factor for Gaussian proposal, to be normalized by the square root of the number of parameters
:parameters: integer, default=1,
    the total number of parameters in simulation: since the controller is initialized before the model, users need to manually provide this information to the sampler (we will try to eliminate this requirement in the next update).
:scaling_min, scaling_max: float, default=(0.01, 1),
    the minimum and maximum values allowed for the scaling factor
:target_acceptance_rate:  float, default=0.234,
    the targeted acceptance rate
:gain:  float, default=None (determined by ``target_acceptance_rate``),
    the feedback gain constant
:max_mc_steps: integer, default=100000,
    the maximum Monte-Carlo steps for one beta step
:min_mc_steps: integer, default=1000,
    the minimum Monte-Carlo steps for one beta step
:beta_stage2: float, default=0.1,
    the start beta value to use another maximum MC steps
:max_mc_steps_stage2: integer, default=None (to be set the same as ``max_mc_steps``),
    the maximum Monte-Carlo steps for one beta step when ``beta`` > ``beta_stage2``
:corr_check_steps:  integer, default=1000,
    the Monte-Carlo steps to compute and check the correlation
:target_correlation: float, default=0.6,
    the threshold of correlation to stop the chain updates

**Configuration examples**

.. code-block:: none

    ApplicationInstanceName:
        controller:
            sampler = altar.cuda.bayesian.adaptivemetropolis  ; only for CUDA
            sampler:
                scaling = 2.38
                parameters = 399 ; number of parameters in model
                min_mc_steps = 3000
                max_mc_steps = 10000
                corr_check_steps = 1000
                target_correlation = 0.6
                beta_stage2 = 0.1
                max_mc_steps_stage2 = 5000

In this example, the initial scaling factor is set to ``scaling`` / sqrt(``parameters``) or :math:`2.38/\sqrt{399}=0.12` (you can also set ``scaling`` directly to 0.12, and use the default value 1 for ``parameters``). After ``min_mc_steps`` (3,000), the correlation between current samples and initial samples are computed every ``corr_check_steps`` (1,000). If the correlation is less than ``target_correlation`` (0.6), the MC update stops and the simulation proceeds to next :math:`\beta` step. If the ``target_correlation`` cannot be achieved by a certain number of steps, ``max_mc_steps`` (10,000) for :math:`\beta <=` ``beta_stage2`` (0.1) while ``max_mc_steps_stage2`` (5,000) for :math:`\beta >` ``beta_stage2`` (0.1), the MC update is forced to stop and the simulation proceeds to next :math:`\beta` step.

Scheduler
---------

A scheduler regulates how :math:`\beta` increases between different :math:`\beta`-steps. The default (and currently the only option) is `COV Scheduler`.

COV Scheduler
~~~~~~~~~~~~~
*See API Reference:*  :mod:`altar.bayesian.COV`

**Algorithm**

The COV (Coefficient of Variation) scheduler targets the effective sample size from resampling between different transient
distributions,

.. math::

    P_m({\boldsymbol \theta}|{\bf d}) = P({\boldsymbol \theta}) P({\bf d}|{\boldsymbol \theta})^{\beta_m},

At the :math:`m`-stage, samples :math:`\theta_{m,k}` are generated with the target equilibrium distribution :math:`P_m({\boldsymbol \theta}|{\bf d})`, where :math:`k=1,2,\ldots, N_s` and :math:`N_s` is the total number of samples (chains). At the :math:`m+1`-stage, the sampling targets :math:`P_{m+1}({\boldsymbol \theta}|{\bf d})` as the new equilibrium distribution. To sample a distribution with samples generated from another distribution is called as importance sampling, with the importance weight

.. math::

    w(\theta_{m,k}) & = \frac {P_{m+1}(\theta_{m,k}|{\bf d})}{P_m({\boldsymbol \theta}|{\bf d})}  \\
      &= P({\bf d}|\theta_{m,k})^{\beta_{m+1} -\beta_{m}}

while the effective sample size (ESS) from the resampling is associated with the COV of :math:`w(\theta_{m,k})`,

.. math::

    ESS  &= \frac {N_s} {1 + COV(w)}, \\
    COV(w) & =  \frac {\bar w} {\sigma}  \\
    {\bar w} &=  \frac {1}{N_s}  \sum_k w(\theta_{m,k}) \\
    \sigma &= \frac {1}{N_s-1} \sum_k [w(\theta_{m,k}) -{\bar w}]^2.

In COV Scheduler, we choose a :math:`\beta_{m+1}` so that COV is of order unity, e.g., :math:`COV=1`, or :math:`ESS=N_s/2`.

**Configurable Attributes**

:target:  float, default=1.0,
    the target value for COV

:solver:  ``altar.bayesian.solver()``, values= ``grid`` (default), ``brent``;
    the δβ solver based on the grid search algorithm (grid) or the Brent minimizer (brent)

:check_positive_definiteness:  bool, values = ``True`` (default), ``False``;
    whether to check the positive definiteness of Σ matrix and condition it accordingly

:min_eigenvalue_ratio: float, default=0.001;
    if checking the positive definiteness, the minimal eigenvalue to be set as a ratio of the maximum eigenvalue

**Configuration examples**

.. code-block:: none

    ApplicationInstanceName:
        controller:
            scheduler: ; default is COV
                target = 2.0
                solver = brent
                check_positive_definiteness = False

Archiver (Output)
-----------------
*See API Reference:*  :mod:`altar.simulations.Archiver`

The Archiver saves progress information. The default is an H5Recorder which saves the Bayesian statistical data to HDF5 files.

.. _H5Recorder:

H5Recorder
~~~~~~~~~~
*See API Reference:*  :mod:`altar.bayesian.H5Recorder`

H5Recorder saves the random samples and their Bayesian probability densities from each :math:`\beta`-step to an HDF5 file,
``output_dir/step_nnn.h5``.

.. code-block:: none

    +---------- step_nnn.h5 ------
    ├── Annealer ; annealing data
    |   ├── beta ; the beta value
    |   └── covariance ; the covariance matrix for Gaussian proposal
    ├── Bayesian ; the Bayesian probabilities
    |   ├── prior ; (log) prior probability for all samples, vector (samples)
    |   ├── likelihood ; (log) data likelihood for all samples
    |   └── posterior ; (log) posterior probability for all samples
    └── ParameterSets ;  samples
        └── theta ; samples of model parameters, 2d array (samples, parameters)

If you use a list of parameter sets, e.g., in Static Inversion, {``strike_slip``, ``dip_slip``, ``insar_ramp``}, their names will be used for their data sets,

.. code-block:: none

    └── ParameterSets ;
        └── strike_slip ; samples of strike slips, 2d array (samples, number of patches)
        └── dip_slip ; samples of dip slips, 2d array (samples, number of patches)
        └── insar_ramp ; samples of insar ramp parameters to be fitted, 2d array (samples, number of ramp parameters)

H5Recorder also records the MCMC statistics from each :math:`\beta`-step to a file ``output_dir/BetaStatistics.txt``. An example for the linear model is as follows

.. code-block:: none

    iteration, beta, scaling, (accepted, invalid, rejected)
    0, 0, 0.3, (0, 0, 0)
    1, 0.00015000000000000001, 0.5925347222222223, (2773, 0, 2347)
    2, 0.00037996549999999997, 0.31666666666666665, (1184, 0, 3936)
    3, 0.00069984391104, 0.5828125, (2717, 0, 2403)
    4, 0.0011195499765973632, 0.3454861111111111, (1350, 0, 3770)
    5, 0.0016789230286104687, 0.5607638888888888, (2590, 0, 2530)
    6, 0.0025175127332664362, 0.3590277777777778, (1428, 0, 3692)
    7, 0.0037843154920951883, 0.5447916666666667, (2498, 0, 2622)
    8, 0.005577503724209416, 0.3751736111111111, (1521, 0, 3599)
    9, 0.008163002214526472, 0.5303819444444444, (2415, 0, 2705)
    10, 0.012229533905446913, 0.37986111111111115, (1548, 0, 3572)
    11, 0.017958602608795324, 0.5154513888888889, (2329, 0, 2791)
    12, 0.026207750346881442, 0.38125, (1556, 0, 3564)
    13, 0.03808801579264949, 0.5, (2240, 0, 2880)
    14, 0.05444051952417445, 0.40243055555555557, (1678, 0, 3442)
    15, 0.07760672679583216, 0.4793402777777778, (2121, 0, 2999)
    16, 0.11173527790438637, 0.42065972222222225, (1783, 0, 3337)
    17, 0.16503116123012318, 0.4588541666666667, (2003, 0, 3117)
    18, 0.24518816975203137, 0.41944444444444445, (1776, 0, 3344)
    19, 0.3470877668355071, 0.46753472222222225, (2053, 0, 3067)
    20, 0.5037867027949854, 0.40625, (1700, 0, 3420)
    21, 0.7176546338903467, 0.47465277777777776, (2094, 0, 3026)
    22, 1.0, 0.41770833333333335, (1766, 0, 3354)

which shows how :math:`\beta` evolves from :math:`\beta`-step iterations, as well the scaling parameter :math:\`alpha`, and the MC acceptance (accepted/rejected = proposals accepted/rejected by Metropolis-Hastings algorithm, invalid = proposals rejected due to being out of range for ranged priors).


**Configurable Attributes**

:output_dir: path(string), default="results";
    the directory to save results

:output_freq: integer, default=1;
    the frequency to write step data to files, e.g., if you only want to save data for every 3 :math:`\beta`-steps, you may choose ``output_freq=3``. The final :math:`\beta`-step, i.e., :math:`\beta=1` will be always saved as ``step_final.h5``.

**Configuration examples**

.. code-block:: none

    ApplicationInstanceName:
        controller:
            archiver: ; default is H5Recorder
                output_dir = results/static_chain_1024
                output_freq = 3


.. _Job Management:

Job
=====
*See API Reference:*  :mod:`altar.simulations.Job`

The ``job`` component in an AlTar application controls the size of the simulation as well as its deployment to different platforms.

Configurable Attributes
-----------------------

.. code-block:: python

    name = altar.properties.str(default="sample")
    name.doc = "the name of the job; used as a stem for making filenames, etc."

    mode = altar.properties.str()
    mode = "the programming model"

    hosts = altar.properties.int(default=1)
    hosts.doc = "the number of hosts to run on"

    tasks = altar.properties.int(default=1)
    tasks.doc = "the number of tasks per host"

    gpus = altar.properties.int(default=0)
    gpus.doc = "the number of gpus per task"

    gpuprecision = altar.properties.str(default="float64")
    gpuprecision.doc = "the precision of gpu computations"
    gpuprecision.validators = altar.constraints.isMember("float64", "float32")

    gpuids = altar.properties.list(schema=altar.properties.int())
    gpuids.default = None
    gpuids.doc = "the list of gpu ids for parallel jobs"

    chains = altar.properties.int(default=1)
    chains.doc = "the number of chains per worker"

    steps = altar.properties.int(default=20)
    steps.doc = 'the length of each Markov chain'

    tolerance = altar.properties.float(default=1.0e-3)
    tolerance.doc = "convergence tolerance for β->1.0"


Simulation Size
----------------

For a single thread simulation, the job size is determined by the number of ``chains`` (per thread), which are processed as a batch. More chains offer better phase space exploration. But the number of chains may be limited by the computer memory size (CPU or GPU). Since the memory usage also depends on the number of parameters and the type of model, users are encouraged to try some chain sizes at first (stop the simulation after one or two beta steps) to determine an optimal setting of ``chains`` for their computer system.

Large-scale simulations can be distributed to multiple threads. Distributing the total number of chains from one thread (sequentially) to multiple threads (in parallel) may also reduce the computation time (wall time). The number of threads are controlled by two parameters ``hosts`` - the number of hosts (nodes), and ``tasks`` - the number of threads per host. The total number of chains is therefore ``hosts*tasks*chains``.

The multi-threading in AlTar is achieved by MPI. An AlTar application is capable of deploying itself automatically to multiple MPI threads in one or more computers/nodes so that users don't need to run ``mpirun``, ``qsub``, or ``sbatch`` explicitly.

The Metropolis sampler uses ``job.steps`` to control the number of MC updates in each :math:`\beta`-step. (*It might be better to move this setting directly to sampler*). This procedure serves as a burn-in to equilibrate samples from one distribution with :math:`\beta_m` to another with :math:`\beta_{m+1}`. Larger ``steps`` allow more equilibration but are not required in CATMIP: the :math:`\beta`-increment (or the total number of :math:`\beta`-steps) will be adjusted.


Single Thread Configuration
---------------------------

The default job setting is to run AlTar with one CPU thread; you don't need to provide any settings in the configuration file. However, if you prefer to keep ``hosts`` and ``tasks`` entries to be modified later, set them to be 1 explicitly.

.. code-block:: none

    ApplicationInstanceName:
        job:
            hosts = 1 ; number of hosts/nodes
            tasks = 1 ; number of threads per host
            chains = 2**12 ; number of Markov chains per thread.
            steps = 2**10 ; length of the Markov chain

Multiple Threads on One Computer
--------------------------------

To run a multi-threaded simulation on a single computer, you need to adjust the ``tasks`` setting, as well as to specify
a ``mpi.shells.mpirun`` shell instead,

From the configuration file

.. code-block:: none

    ApplicationInstanceName:
        job:
            tasks = 8

        shell = mpi.shells.mpirun

    ; additional configurations for mpi shell, if needed
    mpi.shells.mpirun # altar.plexus.shell:
        extra = -mca btl self,tcp

or from the command line

.. code-block:: bash

    $ AlTarApp --job.tasks=8 --shell=mpi.shells.mpirun


If you use an MPI package not installed under the system directory, you may need to provide its configuration to AlTar/pyre framework. For example, for OpenMPI installed with Anaconda, the following additional configurations are required

.. code-block:: none

    mpi.shells.mpirun:
      ; mpi implementation
      mpi = openmpi#mpi_conda

    ; mpi configuration
    pyre.externals.mpi.openmpi # mpi_conda:
      version = 3.0
      launcher = mpirun
      prefix = /opt/anaconda3
      bindir = {mpi_conda.prefix}/bin
      incdir = {mpi_conda.prefix}/include
      libdir = {mpi_conda.prefix}/lib

Since the MPI package information is common for running all jobs on a computer, you may choose to save the above configuration to an ``mpi.pfg`` file, either under ``${HOME}/.pyre`` directory (searchable by all AlTar/pyre applications), or under the work directory with the AlTar application configurable file, e.g., ``linear.pfg``.

Decide the max number of tasks/threads on a computer from the number of physical cores, not from the total (virtual) threads. Hyperthreading may increase the number of available threads, but it might not increase performance for compute-intensive models, e.g., with matrix multiplications.


Multiple Threads Across Several Computers
-----------------------------------------

If a batch scheduler is not required, you may still use the ``mpi.shells.mpirun`` shell with the additional ``hostfile`` configuration. A hostfile is a simple text file with hosts/nodes specified, e.g., ``my_hostfile``

.. code-block:: none

    # This is an example hostfile.  Comments begin with #
    192.168.1.101 slots=16
    192.168.1.102 slots=16
    192.168.1.103 slots=16

To use the hostfile with ``mpi.shells.mpirun`` shell, e.g., with 4 hosts and 8 threads per host,

.. code-block:: none

    ApplicationInstanceName:
        job:
            hosts = 4
            tasks = 8
        shell = mpi.shells.mpirun
        shell:
            hostfile = my_hostfile

Or from the commmand line,

.. code-block:: bash

    $ AlTarApp --job.hosts=4 --job.tasks=8 --shell=mpi.shells.mpirun --shell.hostfile=my_hostfile


If a batch scheduler is available, e.g., `Slurm Workload Manager <https://slurm.schedmd.com/documentation.html>`__, use an ``mpi.shells.slurm`` shell instead. An example configuration is as follows


.. code-block::

    ApplicationInstanceName:
        job:
            hosts = 4
            tasks = 8
        shell = mpi.shells.slurm

    ; for parallel runs
    mpi.shells.slurm :
        submit = True ; if True, submit the job for execution, if not, a slurm script is generated
        queue = gpu ; the name of the queue

Or from the command line

.. code-block:: bash

    $ AlTarApp --job.hosts=4 --job.tasks=8 --shell=mpi.shells.slurm --shell.queue=gpu

If your Slurm Manager requires additional configurations, you can use ``submit=False``, modify the generated Slurm script,
and use ``sbatch`` to submit the job.

.. _GPU Job Configuration:

GPU Configurations
------------------

The GPU support in AlTar is implemented with `CUDA <https://developer.nvidia.com/about-cuda>`__, and therefore is limited to NVIDIA graphical cards.

**To choose GPU or CPU** If you plan to run AlTar simulations on GPU, you may enable it by

.. code-block::

    ApplicationInstanceName:
        job.gpus = 1 ; number of GPU per task,  0 = use gpu


AlTar also checks the availability of ``cuda`` modules (software) and compatible CUDA devices (hardware). If either is unavailable, AlTar enforces ``job.gpus = 0``, or using CPU instead.

Currently, the ``cuda`` modules are not fully integrated with cpu modules. You may need to check whether the model has a cuda implementation, and also select explicitly some cuda components, for example, for the Static Inversion,

.. code-block::

    slipmodel: ; the Application Instance Name

        model = altar.models.seismic.cuda.static
        ; define parametersets
        psets:
            strikeslip = altar.cuda.models.parameterset
            dipslip = altar.cuda.models.parameterset

            strikeslip:
                count = {slipmodel.model.patches}
                prior = altar.cuda.distributions.gaussian
                prior.mean = 0
                prior.sigma = 0.5
            ... ...

        controller:
            sampler = altar.cuda.bayesian.metropolis

        ... ...

*In the next release, we will try to merge cuda modules with cpu modules so that a single ``jobs.gpus`` flag can switch between CPU and GPU computations.*


**To use multiple GPUs** GPUs (device) rely on CPU (host) for job dispatching and data copies from/to GPU memories. AlTar runs on one GPU per (CPU) thread, therefore, the number of GPUs used for simulation is tuned by the number of threads per host, ``job.tasks``, and/or the number of hosts, ``job.hosts``. ``job.gpus`` is always 1 for GPU simulations.

To deploy the simulation to 8 GPUs in one computer/node, the configuration is

.. code-block:: none

    ApplicationInstanceName:
        job.hosts = 1 ; number of hosts
        job.tasks = 8 ; number of threads per host
        job.gpus = 1 ; number of gpus per thread


To deploy the simulation to 4 nodes with 8 GPUs per node, the configuration is

.. code-block:: none

    ApplicationInstanceName:
        job.hosts = 4 ; number of hosts
        job.tasks = 8 ; number of threads per host
        job.gpus = 1 ; number of gpus per thread

For a computer/node with multiple GPUs, the job is distributed sequentially to the first available GPUs (``gpuids`` = 0, 1,2, 3 ...). If you plan to assign the job to specific GPUs, you can use ``job.gpuids`` to specify them,

.. code-block:: none

    ApplicationInstanceName:
        job.hosts = 4 ; number of hosts
        job.tasks = 2 ; number of threads per host
        job.gpus = 1 ; number of gpus per thread
        job.gpuids = [2, 3]

Another method is to use the environmental variable ``CUDA_VISIBLE_DEVICES``. For example,

.. code-block:: bash

    # bash
    $ export CUDA_VISIBLE_DEVICES=2,3
    # csh/tcsh
    $ setenv CUDA_VISIBLE_DEVICES 2,3

which makes only GPU2 and GPU3 visible for applications, appearing as ``gpuids=[0, 1]``. With this method, you don't need to set ``gpuids``.

**To select the precision** AlTar supports both single and double precision GPU computations (the CPU computation is always double precision). However, most NVIDIA gaming cards only have single precision processors. In our tests on Tesla cards, single precision computations run twice faster than double precisions. If you want to choose between single and double precisons, you may use the ``job.gpuprecison`` flag, such as

.. code-block:: none

    ApplicationInstanceName:
        job:
            hosts = 1 ; number of hosts
            tasks = 2 ; number of threads per host
            gpus = 1 ; number of gpus per thread
            gpuprecision = float32 ; double(float64) or single(float32) precision for gpu computations


Model
======

The Model component in AlTar Framework defines the forward problem, and computes the data likelihood accordingly. Each model needs an implementation for a given inverse problem. See :ref:`Models` for details guides on implemented models.

Users may also develop their own models, following the guide in :ref:`Develop Bayesian Model`.


.. include:: Priors.rst





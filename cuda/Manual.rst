
#########################
AlTar 2.0 CUDA User Guide
#########################

.. sectnum::

.. contents:: Table of Contents


Overview
========

AlTar 2.0  is based on the pyre_ framework. Each altar/pyre application has certain configurable components (usually a base class object implementing a corresponding protocol, which can be configured into different implementations of the same protocol) as well as traits (constant variables, such as string: altar.properties.str, integer: altar.properties.int, ...). Each component then could have its own configurable components and traits.  

The configuration of components and traits can be assigned by a configuration file or as command line arguments.   Taking the ``linear`` application as an example, its configuration script ``linear.pfg`` appears as 
::

    ; application name
    linear:
         ; components/traits configuration of the linear application
         model = altar.models.linear
         model:
             ; components/traits configurations of the model
             ; input directory
             case = 9patch
             ; number of parameters
             parameters = 18
             ... ... 
             ; prior distribution of the parameters
             prior = altar.distributions.gaussian
             prior:
                 ; configurations of prior 
                 center = 0.0
                 sigma = 0.5
                 count = {linear.model.parameters}  
             ... ...

where the configurations are indented to show their hierarchy. A declaration with full path or a hybrid declaration with partial path and indentation are also supported, e.g., 
:: 

    linear.model = altar.models.linear
    linear.model.case = 9-patch
    linear.model.parameters = 18
    linear.model:
        prior = altar.distributions.gaussian
        prior.center = 0.0
        prior.sigma = 0.5
        ... ...

To assign configurations at command line (which also overrides the corresponding configuration in ``.pfg`` file), you may add them as options as ``--option=setting``, e.g., 
::
    
    $ linear --model.case=18-patch

If you prefer to run the model with different configurations, e.g., ``linear_mpi.pfg`` for multi-threads, you may run 
::

    $ linear --config=linear_mpi.pfg


An altar application has following configurable components:
* shell, which manages where the job is deployed, e.g., 
    * mpi for job.tasks >1  ``$ linear --shell=mpi.shells.mpirun --job.tasks=4``
    * slurm job scheduler  ``$ linear --shell=mpi.shells.slurm`` 
* jobs, which manages the size of the job
    


Slipmodel for Seismic Static and Kinematic inversions 
=====================================================

Static Inversion script
-----------------------
The static inversion is a linear model, d = G M, where G (Green's function) is a matrix with the dimension(observations, parameters), M (strike/dip slips for each patch) is a vector of the size equal to the total number of parameters, and d (data) is a vector of the size equal to the number of observed data points.

A sample script for static inversion ``static.pfg``

::

    ; the static uoᴉsɹǝʌuᴉ example
    ; application name (has to be the same with the application name) 
    slipmodel: 
        
        ; model 
        model = altar.models.seismic.cuda.static
        model:

            ; the name (also the directory for input files) of the specific case
            case = static_9patch

            ; number of patches Ndd*Nas
            patches = 9

            ; green's function
            ; shape (observations, parameters)
            ; text (.txt) or binary (.bin or .dat) also accepted
            green = static.gf.h5

            ; observed data
            dataobs = altar.cuda.data.datal2
            dataobs:
                observations = 108
                data_file = static.data.h5
                cd_file = static.Cd.h5
                ; use cd_std = 1e-4 instead for a constant standard deviation

            ; list of parametersets (the order must be the same as their orders in Green's function)
            psets_list = [strikeslip, dipslip]

            ; define parametersets
            psets:
                strikeslip = altar.cuda.models.parameterset
                dipslip = altar.cuda.models.parameterset
                ; add insarramp if needed

                strikeslip:
                    count = {cudastatic.model.patches}
                    prior = altar.cuda.distributions.gaussian
                    prior.mean = 0
                    prior.sigma = 0.5

                dipslip:
                    count = {cudastatic.model.patches}
                    prep = altar.models.seismic.cuda.moment
                    prep:
                        support = (-0.5, 20) ; slip range
                        Mw_mean = 7.3 ; mean moment magnitude scale
                        Mw_sigma = 0.2 ; sd for moment magnitude scale
                        Mu = 30 ; in GPa
                        area = 400 ; patch area in km^2
                    prior = altar.cuda.distributions.uniform
                    prior:
                        support = (-0.5, 20)

        controller:
            sampler = altar.cuda.bayesian.metropolis
            archiver:
                output_dir = results/static ; output directory
                output_freq = 3 ; output frequency in beta steps

        monitors:
            ; profiling
            prof = altar.bayesian.profiler

       ; run configuration
       job.tasks = 1 ; number of tasks per host
       job.gpus = 1  ; number of gpus per task
       job.gpuprecision = float32 ; double(float64) or single(float32) precision for gpu computations
       ;job.gpuids = [0] ; a list gpu device ids for tasks on each host, default range(job.gpus)
       job.chains = 2**10 ; number of chains per task
       job.steps = 1000 ; MC burn-in steps for each beta step

       ; shell
       ; shell = mpi.shells.mpirun ; for running with mpi


    ; for parallel runs
    ; mpi.shells.mpirun # altar.plexus.shell:
        ; extra = -mca btl self,tcp

    ; end of file

ParameterSets(psets)
--------------------

A model usually consists of several parameter sets. For example, strike slips, dip slips, and insar ramps in the static model (you could use any name of your preference for each parameter set). The parameters will be arranged in orders in a theta matrix (samples, parameters) in simulation, which should be consistent with the provided Green's function. To enforce the order, users need to specify it in a ``psets_list`` trait at first ::

    psets_list = [strikeslip, dipslip]

Each parameter set has a ``count`` trait (e.g. the count of the strikeslip parameterset is the same as the number of patches), and a ``prior`` trait for its prior distribution, uniform/gaussian/truncated gaussian ... If the distribution to prepare/initialize samples is different, an additional ``prep`` trait can be used. For example, ::

    psets:
        strikeslip = altar.cuda.models.parameterset ;we won't need this after gpu/cpu code are merged
        strikeslip:
            count = {cudastatic.model.patches}
            prior = altar.cuda.distributions.gaussian ; we only need to say gaussian after gpu/cpu code are merged
            prior:
                mean = 0
                sigma = 0.5

For dip slips, we start with samples with their sum conforming to certain moment magnitude scale, and a moment distribution (combining Dirichlet and Gaussian distributions) is used as a ``prep`` ::

        dipslip:
            count = {cudastatic.model.patches}
            prep = altar.models.seismic.cuda.moment
            prep:
                support = (-0.5, 20) ; slip range
                Mw_mean = 7.3 ; mean moment magnitude scale
                Mw_sigma = 0.2 ; sd for moment magnitude scale
                Mu = 30 ; in GPa
                area = 400 ; patch area in km^2
            prior = altar.cuda.distributions.uniform
            prior:
                support = (-0.5, 20)


Inputs
------
HDF5 files (with suffix ``.h5``) are recommended since the metadata for each data set is included with h5 file, such as dimensions, precision. For static model, the support for ``.txt`` or ``.bin`` inputs from AlTar-1.1 is currently preserved.

A conversion tool ``H5Converter`` is provided if you need to convert any ``.txt`` or ``.bin`` files to ``.h5``.

Examples:
    * convert a text file to hdf5 ::

        H5Converter --inputs=static.gf.txt

    * convert a binary file to hdf5, additional precision (default=float32) and shape (default = 1d vector and will be reshaped to 2d in program if needed) information can be added ::

        H5Converter --inputs=kinematicG.gf.bin --precision='float32' --shape=[100,11000]

    * merge several files into one hdf5 ::

        H5Converter --inputs=[static.kernel.pertL1.txt,static.kernel.pertL2.txt] --output=static.kernel.h5

    * for more options ::

        H5Converter --help

job configurations
------------------

You only need to call ``cudaStatic`` to run the program, which handles multi-threads, multi-hosts by the job configuration in the script file.

Examples:
    * For single thread gpu job on GPU n ::

        ; run configuration
        job.tasks = 1 ; number of tasks per host
        job.gpus = 1  ; number of gpus per task
        job.gpuprecision = float32 ; double(float64) or single(float32) precision for gpu computations
        job.gpuids = [n] ; a list gpu device ids for tasks on each host, default range(job.gpus)

    * For multiple threads/gpus, the MPI shell should be enabled. If ``job.gpuids`` is not specified, the program will use the first n-GPUs. Otherwise, you could specify which GPUs are used (they could the same if you would like to share some tasks on the same GPU). For a 4-thread gpu job on GPUs 4,5,6,7 ::

        ; run configuration
        job.tasks = 4 ; number of tasks per host
        job.gpus = 1  ; number of gpus per task
        job.gpuprecision = float32 ; double(float64) or single(float32) precision for gpu computations
        job.gpuids = [4,5,6,7] ; a list gpu device ids for tasks on each host, default range(job.gpus)


        ; shell
        shell = mpi.shells.mpirun ; for running with mpi

You may also provide more options to the MPI shell,  ::

        ; for parallel runs
        mpi.shells.mpirun # altar.plexus.shell:
            extra = -mca btl self,tcp

Outputs
-------

The Bayesian sampling results are written to a directory specified under archiver ::

        controller:
            archiver:
                output_dir = results/static ; output directory
                output_freq = 3 ; output frequency in beta steps

while ``output_freq`` specifies how frequent (in beta steps) you prefer the sampling results are written to files. The final results will always be outputted.

Each output is in HDF5 format, with names ``step_nnn.h5``. ``nnn`` is the number of the beta step. The HDF5 includes three data groups, Annealer, ParameterSets, and Bayesian. Annealer group includes datasets which provide annealing information, such as beta, the covariance matrix for gaussian proposal. Parametersets group includes all parametersets. Instead of one big theta, we now sort them into different datasets according to their names, each data set has the dimension (samples, count). Bayesian group includes prior, datalikelihood, and posterior datasets (each has the dimension samples), which are Bayesian statistics for each sample.


.. _altar: https://github.com/AlTarFramework/altar
.. _altar cuda branch: https://github.com/lijun99/altar
.. _pyre: https://github.com/pyre/pyre
.. _pyre cuda branch: https://github.com/lijun99/pyre


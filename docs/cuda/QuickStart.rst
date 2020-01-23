
QuickStart
==========



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


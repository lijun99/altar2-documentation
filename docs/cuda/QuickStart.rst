.. _quickstart:

Using AlTar: A QuickStart
=========================

In this quickstart guide, we use a linear model example to demonstrate how to run AlTar.

To run AlTar simulations on a specific model, users can follow the following four steps:

#. Prepare a configuration file, e.g., `linear.pfg`, including various configurations to the model as well as the AlTar framework;
#. Prepare other input files for the model, e.g., for the linear model, the Green's function (`green.txt`), the observed data (`data.txt`), and the covariance (uncertainties or errors) of the observed data(`cd.txt`);
#. Run a dedicated python script (as a shell command) to invoke the AlTar application for the model, e.g., `linear` for the linear model.
#. Collect

The illustrated example is available as a jupyter notebook at `github <https://github.com/lijun99/altar2-documentation/tree/cuda/jupyter/linear>`_, and comes with the AlTar source, `${ALTAR_SRC_DIR}/models/linear/examples`, where `${ALTAR_SRC_DIR}` is the


Prepare the configuration file
------------------------------

AlTar 2.0

The configuration of components and traits can be assigned by a configuration file or as command line arguments.   Taking the ``linear`` application as an example, its configuration script ``linear.pfg`` appears as
::

    ; the application
    linear:
        ; the model
        model = linear
        ; the linear model configurations
        model:
            ; the directory for input files
            case = patch-9
            ; the number of parameters
            parameters = 18

            ; the number of observations
            observations = 108
            ; the data observations file
            data = data.txt
            ; the data covariance file
            cd = cd.txt

            ; prior distribution for parameters
            ; prior is used to calculate the prior probability
            ;    and check ranges during the simulation
            prior = gaussian
            ; prior configurations
            prior:
                parameters = {linear.model.parameters}
                center = 0.0
                sigma = 0.5
            ; prep is used to initialize the samples in the beginning of the simulation
            ; it can be different from prior
            prep = uniform
            prep:
                parameters = {linear.model.parameters}
                support = (-0.5, 0.5)

        ; run configuration
        job.tasks = 1 ; number of tasks per host
        job.gpus = 0  ; number of gpus per task
        job.chains = 2**10 ; number of chains per task

    ; end of file


Prepare input files
-------------------




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


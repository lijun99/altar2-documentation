.. _AlTar Framework:

###################
The AlTar Framework
###################

.. _Pyre Framework:

Pyre Framework
==============

Components
----------

One prominent feature of AlTar is that it allows users to configure all the public settings in a program at run time, through the ``components``-based Python programming introduced by pyre_. Components are configurable Python class variables which can be used to set a parameter, an array, or to choose an implementation of a certain functionality. Settings of components can be passed to the program as command line arguments, or more conveniently, by a configuration file.

Three types of configuration files are supported by pyre_/AlTar: ``.pml`` (XML-style), ``.cfg`` (an INI-style format used in AlTar 1.1), and ``.pfg`` (YAML/JSON-style). We recommend ``.pfg`` for its human-readable data serialization format.


.. _Pyre Config Format:

Pyre Config Format (``.pfg``)
-----------------------------

Some basic rules of ``.pfg`` format are

- If a component is not specified or listed in the configuration file, a default value/implementation specified in the Python program will be used instead.
- Strings such as paths, names, don't need quotation marks.
- Whitespace indentation is used for denoting structure, or hierarchy; however, tab characters are not allowed.
- Hierarchy of components can be specified by indentation, or by explicit full path, or by a combination of partial path with indentation. For example, these three configurations are equivalent:

.. code-block:: none

    ; method 1: all by indentation
    linear:
        job:
            tasks = 1
            gpus = 0
            chains = 2**10

    ; method 2: all by full path
    linear.job.tasks = 1
    linear.job.gpus = 0
    linear.job.chains = 2**10

    ; method 3: combination with partial path and indentation
    linear:
        job.tasks = 1
        job.gpus = 0
        job.chains = 2**10


Applications
============
:mod:`altar.shells.application`

An AlTar application is the main

The main components of an AlTar application consist of


* Controller/Annealer :mod:`altar.bayesian.Annealer`, which is the processor of the MCMC simulations of a post
* :mod:`altar.models.model`

Controller(default=annealer), which performs the MCMC simulation as prescribed by CATMIP. It also contains several components
Worker, which can be configured to run with single thread(default), multiple threads, CPU or GPU, and also keeps record of the simulation data such as $\theta$, prior/likelihood/posterior probabilities (in a CoolingStep object).
Sampler, which provides the sample updating process. The default sampler uses a Gaussian proposal and the Metropolis–Hastings algorithm for deciding acceptance/rejection of proposed samples.
Scheduler, which controls the annealing schedule (how $\beta$ evolves from 0 to 1). The default scheduler is based on the Coefficient of Variance (COV), adjusted to maintain 50% the effective sample size.
Model, which controls the data likelihood computation from a prescribed forward model and a set of observed data. Several geophysical models are included in the package. Users can also develop their own models to take advantage of the Bayesian framework.
Job, for users to configure the size of the simulations, such as the number of chains, the number of threads, whether to use GPU.
Rng, the random number generator to be used in other components.


Controller/Annealer
===================
:mod:`altar.bayesian.Annealer`


Worker/AnnealingMethod
----------------------

SequentialAnnealing
~~~~~~~~~~~~~~~~~~~

MPIAnnealing
~~~~~~~~~~~~

CUDAAnnealing
~~~~~~~~~~~~~


Sampler
-------

Metropolis
~~~~~~~~~~

AdaptiveMetropolis
~~~~~~~~~~~~~~~~~~

Schedular
---------










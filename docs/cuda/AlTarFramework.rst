###################
The AlTar Framework
###################

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










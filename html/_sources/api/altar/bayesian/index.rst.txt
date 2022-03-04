:mod:`altar.bayesian`
=====================

.. py:module:: altar.bayesian


Submodules
----------
.. toctree::
   :titlesonly:
   :maxdepth: 1

   Annealer/index.rst
   AnnealingMethod/index.rst
   Brent/index.rst
   COV/index.rst
   CUDAAnnealing/index.rst
   Controller/index.rst
   CoolingStep/index.rst
   Grid/index.rst
   H5Recorder/index.rst
   MPIAnnealing/index.rst
   Metropolis/index.rst
   Notifier/index.rst
   Profiler/index.rst
   Recorder/index.rst
   Sampler/index.rst
   Scheduler/index.rst
   SequentialAnnealing/index.rst
   Solver/index.rst
   ThreadedAnnealing/index.rst


Package Contents
----------------

Classes
~~~~~~~

.. autoapisummary::

   altar.bayesian.controller
   altar.bayesian.sampler
   altar.bayesian.scheduler
   altar.bayesian.monitor
   altar.bayesian.archiver
   altar.bayesian.solver



Functions
~~~~~~~~~

.. autoapisummary::

   altar.bayesian.annealer
   altar.bayesian.cov
   altar.bayesian.brent
   altar.bayesian.grid
   altar.bayesian.metropolis
   altar.bayesian.profiler
   altar.bayesian.recorder


.. py:class:: controller

   Bases: :class:`altar.protocol`

   The protocol that all AlTar controllers must implement

   .. attribute:: dispatcher
      

      

   .. attribute:: doc
      :annotation: = the event dispatcher that activates the registered handlers

      

   .. attribute:: archiver
      

      

   .. attribute:: doc
      :annotation: = the archiver of simulation state

      

   .. method:: posterior(self, model)

      Sample the posterior distribution of the given {model}


   .. method:: initialize(self, application)

      Initialize me and my parts given an {application} context


   .. method:: pyre_default(cls, **kwds)
      :classmethod:

      Supply a default implementation



.. py:class:: sampler

   Bases: :class:`altar.protocol`

   The protocol that all AlTar samplers must implement

   .. method:: initialize(self, application)

      Initialize me and my parts given an {application} context


   .. method:: samplePosterior(self, controller, step)

      Sample the posterior distribution


   .. method:: resample(self, controller, statistics)

      Update my statistics based on the results of walking my Markov chains


   .. method:: pyre_default(cls, **kwds)
      :classmethod:

      Supply a default implementation



.. py:class:: scheduler

   Bases: :class:`altar.protocol`

   The protocol that all AlTar schedulers must implement

   .. method:: initialize(self, application)

      Initialize me and my parts given an {application} context


   .. method:: update(self, step)

      Push {step} forward along the annealing schedule


   .. method:: updateTemperature(self, step)

      Generate the next temperature increment


   .. method:: computeCovariance(self, step)

      Compute the parameter covariance of the sample in the {step}


   .. method:: rank(self, step)

      Rebuild the sample and its statistics sorted by the likelihood of the parameter values


   .. method:: pyre_default(cls, **kwds)
      :classmethod:

      Supply a default implementation



.. py:class:: monitor

   Bases: :class:`altar.protocol`

   The protocol that all AlTar simulation monitors must implement

   Monitors respond to simulation events by generating user diagnostics to report progress

   .. method:: initialize(self, application)

      Initialize me given an {application} context


   .. method:: pyre_default(cls, **kwds)
      :classmethod:

      Supply a default implementation



.. py:class:: archiver

   Bases: :class:`altar.protocol`

   The protocol that all AlTar simulation archivers must implement

   Archivers persist intermediate simulation state and can be used to restart a simulation

   .. method:: initialize(self, application)

      Initialize me given an {application} context


   .. method:: record(self, step)

      Record the final state of the simulation


   .. method:: pyre_default(cls, **kwds)
      :classmethod:

      Supply a default implementation



.. py:class:: solver

   Bases: :class:`altar.protocol`

   The protocol that all δβ solvers must implement

   .. attribute:: tolerance
      

      

   .. attribute:: doc
      :annotation: = the fractional tolerance for achieving convergence

      

   .. method:: initialize(self, application, scheduler)

      Initialize me and my parts given an {application} context and a {scheduler}


   .. method:: solve(self, llk, weight)

      Compute the next temperature in the cooling schedule


   .. method:: pyre_default(cls, **kwds)
      :classmethod:

      Provide a default implementation



.. function:: annealer()


.. function:: cov()


.. function:: brent()


.. function:: grid()


.. function:: metropolis()


.. function:: profiler()


.. function:: recorder()



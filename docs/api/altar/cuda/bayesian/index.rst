:mod:`altar.cuda.bayesian`
==========================

.. py:module:: altar.cuda.bayesian


Submodules
----------
.. toctree::
   :titlesonly:
   :maxdepth: 1

   cudaAdaptiveMetropolis/index.rst
   cudaCoolingStep/index.rst
   cudaMetropolis/index.rst
   cudaMetropolisVaryingSteps/index.rst


Package Contents
----------------

Classes
~~~~~~~

.. autoapisummary::

   altar.cuda.bayesian.controller
   altar.cuda.bayesian.sampler
   altar.cuda.bayesian.scheduler



Functions
~~~~~~~~~

.. autoapisummary::

   altar.cuda.bayesian.metropolis
   altar.cuda.bayesian.metropolisvaryingsteps
   altar.cuda.bayesian.adaptivemetropolis


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



.. function:: metropolis()


.. function:: metropolisvaryingsteps()


.. function:: adaptivemetropolis()



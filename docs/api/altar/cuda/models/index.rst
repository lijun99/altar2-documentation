:mod:`altar.cuda.models`
========================

.. py:module:: altar.cuda.models


Submodules
----------
.. toctree::
   :titlesonly:
   :maxdepth: 1

   cudaBayesian/index.rst
   cudaBayesianEnsemble/index.rst
   cudaParameterEnsemble/index.rst
   cudaParameterSet/index.rst


Package Contents
----------------

.. py:class:: model

   Bases: :class:`altar.protocol`

   The protocol that all AlTar models must implement

   .. method:: posterior(self, application)


      Sample my posterior distribution


   .. method:: initialize(self, application)


      Initialize the state of the model given a {problem} specification


   .. method:: initializeSample(self, step)


      Fill {step.theta} with an initial random sample from my prior distribution.


   .. method:: priorLikelihood(self, step)


      Fill {step.prior} with the likelihoods of the samples in {step.theta} in the prior
      distribution


   .. method:: dataLikelihood(self, step)


      Fill {step.data} with the likelihoods of the samples in {step.theta} given the available
      data. This is what is usually referred to as the "forward model"


   .. method:: posteriorLikelihood(self, step)


      Given the {step.prior} and {step.data} likelihoods, compute a generalized posterior using
      {step.beta} and deposit the result in {step.post}


   .. method:: likelihoods(self, step)


      Convenience function that computes all three likelihoods at once given the current {step}
      of the problem


   .. method:: verify(self, step, mask)


      Check whether the samples in {step.theta} are consistent with the model requirements and
      update the {mask}, a vector with zeroes for valid samples and non-zero for invalid ones


   .. method:: top(self, annealer)


      Notification that a β step is about to start


   .. method:: bottom(self, annealer)


      Notification that a β step just ended


   .. method:: pyre_default(cls, **kwds)
      :classmethod:


      Supply a default implementation



.. py:class:: parameters

   Bases: :class:`altar.protocol`

   The protocol that all AlTar parameter sets must implement

   .. attribute:: count
      

      

   .. attribute:: doc
      :annotation: = the number of parameters in this set

      

   .. attribute:: prior
      

      

   .. attribute:: doc
      :annotation: = the prior distribution

      

   .. attribute:: prep
      

      

   .. attribute:: doc
      :annotation: = the distribution to use to initialize this parameter set

      

   .. method:: initialize(self, model, offset)


      Initialize the parameter set given the {model} that owns it


   .. method:: initializeSample(self, theta)


      Fill {theta} with an initial random sample from my prior distribution.


   .. method:: priorLikelihood(self, theta, priorLLK)


      Fill {priorLLK} with the likelihoods of the samples in {theta} in my prior distribution


   .. method:: verify(self, theta, mask)


      Check whether the samples in {theta} are consistent with the model requirements and update
      the {mask}, a vector with zeroes for valid samples and non-zero for invalid ones


   .. method:: pyre_default(cls, **kwds)
      :classmethod:


      Supply a default implementation



.. function:: bayesian()


.. function:: bayesianensemble()


.. function:: parameterset()



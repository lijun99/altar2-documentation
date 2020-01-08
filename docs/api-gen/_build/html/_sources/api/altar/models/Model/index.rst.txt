:mod:`altar.models.Model`
=========================

.. py:module:: altar.models.Model


Module Contents
---------------

.. py:class:: Model

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




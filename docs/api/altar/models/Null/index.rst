:mod:`altar.models.Null`
========================

.. py:module:: altar.models.Null


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   altar.models.Null.Null



.. py:class:: Null(name, locator, **kwds)

   Bases: :class:`altar.models.Bayesian.Bayesian`

   A trivial model that can be used as a base class for deriving interesting ones

   .. attribute:: parameters
      

      

   .. attribute:: doc
      :annotation: = the number of model degrees of freedom

      

   .. method:: initializeSample(self, step)

      Fill {step.θ} with an initial random sample from my prior distribution


   .. method:: priorLikelihood(self, step)

      Fill {step.prior} with the likelihoods of the samples in {step.theta} in the prior
      distribution


   .. method:: dataLikelihood(self, step)

      Fill {step.data} with the likelihoods of the samples in {step.theta} given the available
      data. This is what is usually referred to as the "forward model"


   .. method:: verify(self, step, mask)

      Check whether the samples in {step.theta} are consistent with the model requirements and
      update the {mask}, a vector with zeroes for valid samples and non-zero for invalid ones


   .. method:: forwardProblem(self, application, theta=None)

      Perform the forward modeling with given {theta}




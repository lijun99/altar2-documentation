:mod:`altar.models.emhp.EMHP`
=============================

.. py:module:: altar.models.emhp.EMHP


Module Contents
---------------

.. py:class:: EMHP

   Bases: :class:`altar.models.bayesian`

   A diagnostic tool

   .. method:: initialize(self, application)


      Initialize the state of the model given a {problem} specification


   .. method:: initializeSample(self, step)


      File {step.theta} with an initial random sample form my prior distribution


   .. method:: priorLikelihood(self, step)


      Fill {step.prior} with the likelihoods of the samples in {step.theta} in the prior
      distribution


   .. method:: dataLikelihood(self, step)


      Fill {step.data} with the likelihoods of the samples in {step.theta} given the available
      data. This is what is usually referred to as the "forward model"


   .. method:: verify(self, step, mask)


      Check whether the samples in {step.theta} are consistent with the model requirements and
      update the {mask}, a vector with zeroes for valid samples and non-zero for invalid ones




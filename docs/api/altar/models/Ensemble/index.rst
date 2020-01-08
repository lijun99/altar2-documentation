:mod:`altar.models.Ensemble`
============================

.. py:module:: altar.models.Ensemble


Module Contents
---------------

.. py:class:: Ensemble

   Bases: :class:`altar.models.Bayesian.Bayesian`

   A collection of AlTar models that comprise a single model

   .. attribute:: models
      

      

   .. attribute:: doc
      :annotation: = the collection of models in this ensemble

      

   .. method:: initialize(self, application)


      Initialize the state of the model given an {application} context


   .. method:: initializeSample(self, step)


      Fill {step.theta} with an initial random sample from my prior distribution.


   .. method:: priorLikelihood(self, step)


      Fill {step.prior} with the likelihoods of the samples in {step.theta} in the prior
      distribution


   .. method:: dataLikelihood(self, step)


      Fill {step.data} with the likelihoods of the samples in {step.theta} given the available
      data. This is what is usually referred to as the "forward model"


   .. method:: verify(self, step, mask)


      Check whether the samples in {step.theta} are consistent with the model requirements and
      update the {mask}, a vector with zeroes for valid samples and non-zero for invalid ones




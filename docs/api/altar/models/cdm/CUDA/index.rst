:mod:`altar.models.cdm.CUDA`
============================

.. py:module:: altar.models.cdm.CUDA


Module Contents
---------------

.. py:class:: CUDA

   A strategy for computing the data log likelihood that is written in pure python

   .. attribute:: source
      

      

   .. method:: initialize(self, application, model)


      Initialize the strategy with {model} information


   .. method:: dataLikelihood(self, model, step)


      Fill {step.data} with the likelihoods of the samples in {step.theta} given the available
      data.




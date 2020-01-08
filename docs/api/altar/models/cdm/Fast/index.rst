:mod:`altar.models.cdm.Fast`
============================

.. py:module:: altar.models.cdm.Fast


Module Contents
---------------

.. py:class:: Fast

   A strategy for computing the data log likelihood that is written in pure python

   .. attribute:: source
      

      

   .. method:: initialize(self, model, **kwds)


      Initialize the strategy with {model} information


   .. method:: dataLikelihood(self, model, step)


      Fill {step.data} with the likelihoods of the samples in {step.theta} given the available
      data.




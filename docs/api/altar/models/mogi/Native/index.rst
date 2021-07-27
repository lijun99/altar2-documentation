:mod:`altar.models.mogi.Native`
===============================

.. py:module:: altar.models.mogi.Native


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   altar.models.mogi.Native.Native



.. py:class:: Native

   A strategy for computing the data log likelihood that is written in pure python

   .. method:: initialize(self, **kwds)

      Initialize the strategy


   .. method:: dataLikelihood(self, model, step)

      Fill {step.data} with the likelihoods of the samples in {step.theta} given the available
      data.




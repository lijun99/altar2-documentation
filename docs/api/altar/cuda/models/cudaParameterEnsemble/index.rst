:mod:`altar.cuda.models.cudaParameterEnsemble`
==============================================

.. py:module:: altar.cuda.models.cudaParameterEnsemble


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   altar.cuda.models.cudaParameterEnsemble.cudaParameterEnsemble



.. py:class:: cudaParameterEnsemble

   Bases: :class:`altar.cuda.models.cudaParameter.cudaParameter`

   An Ensemble of parameter sets

   .. attribute:: psets
      

      

   .. attribute:: doc
      :annotation: = an ensemble of parameter sets in the model

      

   .. method:: initialize(self, application)

      Initialize my distributions


   .. method:: cuInitialize(self, application)

      cuda initialize


   .. method:: cuInitSample(self, theta, batch=None)

      Fill {theta} with an initial random sample from my prior distribution.


   .. method:: cuEvalPrior(self, theta, prior, batch=None)

      Fill {priorLLK} with the log likelihoods of the samples in {theta} in my prior distribution


   .. method:: cuVerify(self, theta, mask, batch=None)

      Check whether the samples in {step.theta} are consistent with the model requirements and
      update the {mask}, a vector with zeroes for valid samples and non-zero for invalid ones




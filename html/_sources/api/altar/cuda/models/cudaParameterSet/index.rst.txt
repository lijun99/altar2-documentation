:mod:`altar.cuda.models.cudaParameterSet`
=========================================

.. py:module:: altar.cuda.models.cudaParameterSet


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   altar.cuda.models.cudaParameterSet.cudaParameterSet



.. py:class:: cudaParameterSet(name, locator, **kwds)

   Bases: :class:`altar.models.Contiguous.Contiguous`

   A contiguous parameter set

   .. attribute:: count
      

      

   .. attribute:: doc
      :annotation: = the number of parameters in this set

      

   .. attribute:: prior
      

      

   .. attribute:: doc
      :annotation: = the prior distribution

      

   .. attribute:: prep
      

      

   .. attribute:: doc
      :annotation: = the distribution to use to initialize this parameter set

      

   .. attribute:: offset
      :annotation: = 0

      

   .. method:: cuInitialize(self, application)

      cuda initialization


   .. method:: cuInitSample(self, theta, batch=None)

      Fill {theta} with an initial random sample from my prior distribution.


   .. method:: cuEvalPrior(self, theta, prior, batch=None)

      Fill {priorLLK} with the log likelihoods of the samples in {theta} in my prior distribution


   .. method:: cuVerify(self, theta, mask, batch=None)

      Check whether the samples in {step.theta} are consistent with the model requirements and
      update the {mask}, a vector with zeroes for valid samples and non-zero for invalid ones


   .. method:: cuRestrict(self, theta)

      Return my portion of the sample matrix {theta}




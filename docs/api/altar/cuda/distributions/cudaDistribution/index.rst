:mod:`altar.cuda.distributions.cudaDistribution`
================================================

.. py:module:: altar.cuda.distributions.cudaDistribution


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   altar.cuda.distributions.cudaDistribution.cudaDistribution



.. py:class:: cudaDistribution(name, locator, **kwds)

   Bases: :class:`altar.distributions.Base.Base`

   The base class for probability distributions

   .. attribute:: parameters
      

      

   .. attribute:: doc
      :annotation: = the number of model parameters that belong to me

      

   .. attribute:: offset
      

      

   .. attribute:: doc
      :annotation: = the starting point of my parameters in the overall model state

      

   .. attribute:: device
      

      

   .. attribute:: idx_range
      

      

   .. attribute:: precision
      

      

   .. method:: initialize(self, rng)

      Initialize with the given random number generator


   .. method:: verify(self, theta, mask)

      Check whether my portion of the samples in {theta} are consistent with my constraints, and
      update {mask}, a vector with zeroes for valid samples and non-zero for invalid ones


   .. method:: cuInitialize(self, application)

      cuda specific initialization


   .. method:: cuInitSample(self, theta)

      cuda process to initialize random samples


   .. method:: cuVerify(self, theta, mask)

      cuda process to verify the validity of samples


   .. method:: cuEvalPrior(self, theta, prior)

      cuda process to compute the prior




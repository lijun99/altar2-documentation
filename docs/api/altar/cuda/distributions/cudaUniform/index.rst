:mod:`altar.cuda.distributions.cudaUniform`
===========================================

.. py:module:: altar.cuda.distributions.cudaUniform


Module Contents
---------------

.. py:class:: cudaUniform

   Bases: :class:`altar.cuda.distributions.cudaDistribution.cudaDistribution`

   The cuda uniform probability distribution

   .. attribute:: support
      

      

   .. attribute:: doc
      :annotation: = the support interval of the prior distribution

      

   .. method:: cuInitSample(self, theta)


      Fill my portion of {theta} with initial random values from my distribution.


   .. method:: cuVerify(self, theta, mask)


      Check whether my portion of the samples in {theta} are consistent with my constraints, and
      update {mask}, a vector with zeroes for valid samples and non-zero for invalid ones
      Arguments:
          theta cuArray (samples x total_parameters)


   .. method:: cuEvalPrior(self, theta, prior, batch)


      Fill my portion of {likelihood} with the likelihoods of the samples in {theta}




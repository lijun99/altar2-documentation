:mod:`altar.cuda.distributions.cudaGaussian`
============================================

.. py:module:: altar.cuda.distributions.cudaGaussian


Module Contents
---------------

.. py:class:: cudaGaussian

   Bases: :class:`altar.cuda.distributions.cudaDistribution.cudaDistribution`

   The cuda gaussian probability distribution

   .. attribute:: mean
      

      

   .. attribute:: doc
      :annotation: = the mean value

      

   .. attribute:: sigma
      

      

   .. attribute:: doc
      :annotation: =  the standard deviation

      

   .. method:: cuInitSample(self, theta)


      Fill my portion of {theta} with initial random values from my distribution.


   .. method:: cuVerify(self, theta, mask)


      Check whether my portion of the samples in {theta} are consistent with my constraints, and
      update {mask}, a vector with zeroes for valid samples and non-zero for invalid ones
      Arguments:
          theta cuArray (samples x total_parameters)   


   .. method:: cuEvalPrior(self, theta, prior, batch)


      Fill my portion of {likelihood} with the likelihoods of the samples in {theta}




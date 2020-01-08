:mod:`altar.bayesian.Metropolis`
================================

.. py:module:: altar.bayesian.Metropolis


Module Contents
---------------

.. py:class:: Metropolis

   Bases: :class:`altar.component`

   The Metropolis algorithm as a sampler of the posterior distribution

   .. attribute:: scaling
      

      

   .. attribute:: doc
      :annotation: = the parameter covariance Σ is scaled by the square of this

      

   .. attribute:: acceptanceWeight
      

      

   .. attribute:: doc
      :annotation: = the weight of accepted samples during covariance rescaling

      

   .. attribute:: rejectionWeight
      

      

   .. attribute:: doc
      :annotation: = the weight of rejected samples during covariance rescaling

      

   .. attribute:: steps
      :annotation: = 1

      

   .. attribute:: uniform
      

      

   .. attribute:: uninormal
      

      

   .. attribute:: sigma_chol
      

      

   .. attribute:: dispatcher
      

      

   .. method:: initialize(self, application)


      Initialize me and my parts given an {application} context


   .. method:: samplePosterior(self, annealer, step)


      Sample the posterior distribution


   .. method:: resample(self, annealer, statistics)


      Update my statistics based on the results of walking my Markov chains


   .. method:: prepareSamplingPDF(self, annealer, step)


      Re-scale and decompose the parameter covariance matrix, in preparation for the
      Metropolis update


   .. method:: walkChains(self, annealer, step)


      Run the Metropolis algorithm on the Markov chains


   .. method:: displace(self, sample)


      Construct a set of displacement vectors for the random walk from a distribution with zero
      mean and my covariance


   .. method:: adjustCovarianceScaling(self, accepted, rejected, unlikely)


      Compute a new value for the covariance sacling factor based on the acceptance/rejection
      ratio




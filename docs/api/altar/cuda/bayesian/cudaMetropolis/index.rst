:mod:`altar.cuda.bayesian.cudaMetropolis`
=========================================

.. py:module:: altar.cuda.bayesian.cudaMetropolis


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   altar.cuda.bayesian.cudaMetropolis.cudaMetropolis



.. py:class:: cudaMetropolis(name, locator, **kwds)

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

      

   .. attribute:: useFixedScaling
      

      

   .. attribute:: doc
      :annotation: = whether to use a fixed scaling

      

   .. attribute:: scalingMin
      

      

   .. attribute:: doc
      :annotation: = the minimum value of the scaling factor

      

   .. attribute:: scalingMax
      

      

   .. attribute:: doc
      :annotation: = the maximum value of the scaling factor

      

   .. attribute:: mcsteps
      :annotation: = 1

      

   .. attribute:: dispatcher
      

      

   .. attribute:: ginit
      :annotation: = False

      

   .. attribute:: gstep
      

      

   .. attribute:: gcandidate
      

      

   .. attribute:: gproposal
      

      

   .. attribute:: gsigma_chol
      

      

   .. attribute:: gvalid_indices
      

      

   .. attribute:: gvalid_samples
      

      

   .. attribute:: ginvalid_flags
      

      

   .. attribute:: gacceptance_flags
      

      

   .. attribute:: precision
      

      

   .. attribute:: gdice
      

      

   .. attribute:: curng
      

      

   .. method:: initialize(self, application)

      Initialize me and my parts given an {application} context


   .. method:: cuInitialize(self, application)


   .. method:: samplePosterior(self, annealer, step)

      Sample the posterior distribution
      :param annealer - the controller:
      :param step - cpu CoolingStep:

      :returns: statistics (accepted/rejected/invalid) or (accepted/unlikely/rejected)


   .. method:: resample(self, annealer, statistics)

      Update my statistics based on the results of walking my Markov chains


   .. method:: prepareSamplingPDF(self, annealer, step)

      Re-scale and decompose the parameter covariance matrix, in preparation for the
      Metropolis update


   .. method:: finishSamplingPDF(self, step)

      procedures after sampling, e.g, copy data back to cpu


   .. method:: walkChains(self, annealer, step)

      Run the Metropolis algorithm on the Markov chains
      :param annealer: cudaAnnealer
      :param step: cudaCoolingStep

      :returns: statistics = (accepted, rejected, unlikely)


   .. method:: displace(self, displacement)

      Construct a set of displacement vectors for the random walk from a distribution with zero
      mean and my covariance


   .. method:: adjustCovarianceScaling(self, accepted, invalid, rejected)

      Compute a new value for the covariance sacling factor based on the acceptance/rejection
      ratio


   .. method:: allocateGPUData(self, samples, parameters)

      initialize gpu work data




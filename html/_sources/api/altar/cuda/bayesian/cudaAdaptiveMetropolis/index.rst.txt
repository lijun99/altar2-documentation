:mod:`altar.cuda.bayesian.cudaAdaptiveMetropolis`
=================================================

.. py:module:: altar.cuda.bayesian.cudaAdaptiveMetropolis


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   altar.cuda.bayesian.cudaAdaptiveMetropolis.cudaAdaptiveMetropolis



.. py:class:: cudaAdaptiveMetropolis(name, locator, **kwds)

   Bases: :class:`altar.component`

   The Adaptive Metropolis algorithm from Thomas Catanach
   Compared with traditional MCMC, there are two modifications:
   1. After certain steps (corr_check_steps), the correlation between the current and the starting samples
   is computed. If the correlation is less than a threshold value (target_correlation), i.e., the chains are
   effectively de-correlated, the MCMC stops. max_mc_steps provides a maximum MCMC step
   2. The scaling factor (scaling) targets an optimal acceptance rate

   .. attribute:: scaling
      

      

   .. attribute:: doc
      :annotation: = scaling factor σ  for Gaussian proposal  ~ N(0, σ^2 Σ), initial value 2.38/sqrt(N_d)

      

   .. attribute:: scaling_min
      

      

   .. attribute:: doc
      :annotation: = the minimum value of the scaling factor

      

   .. attribute:: scaling_max
      

      

   .. attribute:: doc
      :annotation: = the maximum value of the scaling factor

      

   .. attribute:: parameters
      

      

   .. attribute:: doc
      :annotation: = total number of parameters N_d

      

   .. attribute:: target_acceptance_rate
      

      

   .. attribute:: doc
      :annotation: = the targeted acceptance rate

      

   .. attribute:: gain
      

      

   .. attribute:: doc
      :annotation: = Feedback gain constant

      

   .. attribute:: max_mc_steps
      

      

   .. attribute:: doc
      :annotation: = the maximum Monte-Carlo steps for one beta step

      

   .. attribute:: min_mc_steps
      

      

   .. attribute:: doc
      :annotation: = the minimum Monte-Carlo steps for one beta step

      

   .. attribute:: max_mc_steps_stage2
      

      

   .. attribute:: doc
      :annotation: = the maximum Monte-Carlo steps at stage 2, or beta> beta_stage2

      

   .. attribute:: beta_stage2
      

      

   .. attribute:: doc
      :annotation: = beta value to start stage 2, i.e., to use a different max_mc_steps

      

   .. attribute:: corr_check_steps
      

      

   .. attribute:: doc
      :annotation: = the Monte-Carlo steps to compute the de

      

   .. attribute:: target_correlation
      

      

   .. attribute:: doc
      :annotation: = the threshold of correlation to stop the chain

      

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


   .. method:: gainFunction(x)
      :staticmethod:

      Compute the optimal gain constant from a target acceptranceRate {x}




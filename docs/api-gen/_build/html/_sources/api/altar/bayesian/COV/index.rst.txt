:mod:`altar.bayesian.COV`
=========================

.. py:module:: altar.bayesian.COV


Module Contents
---------------

.. py:class:: COV

   Bases: :class:`altar.component`

   Annealing schedule based on attaining a particular value for the coefficient of variation
   (COV) of the data likelihood; after Ching[2007].

   The goal is to compute a proposed update δβ_m to the temperature β_m such that the vector
   of weights w_m given by

       w_m := π(D|θ_m)^{δβ_m}

   has a particular target value for

       COV(w_m) := <w_m> / \sqrt{<(w_m-<w_m>)^2>}

   .. attribute:: target
      

      

   .. attribute:: doc
      :annotation: = the target value for COV

      

   .. attribute:: solver
      

      

   .. attribute:: doc
      :annotation: = the δβ solver

      

   .. attribute:: check_positive_definiteness
      

      

   .. attribute:: doc
      :annotation: = whether to check the positive definiteness of Σ matrix and condition it accordingly

      

   .. attribute:: min_eigenvalue_ratio
      

      

   .. attribute:: doc
      :annotation: = the desired minimal eigenvalue of Σ matrix, as a ratio to the max eigenvalue

      

   .. attribute:: w
      

      

   .. attribute:: cov
      :annotation: = 0.0

      

   .. attribute:: uniform
      

      

   .. attribute:: rng
      

      

   .. method:: initialize(self, application)


      Initialize me and my parts given an {application} context


   .. method:: update(self, step)


      Push {step} forward along the annealing schedule


   .. method:: updateTemperature(self, step)


      Generate the next temperature increment


   .. method:: computeCovariance(self, step)


      Compute the parameter covariance Σ of the sample in {step}

        Σ = c_m^2 \sum_{i \in samples}        ilde{w}_{i} θ_i θ_i^T} - ar{θ} ar{θ}^Τ

      where

        ar{θ} = \sum_{i \in samples}         ilde{w}_{i} θ_{i}

      The covariance Σ gets used to build a proposal pdf for the posterior


   .. method:: rank(self, step)


      Rebuild the sample and its statistics sorted by the likelihood of the parameter values


   .. method:: resampling(self, step)


      Rebuild the sample and its statistics sorted by the likelihood of the parameter values


   .. method:: conditionCovariance(self, Σ)


      Make sure the covariance matrix Σ is symmetric and positive definite


   .. method:: computeSampleMultiplicities(self, step)


      Prepare a frequency vector for the new samples given the scaled data log-likelihood in
      {w} for this cooling step


   .. method:: buildHistogramRanges(self, w)


      Build histogram bins based on the scaled data log-likelihood




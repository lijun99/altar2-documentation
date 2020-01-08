:mod:`altar.models.gaussian.Gaussian`
=====================================

.. py:module:: altar.models.gaussian.Gaussian


Module Contents
---------------

.. py:class:: Gaussian(**kwds)

   Bases: :class:`altar.models.bayesian`

   A model that emulates the probability density for a single observation of the model
   parameters. The observation is treated as normally distributed around a given mean, with a
   covariance constructed out of its eigenvalues and a rotation in configuration
   space. Currently, only two dimensional parameter spaces are supported.

   .. attribute:: parameters
      

      

   .. attribute:: doc
      :annotation: = the number of model degrees of freedom

      

   .. attribute:: support
      

      

   .. attribute:: doc
      :annotation: = the support interval of the prior distribution

      

   .. attribute:: prep
      

      

   .. attribute:: doc
      :annotation: = the distribution used to generate the initial sample

      

   .. attribute:: prior
      

      

   .. attribute:: doc
      :annotation: = the prior distribution

      

   .. attribute:: μ
      

      

   .. attribute:: doc
      :annotation: = the location of the central value of the observation

      

   .. attribute:: λ
      

      

   .. attribute:: doc
      :annotation: = the eigenvalues of the covariance matrix

      

   .. attribute:: φ
      

      

   .. attribute:: doc
      :annotation: = the orientation of the covariance semi-major axis

      

   .. attribute:: peak
      

      

   .. attribute:: σ_inv
      

      

   .. attribute:: normalization
      :annotation: = 1

      

   .. method:: initialize(self, application)


      Initialize the state of the model given a {problem} specification


   .. method:: initializeSample(self, step)


      Fill {step.θ} with an initial random sample from my prior distribution.


   .. method:: priorLikelihood(self, step)


      Fill {step.prior} with the likelihoods of the samples in {step.theta} in the prior
      distribution


   .. method:: dataLikelihood(self, step)


      Fill {step.data} with the likelihoods of the samples in {step.theta} given the available
      data. This is what is usually referred to as the "forward model"


   .. method:: verify(self, step, mask)


      Check whether the samples in {step.theta} are consistent with the model requirements and
      update the {mask}, a vector with zeroes for valid samples and non-zero for invalid ones




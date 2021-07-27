:mod:`altar.models.linear.Linear`
=================================

.. py:module:: altar.models.linear.Linear


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   altar.models.linear.Linear.Linear



.. py:class:: Linear(name, locator, **kwds)

   Bases: :class:`altar.models.bayesian`

   
   .. attribute:: parameters
      

      

   .. attribute:: doc
      :annotation: = the number of parameters in the model

      

   .. attribute:: observations
      

      

   .. attribute:: doc
      :annotation: = the number of data samples

      

   .. attribute:: prep
      

      

   .. attribute:: default
      

      

   .. attribute:: doc
      :annotation: = the distribution used to generate the initial sample

      

   .. attribute:: prior
      

      

   .. attribute:: default
      

      

   .. attribute:: doc
      :annotation: = the prior distribution

      

   .. attribute:: norm
      

      

   .. attribute:: default
      

      

   .. attribute:: doc
      :annotation: = the norm to use when computing the data log likelihood

      

   .. attribute:: case
      

      

   .. attribute:: doc
      :annotation: = the directory with the input files

      

   .. attribute:: green
      

      

   .. attribute:: doc
      :annotation: = the name of the file with the Green functions

      

   .. attribute:: data
      

      

   .. attribute:: doc
      :annotation: = the name of the file with the observations

      

   .. attribute:: cd
      

      

   .. attribute:: doc
      :annotation: = the name of the file with the data covariance matrix

      

   .. attribute:: ifs
      

      

   .. attribute:: G
      

      

   .. attribute:: d
      

      

   .. attribute:: Cd
      

      

   .. attribute:: Cd_inv
      

      

   .. attribute:: residuals
      

      

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


   .. method:: mountInputDataspace(self, pfs)

      Mount the directory with my input files


   .. method:: loadInputs(self)

      Load the data in the input files into memory


   .. method:: computeCovarianceInverse(self, cd)

      Compute the inverse of the data covariance matrix


   .. method:: computeNormalization(self, observations, cd)

      Compute the normalization of the L2 norm


   .. method:: initializeResiduals(self, samples, data)

      Prime the matrix that will hold the residuals (G θ - d) for each sample by duplicating the
      observation vector as many times as there are samples




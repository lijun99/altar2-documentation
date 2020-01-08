:mod:`altar.models.seismic.Static`
==================================

.. py:module:: altar.models.seismic.Static


Module Contents
---------------

.. py:class:: Static

   Bases: :class:`altar.models.bayesian`

   Static inversion with cuda  (d = G theta)
   Modeled as N patches with dip and slip displacements  

   .. attribute:: parametersets
      

      

   .. attribute:: doc
      :annotation: = the set of parameters in the model

      

   .. attribute:: parameters
      

      

   .. attribute:: doc
      :annotation: = total number of parameters in the model

      

   .. attribute:: observations
      

      

   .. attribute:: doc
      :annotation: = the number of data samples

      

   .. attribute:: patches
      

      

   .. attribute:: norm
      

      

   .. attribute:: default
      

      

   .. attribute:: doc
      :annotation: = the norm to use when computing the data log likelihood

      

   .. attribute:: case
      

      

   .. attribute:: doc
      :annotation: = the directory with the input files

      

   .. attribute:: green_file
      

      

   .. attribute:: doc
      :annotation: = the name of the file with the Green functions

      

   .. attribute:: data_file
      

      

   .. attribute:: doc
      :annotation: = the name of the file with the observations

      

   .. attribute:: cd_file
      

      

   .. attribute:: doc
      :annotation: = the name of the file with the data covariance matrix

      

   .. attribute:: output_path
      

      

   .. attribute:: ifs
      

      

   .. attribute:: G
      

      

   .. attribute:: d
      

      

   .. attribute:: Cd
      

      

   .. attribute:: Cd_inv
      

      

   .. attribute:: residuals
      

      

   .. attribute:: normalization
      :annotation: = 1

      

   .. attribute:: processor
      :annotation: = cpu

      

   .. method:: initialize(self, application)


      Initialize the state of the model given a {problem} specification


   .. method:: initializeSample(self, step)


      Fill {step.θ} with an initial random sample from my prior distribution.


   .. method:: computePrior(self, step)


      Fill {step.prior} with the densities of the samples in {step.theta} in the prior
      distribution


   .. method:: computeDataLikelihood(self, step)


      Fill {step.data} with the densities of the samples in {step.theta} given the available
      data. This is what is usually referred to as the "forward model"


   .. method:: verify(self, step, mask)


      Check whether the samples in {step.theta} are consistent with the model requirements and
      update the {mask}, a vector with zeroes for valid samples and non-zero for invalid ones


   .. method:: initializeParameterSets(self)


      Initialize the parameter set


   .. method:: mountInputDataspace(self, pfs)


      Mount the directory with my input files


   .. method:: loadInputs(self)


      Load the data in the input files into memory


   .. method:: initializeCovariance(self, samples)


      Compute the Cholesky decomposition of the inverse of the data covariance
      and merge it to data


   .. method:: computeCovarianceInverse(self, cd)


      Compute the inverse of the data covariance matrix


   .. method:: computeNormalization(self, observations, cd)


      Compute the normalization of the L2 norm


   .. method:: initializeResiduals(self, samples, data)


      Prime the matrix that will hold the residuals (G θ - d) for each sample by duplicating the
      observation vector as many times as there are samples


   .. method:: update(self, annealer)


      Model updating at the bottom of each annealing step
      Output step data


   .. method:: forwardModel(theta, green, data_residuals=None, data_observations=None, batches=None)


      Forward model: compute data prediction or data residuals from a set of theta 
      Args: 
          theta [in, cuarray] parameters with shape=(samples, parameters)
          green [in, cuarray] Green's function with shape = (observations, parameters)
          batches [in, integer, optional] number of samples needto be computed <=samples
          data_observations [in, cuarray, optional] data observations
          data_residuals[inout, cuarray, optional] data predictions or residuals shape=(observations, samples)
      Returns:
          data predictions or residuals if data_observations is provides 




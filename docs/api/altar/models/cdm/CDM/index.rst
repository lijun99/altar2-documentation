:mod:`altar.models.cdm.CDM`
===========================

.. py:module:: altar.models.cdm.CDM


Module Contents
---------------

.. py:class:: CDM

   Bases: :class:`altar.models.bayesian`

   An implementation of the Compound Dislocation Model, Nikhoo et al. [2017]

   .. attribute:: psets
      

      

   .. attribute:: doc
      :annotation: = the model parameter meta-data

      

   .. attribute:: observations
      

      

   .. attribute:: doc
      :annotation: = the number of model degrees of freedom

      

   .. attribute:: norm
      

      

   .. attribute:: default
      

      

   .. attribute:: doc
      :annotation: = the norm to use when computing the data log likelihood

      

   .. attribute:: case
      

      

   .. attribute:: doc
      :annotation: = the directory with the input files

      

   .. attribute:: displacements
      

      

   .. attribute:: doc
      :annotation: = the name of the file with the displacements

      

   .. attribute:: covariance
      

      

   .. attribute:: doc
      :annotation: = the name of the file with the data covariance

      

   .. attribute:: nu
      

      

   .. attribute:: doc
      :annotation: = the Poisson ratio

      

   .. attribute:: mode
      

      

   .. attribute:: doc
      :annotation: = the implementation strategy

      

   .. attribute:: validators
      

      

   .. attribute:: parameters
      :annotation: = 0

      

   .. attribute:: strategy
      

      

   .. attribute:: ifs
      

      

   .. attribute:: d
      

      

   .. attribute:: los
      

      

   .. attribute:: oid
      

      

   .. attribute:: points
      

      

   .. attribute:: cd
      

      

   .. attribute:: xIdx
      :annotation: = 0

      

   .. attribute:: yIdx
      :annotation: = 0

      

   .. attribute:: dIdx
      :annotation: = 0

      

   .. attribute:: openingIdx
      :annotation: = 0

      

   .. attribute:: aXIdx
      :annotation: = 0

      

   .. attribute:: aYIdx
      :annotation: = 0

      

   .. attribute:: aZIdx
      :annotation: = 0

      

   .. attribute:: omegaXIdx
      :annotation: = 0

      

   .. attribute:: omegaYIdx
      :annotation: = 0

      

   .. attribute:: omegaZIdx
      :annotation: = 0

      

   .. attribute:: offsetIdx
      :annotation: = 0

      

   .. attribute:: cd_inv
      

      

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


   .. method:: initializeParameterSets(self)


      Initialize my parameter sets


   .. method:: mountInputDataspace(self, pfs)


      Mount the directory with my input files


   .. method:: loadInputs(self)


      Load the data in the input files into memory


   .. method:: computeNormalization(self)


      Compute the normalization of the L2 norm


   .. method:: computeCovarianceInverse(self)


      Compute the inverse of my data covariance


   .. method:: meta(self)


      Persist the sample layout by recording the parameter set metadata


   .. method:: show(self, job, channel)


      Place model information in the supplied {channel}




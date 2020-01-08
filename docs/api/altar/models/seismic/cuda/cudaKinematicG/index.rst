:mod:`altar.models.seismic.cuda.cudaKinematicG`
===============================================

.. py:module:: altar.models.seismic.cuda.cudaKinematicG


Module Contents
---------------

.. py:class:: cudaKinematicG

   Bases: :class:`altar.cuda.models.cudaBayesian.cudaBayesian`

   KinematicG model with cuda

   .. attribute:: dataobs
      

      

   .. attribute:: default
      

      

   .. attribute:: doc
      :annotation: = the observed data

      

   .. attribute:: green
      

      

   .. attribute:: doc
      :annotation: = the name of the file with the Green functions

      

   .. attribute:: Nas
      

      

   .. attribute:: doc
      :annotation: = number of patches along strike direction

      

   .. attribute:: Ndd
      

      

   .. attribute:: doc
      :annotation: = number of patches along dip direction

      

   .. attribute:: Nmesh
      

      

   .. attribute:: doc
      :annotation: = number of mesh points for each patch for fastsweeping

      

   .. attribute:: dsp
      

      

   .. attribute:: doc
      :annotation: = the distance unit for each patch, in km

      

   .. attribute:: Nt
      

      

   .. attribute:: doc
      :annotation: = number of time intervals for kinematic process

      

   .. attribute:: Npt
      

      

   .. attribute:: doc
      :annotation: = number of mesh points for each time interval for fastsweeping

      

   .. attribute:: dt
      

      

   .. attribute:: doc
      :annotation: = the time unit for each time interval (in s)

      

   .. attribute:: t0s
      

      

   .. attribute:: doc
      :annotation: = the start time for each patch

      

   .. attribute:: cmodel
      

      

   .. attribute:: GF
      

      

   .. attribute:: gGF
      

      

   .. attribute:: gDprediction
      

      

   .. attribute:: cublas_handle
      

      

   .. attribute:: NGbparameters
      

      

   .. attribute:: gt0s
      

      

   .. method:: initialize(self, application)


      Initialize the state of the model given a {problem} specification


   .. method:: forwardModelBatched(self, theta, gf, prediction, batch, observation=None)


      KinematicG forward model in batch: cast Mb(x,y,t)
      :param theta: matrix (samples, parameters), sampling parameters
      :param gf: matrix (2*Ndd*Nas*Nt, observations), kinematicG green's function
      :param prediction: matrix (samples, observations), the predicted data or residual between predicted and observed data
      :param batch: integer, the number of samples to be computed batch<=samples
      :param observation: matrix (samples, observations), duplicates of observed data
      :return: prediction as predicted data(observation=None) or residual (observation is provided)


   .. method:: forwardModel(self, theta, gf, prediction, observation=None)


      KinematicG forward model for single sample: cast Mb(x,y,t)
      :param theta: vector (parameters), sampling parameters
      :param gf: matrix (2*Ndd*Nas*Nt, observations), kinematicG green's function
      :param prediction: vector (observations), the predicted data or residual between predicted and observed data
      :param observation: vector (observations), duplicates of observed data
      :return: prediction as predicted data(observation=None) or residual (observation is provided)


   .. method:: castSlipsOfTime(self, theta, Mb=None)


      Compute Mb (slips of patches over time) from a given set of parameters
      :param theta: a vector arranged in [slip (strike and dip), risetime, ...]
      :param Mb:
      :return: Mb


   .. method:: linearGM(self, gf, Mb, prediction=None, observation=None)


      Perform prediction = Gb * Mb
      :param Gb:
      :param Mb:
      :param prediction:
      :return:  prediction


   .. method:: cuEvalLikelihood(self, theta, likelihood, batch)


      to be loaded by super class cuEvalLikelihood which already decides where the local likelihood is added to


   .. method:: mergeCovarianceToGF(self)


      merge cd with green function




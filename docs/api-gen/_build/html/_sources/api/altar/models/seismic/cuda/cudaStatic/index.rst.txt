:mod:`altar.models.seismic.cuda.cudaStatic`
===========================================

.. py:module:: altar.models.seismic.cuda.cudaStatic


Module Contents
---------------

.. py:class:: cudaStatic

   Bases: :class:`altar.cuda.models.cudaBayesian.cudaBayesian`

   cudaLinear with the new cuda framework

   .. attribute:: dataobs
      

      

   .. attribute:: default
      

      

   .. attribute:: doc
      :annotation: = the observed data

      

   .. attribute:: green
      

      

   .. attribute:: doc
      :annotation: = the name of the file with the Green functions

      

   .. attribute:: GF
      

      

   .. attribute:: gGF
      

      

   .. attribute:: gDataPred
      

      

   .. attribute:: cublas_handle
      

      

   .. method:: initialize(self, application)


      Initialize the state of the model given a {problem} specification


   .. method:: forwardModelBatched(self, theta, green, prediction, batch, observation=None)


      Linear Forward Model prediction= G theta


   .. method:: forwardModel(self, theta, green, prediction, observation=None)


      Static/Linear forward model prediction = green * theta
      :param theta: a parameter set, vector with size parameters
      :param green: green's function, matrix with size (observations, parameters)
      :param prediction: data prediction, vector with size observations
      :return: data prediction if observation is none; otherwise return residual


   .. method:: cuEvalLikelihood(self, theta, likelihood, batch)


      Compute data likelihood from the forward model,
      :param theta: parameters, matrix [samples, parameters]
      :param likelihood: data likelihood P(d|theta), vector [samples]
      :param batch: the number of samples to be computed, batch <=samples
      :return: likelihood, in case of model ensembles, data likelihood of this model
      is added to the input likelihood


   .. method:: mergeCovarianceToGF(self)


      merge data covariance (cd) with green function




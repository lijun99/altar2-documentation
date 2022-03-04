:mod:`altar.models.seismic.cuda.cudaStaticCp`
=============================================

.. py:module:: altar.models.seismic.cuda.cudaStaticCp


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   altar.models.seismic.cuda.cudaStaticCp.cudaStaticCp



.. py:class:: cudaStaticCp

   Bases: :class:`altar.models.seismic.cuda.cudaStatic.cudaStatic`

   Static inversion with Cp (prediction error due to model parameter uncertainty)

   .. attribute:: nCmu
      

      

   .. attribute:: doc
      :annotation: = the number of model parameters with uncertainties (or to be considered)

      

   .. attribute:: cmu_file
      

      

   .. attribute:: doc
      :annotation: = the covariance describing the uncertainty of model parameter, a nCmu x nCmu matrix

      

   .. attribute:: kmu_file
      

      

   .. attribute:: doc
      :annotation: = the sensitivity kernel of model parameters, a hdf5 file including nCmu kernel data sets

      

   .. attribute:: initial_model_file
      

      

   .. attribute:: doc
      :annotation: = the initial mean model

      

   .. attribute:: beta_cp_start
      

      

   .. attribute:: doc
      :annotation: = for beta >= beta_cp_start, incorporate Cp into Cd

      

   .. attribute:: beta_use_initial_model
      

      

   .. attribute:: doc
      :annotation: = for beta <= beta_use_initial_model, use initial_model instead of mean model

      

   .. attribute:: dtype_cp
      

      

   .. attribute:: doc
      :annotation: = single/double precision to compute Cp

      

   .. attribute:: gCmu
      

      

   .. attribute:: gInitModel
      

      

   .. attribute:: gMeanModel
      

      

   .. method:: initialize(self, application)

      Initialize the state of the model given a {problem} specification


   .. method:: initializeCp(self)

      Initialize Cp related
      :return:


   .. method:: updateModel(self, annealer)

      Model method called by Sampler before Metropolis sampling for each beta step starts,
      employed to compute Cp and merge Cp with data covariance
      :param annealer: the annealer for application
      :return: True or False if model parameters are updated or remain the same


   .. method:: computeCp(self, model, cp=None)

      Compute Cp with a mean model
      :param model:
      :return:




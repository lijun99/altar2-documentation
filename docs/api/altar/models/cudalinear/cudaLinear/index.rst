:mod:`altar.models.cudalinear.cudaLinear`
=========================================

.. py:module:: altar.models.cudalinear.cudaLinear


Module Contents
---------------

.. py:class:: cudaLinear

   Bases: :class:`altar.cuda.models.cudaBayesian.cudaBayesian`

   Cuda implementation of a linear model 
   A linear model is defined as data = G theta

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


   .. method:: _forwardModel(self, theta, prediction, batch, observation=None)


      Linear Forward Model prediction= G theta


   .. method:: cuEvalLikelihood(self, theta, likelihood, batch)


      to be loaded by super class cuEvalLikelihood which already decides where the local likelihood is added to


   .. method:: loadGF(self)


      Load the data in the input files into memory


   .. method:: prepareGF(self)


      copy green function to gpu and merge cd with green function




:mod:`altar.models.seismic.StaticCp`
====================================

.. py:module:: altar.models.seismic.StaticCp


Module Contents
---------------

.. py:class:: StaticCp

   Bases: :class:`altar.models.seismic.Static.Static`

   Linear Model with prediction uncertainty Cp, in addition to data uncertainty Cd
   Cp = Kp Cmu Kp^T
   Kp = Kmu * <θ>
   Kp.shape = (observations, nCmu)
   Cmu.shape = (nCmu, nCmu)
   Kmu.shape =(observations, parameters) (same as the green's function)

   .. attribute:: nCmu
      

      

   .. attribute:: doc
      :annotation: = the number of model parameter sets

      

   .. attribute:: cmu_file
      

      

   .. attribute:: doc
      :annotation: = the covariance describing the uncertainty of model parameter

      

   .. attribute:: kmu_file
      

      

   .. attribute:: doc
      :annotation: = the sensitivity kernel of model parameter: input as kmu1.txt, ...

      

   .. attribute:: initialModel_file
      

      

   .. attribute:: doc
      :annotation: = the initial mean model

      

   .. attribute:: G0
      

      

   .. attribute:: d0
      

      

   .. attribute:: Cd0
      

      

   .. attribute:: Cmu
      

      

   .. attribute:: Kmu
      

      

   .. attribute:: Cp
      

      

   .. attribute:: meanModel
      

      

   .. method:: initialize(self, application)


      Initialize the state of the model given a {problem} specification


   .. method:: loadInputsCp(self)


      Load the additional data (for Cp problem) in the input files into memory


   .. method:: initializeCovariance(self, samples)


      initialize data covariance related variables


   .. method:: computeCp(self, theta_mean)


      Calculate Cp


   .. method:: update(self, annealer)


      Model update interface




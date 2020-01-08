:mod:`altar.models.seismic.Moment`
==================================

.. py:module:: altar.models.seismic.Moment


Module Contents
---------------

.. py:class:: Moment

   Bases: :class:`altar.distributions.Uniform.Uniform`

   The probability distribution for displacements (D) conforming to a given Moment magnitude scale 
   Mw = (log M0 - 9.1)/1.5 (Hiroo Kanamori) 
   M0 = Mu A D     
   It inherits uniform distribution for verification and density calculations,
   while generates samples for a combined gaussian and dirichlet distributions

   .. attribute:: area_patches_file
      

      

   .. attribute:: doc
      :annotation: = input file for area of each patch, in unit of km^2

      

   .. attribute:: area
      

      

   .. attribute:: doc
      :annotation: = total area in unit of km^2

      

   .. attribute:: Mw_mean
      

      

   .. attribute:: doc
      :annotation: =  the mean moment magnitude scale

      

   .. attribute:: Mw_sigma
      

      

   .. attribute:: doc
      :annotation: =  the variance of moment magnitude scale

      

   .. attribute:: Mu
      

      

   .. attribute:: doc
      :annotation: = the shear modulus in unit of GPa

      

   .. attribute:: area_patches
      

      

   .. attribute:: patches
      

      

   .. method:: initialize(self, rng)


      Initialize with the given random number generator


   .. method:: initializeSample(self, theta)


      Fill my portion of {theta} with initial random values from my distribution.




:mod:`altar.models.seismic.cuda.cudaMoment`
===========================================

.. py:module:: altar.models.seismic.cuda.cudaMoment


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   altar.models.seismic.cuda.cudaMoment.cudaMoment



.. py:class:: cudaMoment(name, locator, **kwds)

   Bases: :class:`altar.cuda.distributions.cudaUniform.cudaUniform`

   The probability distribution for displacements (D) conforming to a given Moment magnitude scale
   Mw = (log M0 - 9.1)/1.5 (Hiroo Kanamori)
   M0 = Mu A D
   It serves to initialize samples only, with combined gaussian and dirichlet distributions.
   It inherits uniform distribution for verification and density calculations.

   .. attribute:: area_patch_file
      

      

   .. attribute:: doc
      :annotation: = input file for area of each patch, in unit of km^2

      

   .. attribute:: area
      

      

   .. attribute:: doc
      :annotation: = area of each patch in unit of km^2, provide one value if the same for all patches

      

   .. attribute:: Mw_mean
      

      

   .. attribute:: doc
      :annotation: =  the mean moment magnitude scale

      

   .. attribute:: Mw_sigma
      

      

   .. attribute:: doc
      :annotation: =  the variance of moment magnitude scale

      

   .. attribute:: Mu
      

      

   .. attribute:: doc
      :annotation: = the shear modulus for each patch in GPa, provide one value if the same for all patches

      

   .. attribute:: Mu_patch_file
      

      

   .. attribute:: Mu_patch_file
      :annotation: = input file for the shear modulus of each patch, in Km^2

      

   .. attribute:: slip_sign
      

      

   .. attribute:: validators
      

      

   .. attribute:: doc
      :annotation: = the sign of slips, all positive or all negative

      

   .. attribute:: area_patches
      

      

   .. attribute:: mu_patches
      

      

   .. attribute:: patches
      

      

   .. attribute:: rng
      

      

   .. method:: initialize(self, application)

      Initialize with the given random number generator


   .. method:: cuInitialize(self, application)

      cuda interface of initialization


   .. method:: cuInitSample(self, theta)

      Fill my portion of {theta} with initial random values from my distribution.




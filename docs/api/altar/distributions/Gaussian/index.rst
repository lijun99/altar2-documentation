:mod:`altar.distributions.Gaussian`
===================================

.. py:module:: altar.distributions.Gaussian


Module Contents
---------------

.. py:class:: Gaussian

   Bases: :class:`altar.distributions.Base.Base`

   The Gaussian probability distribution

   .. attribute:: mean
      

      

   .. attribute:: doc
      :annotation: = the mean value of the distribution

      

   .. attribute:: sigma
      

      

   .. attribute:: doc
      :annotation: = the standard deviation of the distribution

      

   .. method:: initialize(self, rng)


      Initialize with the given random number generator


   .. method:: verify(self, theta, mask)


      Check whether my portion of the samples in {theta} are consistent with my constraints, and
      update {mask}, a vector with zeroes for valid samples and non-zero for invalid ones




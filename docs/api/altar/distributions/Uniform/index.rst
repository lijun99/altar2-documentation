:mod:`altar.distributions.Uniform`
==================================

.. py:module:: altar.distributions.Uniform


Module Contents
---------------

.. py:class:: Uniform

   Bases: :class:`altar.distributions.Base.Base`

   The uniform probability distribution

   .. attribute:: support
      

      

   .. attribute:: doc
      :annotation: = the support interval of the prior distribution

      

   .. method:: initialize(self, rng)


      Initialize with the given random number generator


   .. method:: verify(self, theta, mask)


      Check whether my portion of the samples in {theta} are consistent with my constraints, and
      update {mask}, a vector with zeroes for valid samples and non-zero for invalid ones




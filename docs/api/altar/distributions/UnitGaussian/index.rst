:mod:`altar.distributions.UnitGaussian`
=======================================

.. py:module:: altar.distributions.UnitGaussian


Module Contents
---------------

.. py:class:: UnitGaussian

   Bases: :class:`altar.distributions.Base.Base`

   Special case of the Gaussian probability distribution with σ = 1

   .. method:: initialize(self, rng)


      Initialize with the given random number generator


   .. method:: verify(self, theta, mask)


      Check whether my portion of the samples in {theta} are consistent with my constraints, and
      update {mask}, a vector with zeroes for valid samples and non-zero for invalid ones




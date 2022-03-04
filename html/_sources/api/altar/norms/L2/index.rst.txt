:mod:`altar.norms.L2`
=====================

.. py:module:: altar.norms.L2


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   altar.norms.L2.L2



.. py:class:: L2(name, locator, **kwds)

   Bases: :class:`altar.component`

   The L2 norm

   .. method:: eval(self, v, sigma_inv=None)

      Compute the L2 norm of the given vector, with or without a covariance matrix


   .. method:: withCovariance(self, v, sigma_inv)

      Compute the L2 norm of the given vector using the given Cholesky decomposed inverse
      covariance matrix




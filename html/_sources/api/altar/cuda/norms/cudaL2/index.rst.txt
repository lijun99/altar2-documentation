:mod:`altar.cuda.norms.cudaL2`
==============================

.. py:module:: altar.cuda.norms.cudaL2


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   altar.cuda.norms.cudaL2.cudaL2



.. py:class:: cudaL2(name, locator, **kwds)

   Bases: :class:`altar.norms.L2.L2`

   The L2 norm

   .. method:: cuEval(self, data, out=None, batch=None, cdinv=None)

      Compute the L2 norm of the given data  ||x||
      :param data - matrix:
      :type data - matrix: samples x observations
      :param batch - number of samples to be computed:
      :type batch - number of samples to be computed: first rows
      :param cdinv - inverse covariance matrix:
      :type cdinv - inverse covariance matrix: observations x observations) in its Cholesky decomposed form (Upper Triangle

      :returns: out - norm vector (samples)


   .. method:: cuEvalLikelihood(self, data, constant=0.0, out=None, batch=None, cdinv=None)

      Compute the L2 norm data likelihood of the given data  const - ||x||^2/2
      :param data - matrix:
      :type data - matrix: samples x observations
      :param batch - number of samples to be computed:
      :type batch - number of samples to be computed: first rows
      :param constant - normalization constant:
      :param cdinv - inverse covariance matrix:
      :type cdinv - inverse covariance matrix: observations x observations) in its Cholesky decomposed form (Upper Triangle

      :returns: out -  data likelihood vector (samples)




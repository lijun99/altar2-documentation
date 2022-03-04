:mod:`altar.bayesian.Brent`
===========================

.. py:module:: altar.bayesian.Brent


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   altar.bayesian.Brent.Brent



.. py:class:: Brent(name, locator, **kwds)

   Bases: :class:`altar.component`

   A δβ solver based on the GSL implementation of the Brent algorithm

   .. attribute:: tolerance
      

      

   .. attribute:: doc
      :annotation: = the fractional tolerance for achieving convergence

      

   .. attribute:: maxiter
      

      

   .. attribute:: doc
      :annotation: = the maximum number of iterations while looking for a δβ

      

   .. attribute:: cov
      

      

   .. method:: initialize(self, application, scheduler)

      Initialize me and my parts given an {application} context and a {scheduler}


   .. method:: solve(self, llk, weight)

      Compute the next temperature in the cooling schedule
      :param llk: data log-likelihood
      :param weight: the normalized weight
      :return: β, cov




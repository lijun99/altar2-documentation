:mod:`altar.bayesian.Grid`
==========================

.. py:module:: altar.bayesian.Grid


Module Contents
---------------

.. py:class:: Grid

   Bases: :class:`altar.component`

   A δβ solver based on a naive grid search

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




:mod:`altar.bayesian.Solver`
============================

.. py:module:: altar.bayesian.Solver


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   altar.bayesian.Solver.Solver



.. py:class:: Solver

   Bases: :class:`altar.protocol`

   The protocol that all δβ solvers must implement

   .. attribute:: tolerance
      

      

   .. attribute:: doc
      :annotation: = the fractional tolerance for achieving convergence

      

   .. method:: initialize(self, application, scheduler)

      Initialize me and my parts given an {application} context and a {scheduler}


   .. method:: solve(self, llk, weight)

      Compute the next temperature in the cooling schedule


   .. method:: pyre_default(cls, **kwds)
      :classmethod:

      Provide a default implementation




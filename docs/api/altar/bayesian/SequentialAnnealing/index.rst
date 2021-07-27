:mod:`altar.bayesian.SequentialAnnealing`
=========================================

.. py:module:: altar.bayesian.SequentialAnnealing


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   altar.bayesian.SequentialAnnealing.SequentialAnnealing



.. py:class:: SequentialAnnealing(annealer, **kwds)

   Bases: :class:`altar.bayesian.AnnealingMethod.AnnealingMethod`

   Implementation that assumes its state is the global state of the solver, and therefore it
   is able to compute the statistical properties of the sample distribution

   .. attribute:: wid
      :annotation: = 0

      

   .. attribute:: workers
      :annotation: = 1

      

   .. method:: start(self, annealer)

      Start the annealing process




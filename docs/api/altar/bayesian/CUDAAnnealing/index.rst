:mod:`altar.bayesian.CUDAAnnealing`
===================================

.. py:module:: altar.bayesian.CUDAAnnealing


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   altar.bayesian.CUDAAnnealing.CUDAAnnealing



.. py:class:: CUDAAnnealing(annealer, **kwds)

   Bases: :class:`altar.bayesian.AnnealingMethod.AnnealingMethod`

   Implementation that takes advantage of CUDA on gpus to accelerate the computation

   .. attribute:: wid
      :annotation: = 0

      

   .. attribute:: workers
      :annotation: = 1

      

   .. attribute:: device
      

      

   .. attribute:: gstep
      

      

   .. method:: initialize(self, application)

      initialize worker


   .. method:: cuInitialize(self, application)

      Initialize the cuda worker


   .. method:: start(self, annealer)

      Start the annealing process




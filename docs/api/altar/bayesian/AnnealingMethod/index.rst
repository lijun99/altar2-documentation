:mod:`altar.bayesian.AnnealingMethod`
=====================================

.. py:module:: altar.bayesian.AnnealingMethod


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   altar.bayesian.AnnealingMethod.AnnealingMethod



.. py:class:: AnnealingMethod(annealer, **kwds)

   Base class for the various annealing implementation strategies

   .. attribute:: step
      

      

   .. attribute:: iteration
      :annotation: = 0

      

   .. attribute:: wid
      :annotation: = 0

      

   .. attribute:: workers
      

      

   .. method:: beta(self)
      :property:

      Return the temperature of my current step


   .. method:: initialize(self, application)

      Initialize me and my parts given an {application} context


   .. method:: start(self, annealer)

      Start the annealing process from scratch


   .. method:: restart(self, annealer)
      :abstractmethod:

      Start the annealing process from a checkpoint


   .. method:: top(self, annealer)

      Notification that we are at the beginning of an update


   .. method:: cool(self, annealer)

      Push my state forward along the cooling schedule


   .. method:: walk(self, annealer)

      Explore configuration space by walking the Markov chains


   .. method:: resample(self, annealer, statistics)

      Analyze the acceptance statistics and take the problem state to the end of the
      annealing step


   .. method:: archive(self, annealer, scaling, stats)

      Notify archiver to record


   .. method:: bottom(self, annealer)

      Notification that we are at the bottom of an update


   .. method:: finish(self, annealer)

      Notification that the simulation is over




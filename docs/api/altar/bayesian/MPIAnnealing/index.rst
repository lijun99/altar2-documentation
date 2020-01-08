:mod:`altar.bayesian.MPIAnnealing`
==================================

.. py:module:: altar.bayesian.MPIAnnealing


Module Contents
---------------

.. py:class:: MPIAnnealing(annealer, worker, communicator=None, **kwds)

   Bases: :class:`altar.bayesian.AnnealingMethod.AnnealingMethod`

   A distributed implementation of the annealing method that uses MPI

   .. attribute:: manager
      :annotation: = 0

      

   .. attribute:: worker
      

      

   .. method:: initialize(self, application)


      Initialize me and my parts given an {application} context


   .. method:: start(self, annealer)


      Start the annealing process


   .. method:: top(self, annealer)


      Notification that we are at the beginning of a β update


   .. method:: cool(self, annealer)


      Push my state forward along the cooling schedule


   .. method:: walk(self, annealer)


      Explore configuration space by walking the Markov chains


   .. method:: resample(self, annealer, statistics)


      Analyze the acceptance statistics and take the problem state to the end of the
      annealing step


   .. method:: archive(self, annealer, scaling, stats)


      Notify archiver to record annealer information


   .. method:: bottom(self, annealer)


      Notification that we are at the end of a β update


   .. method:: finish(self, annealer)


      Shut down the annealing process


   .. method:: device(self)
      :property:



   .. method:: gstep(self)
      :property:



   .. method:: device(self)
      :property:



   .. method:: gstep(self)
      :property:



   .. method:: collect(self)


      Assemble my global state


   .. method:: partition(self)


      Distribute my global state




:mod:`altar.bayesian.Annealer`
==============================

.. py:module:: altar.bayesian.Annealer


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   altar.bayesian.Annealer.Annealer



.. py:class:: Annealer(name, locator, **kwds)

   Bases: :class:`altar.component`

   A Bayesian controller that uses an annealing schedule and MCMC to approximate the posterior
   distribution of a model

   .. attribute:: sampler
      

      

   .. attribute:: doc
      :annotation: = the sampler of the posterior distribution

      

   .. attribute:: scheduler
      

      

   .. attribute:: doc
      :annotation: = the generator of the annealing schedule

      

   .. attribute:: dispatcher
      

      

   .. attribute:: doc
      :annotation: = the event dispatcher that activates the registered handlers

      

   .. attribute:: archiver
      

      

   .. attribute:: doc
      :annotation: = the archiver of simulation state

      

   .. attribute:: model
      

      

   .. attribute:: worker
      

      

   .. attribute:: info
      

      

   .. attribute:: warning
      

      

   .. attribute:: error
      

      

   .. attribute:: debug
      

      

   .. attribute:: firewall
      

      

   .. method:: initialize(self, application)

      Initialize me and my parts given an {application} context


   .. method:: posterior(self, model)

      Sample the posterior distribution


   .. method:: deduceAnnealingMethod(self, job)

      Instantiate an annealing method compatible the user choices


   .. method:: sequential(self)

      Instantiate the plain sequential annealing method


   .. method:: cuda(self)

      Instantiate a CUDA aware annealing method


   .. method:: threaded(self, threads, worker)

      Instantiate the multi-threaded annealing method


   .. method:: mpi(self, worker)

      Instantiate the MPI aware annealing method




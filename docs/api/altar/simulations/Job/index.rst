:mod:`altar.simulations.Job`
============================

.. py:module:: altar.simulations.Job


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   altar.simulations.Job.Job



.. py:class:: Job(name, locator, **kwds)

   Bases: :class:`altar.component`

   The set of parameters in an AlTar run

   .. attribute:: name
      

      

   .. attribute:: doc
      :annotation: = the name of the job; used as a stem for making filenames, etc.

      

   .. attribute:: mode
      

      

   .. attribute:: mode
      :annotation: = the programming model

      

   .. attribute:: hosts
      

      

   .. attribute:: doc
      :annotation: = the number of hosts to run on

      

   .. attribute:: tasks
      

      

   .. attribute:: doc
      :annotation: = the number of tasks per host

      

   .. attribute:: gpus
      

      

   .. attribute:: doc
      :annotation: = the number of gpus per task

      

   .. attribute:: gpuprecision
      

      

   .. attribute:: doc
      :annotation: = the precision of gpu computations

      

   .. attribute:: validators
      

      

   .. attribute:: gpuids
      

      

   .. attribute:: default
      

      

   .. attribute:: doc
      :annotation: = the list of gpu ids for parallel jobs

      

   .. attribute:: chains
      

      

   .. attribute:: doc
      :annotation: = the number of chains per worker

      

   .. attribute:: steps
      

      

   .. attribute:: doc
      :annotation: = the length of each Markov chain

      

   .. attribute:: tolerance
      

      

   .. attribute:: doc
      :annotation: = convergence tolerance for β->1.0

      

   .. method:: initialize(self, application)

      Initialize the job parameters with information from the application context


   .. method:: validateMachineLayout(self, application)

      Adjust the machine parameters based on the {application} context and the runtime
      environment




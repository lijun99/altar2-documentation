:mod:`altar.simulations.Run`
============================

.. py:module:: altar.simulations.Run


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   altar.simulations.Run.Run



.. py:class:: Run

   Bases: :class:`altar.protocol`

   Protocol that specifies the job parameter set

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

      Initialize the run components with context from {application}


   .. method:: pyre_default(cls, **kwds)
      :classmethod:

      Supply a default implementation




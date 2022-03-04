:mod:`altar.simulations`
========================

.. py:module:: altar.simulations


Submodules
----------
.. toctree::
   :titlesonly:
   :maxdepth: 1

   Archiver/index.rst
   Dispatcher/index.rst
   GSLRNG/index.rst
   Job/index.rst
   Monitor/index.rst
   RNG/index.rst
   Recorder/index.rst
   Reporter/index.rst
   Run/index.rst


Package Contents
----------------

Classes
~~~~~~~

.. autoapisummary::

   altar.simulations.archiver
   altar.simulations.dispatcher
   altar.simulations.monitor
   altar.simulations.run
   altar.simulations.rng



Functions
~~~~~~~~~

.. autoapisummary::

   altar.simulations.gsl
   altar.simulations.job
   altar.simulations.recorder
   altar.simulations.reporter


.. py:class:: archiver

   Bases: :class:`altar.protocol`

   The protocol that all AlTar simulation archivers must implement

   Archivers persist intermediate simulation state and can be used to restart a simulation

   .. method:: initialize(self, application)

      Initialize me given an {application} context


   .. method:: record(self, step)

      Record the final state of the simulation


   .. method:: pyre_default(cls, **kwds)
      :classmethod:

      Supply a default implementation



.. py:class:: dispatcher

   Bases: :class:`altar.protocol`

   The protocol that all AlTar simulation dispatchers must implement

   Dispatchers associate event handlers with specific aspects of the calculation and invoke
   them when appropriate

   .. method:: initialize(self, application)

      Initialize me given an {application} context



.. py:class:: monitor

   Bases: :class:`altar.protocol`

   The protocol that all AlTar simulation monitors must implement

   Monitors respond to simulation events by generating user diagnostics to report progress

   .. method:: initialize(self, application)

      Initialize me given an {application} context


   .. method:: pyre_default(cls, **kwds)
      :classmethod:

      Supply a default implementation



.. py:class:: run

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



.. py:class:: rng

   Bases: :class:`altar.protocol`

   The protocol for random number generators

   .. method:: initialize(self, **kwds)

      Initialize the random number generator


   .. method:: pyre_default(cls, **kwds)
      :classmethod:

      Supply a default implementation



.. function:: gsl()


.. function:: job()


.. function:: recorder()


.. function:: reporter()



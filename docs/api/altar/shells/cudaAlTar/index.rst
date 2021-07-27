:mod:`altar.shells.cudaAlTar`
=============================

.. py:module:: altar.shells.cudaAlTar


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   altar.shells.cudaAlTar.cudaAlTar



.. py:class:: cudaAlTar(**kwds)

   Bases: :class:`altar.plexus`

   The main action dispatcher for the simple AlTar application

   .. attribute:: job
      

      

   .. attribute:: doc
      :annotation: = the job input parameters

      

   .. attribute:: model
      

      

   .. attribute:: doc
      :annotation: = the AlTar model to sample

      

   .. attribute:: rng
      

      

   .. attribute:: doc
      :annotation: = the random number generator

      

   .. attribute:: controller
      

      

   .. attribute:: doc
      :annotation: = my simulation controller

      

   .. attribute:: monitors
      

      

   .. attribute:: doc
      :annotation: = a collection of event handlers

      

   .. method:: main(self, *args, **kwds)

      The main entry point


   .. method:: initialize(self)

      Initialize without running, for debug purpose only


   .. method:: pyre_banner(self)

      Place the application banner in the {info} channel


   .. method:: pyre_interactiveSessionContext(self, context)

      Go interactive


   .. method:: pyre_mpi(self)

      Transfer my {job} settings to the MPI shell




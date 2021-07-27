:mod:`altar.shells.cudaApplication`
===================================

.. py:module:: altar.shells.cudaApplication


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   altar.shells.cudaApplication.cudaApplication



.. py:class:: cudaApplication(name=None, **kwds)

   Bases: :class:`altar.application`

   The base class for simple AlTar applications

   .. attribute:: job
      

      

   .. attribute:: doc
      :annotation: = the job input parameters

      

   .. attribute:: model
      

      

   .. attribute:: default
      

      

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


   .. method:: pyre_interactiveSessionContext(self, context)

      Go interactive


   .. method:: pyre_mpi(self)

      Transfer my {job} settings to the MPI shell




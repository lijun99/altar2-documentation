:mod:`altar.models.seismic.shells.Seismic`
==========================================

.. py:module:: altar.models.seismic.shells.Seismic


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   altar.models.seismic.shells.Seismic.Seismic



.. py:class:: Seismic(**kwds)

   Bases: :class:`altar.plexus`

   The main action dispatcher for the simple AlTar application

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


   .. method:: initialize(self)

      Initialize without running, for debug purpose only


   .. method:: forward(self)

      Perform the forward problem once for a given set of parameters


   .. method:: pyre_banner(self)

      Place the application banner in the {info} channel


   .. method:: pyre_interactiveSessionContext(self, context)

      Go interactive




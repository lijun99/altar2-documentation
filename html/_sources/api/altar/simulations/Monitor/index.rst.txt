:mod:`altar.simulations.Monitor`
================================

.. py:module:: altar.simulations.Monitor


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   altar.simulations.Monitor.Monitor



.. py:class:: Monitor

   Bases: :class:`altar.protocol`

   The protocol that all AlTar simulation monitors must implement

   Monitors respond to simulation events by generating user diagnostics to report progress

   .. method:: initialize(self, application)

      Initialize me given an {application} context


   .. method:: pyre_default(cls, **kwds)
      :classmethod:

      Supply a default implementation




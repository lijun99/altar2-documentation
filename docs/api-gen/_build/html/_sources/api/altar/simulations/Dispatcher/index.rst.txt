:mod:`altar.simulations.Dispatcher`
===================================

.. py:module:: altar.simulations.Dispatcher


Module Contents
---------------

.. py:class:: Dispatcher

   Bases: :class:`altar.protocol`

   The protocol that all AlTar simulation dispatchers must implement

   Dispatchers associate event handlers with specific aspects of the calculation and invoke
   them when appropriate

   .. method:: initialize(self, application)


      Initialize me given an {application} context




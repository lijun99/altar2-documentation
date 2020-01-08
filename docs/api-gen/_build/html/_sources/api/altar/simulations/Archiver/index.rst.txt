:mod:`altar.simulations.Archiver`
=================================

.. py:module:: altar.simulations.Archiver


Module Contents
---------------

.. py:class:: Archiver

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




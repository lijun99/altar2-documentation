:mod:`altar.simulations.Recorder`
=================================

.. py:module:: altar.simulations.Recorder


Module Contents
---------------

.. py:class:: Recorder

   Bases: :class:`altar.component`

   Recorder stores the intermediate simulation state in memory

   .. attribute:: theta
      

      

   .. attribute:: doc
      :annotation: = the path to the file with the final posterior sample

      

   .. attribute:: sigma
      

      

   .. attribute:: doc
      :annotation: = the path to the file with the final parameter correlation matrix

      

   .. attribute:: llk
      

      

   .. attribute:: doc
      :annotation: = the path to the file with the final posterior log likelihood

      

   .. method:: initialize(self, application)


      Initialize me given an {application} context


   .. method:: record(self, step, **kwds)


      Record the final state of the calculation




:mod:`altar.bayesian.H5Recorder`
================================

.. py:module:: altar.bayesian.H5Recorder


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   altar.bayesian.H5Recorder.H5Recorder



.. py:class:: H5Recorder(name, locator, **kwds)

   Bases: :class:`altar.component`

   H5Recorder stores the intermediate simulation state to HDF5 files

   .. attribute:: output_dir
      

      

   .. attribute:: doc
      :annotation: = the directory to save results

      

   .. attribute:: output_freq
      

      

   .. attribute:: doc
      :annotation: = the frequency to write step data to files

      

   .. attribute:: statistics
      

      

   .. method:: initialize(self, application)

      Initialize me given an {application} context


   .. method:: record(self, step, iteration, psets, **kwds)

      Record the final state of the calculation


   .. method:: recordstep(self, step, stats, psets)

      Record step to file for ce


   .. method:: saveStats(self)

      Save the statistics information to file




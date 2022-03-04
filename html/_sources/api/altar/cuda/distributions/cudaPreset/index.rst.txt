:mod:`altar.cuda.distributions.cudaPreset`
==========================================

.. py:module:: altar.cuda.distributions.cudaPreset


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   altar.cuda.distributions.cudaPreset.cudaPreset



.. py:class:: cudaPreset

   Bases: :class:`altar.cuda.distributions.cudaDistribution.cudaDistribution`

   The cuda preset distribution - initialize samples from a file
   Note that a preset distribution cannot be used for prior_run.

   .. attribute:: input_file
      

      

   .. attribute:: doc
      :annotation: = input file in hdf5 format

      

   .. attribute:: dataset
      

      

   .. attribute:: doc
      :annotation: = the name of dataset in hdf5

      

   .. attribute:: rank
      :annotation: = 0

      

   .. attribute:: precision
      

      

   .. attribute:: ifs
      

      

   .. attribute:: error
      

      

   .. method:: initialize(self, application)

      Initialize with the given random number generator


   .. method:: cuInitialize(self, application)

      cuda initialize distribution
      :param application:
      :return:


   .. method:: cuInitSample(self, theta)

      Fill my portion of {theta} with initial random values from my distribution.


   .. method:: _loadhdf5(self, theta)

      load from hdf5 file




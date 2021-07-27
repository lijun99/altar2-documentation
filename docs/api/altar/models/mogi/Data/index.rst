:mod:`altar.models.mogi.Data`
=============================

.. py:module:: altar.models.mogi.Data


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   altar.models.mogi.Data.Data



.. py:class:: Data(name, **kwds)

   Bases: :class:`altar.tabular.sheet`

   The layout of the input data file

   .. attribute:: oid
      

      

   .. attribute:: doc
      :annotation: = an integer identifying the data source

      

   .. attribute:: x
      

      

   .. attribute:: doc
      :annotation: = the EW coordinate of the location of the source

      

   .. attribute:: y
      

      

   .. attribute:: doc
      :annotation: = the NS coordinate of the location of the source

      

   .. attribute:: d
      

      

   .. attribute:: doc
      :annotation: = the displacement projected along the line of sight (LOS)

      

   .. attribute:: theta
      

      

   .. attribute:: doc
      :annotation: = the azimuthal angle of the LOS vector to the observing craft

      

   .. attribute:: phi
      

      

   .. attribute:: doc
      :annotation: = the polar angle of the LOS vector to the observing craft

      

   .. method:: read(self, uri)

      Load a data set from a CSV file


   .. method:: write(self, uri)

      Save my data into a CSV file




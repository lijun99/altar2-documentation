:mod:`altar.models.mogi`
========================

.. py:module:: altar.models.mogi


Subpackages
-----------
.. toctree::
   :titlesonly:
   :maxdepth: 3

   ext/index.rst


Submodules
----------
.. toctree::
   :titlesonly:
   :maxdepth: 1

   CUDA/index.rst
   Data/index.rst
   Fast/index.rst
   Mogi/index.rst
   Native/index.rst
   Source/index.rst
   meta/index.rst


Package Contents
----------------

Classes
~~~~~~~

.. autoapisummary::

   altar.models.mogi.source
   altar.models.mogi.data



Functions
~~~~~~~~~

.. autoapisummary::

   altar.models.mogi.mogi


.. py:class:: source(x=x, y=y, d=d, dV=dV, nu=nu, **kwds)

   An implementation of Mogi[1958]

   The surface displacement calculation for a point pressure source in an elastic half space.

   .. attribute:: x
      :annotation: = 0

      

   .. attribute:: y
      :annotation: = 0

      

   .. attribute:: d
      :annotation: = 0

      

   .. attribute:: dV
      :annotation: = 0

      

   .. attribute:: nu
      :annotation: = 0.25

      

   .. method:: displacements(self, locations, los)

      Compute the expected displacements from a point pressure source at a set of observation
      locations



.. py:class:: data(name, **kwds)

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



.. function:: mogi()



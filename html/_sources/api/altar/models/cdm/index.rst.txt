:mod:`altar.models.cdm`
=======================

.. py:module:: altar.models.cdm


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

   CDM/index.rst
   CUDA/index.rst
   Data/index.rst
   Fast/index.rst
   Native/index.rst
   Source/index.rst
   libcdm/index.rst
   meta/index.rst


Package Contents
----------------

Classes
~~~~~~~

.. autoapisummary::

   altar.models.cdm.source
   altar.models.cdm.data



Functions
~~~~~~~~~

.. autoapisummary::

   altar.models.cdm.cdm


.. py:class:: source(x=x, y=y, d=d, ax=ax, ay=ay, az=az, omegaX=omegaX, omegaY=omegaY, omegaZ=omegaZ, opening=opening, v=v, **kwds)

   The source response for a Compound Dislocation Model in an elastic half space.

   .. attribute:: x
      :annotation: = 0

      

   .. attribute:: y
      :annotation: = 0

      

   .. attribute:: d
      :annotation: = 0

      

   .. attribute:: ax
      :annotation: = 0

      

   .. attribute:: ay
      :annotation: = 0

      

   .. attribute:: az
      :annotation: = 0

      

   .. attribute:: omegaX
      :annotation: = 0

      

   .. attribute:: omegaY
      :annotation: = 0

      

   .. attribute:: omegaZ
      :annotation: = 0

      

   .. attribute:: opening
      :annotation: = 0

      

   .. attribute:: v
      :annotation: = 0.25

      

   .. method:: displacements(self, locations, los)

      Compute the expected displacements at a set of observation locations from a compound
      (triaxial) dislocation source at depth.



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



.. function:: cdm()



:mod:`altar.models.cdm.Source`
==============================

.. py:module:: altar.models.cdm.Source


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   altar.models.cdm.Source.Source



.. py:class:: Source(x=x, y=y, d=d, ax=ax, ay=ay, az=az, omegaX=omegaX, omegaY=omegaY, omegaZ=omegaZ, opening=opening, v=v, **kwds)

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




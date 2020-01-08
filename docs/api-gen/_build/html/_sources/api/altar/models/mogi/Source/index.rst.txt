:mod:`altar.models.mogi.Source`
===============================

.. py:module:: altar.models.mogi.Source


Module Contents
---------------

.. py:class:: Source(x=x, y=y, d=d, dV=dV, nu=nu, **kwds)

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




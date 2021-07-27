:mod:`altar.norms.Norm`
=======================

.. py:module:: altar.norms.Norm


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   altar.norms.Norm.Norm



.. py:class:: Norm

   Bases: :class:`altar.protocol`

   The protocol that all AlTar norms must satify

   .. method:: eval(self, v, **kwds)

      Compute the L2 norm of the given vector


   .. method:: pyre_default(cls, **kwds)
      :classmethod:

      Provide a default norm in case the user hasn't selected one




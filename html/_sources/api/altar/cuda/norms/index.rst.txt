:mod:`altar.cuda.norms`
=======================

.. py:module:: altar.cuda.norms


Submodules
----------
.. toctree::
   :titlesonly:
   :maxdepth: 1

   cudaL2/index.rst


Package Contents
----------------

Classes
~~~~~~~

.. autoapisummary::

   altar.cuda.norms.norm



Functions
~~~~~~~~~

.. autoapisummary::

   altar.cuda.norms.l2


.. py:class:: norm

   Bases: :class:`altar.protocol`

   The protocol that all AlTar norms must satify

   .. method:: eval(self, v, **kwds)

      Compute the L2 norm of the given vector


   .. method:: pyre_default(cls, **kwds)
      :classmethod:

      Provide a default norm in case the user hasn't selected one



.. function:: l2()



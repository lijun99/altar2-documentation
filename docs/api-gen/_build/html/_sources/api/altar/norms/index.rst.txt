:mod:`altar.norms`
==================

.. py:module:: altar.norms


Submodules
----------
.. toctree::
   :titlesonly:
   :maxdepth: 1

   L2/index.rst
   Norm/index.rst


Package Contents
----------------

.. py:class:: norm

   Bases: :class:`altar.protocol`

   The protocol that all AlTar norms must satify

   .. method:: eval(self, v, **kwds)


      Compute the L2 norm of the given vector


   .. method:: pyre_default(cls, **kwds)
      :classmethod:


      Provide a default norm in case the user hasn't selected one



.. function:: l2()



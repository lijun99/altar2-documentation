:mod:`altar.cuda.data`
======================

.. py:module:: altar.cuda.data


Submodules
----------
.. toctree::
   :titlesonly:
   :maxdepth: 1

   cudaDataL2/index.rst


Package Contents
----------------

Classes
~~~~~~~

.. autoapisummary::

   altar.cuda.data.data



Functions
~~~~~~~~~

.. autoapisummary::

   altar.cuda.data.datal2


.. py:class:: data

   Bases: :class:`altar.protocol`

   The protocol that all AlTar norms must satify

   .. method:: initialize(self, application)

      initialize data


   .. method:: pyre_default(cls, **kwds)
      :classmethod:

      Provide a default norm in case the user hasn't selected one



.. function:: datal2()



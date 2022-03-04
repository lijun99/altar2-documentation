:mod:`altar.cuda`
=================

.. py:module:: altar.cuda


Subpackages
-----------
.. toctree::
   :titlesonly:
   :maxdepth: 3

   bayesian/index.rst
   data/index.rst
   distributions/index.rst
   ext/index.rst
   models/index.rst
   norms/index.rst


Package Contents
----------------


Functions
~~~~~~~~~

.. autoapisummary::

   altar.cuda.get_current_device
   altar.cuda.use_device
   altar.cuda.curand_generator
   altar.cuda.cublas_handle
   altar.cuda.copyright
   altar.cuda.license
   altar.cuda.version
   altar.cuda.credits


.. function:: get_current_device()

   Return current cuda device


.. function:: use_device(id)

   Set current device to device with id


.. function:: curand_generator()


.. function:: cublas_handle()


.. function:: copyright()

   Return the altar copyright note


.. function:: license()

   Print the altar license


.. function:: version()

   Return the altar version


.. function:: credits()

   Print the acknowledgments



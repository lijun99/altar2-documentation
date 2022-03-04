.. _Common Issues:

#############
Common Issues
#############

.. _Installation Errors:

Installation Issues
===================

Cannot find ``gmake``
---------------------

When the command of GNU make is ``make`` instead of ``gmake``, please set the environmental variable

.. code-block:: bash

    $ export GNU_MAKE=make # for bash
    $ setenv GNU_MAKE make # for csh/tcsh

or set the variable when calling mm,

.. code-block:: bash

    $ GNU_MAKE=make mm


Cannot find ``cublas_v2.h``
---------------------------

For certain Linux systems, NVIDIA installer installs ``cublas`` to the system directory ``/usr/include`` and ``/usr/lib/x86_64-linux-gnu`` instead of ``/usr/local/cuda``. In this case, please add the include and library paths to ``cuda.incpath`` and ``cuda.libpath`` in ``config.mm`` file.

.. _Runtime Errors:

Run-time Issues
===============

.. _Locales:

Locales
-------

.. error:: UnicodeDecodeError: 'ascii' codec can't decode byte 0xc3 in position 18: ordinal not in range(128)

You might need to set the ``LANG`` variable,

.. code-block:: bash

    $ export LANG=en_US.UTF-8

if ``en_US.UTF-8`` locale is not installed, update your locale by

.. code-block:: bash

    $ sudo apt install locales
    $ sudo locale-gen --no-purge --lang en_US.UTF-8
    $ sudo update-locale LANG=en_US.UTF-8 LANGUAGE

Base case name
--------------

.. error:: altar: bad case name: 'patch-9'

The AlTar App cannot find the configuration file (usually) or the input file directory. Please go to the job directory with the configuration and input files, and run the App again. If the configuration is not named as ``theAlTarApp.pfg``, you need ``--config=YourConfigFile.pfg`` option, e.g.,

.. code-block:: bash

    linear --config=my_linear_model.pfg

Configuration Parser Error
--------------------------

.. error::

    File "/opt/anaconda3/envs/altar/lib/python3.9/site-packages/pyre/parsing/Scanner.py", line 71, in pyre_tokenize

    match = stream.match(scanner=self, tokenizer=tokenizer)

This is usually due to a bad format in configuration file.  For example, ``.pfg`` files do not recognize TABs; please check your file for possible TABs and replace them with SPACEs. See :ref:`Pyre Config Format` for more details.

MPI launcher error
------------------

.. error:: launcher = self.mpi.launcher

    AttributeError: 'NoneType' object has no attribute 'launcher'

This happens when AlTar cannot locate the ``mpirun`` command. It can be solved by manually setting up an ``mpi.pfg`` file. See :ref:`MPI setup` for more details.


Intel MKL Library
-----------------

.. error::  Intel MKL FATAL ERROR: Cannot load libmkl_avx2.so.1 or libmkl_def.so.1.

This is due to a Conda issue with MKL libraries. The solution is to preload certain MKL libraries before running AlTar applications,

.. code-block::

    LD_PRELOAD=$CONDA_PREFIX/lib/libmkl_core.so:$CONDA_PREFIX/lib/libmkl_sequential.so altarApp --config=configFile

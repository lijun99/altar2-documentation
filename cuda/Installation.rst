#################################
AlTar 2.0 CUDA Installation Guide
#################################

.. sectnum::

.. contents:: Table of Contents

Overview
========

The AlTar application is built upon pyre_, a framework to build Python scientific applications. In order to install and run altar, one needs to download the source code of pyre_ and altar_, and compile/install these two packages from the source code. (Other installation methods, such as conda, pip, or docker container may be supported in the future). 

In brief, the steps to install AlTar are as follows:

#. check/install all the prerequisite libraries/packages;
#. download the source code of pyre_ and altar_ (for GPU/CUDA versions, download from `pyre cuda branch`_ and `altar cuda branch`_ instead), as well as the mm_ build tool from github;
#. prepare ``config.mm`` file to provide path information of the prerequisite libraries/packages;
#. compile and install ``pyre``; add the path information for ``pyre`` products to ``config.mm``;
#. compile and install ``altar``. 



An altar/pyre application package (including altar itself and various packages in pyre) in general has mixed Python and C/C++/CUDA/Fortran code, as well as Python extension/wrappers. The convention to organize the source files (e.g., in SRC directory) and the compiled products (e.g., in DEST directory) is as follows, taking an application named MyApp as an example,

* The C/C++/CUDA/Fortran source files as well as their header files are located at ``SRC/lib``. They are compiled into a shared library ``libMyApp.so`` to ``DEST/lib`` while the header files are copied to ``DEST/include``.
* The source files of Python extension/wrappers for C/C++/CUDA/Fortran routines are located at ``SRC/ext`` (we recommend the cpython approach, while other semi-automatic wrapping tools such as cython, SWIG are also supported). They are compiled into a shared library ``MyApp.cpython-XXX.so`` to ``DEST/packages/MyApp/ext`` directory; these modules can be loaded in Python, e.g., ``import MyApp.ext.MyApp as libMyApp``. The header file ``capsules.h`` which contains definitions of Python capsules for C/C++ objects is copied to ``DEST\include`` as APIs. 
* the Python programs/scripts are located at ``SRC/MyApp`` or ``SRC/packages/MyApp``. They are copied/compiled to ``DEST/packages/MyApp``. One could add ``DEST/packages`` to the environmental variable ``PYTHONPATH`` for Python to load the packages.
* The executables, e.g., MyApp, a dedicated Python script to invoke the application, are located at ``SRC/bin`` and are copied to ``DEST/bin`` upon compilation. 
An application may also have documentations, examples, tests in additional directories, which can be compiled together or separately with the above core components. 

We adopt the mm_ build tool (please note that it is different from the old mm, or `config <https://github.com/aivazis/config>`__ build tool) to compile/install pyre and altar. The ``mm``  build automation tool follows the source/products file organizations as described above. Each altar/pyre application requires an ``mm`` build description file, similar to Makefile in GNU Make, e.g., ``MyApp.mm`` located at ``SRC/.mm`` directory. For altar and pyre, ``altar.mm`` and ``pyre.mm`` are provided with the source code. An altar/pyre application may also depend on other libraries/packages (as prerequisites). Users are required to prepare a ``config.mm`` file to provide the path information of these libraries or packages according to their specific computer system. For example, Python3 are required for altar, pyre and other altar/pyre applications. If you use Anaconda3 located as ``/opt/anaconda3``, you may add the following settings to ``config.mm``
::
 
    python.version = 3.7
    python.dir = /opt/anaconda3
    python.binpath = /opt/anaconda3/bin
    python.incpath = /opt/anaconda3/include/python3.7m
    python.libpath = /opt/anaconda3/lib

Examples of ``config.mm`` for various systems can be found at github: altar2-install_. 

You may put the ``config.mm`` file in the ``SRC/.mm`` directory, e.g., ``altar/.mm``, or in the ``${HOME}/.mm`` directory to be shared by all altar/pyre applications.

Prerequisites
=============

List of required libraries
--------------------------
To compile altar/pyre, the libraries or packages are required:

* ``python3  >= 3.6``
*  Python packages: ``numpy``, ``h5py``
* ``gcc >= gcc6``
* ``gsl`` 
* ``hdf5`` 
* ``postgresql`` 
* ``mpi``:   ``openmpi`` with ``--enable-mpi-cxx`` option. Other MPI implementations such as MPICH, Intel MPI are also supported. 
*  ``make >= 4.2.1``
*  ``cuda >= 9.0`` (certain linear algebra routines are only available after 9.0)   
* An accelerated BLAS library (recommended), such as ``atlas``, ``openblas``, ``mkl``. 

Downloads
=========

Currently, the CUDA extensions are not fully merged to the master branch. To install and run the CUDA version of AlTar 2.0, one needs to use ``git`` to pull pyre and altar packages from `pyre cuda branch`_ and `altar cuda branch`_, respectively.

The first step is to choose a directory where you plan to put all files, e.g., ``${HOME}/tools``, (if you have admin privileges to your system, you may choose a system folder such as ``/usr/local/`` or ``/opt``) 
::
      
      $ mkdir -p ${HOME}/tools/src
      $ cd ${HOME}/tools/src

Download the mm/pyre/altar from their ``github`` repositories
::

      $ git clone https://github.com/aivazis/mm.git
      $ git clone https://github.com/lijun99/pyre.git
      $ git clone https://github.com/lijun99/altar.git

You shall observe three directories ``mm``, ``pyre``, ``altar`` under ``${HOME}/tools/src`` directory. 



Prepare the ``config.mm`` file
------------------------------
The ``mm`` build tool requires ``config.mm`` to locate dependent libraries or packages. Taking Ubuntu 18.04 as an example, the ``config.mm`` file appear as 
::

    # file config.mm

    # gsl
    gsl.dir = /usr
    gsl.incpath = /usr/include
    gsl.libpath = /usr/lib/x86_64-linux-gnu

    # mpi
    mpi.dir = /usr/lib/x86_64-linux-gnu/openmpi/
    mpi.binpath = /usr/bin
    mpi.incpath = /usr/lib/x86_64-linux-gnu/openmpi/include
    mpi.libpath = /usr/lib/x86_64-linux-gnu/openmpi/lib
    mpi.flavor = openmpi
    mpi.executive = mpirun

    # hdf5
    hdf5.dir = /usr
    hdf5.incpath = /usr/include
    hdf5.libpath = /usr/lib/x86_64-linux-gnu

    # postgresql
    libpq.dir = /usr
    libpq.incpath = /usr/include/postgresql
    libpq.libpath = /usr/lib/x86_64-linux-gnu

    # openblas
    openblas.dir = /usr
    openblas.libpath = /usr/lib/x86_64-linux-gnu

    # python3
    python.version = 3.6
    python.dir = /usr
    python.binpath = /usr/bin
    python.incpath = /usr/include/python3.6m
    python.libpath = /usr/lib/python3.6

    # numpy
    numpy.dir = /usr/lib/python3/dist-packages/numpy/core

    # cuda
    cuda.dir = /usr/local/cuda
    cuda.binpath = /usr/local/cuda/bin
    cuda.incpath = /usr/local/cuda/include
    cuda.libpath = /usr/local/cuda/lib64 /usr/lib/x86_64-linux-gnu/
    cuda.libraries := cudart cublas curand cusolver

    # end of file

The ``config.mm`` can be kept at ``PROJ/.mm`` directory (e.g., ``pyre/.mm``), or user's home directory ``${HOME}/.mm`` to be shared by all pyre/altar projects.
    
Linux: Ubuntu (18.04) and Debian
--------------------------------

Install required packages
~~~~~~~~~~~~~~~~~~~~~~~~~
::

    $ sudo apt update && sudo apt install -y gcc g++ python3 python3-dev python3-numpy python3-h5py libgsl-dev libopenblas-dev libpq-dev libopenmpi-dev libhdf5-serial-dev make git


``config.mm``
~~~~~~~~~~~~~
See above.



Linux: REHL, CentOS, Fedora
---------------------------

Linux: Anaconda3
----------------------
Download the most recent version of `Anaconda3 <https://www.anaconda.com/distribution/#download-section>`__, and install it, e.g., to ${HOME}/anaconda3 directory. 

Install the required libraries/packages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::

  $ conda install -c conda-forge gcc_linux-64 gxx_linux-64 make openmpi gsl postgresql hdf5

Make some links
::
  
    $ cd ${HOME}/anaconda3/bin
    $ ln -sf make gmake
    $ ln -sf x86_64-conda_cos6-linux-gnu-gcc gcc
    $ ln -sf x86_64-conda_cos6-linux-gnu-g++ g++
    $ ln -sf x86_64-conda_cos6-linux-gnu-ld ld
   
Prepare a ``config.mm`` file 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
in ${HOME}/.mm/
::

    # file config.mm

    conda.dir = ${HOME}/anaconda3

    # gsl
    gsl.dir = ${conda.dir}
   
    # mpi
    mpi.dir = ${conda.dir}
    mpi.binpath = /usr/bin
    mpi.flavor = openmpi
    mpi.executive = mpirun

    # hdf5
    hdf5.dir = ${conda.dir}

    # postgresql
    libpq.dir = ${conda.dir} 

    # python3
    python.version = 3.7
    python.dir = ${conda.dir}
    python.incpath = ${conda.dir}/include/python3.7m
    python.libpath = ${conda.dir}/lib

    # numpy
    numpy.dir = ${conda.dir}/lib/python3.7/site-packages/numpy/core

    # cuda; may be different for different systems
    cuda.dir = /usr/local/cuda/cuda-10.1
    cuda.libpath = ${cuda.dir}/lib64
    cuda.libraries := cudart cublas curand cusolver

    # end of file


Linux: with environment modules
-------------------------------

MacOSX: Macports 
----------------

Build pyre
==========
After preparing all required libraries/packages and the ``config.mm`` file (in ``pyre/.mm`` or ``${HOME}/.mm``), you need to compile and install pyre at first. 

Make an alias of the mm_ command, in ``bash``
::

    $ alias mm='python3 ${HOME}/tools/src/mm/mm.py'
 
or in ``csh/tcsh``,
::

    $ alias mm 'python3 ${HOME}/tools/src/mm/mm.py'

Now, you can compile ``pyre`` by
::

    $ cd ${HOME}/tools/src/pyre
    $ mm

By default, the compiled files are located at ``${HOME}/tools/src/pyre/products/debug-shared-linux-x86_64``. If you need to customize the installation, you can check the options offered by ``mm`` by
::

    $ mm --help

For example, if you prefer to install pyre to a system folder, you may use ``--prefix`` option, such as
::

    $ mm --prefix=/usr/local


After compiling/installation, you need to set up some environmental variables for other applications to access
``pyre``, for example, create a ``${HOME}/.pyre.rc`` for ``bash``, 
::
    
    # file .pyre.rc
    export PYRE_DIR=${HOME}/tools/src/pyre/products/debug-shared-linux-x86_64
    export PATH=${PYRE_DIR}/bin:$PATH
    export LD_LIBRARY_PATH=${PYRE_DIR}/lib:$LD_LIBRARY_PATH
    export PYTHONPATH=${PYRE_DIR}/packages:$PYTHONPATH
    export MM_INCLUDES=${PYRE_DIR}/include
    export MM_LIBPATH=${PYRE_DIR}/lib
    # end of file

or ``${HOME}/.pyre.cshrc`` for ``csh/tcsh``,
::
    # file .pyre.cshrc
    setenv PYRE_DIR "${HOME}/tools/src/pyre/products/debug-shared-linux-x86_64"
    setenv PATH "${PYRE_DIR}/bin:$PATH"
    setenv LD_LIBRARY_PATH "${PYRE_DIR}/lib:$LD_LIBRARY_PATH"
    setenv PYTHONPATH "${PYRE_DIR}/packages:$PYTHONPATH"
    setenv MM_INCLUDES "${PYRE_DIR}/include"
    setenv MM_LIBPATH "${PYRE_DIR}/lib"
    # end of file

You will also need to append ``pyre`` configurations to ``${HOME}/.mm/config.mm`` or ``MYPROJ/.mm/config.mm`` for other applications to access ``pyre``,
::

    # append to the following lines to an existing config.mm
    # pyre
    pyre.dir =  ${HOME}/tools/src/pyre/products/debug-shared-linux-x86_64
    pyre.libraries := pyre journal ${if ${value cuda.dir}, pyrecuda}


Build AlTar2
============
First, make sure that you have a prepared ``config.mm`` file, which also includes the ``pyre`` configuration, in either ``altar/.mm/`` or ``${HOME}/.mm`` directory. For example 
::
    $ cd ${HOME}/tools/src/altar
    $ cp ${HOME}/tools/src/pyre/.mm/config.mm .mm/
and append ``pyre.dir`` and ``pyre.libraries`` to ``.mm/config.mm`` as shown above.

Then you can build AlTar2 by
::

    $ cd ${HOME}/tools/src/altar
    $ mm

Similar to ``pyre`` installation, the products are located at ``${HOME}/tools/src/altar/products/debug-shared-linux-x86_64``. You may choose to customize the installation with ``mm`` options, or simply copy the products to somewhere you prefer. 

Also, you need to set up some environmental variables for ``altar`` as well, for example, create a ``${HOME}/.altar2.rc`` for ``bash``,
::
    
    # file .altar2.rc
    export ALTAR2_DIR=${HOME}/tools/src/altar/products/debug-shared-linux-x86_64
    export PATH=${ALTAR2_DIR}/bin:$PATH
    export LD_LIBRARY_PATH=${ALTAR2_DIR}/lib:$LD_LIBRARY_PATH
    export PYTHONPATH=${ALTAR2_DIR}/packages:$PYTHONPATH
    # end of file

or ``${HOME}/.altar2.cshrc`` for ``csh/tcsh``,
::
    # file .altar2.cshrc
    setenv ALTAR2_DIR "${HOME}/tools/src/altar/products/debug-shared-linux-x86_64"
    setenv PATH "${ALTAR2_DIR}/bin:$PATH"
    setenv LD_LIBRARY_PATH "${ALTAR2_DIR}/lib:$LD_LIBRARY_PATH"
    setenv PYTHONPATH "${ALTAR2_DIR}/packages:$PYTHONPATH"
    # end of file 

Before running an altar/pyre application, you need to load the altar/pyre environmental settings
::

    $ source ${HOME}/.pyre.rc
    $ source ${HOME}/.altar.rc


Tests and Examples
==================
Pyre tests are available at ``${HOME}/tools/src/pyre/tests``. 

AlTar examples are are available for different models. Taking the linear model as an example, 
::

    $ cd ${HOME}/tools/src/altar/models/linear/examples
    $ linear

For details how to run AlTar applications, please refer to `User Guide`_. 

Common issues
=============

locales
-------
If you see the error 
::
  
    UnicodeDecodeError: 'ascii' codec can't decode byte 0xc3 in position 18: ordinal not in range(128)

you might need to update your locale, e.g., 
::

    $ sudo apt install locales
    $ sudo locale-gen --no-purge --lang en_US.UTF-8
    $ sudo update-locale LANG=en_US.UTF-8 LANGUAGE


GNU make version 
----------------
For Ubuntu 18.04, the system installed make version is 4.1; you need to update make
::

    $ wget http://mirrors.kernel.org/ubuntu/pool/main/m/make-dfsg/make_4.2.1-1.2_amd64.deb
    $ sudo dpkg -i make_4.2.1-1.2_amd64.deb
    $ sudo ln -s /usr/bin/make /usr/bin/gmake

Cannot find ``gmake``
---------------------
when the command of GNU make is ``make`` instead of ``gmake``, please set the environmental variable 
::

    $ export GNU_MAKE=make # for bash
    $ setenv GNU_MAKE make # for csh/tcsh

or set the variable when calling mm,
::
    
    $ GNU_MAKE=make mm


Cannot find ``cublas_v2.h`` 
---------------------------
For certain Linux systems, NVIDIA installer installs ``cublas`` to the system directory ``/usr/include`` and ``/usr/lib/x86_64-linux-gnu`` instead of ``/usr/local/cuda``. In this case, please add the include and library paths to ``cuda.incpath`` and ``cuda.libpath`` in ``config.mm`` file. 
 

FAQs
====
      


.. _altar: https://github.com/AlTarFramework/altar
.. _altar cuda branch: https://github.com/lijun99/altar
.. _pyre: https://github.com/pyre/pyre
.. _pyre cuda branch: https://github.com/lijun99/pyre
.. _mm: https://github.com/aivazis/mm
.. _altar-install: https://github.com/lijun99/altar-install
.. _User Guide: https://github.com/lijun99/altar/wiki/AlTar-2.0-CUDA-User-Guide



.. _Installation Guide:

##################
Installation Guide
##################

.. _Installation Overview:

Overview
========

AlTar_ is developed upon the pyre_ framework. Both packages include C/C++ libraries, CPython modules and Python scripts. Installations with `CMake <https://cmake.org>`__ or the mm_ build tools are currently supported, and the instructions are provided in this Guide.

In brief, the installation steps consist of:

#. check the :ref:`supported platforms <Platforms>` and the :ref:`prerequisite libraries/packages <Prerequisites>`, and install them if necessary;
#. :ref:`download <Downloads>` the source packages of pyre_ and altar_ from their github repositories (for CUDA versions with extended GPU support, download from `pyre cuda branch`_ and `altar cuda branch`_ instead);
#. compile and install ``pyre``;
#. compile and install ``altar``.

Step-by-step instructions are provided for:

- :ref:`Anaconda3 with CMake (Linux/MacOSX) <Anaconda3>` *recommended method*
- :ref:`Ubuntu with CMake <Ubuntu>` *a standard platform*
- :ref:`Linux with environmental modules <lmod>` *for Linux clusters*
- :ref:`Docker container <Docker>` *out-of-the-box delivery*


.. _Platforms:

Platforms Supported
===================

Hardware
--------

- CPU: ``x86_64`` (Intel/AMD) and ``ppc64`` (IBM) architectures;
- GPU: `NVIDIA graphics cards with CUDA-support <https://en.wikipedia.org/wiki/CUDA#GPUs_supported>`__, with compute capabilities >=3.0

    - Telsa K40, K80, P100, V100 ...
    - gaming cards GTX1080 ... (for single-precision computations only);

- Memory: no specific requirement, depends on the scale of AlTar simulations.

Operation systems
-----------------

- Linux: any distribution should work though not all are tested;
- Linux clusters: with MPI support and a job queue scheduler (PBS/Slurm);
- MacOSX: with `MacPorts <https://www.macports.org/>`__ or `Anaconda <https://www.anaconda.com/distribution/#macos>`__;
- Windows: not supported; `Windows Subsystem for Linux <https://docs.microsoft.com/en-us/windows/wsl/install-win10>`__ or `Cygwin <https://www.cygwin.com/>`__ should work.

.. _Prerequisites:

Prerequisites
=============

AlTar and pyre have several dependencies:

Required:

- ``Python3 >= 3.6`` with additional Python packages ``numpy`` and ``h5py``.
- ``GCC >= gcc7``, with C++17 support. ``gcc6`` might work with some modifications. Note also that CUDA Toolkit may limit the GCC version, see `CUDA Documentation <https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html>`__ for more details.
- ``GSL >= 1.15``, various numerical libraries including BLAS, eigensystems and statistics.
- ``HDF5 >= 1.10``, a data management system for large and complex data sets.
- ``Postgresql``, a SQL database management system.
- ``make >= 4``, if you use the mm build tool, you need ``make >= 4.2.1``.
- ``cmake >= 3.14``, build tool. Numpy component in FindPython is only supported after 3.14.

Optional:

- ``MPI`` for multi-thread computations on single machine or cluster system.  The recommended option is ``openmpi > 1.10`` with CXX support (note that on many cluster systems, openmpi is compiled without the ``--enable-mpi-cxx`` option and therefore doesn't have the `libmpi_cxx.so` library). Other MPI implementations such as MPICH, Intel MPI are also supported.
- ``CUDA toolkit >= 9.0`` for GPU-accelerated computations. Additional libraries including ``cublas``, ``curand``, and ``cusolver`` are also required.
- An accelerated ``BLAS`` library, such as ``atlas``, ``openblas``, or ``mkl``. Otherwise, the ``gslcblas`` library, as included in ``GSL``, will be used by default.

.. _Downloads:

Downloads
=========

Please choose a directory where you plan to put all the source files, e.g., ``${HOME}/tools/src``,
::

    mkdir -p ${HOME}/tools/src
    cd ${HOME}/tools/src

and download the source packages of pyre_ and AlTar_ from their github repositories (master branch):
::

    git clone https://github.com/pyre/pyre.git
    git clone https://github.com/AlTarFramework/altar.git

Currently, some CUDA extensions to pyre and AlTar are not fully merged to the master branch. To install and run the CUDA version of AlTar 2.0, you need to download pyre and altar packages from `pyre cuda branch`_ and `altar cuda branch`_ instead:
::

    git clone https://github.com/lijun99/pyre.git
    git clone https://github.com/lijun99/altar.git

.. note::

    Pyre is under active development and sometimes the newest version doesn't work properly for AlTar. AlTar users are recommended to obtain pyre from the `pyre cuda branch`_ even they don't use CUDA extensions.

Upon successful downloads, you shall observe two directories ``pyre``, ``altar`` under ``${HOME}/tools/src`` directory.

.. _Anaconda3:

Anaconda3 with CMake (Linux/MacOSX)
===================================

Conda(Anaconda/Miniconda) offers an easy way to install Python, packages and libraries on different platforms, especially for users without the admin privilege to their computers. We recommend a full version of `Anaconda3 <https://www.anaconda.com/distribution/>`__. If disk space is an issue, you may use `Miniconda <https://docs.conda.io/en/latest/miniconda.html>`__ instead.

If Anaconda3 is not installed, please `download <https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html>`__ and follow the `instructions <https://docs.conda.io/projects/conda/en/latest/user-guide/install/>`__ to install it. You may choose to install it under you home directory ``${HOME}/anaconda3`` (default) or a system directory, e.g., ``/opt/anaconda3``. The path to the Anaconda3 is set as an environmental variable ``CONDA_PREFIX``. To check whether Anaconda3 is properly installed and loaded, you may try the following commands
::

    $ which conda
    /opt/anaconda3/bin/conda
    $ which python3
    /opt/anaconda3/bin/python3
    $ echo ${CONDA_PREFIX}
    /opt/anaconda3

Install prerequisites
---------------------

Install the required libraries and packages by Conda:
::

    $ conda install git make cmake hdf5 h5py openmpi gsl postgresql numpy


You will also need a c++ compiler.

- Ubuntu 18.04:  GCC 7.4.0 is installed by default and is sufficient. If GCC/G++ are not installed, run
  ::

    $ sudo apt install gcc g++

- Redhat/CentOS 7: GCC 4.x is installed by default. Higher versions of GCC are offered through ``devtoolset``. Please follow instructions for `Redhat <https://access.redhat.com/documentation/en-us/red_hat_developer_toolset/7/>`__ or `CentOS <https://www.softwarecollections.org/en/scls/rhscl/devtoolset-7/>`__ to install, e.g., ``devtoolset-7``.

- MacOSX: you will need to install either the full version of Xcode or the (compact) Command Line Tools. Xcode can be installed from the App Store. To install the Command Line Tools, run
  ::

    $ sudo xcode-select --install

  To select or switch compilers,
  ::

    $ sudo xcode-select --switch /Library/Developer/CommandLineTools/

- Conda also offers compiler packages,
  ::

    # for Linux
    $ conda install gcc_linux-64 gxx_linux-64 gfortran_linux-64
    # for Mac
    $ conda install clang_osx-64 clangxx_osx-64 gfortran_osx-64

    It works well for most systems (Redhat, Mac, ...) but has some library issues on Ubuntu.

If you would like to use a c++ compiler other than the default version, or the version (auto) discovered by ``cmake``, you may use ``-DCMAKE_CXX_COMPILER=...`` to specify the compiler.


Install pyre
------------
Go to the pyre source directory, create a `build` directory, and run the `cmake` command,
::

    $ cd ${HOME}/tools/src/pyre
    $ mkdir build && cd build
    $ cmake ..

An example output for a successful `cmake`, as on a Linux system, appears as
::

    -- Found Git: /opt/anaconda3/bin/git (found version "2.23.0")
    -- The CXX compiler identification is GNU 7.4.0
    -- Check for working CXX compiler: /usr/bin/c++
    -- Check for working CXX compiler: /usr/bin/c++ -- works
    -- Detecting CXX compiler ABI info
    -- Detecting CXX compiler ABI info - done
    -- Detecting CXX compile features
    -- Detecting CXX compile features - done
    -- Found Python3: /opt/anaconda3/bin/python3.7 (found version "3.7.4") found components:  Interpreter Development NumPy
    -- Found PkgConfig: /usr/bin/pkg-config (found version "0.29.1")
    -- Found GSL: /opt/anaconda3/include (found version "2.4")
    -- Found MPI_CXX: /opt/anaconda3/lib/libmpi_cxx.so (found version "3.1")
    -- Found MPI: TRUE (found version "3.1")
    -- Found PostgreSQL: /opt/anaconda3/lib/libpq.so (found version "11.2")
    -- Looking for a CUDA compiler
    -- Looking for a CUDA compiler - /usr/local/cuda/bin/nvcc
    -- The CUDA compiler identification is NVIDIA 10.2.89
    -- Check for working CUDA compiler: /usr/local/cuda/bin/nvcc
    -- Check for working CUDA compiler: /usr/local/cuda/bin/nvcc -- works
    -- Detecting CUDA compiler ABI info
    -- Detecting CUDA compiler ABI info - done
    -- CUDA Toolkit found and CUDA support is enabled
    -- Configuring done
    -- Generating done
    -- Build files have been written to: ${HOME}/tools/src/pyre/build

Please read :ref:`CMake Options` if you have some problems or need more customizations.

After `cmake` generates correct Makefiles, you may continue to run `make` and install,
::

    # compile
    $ make
    # install
    $ make install

If successfully, pyre should be installed to `/usr/local` (by default) or the directory specified by `CMAKE_INSTALL_PREFIX`. The installed files include
::

    --- bin  # executable shell scripts
     |- defaults # default configuration files
     |- include # c/c++ header files
     |- lib # shared libraries
     |- packages # python packages/scripts

You may also run some commands to test
::

    # check pyre module import
    $ python3 -c 'import pyre'
    # check cuda module if enabled
    $ python3 -c 'import cuda'
    # show the pyre installation directory
    $ pyre-config --prefix

More tests are available at `${HOME}/tools/src/pyre/tests`.

.. _CMake Options:

CMake Options
-------------

Some useful ``cmake`` options are

- to specify whether to enable CUDA extensions, which can be set by
::

    $ cmake -DWITH_CUDA=ON (or OFF) ..

By default, `WITH_CUDA=ON` for the cuda branch version and `WITH_CUDA=OFF` for the master branch version. To enable CUDA extensions, you will also need the CUDA Toolkit. If not found, ``cmake`` will automatically turn `WITH_CUDA=OFF`.

- to specify the target GPU architectures. By default, the CUDA compiler `nvcc` produces instruction sets compatible with compute capabilities 3.0 and above. If you want to have an optimized version targeting a specific architecture, e.g., for P100 with `sm_60`,
::

    $ cmake -DCMAKE_CUDA_FLAGS="-arch=sm_60" ..

K40/80 (``-arch=sm_35``), V100 (``-arch=sm_70``), GTX1050/1070/1080 ((``-arch=sm_61``), RTX 2080 (``-arch=sm_75``).

- to choose a build type,
::

    $ cmake -DCMAKE_BUILD_TYPE=Release (or Debug) ..

For the Debug build type, the `-g` compiler flag will be added to generate debugging information. For the Release type, the `-O3` optimization flag will be added. If none is specified, the default flags of `g++` are used.

- to specify the installation directory,
::

    $ cmake -DCMAKE_INSTALL_PREFIX=${HOME}/tools ..

By default,  `cmake` installs the compiled package to `/usr/local`. If you plan to install it to another system directory, or your home directory (the option for users who don't have admin access), such as ${HOME}/tools as shown above (for Mac users, please use the default `/usr/local` option for now as there are some shared library rpath issues need to be fixed).

- to specify the gcc/g++ compiler, e.g., `/usr/bin/g++`, you may use
::

    $ cmake -DCMAKE_CXX_COMPILER=/usr/bin/g++ ..

Note that pyre requires a GCC>=7 for c++17 support.

- to specify the locations of desired libraries instead of the default ones, for example, for some Linux systems, `cmake` may find and use libraries from `/usr/` instead of the libraries provided by conda, you may use
::

    $ cmake -DCMAKE_PREFIX_PATH=${CONDA_PREFIX} ..

For more than one paths, use `-DCMAKE_PREFIX_PATH="PATH1;PATH2;PATH3"`.

For more options of ``cmake``, please check `CMake Documentation <https://cmake.org/documentation/>`__.

Install AlTar
-------------
As pyre is required to install AlTar, you need to add the pyre path information to environmental variables at first,
::

    # for bash
    export PATH=/usr/local/bin:${PATH}
    export LD_LIBRARY_PATH=/usr/local/lib:${LD_LIBRARY_PATH}
    export PYTHONPATH=/usr/local/packages:${PYTHONPATH}
    # for csh/tcsh
    setenv PATH "/usr/local/bin:$PATH"
    setenv LD_LIBRARY_PATH "/usr/local/lib:$LD_LIBRARY_PATH"
    setenv PYTHONPATH "/usr/local/packages:$PYTHONPATH"

If pyre is installed to a directory other than ``/usr/local``, replace ``/usr/local`` with that directory name.

Run ``cmake`` and ``make`` to compile and install AlTar
::

    $ cd ${HOME}/tools/src/altar
    $ mkdir build && cd build
    $ cmake ..
    $ make
    $ make install

Please refer to the :ref:`CMake Options` for ``cmake`` customizations. In general, you use the same ``cmake`` options as being used for pyre.

If successful, AlTar shall be installed to ``/usr/local`` (by default)
or the directory specified by ``CMAKE_INSTALL_PREFIX``.

If AlTar is installed in the same directory as pyre, all the path information has already been set. If it is a different directory, you may follow the same step above to include AlTar paths to environmental variables ``PATH``, ``LD_LIBRARY_PATH`` and ``PYTHONPATH``.

You may try some commands to check whether AlTar is properly installed
::

    ### shell command
    $ altar
    ### import altar module
    $ python3 -c 'import altar'

More tests are available at the AlTar source package, e.g., to run a linear model test,
::

    $ cd ${HOME}/tools/src/altar/models/linear/examples
    $ linear


.. _Ubuntu:

Ubuntu with CMake
=================


Install prerequisites
---------------------
::

    $ sudo apt update && sudo apt install -y gcc g++ python3 python3-dev python3-numpy python3-h5py libgsl-dev libopenblas-dev libpq-dev postgresql-server-dev-all libopenmpi-dev libhdf5-serial-dev make git

For Ubuntu 18.04, the system installed cmake version is 3.10; you need to upgrade cmake from `Kitware Repo <https://apt.kitware.com/>`__ manually, e.g.,
::

    $ sudo wget -O - https://apt.kitware.com/keys/kitware-archive-latest.asc 2>/dev/null | sudo apt-key add -
    $ sudo apt-add-repository 'deb https://apt.kitware.com/ubuntu/ bionic main'
    $ sudo apt-get update
    $ sudo apt-get install cmake


Download and install pyre
-------------------------
::

    ### create a directory to host the source
    $ mkdir -p ${HOME}/tools/src
    $ cd ${HOME}/tools/src
    ### use git to pull source code from github
    $ git clone https://github.com/lijun99/pyre.git
    ### create a build directory for cmake
    $ cd pyre
    $ mkdir build && cd build
    ### call cmake
    $ cmake ..
    ### compile and install
    $ make all && make install

For more build options and customizations, please check :ref:`CMake Options`.

Download and install AlTar
--------------------------
::

    ### go back to src directory
    $ cd ${HOME}/tools/src
    ### use git to pull source code from github
    $ git clone https://github.com/lijun99/altar.git
    ### create a build directory for cmake
    $ cd altar
    $ mkdir build && cd build
    ### call cmake
    $ cmake ..
    ### compile and install
    $ make all && make install

For more build options and customizations, please check :ref:`CMake Options`.


.. _lmod:

Linux with environmental modules
================================
Many clusters use environmental modules to load libraries and software packages, e.g.,
::

    # list available modules
    $ module av
    # load a certain module
    $ module load cuda/10.2

Please load all necessary modules as listed in :ref:`Prerequisites`.

You may follow the `cmake` steps as above to install pyre and altar. One caveat is that the libraries in ``LD_LIBRARY_PATH`` are not passed to `cmake` find_library; you need to specify them by ``-DCMAKE_PREFIX_PATH``, or by, e.g., ``-DGSL_INCLUDE_DIR=${GSL_ROOT}/include``.

Another option is to use ``FindEnvModules`` in `cmake`. This requires some changes to the `CMakeLists.txt` and TBD.


.. _Docker:

Docker container
================
*We will provide the pre-build Docker image for AlTar when we figure out where to

::

    wget https://gitlab.com/nvidia/container-images/cuda/raw/master/dist/ubuntu18.04/10.2/runtime/Dockerfile
    docker build --build-arg IMAGE_NAME=nvidia/cuda . -t cuda/nvidia:10.2
    docker exec -it cuda/nvidia:10.2
    apt update && apt install -y gcc g++ python3 python3-dev python3-numpy python3-numpy-dev python3-h5py libgsl-dev libopenblas-dev libpq-dev postgresql-server-dev-all libopenmpi-dev libhdf5-serial-dev make git wget software-properties-common locales
    locale-gen --no-purge --lang en_US.UTF-8 && update-locale LANG=en_US.UTF-8 LANGUAGE
    wget -O - https://apt.kitware.com/keys/kitware-archive-latest.asc 2>/dev/null | apt-key add - && apt-add-repository 'deb https://apt.kitware.com/ubuntu/ bionic main' && apt-get update && apt install -y cmake
    apt install -y cuda-compiler-10-2 cuda-cudart-dev-10-2 cuda-curand-dev-10-2 libcublas-dev cuda-cusolver-dev-10-2
    ln -sf /usr/lib/python3/dist-packages /usr/local/packages
    cd /usr/local/src
    git clone https://github.com/lijun99/pyre.git
    git clone https://github.com/lijun99/altar.git
    cd /usr/local/src/pyre && mkdir build && cd build && cmake .. && make all && make install
    cd /usr/local/src/altar && mkdir build && cd build && cmake .. && make all && make install
    echo ': "${LANG:=en_US.UTF-8}"; export LANG' >> /etc/profile


In another terminal, find out the *CONTAINER ID* for this image, named *cuda/nvidia:10.2*, and commit the changes to a new image
::

    $ docker commit CONTAINER_ID altar2:2.0.1

To run AlTar from the container
::

    $ docker run --gpus all -ti -v ${PWD}:/mnt altar2:2.0.1

which also mounts the current directory as /mnt in the virtual system. (``export LANG=en_US.UTF-8`` at first).



Install with the mm_ build tool
===============================

The mm_ build tool (please note that it is different from the old mm, or `config <https://github.com/aivazis/config>`__ build tool) is another powerful tool to build hybrid python/c/c++/cuda applications.

Download ``mm``
---------------
::

    cd ${HOME}/tools/src
    git clone https://github.com/aivazis/mm.git

Prepare a ``config.mm`` file
------------------------------

The ``mm`` build tool requires a ``config.mm`` file to locate dependent libraries or packages. Taking Ubuntu 18.04 as an example, the ``config.mm`` file appear as

.. _ubuntu_18.04_config:
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

You may leave the ``config.mm`` file in the ``pyre/.mm``, ``altar/.mm`` directories, or in the ``${HOME}/.mm`` directory to be shared by all projects.

Examples of `config.mm` files are available at :altar_doc_src:`config.mm <config.mm>`.


Install pyre
------------
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

You will also need to append ``pyre`` configurations to ``${HOME}/.mm/config.mm`` or ``altar/.mm/config.mm`` or any other application who requires ``pyre``,
::

    # append to the following lines to an existing config.mm
    # pyre
    pyre.dir =  ${HOME}/tools/src/pyre/products/debug-shared-linux-x86_64
    pyre.libraries := pyre journal ${if ${value cuda.dir}, pyrecuda}


Install AlTar
-------------
First, make sure that you have a prepared ``config.mm`` file, which also includes the ``pyre`` configuration, in either ``altar/.mm/`` or ``${HOME}/.mm`` directory.

Follow the same step to compile AlTar,
::

    $ cd ${HOME}/tools/src/altar
    $ mm

Similar to ``pyre`` installation, the AlTar products are located at ``${HOME}/tools/src/altar/products/debug-shared-linux-x86_64``, or the directory specified by ``mm --prefix=``.

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
    $ source ${HOME}/.altar2.rc


Tests and Examples
==================
Pyre tests are available at ``${HOME}/tools/src/pyre/tests``.

AlTar examples are are available for each model.

For details how to run AlTar applications, please refer to :ref:`User Guide`.


Common issues
=============

locales
-------
If you see the error
::

    UnicodeDecodeError: 'ascii' codec can't decode byte 0xc3 in position 18: ordinal not in range(128)

you might need to set the language variable,
::

    $ export LANG=en_US.UTF-8

if en_US.UTF-8 locale is not installed, update your locale by
::

    $ sudo apt install locales
    $ sudo locale-gen --no-purge --lang en_US.UTF-8
    $ sudo update-locale LANG=en_US.UTF-8 LANGUAGE


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


Support
========
If you meet any troubles in installation, you may seek assistance by

* raise your issues or questions at `github <https://github.com/AlTarFramework/altar/issues>`__;
* join the AlTar users' forum (available soon);
* join the `slack discussion group <https://altar-group.slack.com/>`__ (currently for developers only).

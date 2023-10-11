.. _Installation Guide:

##################
Installation Guide
##################

.. _Installation Overview:

Overview
========

AlTar_ is developed upon the pyre_ framework. Both packages may be installed from the source code with the `CMake <https://cmake.org>`__  build tool. More installation methods, e.g., binaries, will be provided in the future.

In brief, the installation steps consist of:

#. check :ref:`Supported Platforms <Platforms>` and install :ref:`Prerequisites <Prerequisites>`;
#. :ref:`download <Downloads>` the source packages from github;
#. follow the :ref:`Installation Guide <General Steps>` to compile/install ``pyre`` and ``altar``.

Step-by-step instructions are also provided for some representative systems:

    - :ref:`Conda method <Anaconda3>` *recommended method for Linux, Linux Clusters and MacOSX*
    - :ref:`Ubuntu 18.04/20.04 <Ubuntu>` *a standard platform*
    - :ref:`RHEL/CentOS 7 <Redhat>` *a standard platform*
    - :ref:`Linux with environmental modules <lmod>` *for Linux clusters*
    - :ref:`Docker container <Docker>` *out-of-the-box delivery*

.. _Platforms:

Supported Platforms
===================

Hardware
--------

* CPU: ``x86_64`` (Intel/AMD), ``ppc64`` (IBM), ``arm64`` (Apple Silicon/ARM Neoverse/Fujitsu A64FX/...)
* GPU: `NVIDIA graphics cards with CUDA-support <https://en.wikipedia.org/wiki/CUDA#GPUs_supported>`__, with compute capabilities >=3.0

    - Server/Workstation GPUs - Tesla K40, K80, P100, V100, A100, ...
    - Workstation graphic Cards - Quadro K6000, M6000, P6000, GV100, RTX x000, ...
    - Gaming graphic cards GTX10x0, RTX20x0, RTX30x0, ...

.. note::

   AlTar supports both single and double precision GPU computations. Most Quadro and gaming cards have limited double precision computing cores. However, single-precision simulation is sufficient for most models.

Operation systems
-----------------

- Linux: any distribution should work though not all have been tested;
- Linux clusters: with MPI support and a job queue scheduler (PBS/Slurm);
- MacOSX: with `MacPorts <https://www.macports.org/>`__ or `conda <https://www.anaconda.com/distribution/#macos>`__;
- Windows: not tested; `Windows Subsystem for Linux <https://docs.microsoft.com/en-us/windows/wsl/install-win10>`__ or `Cygwin <https://www.cygwin.com/>`__ should work.

.. note::

    AlTar is designed for large scale simulations. We recommend clusters or a workstation with multiple GPUs for simulating compute-intensive models.


.. _Prerequisites:

Prerequisites
-------------

AlTar and pyre have several dependencies:

Required:

- ``Python3 >= 3.6`` with additional Python packages ``numpy`` and ``h5py``.
- C/C++ compiler: ``GCC >= gcc7``, or ``clang >= 7``, with C++17 support. Note also that CUDA Toolkit may require certain versions of C/C++ compiler, see `CUDA Documentation <https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html>`__ for more details.
- ``GSL >= 1.15``, various numerical libraries including linear algebra and statistics.
- ``HDF5 >= 1.10``, a data management system for large and complex data sets.
- ``Postgresql``, a SQL database management system (only the library, the server itself is not required).
- ``make >= 4``, build tool.
- ``cmake >= 3.14``, build tool. Numpy component in FindPython is only supported after 3.14.

Optional:

- ``MPI`` for multi-thread computations on single machine or cluster system.  The recommended option is ``openmpi > 1.10`` with CXX support (note that on many cluster systems, openmpi is compiled without the ``--enable-mpi-cxx`` option and therefore doesn't have the `libmpi_cxx.so` library). Other MPI implementations such as MPICH, Intel MPI are also supported.
- ``CUDA toolkit >= 10.0`` for GPU-accelerated computations. Additional libraries including ``cublas``, ``curand``, and ``cusolver`` are also required.
- An accelerated ``BLAS`` library, such as ``atlas``, ``openblas``, or ``mkl``. Otherwise, the ``gslcblas`` library, as included in ``GSL``, will be used by default.

.. _Downloads:

Downloads
=========

Please choose a directory where you plan to put all the source files, e.g., ``${HOME}/tools/src``,

.. code-block::

    mkdir -p ${HOME}/tools/src
    cd ${HOME}/tools/src

and download the source packages of pyre_ and AlTar_ from their github repositories (main branch):

.. code-block::

    git clone https://github.com/pyre/pyre.git
    git clone https://github.com/AlTarFramework/altar.git

Currently, some CUDA extensions to pyre and AlTar are not fully merged to the main branch. To install and run the CUDA version of AlTar 2.0, you need to download pyre and altar packages from `pyre cuda branch`_ and `altar cuda branch`_ instead:

.. code-block::

    git clone https://github.com/lijun99/pyre.git
    git clone https://github.com/lijun99/altar.git

.. note::

    Pyre is under active development and sometimes the newest version doesn't work properly for AlTar. AlTar users are recommended to obtain pyre from the `pyre cuda branch`_ even if only CPU modules are used.

Upon successful downloads, you shall observe two directories ``pyre``, ``altar`` under ``${HOME}/tools/src`` directory.

.. _CMake Install:

Install with CMake
==================

.. _General Steps:

General steps
-------------

This section provides a general instruction on installation procedures. Please refer to the following sections for more system-specific instructions.

Compile and install PYRE at first, with the following commands,

.. code-block:: bash

    # enter the source directory
    cd ${HOME}/tools/src/pyre
    # create a build directory
    mkdir build && cd build
    # call cmake to generate make files
    cmake .. -DCMAKE_INSTALL_PREFIX=TARGET_DIR -DCMAKE_CUDA_ARCHITECTURES="xx"
    # compile
    make  # or make -j to use multi-threads
    # install
    make install # or sudo make install

By default, without using ``-DCMAKE_INSTALL_PREFIX``, CMake installs the package to ``/usr/local``, . If you plan to install the packages to another directory ``TARGET_DIR``, you may use the ``-DCMAKE_INSTALL_PREFIX`` option. It is always a good practice to specify the targeted GPU architecture by, e.g, ``-DCMAKE_CUDA_ARCHITECTURES="60"`` (targeting NVIDIA Tesla P100 GPU) or ``-DCMAKE_CUDA_ARCHITECTURES="35;60"`` (targeting both K40/K80 and P100 GPUs). Please refer to :ref:`CMake Options <CMake Options>` for more details and more options.

The installed files will appear as

.. code-block:: none

  <install_prefix>
     |--- bin  # executable shell scripts
     |   |- pyre, pyre-config ...
     |- defaults # default configuration files
     |   |- pyre.pfg, merlin.pfg
     |- include # c/c++ header files
     |   |- portinfo, <pyre>
     |- lib # shared libraries
     |   |- libjournal.so libpyre.so ... (or .dylib for Mac)
     |- packages # python packages/scripts
         |- <pyre>, <merlin>, <journal> ...

You may also run a few tests to check whether pyre is properly installed.

First, set up the environmental variables (you may also consider to add them to your ``.bashrc`` or ``.cshrc``),

.. code-block:: bash

    # for bash/zsh
    export PATH=/usr/local/bin:${PATH}
    export LD_LIBRARY_PATH=/usr/local/lib:${LD_LIBRARY_PATH}
    export PYTHONPATH=/usr/local/packages:${PYTHONPATH}
    # for csh/tcsh
    setenv PATH "/usr/local/bin:$PATH"
    setenv LD_LIBRARY_PATH "/usr/local/lib:$LD_LIBRARY_PATH"
    setenv PYTHONPATH "/usr/local/packages:$PYTHONPATH"

then run commands such as

.. code-block:: bash

    # check pyre module import
    python3 -c 'import pyre'
    # check cuda module if enabled
    # an error will be reported if the module couldn't find a GPU device
    python3 -c 'import cuda'
    # show the pyre installation directory
    pyre-config --prefix

There are more test scripts under the source package ``${HOME}/tools/src/pyre/tests``.

After installing PYRE and setting up properly the PATHs, you may proceed to compile/install AlTar, with the same procedure,

.. code-block:: bash

    # enter the source directory
    cd ${HOME}/tools/src/altar
    # create a build directory
    mkdir build && cd build
    # call cmake to generate make files
    cmake .. -DCMAKE_INSTALL_PREFIX=TARGET_DIR -DCMAKE_CUDA_ARCHITECTURES="xx"
    # compile
    make  # or make -j  to use multi-threads
    # install
    make install # or sudo make install

By default, AlTar is also installed to ``/usr/local``. If you choose to install to another directory, you may use the same ``-DCMAKE_INSTALL_PREFIX`` as for PYRE. By doing so, all the PATHs only need to be set once.

To test whether AlTar is properly installed, you may run the following commands

.. code-block:: bash

    # check altar module import
    python3 -c 'import altar'
    # show the altar installation directory
    altar about prefix

There are also tests available in ``examples`` directories under each model in the source package, for example, ``$(HOME)/tools/src/altar/models/linear/examples``.

.. _CMake Options:

CMake Options
-------------

Here are some commonly used options to control the compilation/installation.

Installation path
~~~~~~~~~~~~~~~~~

.. code-block:: bash

    cmake -DCMAKE_INSTALL_PREFIX=${HOME}/tools ..

By default,  ``cmake`` installs the compiled package to ``/usr/local``. If you plan to install it to another system directory, or your home directory (for users who don't have admin access), such as ${HOME}/tools as shown above. Remember to set properly the environmental variables ``PATH``, ``LD_LIBRARY_PATH`` and ``PYTHONPATH``. If you use ``Conda``, you may use ``-DCMAKE_INSTALL_PREFIX=$CONDA_PREFIX``.

Enable/disable CUDA
~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    cmake -DWITH_CUDA=ON (or OFF) ..

By default, `WITH_CUDA=ON` for the cuda branch version and `WITH_CUDA=OFF` for the main branch version. To enable CUDA extensions, you will also need the CUDA Toolkit. If not found, ``cmake`` will automatically turn `WITH_CUDA=OFF`.

.. _GPU architecture:

Target GPU architecture(s)
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

    We recommend specifying a proper GPU architecture with ``-DCMAKE_CUDA_ARCHITECTURES="xx"`` or ``-DCMAKE_CUDA_FLAGS="-arch=sm_xx"``. It not only ensures the efficient GPU executable code for your device, but also avoids the issue of code incompatibilities. CUDA Toolkit 9 and 10 use ``sm_30`` as the default target architecture, while CUDA 11 uses ``sm_52``. The compiled code will continue to run on GPU devices with higher compute capabilities, but not on GPU devices with lower compute capabilities, reporting an error ``no kernel image is available for execution on the device.`` This happens, e.g., when you have a K40 (``sm_35``) and use a ``sm_52`` flag (default by CUDA 11). AlTar does not support CUDA on Mac, and ``-DCMAKE_CUDA_FLAGS=...`` will be neglected if provided.

To specify the targeted GPU architecture(s),

.. code-block:: bash

    # target one architecture
    cmake -DCMAKE_CUDA_ARCHITECTURES="60" ..
    # target multiple architectures
    cmake -DCMAKE_CUDA_ARCHITECTURES="35;60" ..

Note that ``CUDA_ARCHITECTURES`` is only available on CMake 3.18 and later versions. For earlier versions, you may use ``CUDA_FLAGS`` instead,

.. code-block:: bash

    # target one architecture
    cmake -DCMAKE_CUDA_FLAGS="-arch=sm_60" ..
    # target multiple architectures
    cmake -DCMAKE_CUDA_FLAGS="-gencode arch=compute_35,code=sm_35 -gencode arch=compute_60,code=sm_60" ..

``CUDA_FLAGS`` may also be used to pass other compiling options to CUDA compiler ``nvcc``.

You may find out which type(s) of GPU are installed by running

.. code-block:: bash

   nvidia-smi

Compute capabilities for some common NVIDIA GPUs are K40/80 (``sm_35``), V100 (``sm_70``), A100 (``sm_80``), GTX1050/1070/1080 ((``sm_61``), RTX 2060/2070/2080 (``sm_75``), RTX 3060/3070/3080(``sm_86``. More details can be found at `NVIDIA <https://developer.nvidia.com/cuda-GPUs>`__ website. If pyre is already installed, you may also use its cuda utilities to find out:

.. code-block:: bash

    python3 -c "import cuda; [print(f'Device {device.id} {device.name} has compute capability {device.capability}') for device in cuda.devices]"


C++ Compiler
~~~~~~~~~~~~

To specify the C++ compiler, e.g., `/usr/bin/g++`, you may use

.. code-block:: bash

    cmake -DCMAKE_CXX_COMPILER=/usr/bin/g++ ..

Note that pyre requires a GCC>=7 for c++17 support.

C++ compiler may also be specified from the environmental variable ``CXX``, for example,

.. code-block:: bash

    # bash/zsh
    export CXX = "/usr/bin/g++"
    # csh/tcsh
    setenv CXX  "/usr/bin/g++"


.. _CUDA Compiler:

CUDA Compiler
~~~~~~~~~~~~~

To specify the CUDA compiler ``nvcc``, e.g., `/usr/local/cuda-11.3/bin/nvcc`, you may use

.. code-block:: bash

    cmake -DCMAKE_CUDA_COMPILER=/usr/local/cuda-11.3/bin/nvcc ..

C++ compiler may also be specified from the environmental variable ``CUDACXX``, for example,

.. code-block:: bash

    # bash/zsh
    export CUDACXX = "/usr/local/cuda-11.3/bin/nvcc -arch=sm_60"
    # csh/tcsh
    setenv CUDACXX  "/usr/local/cuda-11.3/bin/nvcc -arch=sm_60"

BLAS Library
~~~~~~~~~~~~

Pyre requires a BLAS library for its ``gsl`` module. CMake searches automatically an available BLAS library by default. If none is found, the ``gslcblas`` library included with GSL package will be used. You may also specify which BLAS library to use by

.. code-block:: bash

    cmake .. -DBLA_VENDOR=vendor

where ``vendor`` can be ``Generic``(``libblas.so``), ``ATLAS``, ``Intel10_64lp``, ``OpenBLAS`` .... You may also add ``-DCMAKE_PREFIX_PATH=/path/to/blas`` to enforce a search path.


Library search path
~~~~~~~~~~~~~~~~~~~

To specify the locations of a prerequisite library instead of the default one, for example, on some Linux systems, ``cmake`` may find and use libraries from ``/usr/`` instead of the libraries provided by conda, you may use

.. code-block:: bash

    cmake -DCMAKE_PREFIX_PATH=${CONDA_PREFIX} ..

to enforce libraries installed under Conda to be used.

For more than one paths, use a semicolon separated list, `-DCMAKE_PREFIX_PATH="PATH1;PATH2;PATH3"`.

Build type
~~~~~~~~~~

.. code-block:: bash

    cmake -DCMAKE_BUILD_TYPE=Release (or Debug) ..

For the Debug build type, the ``-g`` compiler flag will be added to generate debugging information. For the Release type, the ``-O3`` optimization flag will be added. If none is specified, the default flags of ``g++`` are used.


Show compiling details
~~~~~~~~~~~~~~~~~~~~~~

By default, the compiling step ``make`` only shows one line summary of each file being compiled. To the detailed compiling command and options, you may use

.. code-block:: bash

    make VERBOSE=1

More options
~~~~~~~~~~~~

For more options of ``cmake``, please check `CMake Documentation <https://cmake.org/documentation/>`__.


.. _Anaconda3:

Conda method (Linux/MacOSX)
===========================

Install Anaconda/Miniconda
--------------------------

Conda(Anaconda/Miniconda) offers an easy way to install Python, packages and libraries on different platforms, especially for users without the admin privilege to their computers. We recommend a full version of `Anaconda3 <https://www.anaconda.com/distribution/>`__. If disk space is an issue or you plan to use a virtual environment, you may use `Miniconda <https://docs.conda.io/en/latest/miniconda.html>`__ instead.

For MacOSX with Apple Silicon, you may install the native ``arm64`` version from `Miniforge <https://github.com/conda-forge/miniforge>`__.

If Anaconda3 is not installed, please `download <https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html>`__ and follow the `instructions <https://docs.conda.io/projects/conda/en/latest/user-guide/install/>`__ to install it. You may choose to install it under you home directory ``${HOME}/anaconda3`` (default) or a system directory, e.g., ``/opt/anaconda3``. The path to the Anaconda3 is set as an environmental variable ``CONDA_PREFIX``. To check whether Anaconda3 is properly installed and loaded, you may try the following commands

.. code-block:: bash

    $ which conda
    /opt/anaconda3/bin/conda
    $ which python3
    /opt/anaconda3/bin/python3
    $ echo ${CONDA_PREFIX}
    /opt/anaconda3

You may also create a virtual environment

.. code-block:: bash

    $ conda create -n altar
    $ conda activate altar
    $ which python3
    /opt/anaconda3/envs/altar/bin/python3
    $ echo ${CONDA_PREFIX}
    /opt/anaconda3/envs/altar


Install Conda packages
----------------------

Install the required libraries and packages by Conda:

.. code-block:: bash

    $ conda install git make cmake hdf5 h5py openmpi gsl openblas postgresql numpy scipy


C++ Compiler
------------

You will also need a c++ compiler.

- **Ubuntu 18.04/20.04**  GCC 7.4.0/9.3.0 is installed by default and is sufficient. If GCC/G++ are not installed, run

.. code-block:: bash

    sudo apt install gcc g++

- **Redhat/CentOS 7** The system default compiler GCC 4.x doesn't support C++17. Higher versions of GCC are offered through ``devtoolset``. Please follow instructions for `Redhat <https://access.redhat.com/documentation/en-us/red_hat_developer_toolset/7/>`__ or `CentOS <https://www.softwarecollections.org/en/scls/rhscl/devtoolset-7/>`__ to install, e.g., ``devtoolset-7``. An alternative is to use GNU compilers provided by Conda, see below.

- **MacOSX** You will need to install either the full version of Xcode or the (compact) Command Line Tools. Xcode can be installed from the App Store. To install the Command Line Tools, run

.. code-block:: bash

    sudo xcode-select --install
    # To select or switch compilers,
    sudo xcode-select --switch /Library/Developer/CommandLineTools/

- **Conda GNU Compilers** Conda also offers compiler packages, which work well for most Linux/MacOSX(Intel) systems,

.. code-block:: bash

    # for Linux x86_64
    conda install gcc_linux-64 gxx_linux-64
    # for Mac (Intel Only)
    conda install clang_osx-64 clangxx_osx-64
    # for Mac Big Sur with Xcode 12 (Intel only), you need to use clang-11,
    conda install clang_osx-64=11.0.0 clangxx_osx-64=11.0.0 -c conda-forge
    # for Mac with Apple Silicon, please use only Command Line Tools or Xcode

If you would like to use a c++ compiler other than the default version, or the version (auto) discovered by ``cmake``, you may use ``-DCMAKE_CXX_COMPILER=...`` to specify the compiler.

.. _CUDA Toolkit:

CUDA compiler (nvcc)
--------------------

CUDA Toolkit integrates tools to develop GPU applications, including the compiler (``nvcc``), libraries (``libcudart.so``, ``libcublas.so`` ...). If CUDA is installed, you may obtain and install CUDA Toolkit following the `NVIDIA Toolkit Documentation <https://docs.nvidia.com/cuda/cuda-quick-start-guide/index.html>`__.

CUDA Toolkit is usually installed to ``/usr/local/cuda``. On Linux clusters, many version of CUDA toolkit may be provided as modules. You may select a version by

.. code-block:: bash

    module load cuda/11.3

Conda also provides a CUDA Toolkit package,

.. code-block:: bash

    conda install cudatoolkit

which is installed to ``$CONDA_PREFIX`` directory.

You may check the CUDA Toolkit installation by

.. code-block:: bash

    # check the nvcc availability and path
    $ which nvcc
    /usr/local/cuda/bin/nvcc
    # check the CUDA Toolkit version
    $ nvcc --version
    nvcc: NVIDIA (R) Cuda compiler driver
    Cuda compilation tools, release 11.3, V11.3.109

``CMake`` discovers the default ``nvcc`` command to compile CUDA programs. You may also specify anther CUDA compiler by ``-DCMAKE_CUDA_COMPILER=/path/to/nvcc``.

Note that NVIDIA driver, including the CUDA driver (``libcuda.so``), is required on a GPU workstation or GPU nodes in a cluster. NVIDIA drivers can only be installed/updated by *root* users.  You may check their availability and versions by the command ``nvidia-smi``. CUDA shared libraries should also be available on GPU workstations.


Download pyre and AlTar
-----------------------

Please download the source packages of pyre/AlTar from github following the :ref:`Download instructions <Downloads>`. Taking CUDA branch versions as an example,

.. code-block:: bash

    mkdir -p ${HOME}/tools/src
    cd ${HOME}/tools/src
    git clone https://github.com/lijun99/pyre.git
    git clone https://github.com/lijun99/altar.git


Install pyre
------------

With Conda, we recommend installing pyre and AlTar to ``$CONDA_PREFIX``, so that both packages are loaded automatically when conda or conda venv is activated.  We need an extra step to make a symbolic link to ``lib/python3.x/site-packages``,

.. code-block:: bash

    # the python command returns the path of site-packages, and we link it as $CONDA_PREFIX/packages
    ln -sf `python3 -c 'import site; print(site.getsitepackages()[0])'` $CONDA_PREFIX/packages

Compile and install pyre

.. code-block:: bash

    cd ${HOME}/tools/src/pyre
    mkdir build && cd build
    cmake .. -DCMAKE_INSTALL_PREFIX=$CONDA_PREFIX -DCMAKE_PREFIX_PATH=$CONDA_PREFIX -DCMAKE_CUDA_ARCHITECTURES=native -DBLA_VENDOR=OpenBLAS -DPython3_EXECUTABLE=$CONDA_PREFIX/bin/python3

    make -j && make install

where ``INSTALL_PREFIX`` is the installation path and ``PREFIX_PATH`` is the path to search the prerequisite packages. Replace ``native`` with appropriate compute capability number(s) for your GPU(s). See :ref:`GPU architecture(s) <GPU architecture>` for more details.

**Note**: ``FindPython3`` in new versions of ``cmake`` sometimes finds the system python3 interpreter instead of the conda installed one, please add ``-DPython3_EXECUTABLE=$CONDA_PREFIX/bin/python3`` as above to assist the search. The new standard is to use ``FindPython`` instead; we will update the pyre/altar cmake files.

Install AlTar
-------------

Since pyre is installed to ``$CONDA_PREFIX``, there is no need to set the PATHs. We proceed to compile and install AlTar, with the same procedure,

.. code-block:: bash

    cd ${HOME}/tools/src/altar
    mkdir build && cd build
    cmake .. -DCMAKE_INSTALL_PREFIX=$CONDA_PREFIX -DCMAKE_PREFIX_PATH=$CONDA_PREFIX -DCMAKE_CUDA_ARCHITECTURES=native -DPython3_EXECUTABLE=$CONDA_PREFIX/bin/python3

    make -j && make install

Please read :ref:`CMake Options <CMake Options>` if you have some problems or need more customizations. Please also read :ref:`Installation instructions <General Steps>` on how to make tests.

For future runs, you may simply activate conda or the conda venv to load AlTar,

.. code-block:: bash

    # activate altar if it is installed in a venv
    conda activate altar
    # test
    altar about

.. _MPI setup:

MPI setup
---------

AlTar runs MPI jobs by automatically forking multiple threads and invoking ``mpirun`` command with any AlTar Application, a capability offered by pyre ``mpi`` shell. However, pyre sometimes does not recognize the Conda-installed openMPI. You will need to create manually a configuration file, ``mpi.pfg``, either under ``$(HOME)/.pyre`` directory or under the current job directory, as

.. code-block:: none

    ; mpi.pfg file

    mpi.shells.mpirun:
      ; mpi implementation
      mpi = openmpi#mpi_conda

    ; mpi configuration
    pyre.externals.mpi.openmpi # mpi_conda:
      version = 4.0.5
      launcher = mpirun
      prefix = /opt/anaconda3/envs/altar
      bindir = {mpi_conda.prefix}/bin
      incdir = {mpi_conda.prefix}/include
      libdir = {mpi_conda.prefix}/lib

You need to replace ``/opt/anaconda3/envs/altar`` with the actual path of your ``$CONDA_PREFIX``, which can be revealed by the command ``echo $CONDA_PREFIX``.

Another option is to insert these lines to your job configuration file, without creating a separate ``mpi.pfg`` file.

This setup procedure also applies to other MPIs not automatically recognized by pyre, e.g., loaded by environmental modules.

.. _Linux:

Linux Systems
=============

We recommend Conda methods for all Linux systems. If you prefer to use the standard Linux packages, please follow the instructions in this section.

.. _Ubuntu:

Ubuntu 18.04/20.04
------------------

Install prerequisites
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    $ sudo apt update && sudo apt install -y gcc g++ python3 python3-dev python3-numpy python3-scipy python3-h5py libgsl-dev libopenblas-dev libpq-dev postgresql-server-dev-all libopenmpi-dev libhdf5-serial-dev make git

For Ubuntu 18.04 only: the system CMake version is 3.10; you need to manually upgrade cmake from `Kitware Repo <https://apt.kitware.com/>`__,  e.g.,

.. code-block:: bash

    $ sudo wget -O - https://apt.kitware.com/keys/kitware-archive-latest.asc 2>/dev/null | sudo apt-key add -
    $ sudo apt-add-repository 'deb https://apt.kitware.com/ubuntu/ bionic main'
    $ sudo apt-get update
    $ sudo apt-get install cmake

To install/run CUDA modules, you will also need to install CUDA Toolkit if it is not pre-installed. See :ref:`CUDA Toolkit` for more details.

Install pyre/AlTar
~~~~~~~~~~~~~~~~~~

Please follow the instructions in :ref:`General Steps`.


.. _Redhat:

RHEL/CentOS 7
-------------

Install prerequisites
~~~~~~~~~~~~~~~~~~~~~

Enable EPEL repo

.. code-block:: bash

    yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm

and install prerequisites

.. code-block:: bash

    yum install -y python3 python3-devel hdf5-devel gsl-devel postgresql-devel openmpi openmpi-devel git environment-modules
    # install numpy/scipy/h5py via pip
    pip3 install numpy scipy h5py
    # load openmpi
    module load mpi
    # install cmake from Kitware
    wget https://github.com/Kitware/CMake/releases/download/v3.19.3/cmake-3.19.3-Linux-x86_64.sh
    sh cmake-3.19.3-Linux-x86_64.sh  --skip-license --prefix=/usr/local

Install C/C++ compiler

.. code-block:: bash

    # 1. Install a package with repository for your system:
    # On CentOS, install package centos-release-scl available in CentOS repository:
    sudo yum install centos-release-scl

    # On RHEL, enable RHSCL repository for you system:
    sudo yum-config-manager --enable rhel-server-rhscl-7-rpms

    # 2. Install the collection:
    sudo yum install devtoolset-7

    # 3. Start using software collections:
    scl enable devtoolset-7 bash

Install pyre/AlTar
~~~~~~~~~~~~~~~~~~

Please follow the instructions in :ref:`General Steps`.

.. _lmod:

Linux with software modules
---------------------------

Many clusters use software modules to load libraries and software packages, e.g.,

.. code-block:: bash

    # list available modules
    module av
    # load a certain module
    module load cuda/10.2
    # list loaded modules
    module list
    # show the loaded module information
    module show cuda

Please load all necessary modules as listed in :ref:`Prerequisites`. You may then follow the :ref:`General Steps` above to install pyre and AlTar.

Since modules are set up differently in different computers, we only provide a general prescription if CMake fails to locate the prerequisite package from auto search.

You may provide the package path to CMake by,

    - ``-DCMAKE_PREFIX_PATH``, which specifies the package installation prefix to be searched. Files are expected to be arranged in a standard fashion under prefix, ``bin``, ``includes``, ``lib``. If the files are not arranged in the standard way, you may use options below,
    - ``-DCMAKE_INCLUDE_PATH``, which specifies the search path(s) for header files;
    - ``-DCMAKE_LIBRARY_PATH``. which specifies the search paths(s) for library files.

Each of these three parameters can be a semicolon-separated list to include more than one paths, e.g., ``-DCMAKE_PREFIX_PATH="/PATH/To/GSL;/PATH/To/HDF5;/PATH/To/MPI``.

CMake uses various builtin *Find modules* to search various packages, while each *Find module* may use some *hints* to locate the package. For example, ``FindGSL`` uses ``GSL_ROOT_DIR``, and ``FindMPI`` uses ``MPIEXEC_EXECUTABLE`` or ``MPI_HOME``. These mint may be passed as environmental variables ``export GSL_ROOT_DIR=...`` or as cmake options, e.g., ``-DGSL_ROOT_DIR=...``.

.. note:: Many clusters have their own recommended MPI packages which are optimized for the specific type of interconnects. Before using these pre-installed MPI packages, please check whether they have ``cxx`` devel support, or ``libmpi_cxx.so`` is available, which is required by AlTar.


.. _Docker:

Docker container
================

You may follow the steps below to build a docker image, based on a NVIDIA cuda 10.2 image with Ubuntu.

.. code-block:: bash

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


Open another terminal, find out the *CONTAINER ID* for this image, named *cuda/nvidia:10.2*, and commit the changes to a new image

.. code-block:: bash

    $ docker commit CONTAINER_ID altar:2.0.2-cuda

To run AlTar from the container

.. code-block:: bash

    $ docker run --gpus all -ti -v ${PWD}:/mnt altar:2.0.2-cuda

which also mounts the current directory as /mnt in the virtual system. You may go to your job directory and run AlTar from there.

If you meet a ``UnicodeDecodeError``, you will need to ``export LANG=en_US.UTF-8`` at first. See :ref:`Locales` for more details.

OpenMPI may issue a warning to run MPI jobs as a *root* user, you may add the ``--allow-run-as-root`` option to your job configuration file as follows,

.. code-block:: none

    ; for parallel runs
    mpi.shells.mpirun:
        extra = -mca btl self,tcp --allow-run-as-root




Install with the mm_ build tool
===============================

The mm_ build tool (please note that it is different from the old mm, or `config <https://github.com/aivazis/config>`__ build tool) is another powerful tool to build hybrid python/c/c++/cuda applications.

Download ``mm`` build tool
--------------------------

.. code-block:: bash

    cd ${HOME}/tools/src
    git clone https://github.com/aivazis/mm.git

Prepare a ``config.mm`` file
------------------------------

The ``mm`` build tool requires a ``config.mm`` file to locate dependent libraries or packages. Taking Ubuntu 18.04 as an example, the ``config.mm`` file appear as

.. _ubuntu_18.04_config:

.. code-block:: python

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

.. code-block:: bash

    $ alias mm='python3 ${HOME}/tools/src/mm/mm.py'

or in ``csh/tcsh``,

.. code-block:: bash

    $ alias mm 'python3 ${HOME}/tools/src/mm/mm.py'

Now, you can compile ``pyre`` by

.. code-block:: bash

    $ cd ${HOME}/tools/src/pyre
    $ mm

By default, the compiled files are located at ``${HOME}/tools/src/pyre/products/debug-shared-linux-x86_64``. If you need to customize the installation, you can check the options offered by ``mm`` by

.. code-block:: bash

    $ mm --help

For example, if you prefer to install pyre to a system folder, you may use ``--prefix`` option, such as

.. code-block:: bash

    $ mm --prefix=/usr/local


After compiling/installation, you need to set up some environmental variables for other applications to access
``pyre``, for example, create a ``${HOME}/.pyre.rc`` for ``bash``,

.. code-block:: none

    # file .pyre.rc
    export PYRE_DIR=${HOME}/tools/src/pyre/products/debug-shared-linux-x86_64
    export PATH=${PYRE_DIR}/bin:$PATH
    export LD_LIBRARY_PATH=${PYRE_DIR}/lib:$LD_LIBRARY_PATH
    export PYTHONPATH=${PYRE_DIR}/packages:$PYTHONPATH
    export MM_INCLUDES=${PYRE_DIR}/include
    export MM_LIBPATH=${PYRE_DIR}/lib
    # end of file

or ``${HOME}/.pyre.cshrc`` for ``csh/tcsh``,

.. code-block:: none

    # file .pyre.cshrc
    setenv PYRE_DIR "${HOME}/tools/src/pyre/products/debug-shared-linux-x86_64"
    setenv PATH "${PYRE_DIR}/bin:$PATH"
    setenv LD_LIBRARY_PATH "${PYRE_DIR}/lib:$LD_LIBRARY_PATH"
    setenv PYTHONPATH "${PYRE_DIR}/packages:$PYTHONPATH"
    setenv MM_INCLUDES "${PYRE_DIR}/include"
    setenv MM_LIBPATH "${PYRE_DIR}/lib"
    # end of file

You will also need to append ``pyre`` configurations to ``${HOME}/.mm/config.mm`` or ``altar/.mm/config.mm`` or any other application who requires ``pyre``,

.. code-block:: none

    # append to the following lines to an existing config.mm
    # pyre
    pyre.dir =  ${HOME}/tools/src/pyre/products/debug-shared-linux-x86_64
    pyre.libraries := pyre journal ${if ${value cuda.dir}, pyrecuda}


Install AlTar
-------------
First, make sure that you have a prepared ``config.mm`` file, which also includes the ``pyre`` configuration, in either ``altar/.mm/`` or ``${HOME}/.mm`` directory.

Follow the same step to compile AlTar,

.. code-block:: bash

    $ cd ${HOME}/tools/src/altar
    $ mm

Similar to ``pyre`` installation, the AlTar products are located at ``${HOME}/tools/src/altar/products/debug-shared-linux-x86_64``, or the directory specified by ``mm --prefix=``.

Also, you need to set up some environmental variables for ``altar`` as well, for example, create a ``${HOME}/.altar2.rc`` for ``bash``,

.. code-block:: bash

    # file .altar2.rc
    export ALTAR2_DIR=${HOME}/tools/src/altar/products/debug-shared-linux-x86_64
    export PATH=${ALTAR2_DIR}/bin:$PATH
    export LD_LIBRARY_PATH=${ALTAR2_DIR}/lib:$LD_LIBRARY_PATH
    export PYTHONPATH=${ALTAR2_DIR}/packages:$PYTHONPATH
    # end of file

or ``${HOME}/.altar2.cshrc`` for ``csh/tcsh``,

.. code-block:: none

    # file .altar2.cshrc
    setenv ALTAR2_DIR "${HOME}/tools/src/altar/products/debug-shared-linux-x86_64"
    setenv PATH "${ALTAR2_DIR}/bin:$PATH"
    setenv LD_LIBRARY_PATH "${ALTAR2_DIR}/lib:$LD_LIBRARY_PATH"
    setenv PYTHONPATH "${ALTAR2_DIR}/packages:$PYTHONPATH"
    # end of file

Before running an altar/pyre application, you need to load the altar/pyre environmental settings

.. code-block:: bash

    $ source ${HOME}/.pyre.rc
    $ source ${HOME}/.altar2.rc


Tests and Examples
==================

Pyre tests are available at ``${HOME}/tools/src/pyre/tests``.

AlTar examples are are available for each model.

For details how to run AlTar applications, please refer to :ref:`User Guide`.



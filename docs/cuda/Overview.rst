
.. _Overview:

########
Overview
########

AlTar is a software package implementing the :ref:`CATMIP` and other Markov-Chain Monte-Carlo algorithms for Bayesian inference. Its software architecture follows the pyre_ framework, aiming to make high performance scientific computations more accessible to researchers with minimum knowledge of software engineering.

- AlTar's framework is developed in Python while the compute-intensive routines are developed as C/C++ or CUDA(for GPUs) extension modules, to offer a user-friendly interface without scarifying the efficiency.

- AlTar follows the ``components``-based programming model of pyre_. Components, as Python classes with extended functionalities, not only facilitate the modularized software development, but also offer user with great convenience to config settings and parameters *at runtime*:

    - to choose between different implementations of a prescribed functionality (protocol), e.g., to choose different Metropolis sampling algorithms;
    - to turn features on or off, e.g., the debugger, profiler;
    - parameters and other attributes are also implemented as configurable properties (traits).

- AlTar utilizes the job management system from pyre_ to self-deploy the simulations to different platforms, single thread or multiple threads, single machine or clusters, CPU or GPUs.


The main components of AlTar are

- the Bayesian framework (controller/annealer), which performs the MCMC sampling of the Bayesian posterior distribution;
- a model, which performs the forward modelling and feeds the resulting data likelihood to the Bayesian framework;
- job, which manages the size of a simulation and its deployment to different platforms.

These components are organized in an AlTar application, as the *root* component, to execute the AlTar simulations. The detailed instructions on each component are provided in this User Guide, which is organized as follows,

- :ref:`Quickstart <Quickstart>`: to demonstrate how to run AlTar simulations with a linear inverse problem;
- :ref:`An introduction to pyre <Pyre Framework>`: to offer a brief introduction to pyre_, especially the pyre config format ``.pfg`` which is adopted to configure various parameters/settings of an AlTar application;
- :ref:`The AlTar framework <AlTar Framework>`: to list the components of the default CATMIP annealer, other modified versions are also provided;
- :ref:`Job Management <Job Management>`: to explain how to configure the job deployment to different platforms;
- Models: to provide instructions on how to prepare data and run simulations for the following earthquake, volcano inverse problems,

    - Static inversion
    - Static inversion with Cp (forward model uncertainty)
    - Kinematic inversion
    - Mogi
    - CDM

    Users may also develop new models for other inverse problems, following the :ref:`Programming Guide`.

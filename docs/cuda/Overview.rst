
.. _Overview:

########
Overview
########

AlTar is a software package implementing the :ref:`CATMIP` and other Markov-Chain Monte-Carlo algorithms for Bayesian inference. It adopts the component-based software architecture and the job management system from the pyre_ framework, aiming to make high performance scientific computations more accessible to researchers with minimum knowledge of software engineering.

An AlTar application includes the following root components,

    - the Bayesian framework (controller/annealer), which performs the MCMC sampling of the Bayesian posterior distribution;
    - a model, which performs the forward modelling and feeds the resulting data likelihood to the Bayesian framework;
    - job, which manages the size of a simulation and its deployment to different platforms;

while each component can be configured from the configuration file, e.g., switching between different algorithms/implementations, turning on/off features, and of course, changing the value of a parameter.

To run AlTar simulations, it is usually done by a simple command

.. code-block::

    anAlTarApp --config=anAlTarApp.pfg

where ``anAlTarApp`` is an AlTar application tailed for a given inverse problem, while ``anAlTarApp.pfg`` is a configuration file you where specify settings for your simulation.

We have provided examples with each implemented inverse problem. You may use them as templates to prepare your own simulation. This Guides aims to provide detailed instructions on how to configure each component, which is organized as follows,

- :ref:`Quickstart <Quickstart>`: to demonstrate how to run AlTar simulations with a linear inverse problem;
- :ref:`An introduction to pyre <Pyre Framework>`: to offer a brief introduction to components and the ``.pfg`` configuration file format;
- :ref:`The AlTar framework <AlTar Framework>`: how to configure the components of the MCMC simulation;
- :ref:`Job Management <Job Management>`: how to configure the job deployment to different platforms;
- Models: to provide instructions on how to prepare data and run simulations for inverse problems in geophysics,

    - :ref:`Static inversion of earthquake source models <Static Inversion>`;
    - :ref:`Static inversion with Cp (forward model uncertainty) <Static Inversion Cp>`;
    - :ref:`Kinematic inversion of earthquake source models <Kinematic Inversion>`;
    - Mogi source model for volcanoes (TBD);
    - Compound dislocation model (CDM) for volcanoes (TBD).

Users may also develop new models for other inverse problems. A :ref:`Programming Guide` is also provided.
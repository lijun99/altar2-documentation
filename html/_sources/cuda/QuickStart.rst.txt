.. _QuickStart:

QuickStart
==========

As a quick start, we use the linear model as an example to demonstrate how to run Bayesian MCMC simulations with AlTar. :

#. Prepare a configuration file, e.g., ``linear.pfg``, to specify various parameters and settings;
#. Prepare input data files required for the model, e.g., for the linear model, the observed data, the data covariance and the Green's function;
#. Run a dedicated AlTar application, e.g., ``linear`` for the linear model;
#. Collect and analyze the simulation results.

The linear model example demonstrated here comes with the AlTar source package, under the directory :altar_src:`models/linear/examples <models/linear/examples>`. It is also available as a jupyter notebook in :tutorials:`linear`.

Prepare the configuration file
------------------------------

A configuration file is used to pass various settings to an AlTar application. Here is an example for the linear model,

.. literalinclude:: ../../jupyter/linear/linear.pfg
    :language: none
    :caption: linear.pfg
    :linenos:

The ``.pfg`` (pyre config) files follow a human-readable data-serialization format similar to YAML, where the data-structure hierarchy is maintained by whitespace indentation (or by full/partial paths, such as `job.tasks`, see :ref:`Pyre Config Format` for more detailed instructions).

The name of the AlTar application (instance), ``linear``, is set as the root. Configurable components of an AlTar application include

- ``model``, for model specific configurations, such as the prior distributions of the model parameters, parameters in the forward model, and the data observations;
- ``job``, which configures the size of the simulation, and how the job will be deployed, e.g., single or multiple threads, single machine or multi-node cluster, CPU or GPU;
- ``controller``, for configurations to control the Bayesian MCMC procedure.

.. note::

    If a component is not specified in the configuration, its `default` value/implementation will be used instead.

Model configurations vary depending on its own forward problem: model-specific instructions are provided in the respective sections of this Guide. Instructions for the main framework, such as ``job`` and ``controller``, can be found in the :ref:`AlTar Framework` section.


Prepare input files
-------------------

While simple configurations can be specified in the configuration file,
large sets of data are passed to the AlTar application by data files. Different model may require different categories of data, in different input format.

For the  linear model, the data likelihood is computed as

.. math::

    P({\bf d}|{\boldsymbol \theta}) &= \frac {1} {\sqrt{(2\pi)^m \text{det}(C_d)}}  \\
     &\times \exp\left[- \frac {1}{2} \left({\bf d} - {\bf d}^{pred} \right)^T C_d^{-1}  \left({\bf d} - {\bf d}^{pred} \right)\right]


where :math:`{\boldsymbol \theta}` is a vector with :math:`n` unknown model parameters, :math:`{\bf d}` a vector with :math:`m` observations, the covariance :math:`C_d` a :math:`m \times m` matrix representing the data uncertainties. The data prediction :math:`{\bf d}^{pred}` is given by the forward model

.. math::

   {\bf d}^{pred} = \mathcal{G}  {\boldsymbol \theta}.

where the Green's function :math:`\mathcal{G}`,  is a :math:`n\times m` matrix.

The computation requires three users' input, :math:`{\bf d}`, :math:`C_d`, and :math:`\mathcal{G}`, as plain text files ``data.txt``, ``cd.txt`` and ``green.txt``. The location of the files can be specified by the ``linear.model.case`` parameter in the configuration file, while the file names can be specified by ``linear.model.data``, ``linear.model.cd`` and ``linear.model.green``.


Run an AlTar application
------------------------

For each model, we have provided a dedicated command for running AlTar simulations (in fact, you can run ``altar`` for all models, but it may require some changes to the configuration file). The dedicated command for the linear model is ``linear``, which is a Python script as shown below

.. literalinclude:: ../../jupyter/linear/linear
    :language: python
    :linenos:

It defines a ``Linear`` application class and provides a ``main`` entry point for execution. The ``linear`` can be run as any other shell commands, but you do need to run it at the directory where the ``linear.pfg`` and the ``case (patch-9)`` directory are located,

.. code-block:: bash

    linear

and the simulation begins.

If you would like to use a different script file other than ``linear.pfg``

.. code-block:: bash

    linear --config=linear2.pfg

or if you would like to pass/change a parameter from command lines, e.g., to increase the number of Markov chains

.. code-block:: bash

    linear --job.chains=2**10

More run options will be explained in the :ref:`AlTar Framework` section.


Collect and analyze results
----------------------------

AlTar offers several options how to output the simulation results. The default is an HDF5 archiver, which outputs the simulation results from each :math:`\beta`-step to HDF5 files located at ``results`` directory. Data in these HDF5 files, named as ``step_nnn.h5``, can be viewed by a HDF Viewer, such as HDFView, HDFCompass.

For each ``step_nnn.h5``, the following structures are used

.. code-block:: none

    +---------- step_nnn.h5 ------
    ├── Annealer ; annealing data
    |   ├── beta ; the beta value
    |   └── covariance ; the covariance matrix for Gaussian proposal
    ├── Bayesian ; the Bayesian probabilities
    |   ├── prior ; prior probability for all samples, vector (samples)
    |   ├── likelihood ; data likelihood for all samples
    |   └── posterior ; posterior probability for all samples
    └── ParameterSets ;  samples
        └── theta ; samples of model parameters, 2d array (samples, parameters)


.. code-block:: python

    import h5py
    import numpy




You may draw a histogram of the posterior to check its distribution. Since the log values of the probabilities are used and saved, the distribution will normally show a lognormal form. You may also do some statistics on the samples, for example, mean and standard deviations. If the posterior assumes a Gaussian distribution, the mean model provides an estimated solution to the linear inverse problem. Some of the data analysis programs are also included with AlTar.



AlTar is a software package developed to perform Bayesian inference to inverse problems with the Markov Chain Monte-Carlo methods. It consists of

- a main framework which performs the Bayesian MCMC, and controls the job deployment;
- a model which performs the forward modeling and feeds the data likelihood results to the Bayesian framework. Model implementations for various inverse problems are included. Users may add new models by

An AlTar application integrates a model with the main framework and serves as the main program to run simulations.

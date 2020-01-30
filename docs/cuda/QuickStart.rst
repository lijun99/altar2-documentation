.. _QuickStart:

Getting Started
================

As a quick start, we use the linear model as an example to demonstrate how to use AlTar.

Running an AlTar simulation on a specific model usually consists of the following steps:

#. Prepare a configuration file, e.g., ``linear.pfg``, to specify various settings/configurations to the model and the AlTar framework;
#. Prepare input data files required for the model, e.g., for the linear model, the observed data, the data covariance and the Green's function;
#. Run a dedicated python script (as a shell command) to invoke the AlTar application for the model, e.g., ``linear`` for the linear model;
#. Collect and analyze the simulation results.

The linear model example demonstrated here comes with the AlTar source package, under the directory :altar_src:`models/linear/examples <models/linear/examples>`. It is also available as a jupyter notebook in :tutorials:`linear`. Examples for any other model in AlTar are also provided in the source package. Users may use these examples as templates to prepare their own projects.

Prepare the configuration file
------------------------------

A configuration file is used to pass various settings to an AlTar application. Here is an example for the linear model,

.. literalinclude:: ../../jupyter/linear/linear.pfg
    :language: none
    :caption: linear.pfg
    :linenos:

The ``.pfg`` (pyre config) files follow a human-readable data-serialization format similar to YAML, where the data-structure hierarchy is maintained by whitespace indentation (or by full/partial paths, such as `job.tasks`, see :ref:`Pyre Config Format` for more detailed instructions).

The name of the AlTar application (instance), ``linear``, is set as the root. Configurable components of an AlTar application include

- ``model``, for model specific configurations, such as the prior distributions of the model parameters, the forward modelling, and the data observations;
- ``job``, which configures the size of the simulation, and how the job will be deployed: single or multiple threads, single machine or multi-node cluster, CPU or GPU;
- ``controller``, for configurations to control the Bayesian inference procedure.

.. note::

    If a component is not specified in the configuration, its `default` value/implementation will be used instead.

Different models may have different configurable components: model-specific instructions are provided in the respective sections of this Guide. Instructions for the main framework, shared by all models, can be found in the :ref:`AlTar Framework` section.


Prepare input files
-------------------

Large sets of data are passed to the AlTar application by data files.

Different model may require different categories of data. For the linear model, the data likelihood for

.. math::

    P(d_1, \ldots, d_m |\theta_1, \ldots, \theta_n) &= \frac {1} {\sqrt{(2\pi)^m \text{det}C_d}} \\
     &\times \exp\left[- \frac {1}{2} \left({\bf d} - {\bf d}^{pred} \right)^T C_d^{-1}  \left({\bf d} - {\bf d}^{pred} \right)\right] \\
    \mathbb{d^{pred}} &= G  \mathbb{\theta}



the Green's function, a :math:`n\times m` array :math:`G_{ij}`, is needed to calculate the :math:`$n$-` predicted data (:math:`\{d_i\}` from :math:`$m$-` model parameters


To assign configurations at command line (which also overrides the corresponding configuration in ``.pfg`` file), you may add them as options as ``--option=setting``, e.g.,
::

    $ linear --model.case=18-patch

If you prefer to run the model with different configurations, e.g., ``linear_mpi.pfg`` for multi-threads, you may run
::

    $ linear --config=linear_mpi.pfg



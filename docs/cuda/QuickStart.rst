.. _QuickStart:

Getting Started
================

Please follow the :ref:`Installation Guide` to install AlTar 2.0.

As a quick start, we use the linear model as an example to demonstrate how to use AlTar.

To run an AlTar simulation on a specific model, users can follow these steps:

#. Prepare a configuration file, e.g., ``linear.pfg``, to specify various settings/configurations to the model and the AlTar framework;
#. Prepare input data files, e.g., for the linear model, the observed data, the data covariance and the Green's function;
#. Run a dedicated python script (as a shell command) to invoke the AlTar application for the model, e.g., ``linear`` for the linear model;
#. Collect and analyze the simulation results.

The linear model example demonstrated here comes with the AlTar source package, under the directory :altar_src:`models/linear/examples <models/linear/examples>`. It is also available as a jupyter notebook in :tutorials:`linear`.

For each model in AlTar, examples are provided in the source package. Users may use these examples as templates to prepare their own projects. Model-specific instructions are also provided in this Guide.

Prepare the configuration file
------------------------------

One prominent feature of AlTar is that it allows users to configure all the public settings in a program at run time, through the ``components``-based Python programming introduced by pyre_. Components are configurable Python class variables which can be used to set a parameter, an array, or to choose an implementation of a certain functionality. Settings of components can be passed to the program as command line arguments, or more conveniently, by a configuration file.

Three types of configuration files are supported by pyre_, and therefore AlTar: ``.pml`` (XML-style), ``.cfg`` (an INI-style format used in AlTar 1.1), and ``.pfg`` (JSON/YAML-style). We recommend ``.pfg`` for its human-readable data serialization format.

An example configuration file for the linear model, ``linear.pfg`` , appears as

.. literalinclude:: ../../jupyter/linear/linear.pfg
    :language: none
    :linenos:

The instance name of the AlTar application, ``linear`` is set as the root. Configurable components of the ``linear`` application, such as ``model``, ``controller``, ``job``, are listed under ``linear`` with indentation. Subsequently, components of ``model`` are listed under ``model``.

.. note::
   - If a component is not specified or listed in the configuration file, a default value/implementation is chosen instead.
   - Whitespace indentation is used for denoting structure, or hierarchy; however, tab characters are not allowed.





Users are encouraged to read the `pyre Documentation`_ for better understandings of the pyre_ framework as well as the ``.pfg`` configuration file.


Prepare input files
-------------------




To assign configurations at command line (which also overrides the corresponding configuration in ``.pfg`` file), you may add them as options as ``--option=setting``, e.g.,
::

    $ linear --model.case=18-patch

If you prefer to run the model with different configurations, e.g., ``linear_mpi.pfg`` for multi-threads, you may run
::

    $ linear --config=linear_mpi.pfg



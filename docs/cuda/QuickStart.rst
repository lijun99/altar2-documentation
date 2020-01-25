.. _QuickStart:

Getting Started
================


Please follow the :ref:`Installation Guide` to install AlTar 2.0 (as well as pyre_).




As a quick start, we use the linear model as an example to demonstrate how to use AlTar.

To run an AlTar simulation on a specific model, users can follow these steps:

#. Prepare a configuration file, e.g., ``linear.pfg``, to specify various settings/configurations to the model and the AlTar framework;
#. Prepare input data files, e.g., for the linear model, the observed data, the data covariance and the Green's function;
#. Run a dedicated python script (as a shell command) to invoke the AlTar application for the model, e.g., ``linear`` for the linear model;
#. Collect and analyze the simulation results.

The linear model example demonstrated below comes with the AlTar source code, under the directory :altar_src:`models/linear/examples <models/linear/examples>`. It is also available as a jupyter notebook in :tutorials:`linear`.

For each model in AlTar, we have prepared examples included in the source code package. Users may use these examples as templates to prepare their own projects. Detailed instructions for each model are also provided in this Guide.

Prepare the configuration file
------------------------------

AlTar 2.0 is based on the pyre_  framework, and accepts ``.pfg`` (pyre config)  configuration files. While other pyre configuration formats such as ``.pml`` (pyre XML) and ``.cfg`` (an INI-style configuration file used in AlTar 1.1) are also accepted, we recommend ``.pfg`` for its human-readable data serialization format, similar to JSON and YAML.

An example of the configuration file ``linear.pfg`` for the linear model appears as

.. literalinclude:: ../../jupyter/linear/linear.pfg
    :language: none
    :linenos:

One of the key concepts in AlTar programming, as inherited from the pyre_ framework, is ``components``, which may appear like Python Class variables but have extended functionalities: they are highly configurable and can be specified by users at runtime.


Users are encouraged to read the `pyre Documentation`_ for better understandings of the pyre_ framework as well as the ``.pfg`` configuration file.


Prepare input files
-------------------




To assign configurations at command line (which also overrides the corresponding configuration in ``.pfg`` file), you may add them as options as ``--option=setting``, e.g.,
::

    $ linear --model.case=18-patch

If you prefer to run the model with different configurations, e.g., ``linear_mpi.pfg`` for multi-threads, you may run
::

    $ linear --config=linear_mpi.pfg



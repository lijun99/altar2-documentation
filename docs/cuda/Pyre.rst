.. _Pyre Framework:

############################
Pyre: a short introduction
############################

AlTar's architecture is based on the pyre_ framework. Before the official documentation for pyre is released, we offer here a brief introduction to pyre, its programming design and its configuration file format which are necessary for AlTar users.

Programming Design
==================

Python offers a modular programming design with modules and classes while pyre extends the functionalities of python classes to facilitate their integrations and configurations, through *components*.

Protocol and Components
-----------------------

A prescribed functionality is defined as a *protocol* (similar to an abstract class). For example, various distributions are used in AlTar, mainly serving as prior distributions. We first define a protocol,

.. code-block:: python

    # the protocol
    class Distribution(altar.protocol, family="altar.distributions"):
        """
        The protocol that all AlTar probability distributions must satisfy
        """

        # required behaviors
        @altar.provides
        def initialize(self, **kwds):
            """
            Initialize with the given random number generator
            """

        # model support
        @altar.provides
        def initializeSample(self, theta):
            """
            Fill my portion of {theta} with initial random values from my distribution.
            """

        @altar.provides
        def priorLikelihood(self, theta, prior):
            """
            Fill my portion of {prior} with the likelihoods of the samples in {theta}
            """

        @altar.provides
        def verify(self, theta, mask):
            """
            Check whether my portion of the samples in {theta} are consistent with my constraints, and
            update {mask}, a vector with zeroes for valid samples and non-zero for invalid ones
            """

        ... ...

        # framework hooks
        @classmethod
        def pyre_default(cls):
            """
            Supply a default implementation
            """
            # use the uniform distribution
            from .Uniform import Uniform as default
            # and return it
            return default

where ``@altar.provides`` decorator specifies the behaviors (methods) that its implementations must define. An implementation, for example, the Uniform distribution, is defined as a *component*,

.. code-block:: python

    class Uniform(altar.component, family="altar.distributions.uniform"):
        """
        The uniform probability distribution
        """

        # user configurable state
        parameters = altar.properties.int()
        parameters.doc = "the number of model parameters that i take care of"

        offset = altar.properties.int(default=0)
        offset.doc = "the starting point of my parameters in the overall model state"

        # user configurable state
        support = altar.properties.array(default=(0,1))
        support.doc = "the support interval of the prior distribution"


        # protocol obligations
        @altar.export
        def initialize(self, rng):
            """
            Initialize with the given random number generator
            """
            # set up my pdf
            self.pdf = altar.pdf.uniform(rng=rng.rng, support=self.support)
            # all done
            return self

        @altar.export
        def initializeSample(self, theta):
            """
            Fill my portion of {theta} with initial random values from my distribution.
            """
            # grab the portion of the sample that's mine
            θ = self.restrict(theta=theta)
            # fill it with random numbers from my initializer
            self.pdf.matrix(matrix=θ)
            # and return
            return self


        @altar.export
        def verify(self, theta, mask):
            """
            Check whether my portion of the samples in {theta} are consistent with my constraints, and
            update {mask}, a vector with zeroes for valid samples and non-zero for invalid ones
            """

            ... ...

            # all done; return the rejection map
            return mask

        ... ...

        # private data
        pdf = None # the pdf implementation

where the required behaviors specific to the Uniform distribution are defined. Besides behaviors, a component may also include attributes such as

  - Properties, configurable parameters in terms of basic Python data type, such as an integer [defined as ``altar.properties.int()``;
  - Sub-Components, configurable attributes in terms of components;
  - Non-configurable attributes, regular Python objects such as static properties or objects determined at runtime, e.g., the *pdf* function in ``Distribution``.

Components are building blocks of AlTar. For example, Distribution can be used as the prior distribution in a Bayesian model,

.. code-block:: python

    class Bayesian(altar.component, family="altar.models.bayesian", implements=model):
    """
    The base class of AlTar models that are compatible with Bayesian explorations
    """

        prior = altar.distributions.distribution()
        prior.doc = "the prior distribution"

        ... ...

Here, prior is a configurable component, for which users can specify at runtime by ``model.prior=uniform`` or any other distributions implementing the Distribution-protocol. Since the protocol defines the uniform distribution as its default implementation, if none is specified at runtime, the uniform distribution is used by default.

Note also that *components* are abstract methods and can be only be instantiated by an AlTar application instance. If you create a component instance in a Python shell, it will not behave as a regular Python class.


.. _Pyre Config Format:

Pyre Config Format (``.pfg``)
=============================

Configurations of properties and components can be passed to the program as command line arguments, or more conveniently, by a configuration file. Three types of configuration files are supported by pyre_/AlTar: ``.pml`` (XML-style), ``.cfg`` (an INI-style format used in AlTar 1.1), and ``.pfg`` (YAML/JSON-style). We recommend ``.pfg`` for its human-readable data serialization format.

An example of ``.pfg`` file is provided in :ref:`QuickStart`, for the linear model.

Some basic rules of ``.pfg`` format are

- Whitespace indentation is used for denoting structure, or hierarchy; however, tab characters are not allowed.
- Hierarchy of components can be specified by indentation, or by explicit full path, or by a combination of partial path with indentation. For example, these three configurations are equivalent:

    .. code-block:: none

        ; method 1: all by indentation
        linear:
            job:
                tasks = 1
                gpus = 0
                chains = 2**10

        ; method 2: all by full path
        linear.job.tasks = 1
        linear.job.gpus = 0
        linear.job.chains = 2**10

        ; method 3: combination with partial path and indentation
        linear:
            job.tasks = 1
            job.gpus = 0
            job.chains = 2**10

- If a component is not specified or listed in the configuration file, a default value/implementation specified in the Python program will be used instead.
- Strings such as paths, names, don't need quotation marks.

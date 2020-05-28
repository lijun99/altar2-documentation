
.. _Prior Distributions:

######################
(Prior) Distributions
######################

There are several probability distributions defined in AlTar, serving as prior distributions.

For a prior distribution :mod:`altar.distributions.distribution`, the following methods are required

.. code-block:: python


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

In AlTar, the logarithmic values of the Bayesian probability densities are processed. Therefore, in addition to ``priorLikelihood``, a ``verify`` method is needed for certain ranged distributions to check whether the proposed samples fall outside the range.

For a parameter to be sampled, the distributions for generating the initial samples and computing the prior probability densities during the simulation may be different. For example, in static inversion of earthquakes, you may want to use a Moment Scale distribution to generate (strike or dip) slips whose sum is consistent with a given moment magnitude scale, while during the simulation, while a simple uniform distribution for ``priorLikelihood`` and ``verify``.

Please note that AlTar processes samples in batch, where :math:`\theta` is a 2d array ``shape=(samples, parameters)``. Also, in a specific Model, there may be different parameter sets which observe different prior distributions. Therefore, the methods in a prior distribution are responsible for its own portion of parameters (selected columns of :math:`\theta`) and for a batched samples (rows of :math:`\theta`).

Uniform
========

The probability density function (PDF) for a uniform distribution is

.. math::

    f(x; a, b) &= \frac {1}{b-a}, \text{for } x \in [a,b] \\
        &= 0, \text{otherwise}

where :math:`[a, b]` is the support or range.

:Example:

.. code-block:: none

    prior = uniform
    prior:
        support = (0, 1)

Gaussian
=========

The PDF for the Gaussian (normal) distribution is defined as

.. math::

    f(x; \mu, \sigma) = \frac {1}{\sqrt{2\pi} \sigma} e^{-\frac{(x-\mu)^2}{2\sigma^2}},

where :math:`\mu` and :math:`\sigma^2` are mean (center) and variance, respectively.

:Example:

.. code-block:: none

    prior = gaussian
    prior:
        mean = 0
        sigma = 2

Truncated Gaussian
==================

The `truncated Gaussian distribution <https://en.wikipedia.org/wiki/Truncated_normal_distribution>`_ is derived from the Gaussian distribution but is only finite within the support range.

:Example:

(Currently only implemented in CUDA).

.. code-block:: none

    prior = altar.cuda.distributions.tgaussian
    prior:
        support = (-1, 1)
        mean = 0
        sigma = 2

Preset
======

The ``Preset`` distribution is used to load initial samples from pre-calculated ones. Therefore, it only serves as a preparation (``prep``) distribution. The currently support input format is HDF5, as the default output for AlTar simulation results.

:Example:

(Currently only implemented in CUDA).

For example, in the earthquake (seismic) inversion, we have samples of ``strikeslip`` generated from the static inversion and would like to load them for the kinematic inversion,

.. code-block:: none

    prep = altar.cuda.distributions.preset ; load preset samples
    prep.input_file = theta_cascaded.h5 ; file name
    prep.dataset = ParameterSets/strikeslip ; dataset name in h5

Other Distributions
===================

More prior distributions can be easily added. You may follow the existing distributions as examples. Or please write to us so that we add them to the package.






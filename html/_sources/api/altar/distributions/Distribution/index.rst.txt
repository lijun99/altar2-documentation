:mod:`altar.distributions.Distribution`
=======================================

.. py:module:: altar.distributions.Distribution


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   altar.distributions.Distribution.Distribution



.. py:class:: Distribution

   Bases: :class:`altar.protocol`

   The protocol that all AlTar probability distributions must satisfy

   .. attribute:: parameters
      

      

   .. attribute:: doc
      :annotation: = the number of model parameters that i take care of

      

   .. attribute:: offset
      

      

   .. attribute:: doc
      :annotation: = the starting point of my parameters in the overall model state

      

   .. method:: initialize(self, **kwds)

      Initialize with the given random number generator


   .. method:: initializeSample(self, theta)

      Fill my portion of {theta} with initial random values from my distribution.


   .. method:: priorLikelihood(self, theta, prior)

      Fill my portion of {prior} with the likelihoods of the samples in {theta}


   .. method:: verify(self, theta, mask)

      Check whether my portion of the samples in {theta} are consistent with my constraints, and
      update {mask}, a vector with zeroes for valid samples and non-zero for invalid ones


   .. method:: sample(self)

      Sample the distribution using a random number generator


   .. method:: density(self, x)

      Compute the probability density of the distribution at {x}


   .. method:: vector(self, vector)

      Fill {vector} with random values


   .. method:: matrix(self, matrix)

      Fill {matrix} with random values


   .. method:: pyre_default(cls)
      :classmethod:

      Supply a default implementation




:mod:`altar.distributions.Base`
===============================

.. py:module:: altar.distributions.Base


Module Contents
---------------

.. py:class:: Base

   Bases: :class:`altar.component`

   The base class for probability distributions

   .. attribute:: parameters
      

      

   .. attribute:: doc
      :annotation: = the number of model parameters that belong to me

      

   .. attribute:: offset
      

      

   .. attribute:: doc
      :annotation: = the starting point of my parameters in the overall model state

      

   .. attribute:: pdf
      

      

   .. method:: initialize(self, rng)
      :abstractmethod:


      Initialize with the given random number generator


   .. method:: initializeSample(self, theta)


      Fill my portion of {theta} with initial random values from my distribution.


   .. method:: priorLikelihood(self, theta, likelihood)


      Fill my portion of {likelihood} with the likelihoods of the samples in {theta}


   .. method:: verify(self, theta, mask)
      :abstractmethod:


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


   .. method:: restrict(self, theta)


      Return my portion of the {theta}




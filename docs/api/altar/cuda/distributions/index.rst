:mod:`altar.cuda.distributions`
===============================

.. py:module:: altar.cuda.distributions


Submodules
----------
.. toctree::
   :titlesonly:
   :maxdepth: 1

   cudaDistribution/index.rst
   cudaGaussian/index.rst
   cudaPreset/index.rst
   cudaTGaussian/index.rst
   cudaUniform/index.rst


Package Contents
----------------

.. py:class:: distribution

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



.. py:class:: cudaDistribution

   Bases: :class:`altar.distributions.Base.Base`

   The base class for probability distributions

   .. attribute:: parameters
      

      

   .. attribute:: doc
      :annotation: = the number of model parameters that belong to me

      

   .. attribute:: offset
      

      

   .. attribute:: doc
      :annotation: = the starting point of my parameters in the overall model state

      

   .. attribute:: device
      

      

   .. attribute:: idx_range
      

      

   .. attribute:: precision
      

      

   .. method:: initialize(self, rng)


      Initialize with the given random number generator


   .. method:: verify(self, theta, mask)



   .. method:: cuInitialize(self, application)


      cuda specific initialization


   .. method:: cuInitSample(self, theta)


      cuda process to initialize random samples


   .. method:: cuVerify(self, theta, mask)


      cuda process to verify the validity of samples


   .. method:: cuEvalPrior(self, theta, prior)


      cuda process to compute the prior



.. function:: uniform()


.. function:: gaussian()


.. function:: tgaussian()


.. function:: preset()



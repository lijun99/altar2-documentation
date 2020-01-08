:mod:`altar.models.ParameterSet`
================================

.. py:module:: altar.models.ParameterSet


Module Contents
---------------

.. py:class:: ParameterSet

   Bases: :class:`altar.protocol`

   The protocol that all AlTar parameter sets must implement

   .. attribute:: count
      

      

   .. attribute:: doc
      :annotation: = the number of parameters in this set

      

   .. attribute:: prior
      

      

   .. attribute:: doc
      :annotation: = the prior distribution

      

   .. attribute:: prep
      

      

   .. attribute:: doc
      :annotation: = the distribution to use to initialize this parameter set

      

   .. method:: initialize(self, model, offset)


      Initialize the parameter set given the {model} that owns it


   .. method:: initializeSample(self, theta)


      Fill {theta} with an initial random sample from my prior distribution.


   .. method:: priorLikelihood(self, theta, priorLLK)


      Fill {priorLLK} with the likelihoods of the samples in {theta} in my prior distribution


   .. method:: verify(self, theta, mask)


      Check whether the samples in {theta} are consistent with the model requirements and update
      the {mask}, a vector with zeroes for valid samples and non-zero for invalid ones


   .. method:: pyre_default(cls, **kwds)
      :classmethod:


      Supply a default implementation




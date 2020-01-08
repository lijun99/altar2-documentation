:mod:`altar.models.Contiguous`
==============================

.. py:module:: altar.models.Contiguous


Module Contents
---------------

.. py:class:: Contiguous

   Bases: :class:`altar.component`

   A contiguous parameter set

   .. attribute:: count
      

      

   .. attribute:: doc
      :annotation: = the number of parameters in this set

      

   .. attribute:: prior
      

      

   .. attribute:: doc
      :annotation: = the prior distribution

      

   .. attribute:: prep
      

      

   .. attribute:: doc
      :annotation: = the distribution to use to initialize this parameter set

      

   .. attribute:: offset
      :annotation: = 0

      

   .. method:: initialize(self, model, offset)


      Initialize my state given the {model} that owns me


   .. method:: initializeSample(self, theta)


      Fill {theta} with an initial random sample from my prior distribution.


   .. method:: priorLikelihood(self, theta, priorLLK)


      Fill {priorLLK} with the log likelihoods of the samples in {theta} in my prior distribution


   .. method:: verify(self, theta, mask)


      Check whether the samples in {step.theta} are consistent with the model requirements and
      update the {mask}, a vector with zeroes for valid samples and non-zero for invalid ones


   .. method:: restrict(self, theta)


      Return my portion of the sample matrix {theta}




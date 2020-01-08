:mod:`altar.models.Bayesian`
============================

.. py:module:: altar.models.Bayesian


Module Contents
---------------

.. py:class:: Bayesian

   Bases: :class:`altar.component`

   The base class of AlTar models that are compatible with Bayesian explorations

   .. attribute:: offset
      

      

   .. attribute:: doc
      :annotation: = the starting point of my state in the overall controller state

      

   .. attribute:: parameters
      

      

   .. attribute:: doc
      :annotation: = the number of model degrees of freedom

      

   .. attribute:: psets
      

      

   .. attribute:: default
      

      

   .. attribute:: doc
      :annotation: = an ensemble of parameter sets in the model

      

   .. attribute:: rng
      

      

   .. attribute:: controller
      

      

   .. attribute:: job
      

      

   .. attribute:: info
      

      

   .. attribute:: warning
      

      

   .. attribute:: error
      

      

   .. attribute:: default
      

      

   .. attribute:: firewall
      

      

   .. method:: initialize(self, application)


      Initialize the state of the model given an {application} context


   .. method:: posterior(self, application)


      Sample my posterior distribution


   .. method:: initializeSample(self, step)


      Fill {step.theta} with an initial random sample from my prior distribution.


   .. method:: priorLikelihood(self, step)


      Fill {step.prior} with the likelihoods of the samples in {step.theta} in the prior
      distribution


   .. method:: dataLikelihood(self, step)


      Fill {step.data} with the likelihoods of the samples in {step.theta} given the available
      data. This is what is usually referred to as the "forward model"


   .. method:: posteriorLikelihood(self, step)


      Given the {step.prior} and {step.data} likelihoods, compute a generalized posterior using
      {step.beta} and deposit the result in {step.post}


   .. method:: likelihoods(self, annealer, step)


      Convenience function that computes all three likelihoods at once given the current {step}
      of the problem


   .. method:: verify(self, step, mask)
      :abstractmethod:


      Check whether the samples in {step.theta} are consistent with the model requirements and
      update the {mask}, a vector with zeroes for valid samples and non-zero for invalid ones


   .. method:: top(self, annealer)


      Notification that a β step is about to start


   .. method:: bottom(self, annealer)


      Notification that a β step just ended


   .. method:: mountInputDataspace(self, pfs)


      Mount the directory with my input files


   .. method:: restrict(self, theta)


      Return my portion of the sample matrix {theta}




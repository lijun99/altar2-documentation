:mod:`altar.cuda.models.cudaBayesianEnsemble`
=============================================

.. py:module:: altar.cuda.models.cudaBayesianEnsemble


Module Contents
---------------

.. py:class:: cudaBayesianEnsemble

   Bases: :class:`altar.models.Bayesian.Bayesian`

   A collection of AlTar models that comprise a single model

   .. attribute:: models
      

      

   .. attribute:: doc
      :annotation: = the collection of models in this ensemble

      

   .. attribute:: parameters
      

      

   .. attribute:: doc
      :annotation: = the number of model degrees of freedom

      

   .. attribute:: psets_list
      

      

   .. attribute:: doc
      :annotation: = list of parameter sets, used to set orders

      

   .. attribute:: psets
      

      

   .. attribute:: doc
      :annotation: = an ensemble of parameter sets in the model

      

   .. attribute:: case
      

      

   .. attribute:: doc
      :annotation: = the directory with the input files

      

   .. attribute:: datallk
      

      

   .. method:: initialize(self, application)


      Initialize the state of the model given an {application} context


   .. method:: cuInitialize(self, application)


      cuda initialization


   .. method:: posterior(self, application)


      Sample my posterior distribution


   .. method:: cuInitSample(self, theta)


      Fill {theta} with an initial random sample from my prior distribution.


   .. method:: cuVerify(self, theta, mask)


      Check whether the samples in {step.theta} are consistent with the model requirements and
      update the {mask}, a vector with zeroes for valid samples and non-zero for invalid ones


   .. method:: cuEvalPrior(self, theta, prior, batch)


      Fill {priorLLK} with the log likelihoods of the samples in {theta} in my prior distribution


   .. method:: cuEvalLikelihood(self, step, batch)


      Fill {step.data} with the likelihoods of the samples in {step.theta} given the available
      data. This is what is usually referred to as the "forward model"


   .. method:: cuEvalPosterior(self, step, batch)


      Given the {step.prior} and {step.data} likelihoods, compute a generalized posterior using
      {step.beta} and deposit the result in {step.post}


   .. method:: updateModel(self, annealer)


      Update model parameters if needed
      :param annealer:
      :return:


   .. method:: likelihoods(self, annealer, step, batch)


      Convenience function that computes all three likelihoods at once given the current {step}
      of the problem


   .. method:: verify(self, step, mask)


      Check whether the samples in {step.theta} are consistent with the model requirements and
      update the {mask}, a vector with zeroes for valid samples and non-zero for invalid ones




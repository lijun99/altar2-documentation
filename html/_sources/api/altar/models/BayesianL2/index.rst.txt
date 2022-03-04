:mod:`altar.models.BayesianL2`
==============================

.. py:module:: altar.models.BayesianL2


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   altar.models.BayesianL2.BayesianL2



.. py:class:: BayesianL2(name, locator, **kwds)

   Bases: :class:`altar.models.Bayesian.Bayesian`

   A (Simplified) Bayesian Model with ParameterSets and L2 data norm

   .. attribute:: parameters
      

      

   .. attribute:: doc
      :annotation: = the number of model degrees of freedom

      

   .. attribute:: cascaded
      

      

   .. attribute:: doc
      :annotation: = whether the model is cascaded (annealing temperature is fixed at 1)

      

   .. attribute:: embedded
      

      

   .. attribute:: doc
      :annotation: = whether the model is embedded in an ensemble of models

      

   .. attribute:: psets_list
      

      

   .. attribute:: doc
      :annotation: = list of parameter sets, used to set orders

      

   .. attribute:: psets
      

      

   .. attribute:: default
      

      

   .. attribute:: doc
      :annotation: = an ensemble of parameter sets in the model

      

   .. attribute:: dataobs
      

      

   .. attribute:: default
      

      

   .. attribute:: doc
      :annotation: = observed data

      

   .. attribute:: case
      

      

   .. attribute:: doc
      :annotation: = the directory with the input files

      

   .. attribute:: idx_map
      

      

   .. attribute:: default
      

      

   .. attribute:: doc
      :annotation: = the indices for model parameters in whole theta set

      

   .. attribute:: return_residual
      

      

   .. attribute:: doc
      :annotation: = the forward model returns residual(True) or prediction(False)

      

   .. attribute:: observations
      

      

   .. attribute:: device
      

      

   .. attribute:: precision
      

      

   .. attribute:: ifs
      

      

   .. method:: initialize(self, application)

      Initialize the state of the model given an {application} context


   .. method:: posterior(self, application)

      Sample my posterior distribution


   .. method:: initializeSample(self, step)

      Fill {step.θ} with an initial random sample from my prior distribution.


   .. method:: verify(self, step, mask)

      Check whether the samples in {step.theta} are consistent with the model requirements and
      update the {mask}, a vector with zeroes for valid samples and non-zero for invalid ones


   .. method:: evalPrior(self, theta, prior)

      Fill {priorLLK} with the log likelihoods of the samples in {theta} in my prior distribution


   .. method:: forwardModel(self, theta, prediction)
      :abstractmethod:

      The forward model for a single set of parameters


   .. method:: forwardModelBatched(self, theta, prediction)

      The forward model for a batch of theta: compute prediction from theta
      also return {residual}=True, False if the difference between data and prediction is computed


   .. method:: evalDataLikelihood(self, theta, likelihood)

      calculate data likelihood and add it to step.prior or step.data


   .. method:: evalPosterior(self, step)

      Given the {step.prior} and {step.data} likelihoods, compute a generalized posterior using
      {step.beta} and deposit the result in {step.post}


   .. method:: likelihoods(self, annealer, step)

      Convenience function that computes all three likelihoods at once given the current {step}
      of the problem


   .. method:: updateModel(self, annealer)

      Update Model parameters if needed
      :param annealer:
      :return: default is False


   .. method:: mountInputDataspace(self, pfs)

      Mount the directory with my input files


   .. method:: loadFile(self, filename, shape=None, dataset=None, dtype=None)

      Load an input file to a gsl vector or matrix (for both float32/64 support)
      Supported format:
      1. text file in '.txt' suffix, stored in prescribed shape
      2. binary file with '.bin' or '.dat' suffix,
          the precision must be same as the desired gpuprecision,
          and users must specify the shape of the data
      3. (preferred) hdf5 file in '.h5' suffix (preferred)
          the metadata of shape, precision is included in .h5 file
      :param filename: str, the input file name
      :param shape: list of int
      :param dataset: str, name/key of dataset for h5 input only
      :return: output gsl vector/matrix


   .. method:: restrict(self, theta)

      Return my portion of the sample matrix {theta}




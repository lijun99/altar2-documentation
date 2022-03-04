:mod:`altar.cuda.models.cudaBayesianEnsemble`
=============================================

.. py:module:: altar.cuda.models.cudaBayesianEnsemble


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   altar.cuda.models.cudaBayesianEnsemble.cudaBayesianEnsemble



.. py:class:: cudaBayesianEnsemble(name, locator, **kwds)

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

      

   .. attribute:: forwardonly
      

      

   .. attribute:: doc
      :annotation: = whether to run the simulation or the forward problem only

      

   .. attribute:: theta_input
      

      

   .. attribute:: doc
      :annotation: = the theta input file with a vector of parameters

      

   .. attribute:: theta_dataset
      

      

   .. attribute:: doc
      :annotation: = the name/path of the theta dataset in h5 file

      

   .. attribute:: forward_output
      

      

   .. attribute:: doc
      :annotation: = the name/path of the file to save forward problem results

      

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


   .. method:: mountInputDataspace(self, pfs)

      Mount the directory with my input files


   .. method:: loadFile(self, filename, shape=None, dataset=None, dtype=None)

      Load an input file to a numpy array (for both float32/64 support)
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
      :return: output numpy.array


   .. method:: loadFileToGPU(self, filename, shape=None, dataset=None, out=None, dtype=None)

      Load an input file to a gpu (for both float32/64 support)
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
      :return: out altar.cuda.matrix/vector


   .. method:: forwardProblem(self, application, theta=None)

      Perform the forward modeling with given {theta}




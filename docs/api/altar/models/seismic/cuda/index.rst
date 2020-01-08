:mod:`altar.models.seismic.cuda`
================================

.. py:module:: altar.models.seismic.cuda


Submodules
----------
.. toctree::
   :titlesonly:
   :maxdepth: 1

   cudaCascaded/index.rst
   cudaKinematicG/index.rst
   cudaKinematicGCp/index.rst
   cudaMoment/index.rst
   cudaStatic/index.rst
   cudaStaticCp/index.rst


Package Contents
----------------

.. py:class:: model

   Bases: :class:`altar.models.Bayesian.Bayesian`

   The base class of AlTar models that are compatible with Bayesian explorations

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

      

   .. attribute:: observations
      

      

   .. attribute:: device
      

      

   .. attribute:: precision
      

      

   .. attribute:: ifs
      

      

   .. attribute:: gidx_map
      

      

   .. attribute:: gtheta
      

      

   .. method:: initialize(self, application)


      Initialize the state of the model given an {application} context


   .. method:: cuInitialize(self, application)


      cuda interface


   .. method:: posterior(self, application)


      Sample my posterior distribution


   .. method:: cuInitSample(self, theta)


      Fill {theta} with an initial random sample from my prior distribution.


   .. method:: cuVerify(self, theta, mask)


      Check whether the samples in {step.theta} are consistent with the model requirements and
      update the {mask}, a vector with zeroes for valid samples and non-zero for invalid ones


   .. method:: cuEvalPrior(self, theta, prior, batch)


      Fill {priorLLK} with the log likelihoods of the samples in {theta} in my prior distribution


   .. method:: cuEvalLikelihood(self, theta, likelihood, batch)


      calculate data likelihood and add it to step.prior or step.data


   .. method:: cuEvalPosterior(self, step, batch)


      Given the {step.prior} and {step.data} likelihoods, compute a generalized posterior using
      {step.beta} and deposit the result in {step.post}


   .. method:: likelihoods(self, annealer, step, batch=None)


      Convenience function that computes all three likelihoods at once given the current {step}
      of the problem


   .. method:: verify(self, step, mask)


      Check whether the samples in {step.theta} are consistent with the model requirements and
      update the {mask}, a vector with zeroes for valid samples and non-zero for invalid ones


   .. method:: updateModel(self, annealer)


      Update Model parameters if needed
      :param annealer:
      :return: default is False


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


   .. method:: restricted(self, theta, batch)


      extract theta which contains model's own parameters



.. function:: moment()


.. function:: static()


.. function:: staticcp()


.. function:: kinematicg()


.. function:: cascaded()



:mod:`altar.cuda.data.cudaDataL2`
=================================

.. py:module:: altar.cuda.data.cudaDataL2


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   altar.cuda.data.cudaDataL2.cudaDataL2



.. py:class:: cudaDataL2(name, locator, **kwds)

   Bases: :class:`altar.data.DataL2.DataL2`

   The observed data with L2 norm

   .. attribute:: data_file
      

      

   .. attribute:: doc
      :annotation: = the name of the file with the observations

      

   .. attribute:: observations
      

      

   .. attribute:: doc
      :annotation: = the number of observed data

      

   .. attribute:: cd_file
      

      

   .. attribute:: doc
      :annotation: = the name of the file with the data covariance matrix

      

   .. attribute:: cd_std
      

      

   .. attribute:: doc
      :annotation: = the constant covariance for data, sigma^2

      

   .. attribute:: dtype_cd
      

      

   .. attribute:: doc
      :annotation: = the data type (float32/64) for Cd computations if different from others

      

   .. attribute:: norm
      

      

   .. attribute:: default
      

      

   .. attribute:: doc
      :annotation: = l2 norm for calculating likelihood

      

   .. attribute:: merge_cd_to_data
      :annotation: = True

      

   .. attribute:: normalization
      :annotation: = 0

      

   .. attribute:: precision
      

      

   .. attribute:: gdataObsBatch
      

      

   .. attribute:: gcd_inv
      

      

   .. method:: initialize(self, application)

      Initialize data obs from model


   .. method:: cuEvalLikelihood(self, prediction, likelihood, residual=True, batch=None)

      compute the datalikelihood for prediction
      :param prediction: (samples x observations) input of predicted data
      :param likelihood: (samples) pre-allocated likelihood/norm
      :param residual: whether prediction is already subtracted by observed data
      :param batch: number of (first few) samples to be computed
      :return: likelihood


   .. method:: cd_inv(self)
      :property:

      Inverse of data covariance, in Cholesky decomposed form


   .. method:: release_cd(self)

      release gcd_inv


   .. method:: dataobsBatch(self)
      :property:

      A batch of duplicated observations


   .. method:: loadFile(self, filename, shape, dataset=None, dtype=None)

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


   .. method:: initializeCovariance(self)

      initialize gpu data and data covariance


   .. method:: updateCovariance(self, cp=None)

      Update the data covariance C_chi = Cd + Cp
      :param cp: cuda matrix with shape(obs, obs), data covariance due to model uncertainty
      :return:


   .. method:: checkPositiveDefiniteness(self, matrix, name=None)

      Check positive definiteness of a GPU matrix
      :param matrix: a real symmetric (GPU) matrix
      :return: true or false


   .. method:: mergeCdtoData(self, cd_inv, data)

      Merge the data covariance matrix to observed data
      :param cd_inv: the inverse of covariance matrix in Cholesky-decomposed form, with Lower matrix filled
      :param data: raw observed data
      :return:  cd_inv*data, a cuda vector




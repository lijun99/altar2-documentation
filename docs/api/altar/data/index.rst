:mod:`altar.data`
=================

.. py:module:: altar.data


Submodules
----------
.. toctree::
   :titlesonly:
   :maxdepth: 1

   DataL2/index.rst
   DataObs/index.rst


Package Contents
----------------

Classes
~~~~~~~

.. autoapisummary::

   altar.data.data
   altar.data.DataL2



Functions
~~~~~~~~~

.. autoapisummary::

   altar.data.datal2


.. py:class:: data

   Bases: :class:`altar.protocol`

   The protocol that all AlTar norms must satify

   .. method:: initialize(self, application)

      initialize data


   .. method:: pyre_default(cls, **kwds)
      :classmethod:

      Provide a default norm in case the user hasn't selected one



.. py:class:: DataL2(name, locator, **kwds)

   Bases: :class:`altar.component`

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
      :annotation: = the constant covariance for data

      

   .. attribute:: merge_cd_with_data
      

      

   .. attribute:: doc
      :annotation: = whether to merge cd with data

      

   .. attribute:: norm
      

      

   .. attribute:: default
      

      

   .. attribute:: doc
      :annotation: = the norm to use when computing the data log likelihood

      

   .. attribute:: normalization
      :annotation: = 0

      

   .. attribute:: ifs
      

      

   .. attribute:: samples
      

      

   .. attribute:: dataobs
      

      

   .. attribute:: dataobs_batch
      

      

   .. attribute:: cd
      

      

   .. attribute:: cd_inv
      

      

   .. attribute:: error
      

      

   .. method:: initialize(self, application)

      Initialize data obs from model


   .. method:: evalLikelihood(self, prediction, likelihood, residual=True, batch=None)

      compute the datalikelihood for prediction (samples x observations)


   .. method:: dataobsBatch(self)

      Get a batch of duplicated dataobs


   .. method:: loadData(self)

      load data and covariance


   .. method:: initializeCovariance(self, cd)

      For a given data covariance cd, compute L2 likelihood normalization, inverse of cd in Cholesky decomposed form,
      and merge cd with data observation, d-> L*d with cd^{-1} = L L*
      :param cd:
      :return:


   .. method:: updateCovariance(self, cp)

      Update data covariance with cp, cd -> cd + cp
      :param cp: a matrix with shape (obs, obs)
      :return:


   .. method:: computeNormalization(self, observations, cd)

      Compute the normalization of the L2 norm


   .. method:: computeCovarianceInverse(self, cd)

      Compute the inverse of the data covariance matrix



.. function:: datal2()



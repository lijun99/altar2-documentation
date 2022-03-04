:mod:`altar.models.regression.Linear`
=====================================

.. py:module:: altar.models.regression.Linear


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   altar.models.regression.Linear.Linear



.. py:class:: Linear(name, locator, **kwds)

   Bases: :class:`altar.models.BayesianL2.BayesianL2`

   Linear Regression model y= ax +b

   .. attribute:: x_file
      

      

   .. attribute:: doc
      :annotation: = the input file for x variable

      

   .. attribute:: x
      

      

   .. attribute:: y
      

      

   .. method:: initialize(self, application)

      Initialize the state of the model


   .. method:: forwardModel(self, theta, prediction)

      Forward Model
      :param theta: sampling parameters for one sample
      :param prediction: data prediction or residual (prediction - observation)
      :return: none




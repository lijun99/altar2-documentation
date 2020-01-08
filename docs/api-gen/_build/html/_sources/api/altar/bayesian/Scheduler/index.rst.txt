:mod:`altar.bayesian.Scheduler`
===============================

.. py:module:: altar.bayesian.Scheduler


Module Contents
---------------

.. py:class:: Scheduler

   Bases: :class:`altar.protocol`

   The protocol that all AlTar schedulers must implement

   .. method:: initialize(self, application)


      Initialize me and my parts given an {application} context


   .. method:: update(self, step)


      Push {step} forward along the annealing schedule


   .. method:: updateTemperature(self, step)


      Generate the next temperature increment


   .. method:: computeCovariance(self, step)


      Compute the parameter covariance of the sample in the {step}


   .. method:: rank(self, step)


      Rebuild the sample and its statistics sorted by the likelihood of the parameter values


   .. method:: pyre_default(cls, **kwds)
      :classmethod:


      Supply a default implementation




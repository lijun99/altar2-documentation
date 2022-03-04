:mod:`altar.bayesian.Sampler`
=============================

.. py:module:: altar.bayesian.Sampler


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   altar.bayesian.Sampler.Sampler



.. py:class:: Sampler

   Bases: :class:`altar.protocol`

   The protocol that all AlTar samplers must implement

   .. method:: initialize(self, application)

      Initialize me and my parts given an {application} context


   .. method:: samplePosterior(self, controller, step)

      Sample the posterior distribution


   .. method:: resample(self, controller, statistics)

      Update my statistics based on the results of walking my Markov chains


   .. method:: pyre_default(cls, **kwds)
      :classmethod:

      Supply a default implementation




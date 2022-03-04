:mod:`altar.bayesian.Profiler`
==============================

.. py:module:: altar.bayesian.Profiler


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   altar.bayesian.Profiler.Profiler



.. py:class:: Profiler(**kwds)

   Bases: :class:`altar.component`

   Profiler times the various simulation phases

   .. attribute:: seed
      

      

   .. attribute:: doc
      :annotation: = a template for the filename with the timing results

      

   .. attribute:: default
      :annotation: = prof-{{wid:05}}-{{beta:03}}x{{parameters:03}}x{{chains:06}}x{{steps:03}}.csv

      

   .. attribute:: pfs
      

      

   .. method:: initialize(self, application)

      Initialize me given an {application} context


   .. method:: simulationStart(self, controller, **kwds)

      Handler invoked when the simulation is about to start


   .. method:: samplePosteriorStart(self, controller, **kwds)

      Handler invoked at the beginning of sampling the posterior


   .. method:: prepareSamplingPDFStart(self, controller, **kwds)

      Handler invoked at the beginning of the preparation of the sampling PDF


   .. method:: prepareSamplingPDFFinish(self, controller, **kwds)

      Handler invoked at the end of the preparation of the sampling PDF


   .. method:: betaStart(self, controller, **kwds)

      Handler invoked at the beginning of the beta step


   .. method:: walkChainsStart(self, controller, **kwds)

      Handler invoked at the beginning of the chain walk


   .. method:: chainAdvanceStart(self, controller, **kwds)

      Handler invoked at the beginning of a single step of chain walking


   .. method:: chainAdvanceFinish(self, controller, **kwds)

      Handler invoked at the end of a single step of chain walking


   .. method:: verifyStart(self, controller, **kwds)

      Handler invoked before we start verifying the generated sample


   .. method:: verifyFinish(self, controller, **kwds)

      Handler invoked after we are done verifying the generated sample


   .. method:: priorStart(self, controller, **kwds)

      Handler invoked before we compute the prior


   .. method:: priorFinish(self, controller, **kwds)

      Handler invoked after we compute the prior


   .. method:: dataStart(self, controller, **kwds)

      Handler invoked before we compute the data likelihood


   .. method:: dataFinish(self, controller, **kwds)

      Handler invoked after we compute the data likelihood


   .. method:: posteriorStart(self, controller, **kwds)

      Handler invoked before we assemble the posterior


   .. method:: posteriorFinish(self, controller, **kwds)

      Handler invoked after we assemble the posterior


   .. method:: acceptStart(self, controller, **kwds)

      Handler invoked at the beginning of sample accept/reject


   .. method:: acceptFinish(self, controller, **kwds)

      Handler invoked at the end of sample accept/reject


   .. method:: resampleStart(self, controller, **kwds)

      Handler invoked at the beginning of resampling


   .. method:: resampleFinish(self, controller, **kwds)

      Handler invoked at the end of resampling


   .. method:: walkChainsFinish(self, controller, **kwds)

      Handler invoked at the end of the chain walk


   .. method:: betaFinish(self, controller, **kwds)

      Handler invoked at the end of the beta step


   .. method:: samplePosteriorFinish(self, controller, **kwds)

      Handler invoked at the end of sampling the posterior


   .. method:: simulationFinish(self, controller, **kwds)

      Handler invoked when the simulation is about to finish


   .. method:: save(self, controller)

      Save the times collected by my timers




:mod:`altar.bayesian.Notifier`
==============================

.. py:module:: altar.bayesian.Notifier


Module Contents
---------------

.. py:class:: Notifier(**kwds)

   Bases: :class:`altar.component`

   A dispatcher of events generated during the annealing process

   .. attribute:: start
      :annotation: = simulationStart

      

   .. attribute:: samplePosteriorStart
      :annotation: = samplePosteriorStart

      

   .. attribute:: prepareSamplingPDFStart
      :annotation: = prepareSamplingPDFStart

      

   .. attribute:: prepareSamplingPDFFinish
      :annotation: = prepareSamplingPDFFinish

      

   .. attribute:: betaStart
      :annotation: = betaStart

      

   .. attribute:: walkChainsStart
      :annotation: = walkChainsStart

      

   .. attribute:: chainAdvanceStart
      :annotation: = chainAdvanceStart

      

   .. attribute:: verifyStart
      :annotation: = verifyStart

      

   .. attribute:: verifyFinish
      :annotation: = verifyFinish

      

   .. attribute:: priorStart
      :annotation: = priorStart

      

   .. attribute:: priorFinish
      :annotation: = priorFinish

      

   .. attribute:: dataStart
      :annotation: = dataStart

      

   .. attribute:: dataFinish
      :annotation: = dataFinish

      

   .. attribute:: posteriorStart
      :annotation: = posteriorStart

      

   .. attribute:: posteriorFinish
      :annotation: = posteriorFinish

      

   .. attribute:: acceptStart
      :annotation: = acceptStart

      

   .. attribute:: acceptFinish
      :annotation: = acceptFinish

      

   .. attribute:: chainAdvanceFinish
      :annotation: = chainAdvanceFinish

      

   .. attribute:: walkChainsFinish
      :annotation: = walkChainsFinish

      

   .. attribute:: resampleStart
      :annotation: = resampleStart

      

   .. attribute:: resampleFinish
      :annotation: = resampleFinish

      

   .. attribute:: betaFinish
      :annotation: = betaFinish

      

   .. attribute:: samplePosteriorFinish
      :annotation: = samplePosteriorFinish

      

   .. attribute:: finish
      :annotation: = simulationFinish

      

   .. method:: initialize(self, application)


      Initialize me given an {application} context


   .. method:: register(self, monitor)


      Enable {monitor} as an observer of simulation events


   .. method:: notify(self, event, controller)


      Notify all handlers that are waiting for {event}




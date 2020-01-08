:mod:`altar.bayesian.Controller`
================================

.. py:module:: altar.bayesian.Controller


Module Contents
---------------

.. py:class:: Controller

   Bases: :class:`altar.protocol`

   The protocol that all AlTar controllers must implement

   .. attribute:: dispatcher
      

      

   .. attribute:: doc
      :annotation: = the event dispatcher that activates the registered handlers

      

   .. attribute:: archiver
      

      

   .. attribute:: doc
      :annotation: = the archiver of simulation state

      

   .. method:: posterior(self, model)


      Sample the posterior distribution of the given {model}


   .. method:: initialize(self, application)


      Initialize me and my parts given an {application} context


   .. method:: pyre_default(cls, **kwds)
      :classmethod:


      Supply a default implementation




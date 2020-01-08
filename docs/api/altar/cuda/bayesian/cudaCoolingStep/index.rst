:mod:`altar.cuda.bayesian.cudaCoolingStep`
==========================================

.. py:module:: altar.cuda.bayesian.cudaCoolingStep


Module Contents
---------------

.. py:class:: cudaCoolingStep(beta, theta, likelihoods, **kwds)

   Encapsulation of the state of the calculation at some particular β value

   .. attribute:: beta
      

      

   .. attribute:: theta
      

      

   .. attribute:: prior
      

      

   .. attribute:: data
      

      

   .. attribute:: posterior
      

      

   .. attribute:: precision
      

      

   .. method:: samples(self)
      :property:


      The number of samples


   .. method:: parameters(self)
      :property:


      The number of model parameters


   .. method:: start(cls, annealer)
      :classmethod:


      Build the first cooling step by asking {model} to produce a sample set from its
      initializing prior, compute the likelihood of this sample given the data, and compute a
      (perhaps trivial) posterior


   .. method:: alloc(cls, samples, parameters, dtype)
      :classmethod:


      Allocate storage for the parts of a cooling step


   .. method:: clone(self)


      Make a new step with a duplicate of my state


   .. method:: computePosterior(self, batch=None)


      (Re-)Compute the posterior from prior, data, and (updated) beta


   .. method:: copyFromCPU(self, step)


      Copy cpu step to gpu step


   .. method:: copyToCPU(self, step)


      copy gpu step to cpu step




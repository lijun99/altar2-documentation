:mod:`altar.bayesian.CoolingStep`
=================================

.. py:module:: altar.bayesian.CoolingStep


Module Contents
---------------

.. py:class:: CoolingStep(beta, theta, likelihoods, sigma=None, **kwds)

   Encapsulation of the state of the calculation at some particular β value

   .. attribute:: beta
      

      

   .. attribute:: theta
      

      

   .. attribute:: prior
      

      

   .. attribute:: data
      

      

   .. attribute:: posterior
      

      

   .. attribute:: sigma
      

      

   .. attribute:: mean
      

      

   .. attribute:: std
      

      

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


   .. method:: allocate(cls, annealer)
      :classmethod:



   .. method:: alloc(cls, samples, parameters)
      :classmethod:


      Allocate storage for the parts of a cooling step


   .. method:: clone(self)


      Make a new step with a duplicate of my state


   .. method:: computePosterior(self)


      Compute the posterior from prior, data, and beta


   .. method:: statistics(self)


      Compute the statistics of samples
      :return:


   .. method:: print(self, channel, indent=' ' * 2)


      Print info about this step


   .. method:: save_hdf5(self, path=None, iteration=None, psets=None)


      Save Coolinging Step to HDF5 file
      Args:
          step altar.bayesian.CoolingStep
          path altar.primitives.path
      Returns:
          None


   .. method:: load_hdf5(self, path=None, iteration=0)


      load CoolingStep from HDF5 file




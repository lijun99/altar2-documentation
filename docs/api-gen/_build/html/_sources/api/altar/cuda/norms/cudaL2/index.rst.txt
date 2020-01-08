:mod:`altar.cuda.norms.cudaL2`
==============================

.. py:module:: altar.cuda.norms.cudaL2


Module Contents
---------------

.. py:class:: cudaL2

   Bases: :class:`altar.norms.L2.L2`

   The L2 norm

   .. method:: cuEval(self, data, out=None, batch=None, cdinv=None)


      Compute the L2 norm of the given data  ||x||
      Arguments:
          data - matrix (samples x observations) 
          batch - number of samples to be computed (first rows)
          cdinv - inverse covariance matrix (observations x observations) in its Cholesky decomposed form (Upper Triangle)   
      Return:
          out - norm vector (samples)  


   .. method:: cuEvalLikelihood(self, data, constant=0.0, out=None, batch=None, cdinv=None)


      Compute the L2 norm data likelihood of the given data  const - ||x||^2/2
      Arguments:
          data - matrix (samples x observations) 
          batch - number of samples to be computed (first rows)
          constant - normalization constant
          cdinv - inverse covariance matrix (observations x observations) in its Cholesky decomposed form (Upper Triangle)   
      Return:
          out -  data likelihood vector (samples)  




.. _Background:

#############
Background
#############

Inverse problem
===============

An inverse problem in science is to infer a set of model parameters, :math:`{\boldsymbol \theta} = \{ \theta_1, \theta_2, \ldots, \theta_m \}`, given a model :math:`{ G}({\boldsymbol \theta})` and a set of observations :math:`{\bf d}=\{d_1, d_2, \ldots, d_n\}`. For example, in Seismology,  we deduce the earthquake rupture information :math:`{\boldsymbol \theta}` from ground motions :math:`{\bf d}` measured by seismometers, GPS, InSAR and other methods.  Here, the forward problem :math:`{\bf d} = G({\boldsymbol \theta})` is well defined but the inverse :math:`{\boldsymbol \theta} = G^{-1}({\bf d})`, in most cases, is not.  This happens to linear systems :math:`G({\boldsymbol \theta})= {\bf G} {\boldsymbol \theta}` when the observation matrix :math:`{\bf G}` is ill-posed, and nonlinear systems where the inverse is inherently difficult.

Bayesian Approach to Inverse problems
=====================================

Bayesian inference offers a statistical solution to inverse problems by modelling unknown parameters :math:`{\boldsymbol \theta}` as random variables subject to a conditional probability :math:`$P({\boldsymbol \theta}|{\bf d})`. According to Bayes' theorem, the probability is given by

.. math::

    \begin{eqnarray}
    P({\boldsymbol \theta}|{\bf d}) &=&  \frac {P({\boldsymbol \theta}) P({\bf d}|{\boldsymbol \theta})} {P({\bf d})}, \\
    P({\boldsymbol \theta}|{\bf d}) &:&  \text{posterior, the probability of observing ${\boldsymbol \theta}$ given that ${\bf d}$ is true},  \nonumber \\
     P({\boldsymbol \theta}) &:& \text{prior, the probability of observing ${\boldsymbol \theta}$ without regard to ${\bf d}$}, \nonumber \\
    P({\bf d}|{\boldsymbol \theta}) &:&  \text{likelihood, the probability of observing ${\bf d}$ given that  ${\boldsymbol \theta}$ is true},  \nonumber \\
    P({\bf d}) &:& \text{the probability of observing ${\bf d}$ independent of ${\boldsymbol \theta}$,}. \nonumber
    \end{eqnarray}

where :math:`P({\bf d})` is the same for all possible :math:`{\boldsymbol \theta}` and treated as a constant. The likelihood :math:`P({\bf d}|{\boldsymbol \theta})` can be determined from the forward modeling. For example, assuming a Gaussian probability density form,

.. math::

    \begin{eqnarray}
    P({\bf d}| {\bf \theta}) & =& e^{-\frac 12 \left[ {\bf d} - G({\boldsymbol \theta}) \right]^T C_\chi^{-1} \left[ {\bf d} - G({\boldsymbol \theta}) \right]},
    \end{eqnarray}

where the covariance matrix :math:`C_{\chi}` captures noises/errors in observations :math:`{\bf d}`, as well as uncertainties in the forward function :math:`G({\boldsymbol \theta})`.


The set of model parameters :math:`{\boldsymbol \theta}` with the maximum posterior probability (MAP) provides an estimate solution to the inverse problem. By fully evaluating the posterior density, Bayesian approach can also address situations when several sets of :math:`{\boldsymbol \theta}` have equal or comparable probabilities, or the posterior distribution is not unimodal, which other point estimators fail to. In addition, Bayesian approach accommodates uncertainty quantification, by including various types of uncertainties in the calculation.


CATPMIP Algorithm
=================

The posterior distribution :math:`P({\boldsymbol \theta}|{\bf d})` can be determined, for example, by evaluating :math:`P({\boldsymbol \theta}) P({\bf d}|{\boldsymbol \theta})` for all possible :math:`{\boldsymbol \theta}`. Instead of uniformly sampling over the entire :math:`{\bf \theta}`-space, we rely on Markov-Chain Monte-Carlo (MCMC) methods, which draw efficiently *weighted* samples pursuant to a prescribed probability distribution.

The CATMIP (Cascading Adaptive Transitional Metropolis in Parallel) algorithm belongs to a class of MCMC methods which use transitioning: samples are initially drawn from the prior distribution and subsequently *annealed* to the posterior through a series of transient distributions

.. math::

    \begin{eqnarray}
    P_m({\boldsymbol \theta}|{\bf d}) &=& P({\boldsymbol \theta}) P({\bf d}|{\boldsymbol \theta})^{\beta_m},
    \end{eqnarray}

where :math:`\beta_m` (in analogy to the inverse of temperature in statistical physics) is gradually increased from :math:`\beta_0=0` to :math:`\beta_M=1` in :math:`M` steps.

The procedure of CATMIP is as follows:

#. For :math:`m=0`, or :math:`\beta_0=0`, generate :math:`N_s` random samples from the distribution :math:`P_0 ({\boldsymbol \theta}|{\bf d}) = P({\boldsymbol \theta})`, as seeds of :math:`N_s` parallel chains.
#. Determine :math:`\beta_{m+1}` for the next :math:`\beta`-step, e.g., from the statistics of the samples from the :math:`m` :math:`\beta`-step. CATMIP uses an annealing schedule based on the coefficient of variance (COV) of the importance weights :math:`w_i = P({\bf d}|{\boldsymbol \theta}_i)^{\beta_{m+1}-\beta_m}`. The targeted COV is typically set as 1, or the effective sample size (ESS) equals to 50%.
#. Perform a resampling of samples based on their importance weights :math:`\{w_i\}`: some samples with small weights may be discarded while some samples with large weights are duplicated. The total number of samples is kept the same, as seeds for :math:`N_s` chains in the :math:`\beta_{m+1}`-step.
#. At the :math:`\beta_{m+1}`-step, a burn-in MCMC process is preformed with the Metropolis-Hastings algorithm. New samples are proposed from the distribution :math:`P_{m}  ({\boldsymbol \theta}|{\bf d})`, assuming a multivariate Gaussian form, and accepted/rejected subject to the probability density :math:`P_{m+1}  ({\boldsymbol \theta}|{\bf d})`. The acceptance ratio is also recorded, which is used to scale the jump distances for proposals in the next :math:`\beta`-step.
#. Repeat Steps 2-4 until :math:`\beta_{M}=1` is reached, or the desired equilibrium distribution :math:`P ({\boldsymbol \theta}|{\bf d})` is achieved.

Step 4 presents the majority of the computational load. Since each chain is updated independently, the computation is embarrassingly parallel, which makes CATMIP an ideal algorithm to be implemented on parallel computers, including GPUs.


References
==========
.. ruburic:: References

.. [Tar05] A. Tarantola, *Inverse Problem Theory and Methods for Model Parameter Estimation*, SIAM, 2005. ISBN: 978-0-89871-572-9.

.. [Minson13] S. E. Minson,  M. Simons,  and J. L. Beck, *Bayesian inversion for finite fault earthquake source models I—theory and algorithm*, Geophysical Journal International, Vol. 194, 1701 (2013).

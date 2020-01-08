############
Introduction
############

Bayesian Approach to Inverse problems
=====================================

According to Bayes' theorem

.. math::

    P(\theta|d) = \frac {P(d|\theta) P(\theta)}{P(d)}

the probability to find a set of parameters :math:`\theta` to produce a given set of observations :math:`d` \[:math:`P(\theta|d)`, the posterior\] is proportional to the likelihood of :math:`d` for a given set of :math:`\theta` \[:math:`P(d|\theta)`, the data likelihood\] and the initial belief of :math:`\theta` independent of the observations [:math:`P(\theta)`, the prior\].


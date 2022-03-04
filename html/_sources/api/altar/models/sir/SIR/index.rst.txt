:mod:`altar.models.sir.SIR`
===========================

.. py:module:: altar.models.sir.SIR


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   altar.models.sir.SIR.SIR



.. py:class:: SIR(name, locator, **kwds)

   Bases: :class:`altar.models.BayesianL2.BayesianL2`

   SIR model in epidemiology
   This model assumes five parameters
     S0 - The initial value of susceptible population (times the population base factor)
     I0 - The initial value of infectious
     R0 - The initial value of Recovered/Deaths
     β - the average number of contacts per person per time
     γ -  the rate of recovery or mortality
   to generate the time sequence of S(t), I(t) and R(t)
   It uses the new cases per day as data observations, or S(t-1)-S(t)

   .. attribute:: population_base
      

      

   .. attribute:: doc
      :annotation: = the base factor for population

      

   .. method:: _SIR_Rate(self, S, I, N, β, γ)

      SIR Rate equation


   .. method:: forwardModel(self, theta, prediction)

      Forward SIR model




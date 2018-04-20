#!/usr/bin/env python
"""Power Law dist: 3% -20% rich people income
#  city size, incomes, word frequencies, earthquake magnitudes.
#  /small occurrences are extremely common, large instances are extremely rare/.
#  ----
#  License: BSD
#  ----
#  0.1   - init version - 2018.4 - by Nick Qian
"""

import matplotlib.pyplot as plt
import math
from scipy.stats import powerlaw
import numpy as np


""" Power law dist: P[X = x] ~ x^-(k+1) = x^-a
    where event is just X = x. number of people.
"""
def power_law_dist(a):
    x = np.linspace(powerlaw.ppf(0.01, a), powerlaw.ppf(0.99, a), 100)
    return x



"""Zipf is directly power laws
   n ~ r^-b,   where n = income, r = rank of person inth income n
"""
def zipf_dist():
    pass




""" Pareto: P[X > x] ~ x^-k, where event is X > x
    r ~ n^-1/b,  where n = income, r = number of people whose income >= n
    Pareto dist just flip the x and y axes of Zipf dist.
"""
def pareto_dist():
    pass



""" log-log power-law distribution
     y_ln = c * x_ln
"""
def power_law_loglog():
    x_ln = [math.log(i) for i in x]
    y_ln = [math.log(i) for i in y]
    plt.plot(x_ln, y_ln)
    plt.show()





def main(a):

    #arg = raw_input("Zipf & Pareto belongs to power law. Please select: 1: Pareto\'s Law, 2: Zipf\'s law") )

    fig, ax = plt.subplots(1, 1)
    mean, var, skew, kurt = powerlaw.stats(a, moments='mvsk')

    x = power_law_dist(a)

    ax.plot(x, powerlaw.pdf(x, a), 'r-', lw=5, alpha=0.6, label='powerlaw pdf')
    rv = powerlaw(a)
    ax.plot(x, rv.pdf(x), 'k-', lw=2, label = 'frozen pdf')
    r = powerlaw.rvs(a, size=1000)
    ax.legend(loc='best', frameon=False)

    #plt.plt(x,y)
    plt.show()





if __name__ == "__main__":

    a = 0.87
    main(a)



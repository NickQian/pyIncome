#!/usr/bin/env python
""" exponential distribution: US and England "free economy"'s most people
#  ----
#  License: BSD
#  ----
#  0.1   - init version - 2018.4 - by Nick Qian
"""

import matplotlib.pyplot as plt
import math
from scipy.stats import expon
import numpy as np



"""exponential dist
#    y = c ** x
#
"""
def exp_dist(c):
    x = np.linspace(expon.ppf(0.1), expon.ppf(0.99), 100)

    return x




"""log-log exponential distribution
    y_ln = ln(c) * exp(x_ln)
"""
def exp_dist_loglog(c):
    x = list(range(1,100))
    y = [c**i for i in x]
    x_ln = [math.log(i) for i in x]
    y_ln = [math.log(i) for i in y]
    return x_ln, y_ln


def main():
    fix, ax = plt.subplots(1, 1)
    mean, var, skew, kurt = expon.stats(moments='mvsk')

    x = exp_dist(0.9)    #c=0.9

    ax.plot(x, expon.pdf(x), 'r-', lw=5, alpha=0.6, label='expon pdf')

    #freeze
    rv = expon()
    ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')

    #generate random num
    r = expon.rvs(size = 1000)

    # compare
    #ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
    ax.legend(loc='best', frameon=False)

    plt.show()



if __name__ == "__main__":
    main()

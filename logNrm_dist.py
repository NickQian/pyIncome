#!/usr/bin/env python
""" logarithmic normal distribution: China most people
#  ----
#  License: BSD
#  ----
#  0.1   - init version - 2018.4 - by Nick Qian
"""

from scipy.stats import lognorm
import matplotlib.pyplot as plt
import numpy as np




def logNrm_dist(s):
    x = np.linspace(lognorm.ppf(0.01, s), lognorm.ppf(0.99, s), 100)
    return x



def main(sharp):

    fig, ax = plt.subplots(1, 1)
    mean, var, skew, kurt = lognorm.stats(s, moments='mvsk')

    x = logNrm_dist(s)
    ax.plot(x, lognorm.pdf(x, s), 'r-', lw=5, alpha=0.6, label='lognorm pdf')

    # freeze the dist and display the frozen pdf 
    rv = lognorm(s)
    ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')

    # gen radom numbers
    r = lognorm.rvs(s, size=1000)

    #ax.hist(r, histtype='stepfilled', alpha=0.2)
    ax.legend(loc='best', frameon=False)

    plt.show()



if __name__ == "__main__":

    s = 0.654
    main(s)

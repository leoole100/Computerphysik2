#!/usr/bin/env python3

##
# Aufgabe 1a
# Die Binomialverteilung n¨ahert sich fur ¨ n → ∞ und p → 0 mit festem λ = np der
# Poissonverteilung. Plotte und vergleiche die Binomialverteilung fur ¨ n = 2, 100, 1000 fur ¨
# λ = 1 mit der Poissonverteilung. Diskutiere dazu den Mittelwert und die
# Standardabweichung.

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

def binomial(n, p, x):
	return stats.binom.pmf(x, n, p)

def poisson(lam, x):
	return stats.poisson.pmf(x, lam)


n = [2, 100, 1000]
p = 0.01
lam = 1
x = np.arange(0, 100, 1)
for i in n:
	plt.plot(x, binomial(i, p, x), label="Binomial n = " + str(i))
plt.plot(x, poisson(lam, x), label="Poisson")
plt.legend()
plt.show()

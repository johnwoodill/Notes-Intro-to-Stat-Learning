import pandas as pd
import numpy as np 
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from patsy import dmatrix

# Polynomial function
def poly(x, p):
    x = np.array(x)
    X = np.transpose(np.vstack((x**k for k in range(p+1))))
    return np.linalg.qr(X)[0][:,1:]

# Load data
dat = pd.read_csv('data/Wage.csv')

# Basis spline
t_X = dmatrix("bs(dat.age, knots=(25, 40, 60), degree=3, include_intercept=False)")

sfit = sm.OLS(y, t_X).fit()

snewdat = dmatrix("bs(agegrid, knots=(25, 40, 60), degree=3, include_intercept=False)")
spred = sfit.predict(snewdat)

fig, ax = plt.subplots()
ax.plot(dat.age, dat.wage, 'o', label="Data", alpha=0.1)
ax.plot(agegrid, spred, 'b-', label="True")
ax.legend(loc="best");
fig.show()
plt.close()

# Natural Splines

t_X = dmatrix("cr(dat.age, df=3)")

sfit = sm.OLS(y, t_X).fit()

snewdat = dmatrix("cr(agegrid, df=3)")
spred = sfit.predict(snewdat)

fig, ax = plt.subplots()
ax.plot(dat.age, dat.wage, 'o', label="Data", alpha=0.1)
ax.plot(agegrid, spred, 'b-', label="True")
ax.legend(loc="best");
fig.show()
plt.close()
import pandas as pd
import numpy as np 
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from patsy import dmatrix
from pygam import LinearGAM, s, f
from pygam.datasets import wage
from pygam.utils import generate_X_grid

# Polynomial function
def poly(x, p):
    x = np.array(x)
    X = np.transpose(np.vstack((x**k for k in range(p+1))))
    return np.linalg.qr(X)[0][:,1:]

# Load data
dat = pd.read_csv('data/Wage.csv')
X, y = wage(return_X_y=True)
gfit = LinearGAM(s(0) + s(1) + f(2)).fit(X, y).gridsearch(X, y)
#gfit.gridsearch(X, y)

# Manual predictions
#XX = gfit.generate_X_grid(term=0)
#XXpred = gfit.partial_dependence(0, XX)
#gpred = gfit.predict(X)

## plotting
plt.figure();
fig, axs = plt.subplots(1,3);

titles = ['year', 'age', 'education']
for i, ax in enumerate(axs):
    XX = gfit.generate_X_grid(term=i)
    ax.plot(XX[:, i], gfit.partial_dependence(term=i, X=XX))
    ax.plot(XX[:, i], gfit.partial_dependence(term=i, X=XX, width=.95)[1], c='r', ls='--')
    if i == 0:
        ax.set_ylim(-30,30)
    ax.set_title(titles[i]);

plt.show()
plt.close()

import pandas as pd
import numpy as np 
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures

# Polynomial function
def poly(x, p):
    x = np.array(x)
    X = np.transpose(np.vstack((x**k for k in range(p+1))))
    return np.linalg.qr(X)[0][:,1:]

# Load data
dat = pd.read_csv('data/Wage.csv')

y = dat.wage
X = PolynomialFeatures(4).fit_transform(dat.age.values.reshape(-1,1))

fit = sm.OLS(y, X).fit()
fit.summary()

agegrid= np.arange(dat.age.min(), dat.age.max()).reshape(-1,1)
newdat = PolynomialFeatures(4).fit_transform(agegrid)

preds = fit.predict(newdat)

fig, ax = plt.subplots()
ax.plot(dat.age, dat.wage, 'o', label="Data")
ax.plot(agegrid, preds, 'b-', label="True")
ax.legend(loc="best");
fig.show()
plt.close()

# Deciding on degrees
X1 = PolynomialFeatures(1).fit_transform(dat.age.values.reshape(-1,1))
X2 = PolynomialFeatures(2).fit_transform(dat.age.values.reshape(-1,1))
X3 = PolynomialFeatures(3).fit_transform(dat.age.values.reshape(-1,1))
X4 = PolynomialFeatures(4).fit_transform(dat.age.values.reshape(-1,1))
X5 = PolynomialFeatures(5).fit_transform(dat.age.values.reshape(-1,1))

fit1 = sm.OLS(y, X1).fit()
fit2 = sm.OLS(y, X2).fit()
fit3 = sm.OLS(y, X3).fit()
fit4 = sm.OLS(y, X4).fit()
fit5 = sm.OLS(y, X5).fit()

print(sm.stats.anova_lm(fit1, fit2, fit3, fit4, fit5, type=1))

# Step functions
dat_cut, bins = pd.cut(dat.age, 4, retbins = True, right = True)
dat_cut.value_counts(sort=False)

dat_steps = pd.concat([dat.age, dat_cut, dat.wage], keys = ['age', 'age_cuts', 'wage'], axis = 1)

dat_step_dummies = pd.get_dummies(dat_steps.age_cuts)

dat_step_dummies = sm.add_constant(dat_step_dummies)

dat_step_dummies = dat_step_dummies.drop(dat_step_dummies.columns[1], axis = 1)


cfit1 = sm.OLS(dat_steps.wage, dat_step_dummies).fit()
cfit1.summary()

bin_mapping = np.digitize(agegrid.ravel(), bins)
newdat2 = sm.add_constant(pd.get_dummies(bin_mapping).drop(1, axis=1))

cpreds = cfit1.predict(newdat2)
cpreds

fig, ax = plt.subplots()
ax.plot(dat.age, dat.wage, 'o', label="Data")
ax.plot(agegrid, cpreds, 'b-', label="True")
ax.legend(loc="best");
fig.show()
plt.close()
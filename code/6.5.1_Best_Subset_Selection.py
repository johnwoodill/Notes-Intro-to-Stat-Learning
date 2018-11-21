import pandas as pd
import numpy as np 
import itertools
import statsmodels.api as sm

# Load data
dat = pd.read_csv("pCloud Drive/Projects/Notes-Intro-to-Stat-Learning/data/Hitters.csv")

# Drop NA
dat = dat.dropna()

def processSubset(feature_set):
    # Fit model on feature_set and calculate RSS
    model = sm.OLS(y,X[list(feature_set)])
    regr = model.fit()
    fit = regr.predict(X[list(feature_set)])
    res = regr.resid
    RSS = np.sum(res ** 2)
    TSS = np.sum((fit) ** 2)
    R2 = TSS/(RSS + TSS)
    d = len(regr.params)
    n = len(y)
    sigma2 = RSS/(n - d + 1)
    Cp = (1/n) * (RSS + 2*d * sigma2)
    AIC = (1/(n*sigma2))*(RSS + 2*d*sigma2)
    BIC = (1/(n*sigma2))*(RSS + np.log(n)*d*sigma2)
    AR2 = 1 - ((RSS/(n-d-1))/((TSS/(n-1))))
    return {"model":regr, "RSS":RSS, "TSS":TSS, "Cp":Cp, "AIC":AIC, "BIC":BIC, "R2":R2, "AR2":AR2}


model = sm.OLS(y,X)
regr = model.fit()
fit = regr.predict(X)
res = regr.resid
RSS = np.sum(res ** 2)
TSS = np.sum((fit) ** 2)
R2 = TSS/(RSS + TSS)
d = len(regr.params)
n = len(y)
sigma2 = RSS/(n - d + 1)
Cp = (1/n) * (RSS + 2*d * sigma2)
AIC = (1/(n*sigma2))*(RSS + 2*d*sigma2)
BIC = (1/(n*sigma2))*(RSS + np.log(n)*d*sigma2)
AR2 = 1 - ((RSS/(n-d-1))/((TSS/(n-1))))

dummies = pd.get_dummies(dat[['League', 'Division', 'NewLeague']])
y = dat.Salary

# Drop the column with the independent variable (Salary), and columns for which we created dummy variables
X_ = dat.drop(['Salary', 'League', 'Division', 'NewLeague'], axis=1).astype('float64')

# Define the feature set X.
X = pd.concat([X_, dummies[['League_N', 'Division_W', 'NewLeague_N']]], axis=1)

results = []
k = 2
for combo in itertools.combinations(X.columns, k):
    results.append(processSubset(combo))

# Wrap everything up in a nice dataframe
models = pd.DataFrame(results)

# Choose the model with the highest RSS
best_model = models.loc[models['RSS'].idxmin()]
best_model
best_model['model'].rsquared
best_model['model'].aic

best_model['model'].summary()
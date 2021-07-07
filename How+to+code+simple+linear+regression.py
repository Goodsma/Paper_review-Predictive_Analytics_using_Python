
# coding: utf-8

# # How to code simple linear regression
# 
# First, let's build a linear regression model using the *statsmodels* package. This package builds several statistical models and provides a nice output summary of the linear regression model.

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm

#We will build a statistical linear regression model first
#If we would be using linear regression just for prediction, we use sklearn

#Make the data
#y are box offce revenues, x: advertising. All variables are expressed in 000s
#Linear regression accepts Pandas DataFrame 
d = {"y":[23,12,36,27,45],"x":[29,49,89,110,210]}
data = pd.DataFrame(data = d)

#We seperate the predictor and the response
#Linear regression only accepts a dataframe as input for the predictors
#so we use [[]] to select x from the data
x = data[['x']] 
y = data['y']


# In[2]:


#Make a scatterplot of the data and add the regression line: y_i =14.179+0.1481x_i
plt.scatter(x,y)
plt.plot(x,14.179 + 0.1481*x,'b-')
plt.show()


# In[3]:


#The statsmodels package does not add an intercept by default
#First,we need to add a constant
x = sm.add_constant(x)

#Fit an OLS model
linreg = sm.OLS(y,x).fit()
print(linreg.summary())


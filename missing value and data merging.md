# SICE: an improved missing data imputation technique
Shahidul Islam Khan1,2* and Abu Sayed Md Latiful Hoque1<br>
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7291187/

#### Type of missing data
* Missing Completely at Random (MCAR): Data are missing independently of both
observed and unobserved data.<br>
* Missing at Random (MAR): Given the observed data, data are missing independently of
unobserved data.<br>
* Missing Not at Random (MNAR): Missing observations are related to values of unobserved
data itself.<br>

### Single imputation
Single imputation techniques generate a specific value for a missing real value in a dataset.
This technique requires less computational cost. There are many types of single imputation
methods proposed by the researchers. The general procedure is to pick the highest possible
response by analyzing other responses. The value may be obtained by mean, median, mode
of the available values of that variable.

### Multiple imputation
Multiple imputation methods produce multiple values for the imputation of a single
missing value using different simulation models.
MICE algorithm, proposed by V. S. Buuren and K. Groothuis-Oudshoorn, is widely used
for multiple imputation. It pretends the probability of a missing variable depends on the observed
data. MICE provides multiple values in the place of one missing value by creating a series
of regression (or other suitable) models, depending on its ‘method’ parameter. 
Then it replaces missing values using the predicted values and creates a dataset called imputed
dataset. By iteration, it creates multiple imputed datasets. Each dataset is then analyzed
using standard statistical analysis techniques, and multiple analysis results are provided.
<br>
<br>

-------
Multiple imputation based approach such as MICE is a better strategy for handling missing data than single imputation as multiple imputations consider the uncertainty of missing data. 
However, It is complex to use MICE in practical cases with a massive dataset as the data analyst has to preserve and analyze multiple datasets instead of one.
This paper propose an algorithm Single Center Imputation from Multiple Chained Equation(SICE). It is an extension of
the existing MICE algorithm. It has two variants of SICE, namely SICE-Categorical and SICE-Numeric.
Experimental results with four different datasets show that our proposed method SICE performed better for
the imputation of binary and numeric data. So, we can say that SICE is an excellent
choice for missing data imputation, especially for massive datasets where MICE is
impractical to use because of its complexity.

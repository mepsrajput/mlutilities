# data analysis and wrangling
import pandas as pd
import numpy as np
from IPython.display import IFrame
from pandas_profiling import ProfileReport

# ML - Classifiers
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier

# visualization
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

# Design Changes
import warnings
warnings.filterwarnings('ignore')

# Dataframe Values upto 2 decimals
pd.set_option("display.float_format", lambda x: '%.2f' % x)

# Changing Default Table Style
%%html
<style>
table {float: left;}
table, th, tr, td {border: 1px solid #ccc !important}
</style>

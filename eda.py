""" -------------"""
# Basic Exploration
"""--------------"""

# Dataframe Profiling
ProfileReport(data, minimal=True, progress_bar=False).to_widgets()

# Display the Number of Variables & Number of Observations
df.shape

# Display the Variable Names and their Data Types
df.dtypes

# Descriptive Statistics
df.describe()

# Descriptive Statistics - Include the categoric vars
df.describe(include = 'all')

# Count the Number of Non-Missing Values for each Variable
df.count()

# Display the Metadata of the dataset
df.info()

# Frequency distribution of categoric variables
def freq(df, freq_list):
    freq_output = [
        pd.DataFrame({'dist': df[var].value_counts(dropna=False),
        '%': (df[var].value_counts(normalize=True, dropna=False)*100).round(1).astype(str) + ' %'
    }) for var in freq_list]
    
    return freq_output
        
freq(data, ["DISTRIBUTOR","MPAA RATING","GENRE"])


""" -------------"""
# Handling Duplicates
"""--------------"""

# 1. Check duplicates
df.duplicated()

# 2. Drop duplicates
df.drop_duplicates()

# 3. Drop duplicates - on a Column
df.drop_duplicates(subset='User_ID')


""" -------------"""
# Handling Outliers
"""--------------"""

# 1. Detecting Outliers
def detect_outliers(df, var_list):
  for var in var_list:
    min = df.var.min()
    p25 = df.var.quantile(0.25)
    median = df.var.quantile(0.5)
    p75 = df.var.quantile(0.75)
    max = df.var.max()
    iqr = q75-p25
    lc = q25 - 1.5*iqr
    uc = q75 + 1.5*iqr
    print(f"min_{var}: min, max_{var}: max, lc_{var}: lc , uc{var}: uc)
    df.var.plot(kind='box')

detect_outliers(df, [var1, var2])
          
# 2. Outlier Treatment
# 2.1 Clipping
def clip_outliers(df, var_list):
  for var in var_list:          
    df.var.clip(upper=uc, inplace=True)
    df.var.clip(lower=lc, inplace=True)
    df.var.plot(kind='box')
          
clip_outliers(df, [var1, var2])
          
          
""" -------------"""
# Handling Missing
"""--------------"""
          
# 1. Detecting the Missing Values
# percentage of missing values in each variable  
def missing_checker(df)
  df.isna().sum()/df.shape[0]

missing_checker(df)
    
# 2. Missing Value Treatment
# 2.1 Impute by Mode
def impute_mode(df, var_list):
  for var in var_list:        
    df.var.fillna(df.var.mode()[0],inplace=True)
    missing_checker(df)
          
impute_mode(df, [var1, var2])
          
# 2.2 Drop the Var
def drop_var(df, var_list):
  for var in var_list:        
    df.var.dropna(axis=1,inplace=True)
    missing_checker(df)
          
drop_var(df, [var1, var2])
          
                    
""" -------------"""
# Univariate Analysis
"""--------------"""
          
# 1. Numeric
          
# 1.1 Histogram 
def hist_plot(df, x, y, bin):
    df.plot.hist(bins=bin, grid=False, figsize=(23, 5), subplots=True, layout=(x,y))
    plt.show()
          
hist_plot(data, 1, 4, 20)
          
# 1.2 Boxplot
def box_plot(df, x, y):
    df.plot.box(figsize=(23, 5), subplots=True, layout=(x,y))
    plt.show()
    
box_plot(data, 1, 4)
         
# 2. Categoric

# 2.1 Pie Plot
def pie_plot(df, groupby_list):
    [df.groupby(var[0]).count().plot.pie(y=var[1], subplots=True, figsize=(22, 11), layout=(2,1)) for var in groupby_list]
    plt.show()
        
pie_plot(data, [("var1", "var2"), ("var3", "var4")])
     
          
""" -------------"""
# Bivariate Analysis
"""--------------"""
          
# 1. Numeric
          
# 1.1. Scatter Plot
def scatter_plot(df, cols, x, y):
    [df.plot.scatter(x=col[0],y=col[1],figsize=(23, 5), subplots=True, layout=(x,y)) for col in cols]
    plt.show()

scatter_plot(data, [("TICKETS SOLD", "YEAR"), ("TICKETS SOLD", "YEAR")], 1, 2)

# 1.2. Correlation Plot
def corr_plot(df, method):
    return df.corr(method=method).style.background_gradient(cmap='PuBuGn',axis=None).set_precision(1)

corr_plot(data, 'kendall')
# pearson : standard correlation coefficient
# kendall : Kendall Tau correlation coefficient
# spearman : Spearman rank correlation

# 2. Categoric

# 2.1. Correlation Plot          
def crosstab_plot(df, crosstab_list,x, y):
    [pd.crosstab(df[var[0]],df[var[1]]).plot.bar(rot=0, figsize=(15, 5), layout=(x,y)) for var in crosstab_list]
    plt.show()
        
crosstab_plot(data, [("DISTRIBUTOR", "MPAA RATING"), ("DISTRIBUTOR", "GENRE")], 5, 3)

     



               
          
          
          


      
          


          
















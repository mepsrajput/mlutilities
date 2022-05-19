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

# Handling Duplicates
# 1. Check duplicates
df.duplicated()

# 2. Drop duplicates
df.drop_duplicates()

# 3. Drop duplicates - on a Column
df.drop_duplicates(subset='User_ID')

# Handling Outliers
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
          
# Handling Missing
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
          
# Univariate Analysis
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
     
# Bivariate Analysis

     



               
          
          
          


      
          


          
















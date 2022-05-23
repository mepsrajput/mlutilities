""" -------------"""
# Basic Exploration
"""--------------"""

# Dataframe Profiling
ProfileReport(data, minimal=True, progress_bar=False).to_widgets()

# Display the Number of Variables & Number of Observations
df.shape

# Display the Variable Names and their Data Types
df.dtypes

# Describe Numeric Cols
df.describe()

# Describe Numeric Cols - Include the categoric vars
df.describe(include = 'all')

# Count the Number of Non-Missing Values for each Variable
df.count()

# Dataframe Summary
df.info()

# Unique values in each col
df.nunique(dropna = False)

# Describe Categoric Cols - Distinct Values
def distinct_val(cat_list):
    [print(col,"\n", data[col].unique(), "\n") for col in cat_list]
distinct_val(['YEAR', 'DISTRIBUTOR', 'GENRE'])

# Describe Categoric Cols - Distinct Values with Count
def freq(df, freq_list):
    freq_output = [
        pd.DataFrame({'dist': df[var].value_counts(dropna=False),
        '%': (df[var].value_counts(normalize=True, dropna=False)*100).round(1).astype(str) + ' %'
    }) for var in freq_list]
    
    return freq_output
        
freq(data, ["DISTRIBUTOR","MPAA RATING","GENRE"])

# ON_WHICH_COLUMNS.groupby(WHAT_TO_AGGREGATE).WHICH_AGGREGATION()
df[['on_col1', 'on_col2']].groupby(df['agg_col']).agg_function()
# Min, Max, Mean, Median, Count


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

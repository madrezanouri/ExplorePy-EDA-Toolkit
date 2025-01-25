#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
import seaborn as sns

def univariate_analysis(df, column):
    """
    Perform univariate analysis on a given column.
    
    Args:
        df (pd.DataFrame): Dataset.
        column (str): Column to analyze.
        
    Returns:
        None
    """
    print(f"Summary Statistics for {column}:")
    print(df[column].describe(include='all'))
    print("\n")

    if df[column].dtype in ['int64', 'float64']:  # Numerical data
        plt.figure(figsize=(14, 6))
        
        plt.subplot(1, 2, 1)
        sns.histplot(df[column], kde=True, color='blue', bins=30)
        plt.title(f"Histogram of {column}")
        
        plt.subplot(1, 2, 2)
        sns.boxplot(x=df[column], color='blue')
        plt.title(f"Boxplot of {column}")
        
        plt.show()
    
    elif df[column].dtype == 'object':  # Categorical data
        plt.figure(figsize=(8, 6))
        sns.countplot(y=df[column], palette='viridis', order=df[column].value_counts().index)
        plt.title(f"Frequency Count of {column}")
        plt.show()


# In[ ]:


# Numerical column
univariate_analysis(df, 'age')

# Categorical column
univariate_analysis(df, 'gender')


# In[ ]:


def bivariate_analysis(df, col1, col2):
    """
    Perform bivariate analysis between two columns.
    
    Args:
        df (pd.DataFrame): Dataset.
        col1 (str): First column.
        col2 (str): Second column.
        
    Returns:
        None
    """
    print(f"Analyzing Relationship Between {col1} and {col2}:")

    if df[col1].dtype in ['int64', 'float64'] and df[col2].dtype in ['int64', 'float64']:
        # Numerical vs Numerical
        corr = df[col1].corr(df[col2])
        print(f"Correlation Coefficient: {corr}")
        sns.scatterplot(x=df[col1], y=df[col2], alpha=0.7)
        plt.title(f"Scatter Plot: {col1} vs {col2}")
        plt.show()

    elif df[col1].dtype == 'object' and df[col2].dtype in ['int64', 'float64']:
        # Categorical vs Numerical
        sns.boxplot(x=df[col1], y=df[col2], palette='coolwarm')
        plt.title(f"Boxplot: {col1} vs {col2}")
        plt.show()
    
    elif df[col1].dtype == 'object' and df[col2].dtype == 'object':
        # Categorical vs Categorical
        crosstab = pd.crosstab(df[col1], df[col2])
        sns.heatmap(crosstab, annot=True, fmt='d', cmap='YlGnBu')
        plt.title(f"Heatmap: {col1} vs {col2}")
        plt.show()


# In[ ]:


# Numerical vs Numerical
bivariate_analysis(df, 'age', 'salary')

# Categorical vs Numerical
bivariate_analysis(df, 'department', 'salary')

# Categorical vs Categorical
bivariate_analysis(df, 'gender', 'department')


# In[ ]:


def multivariate_analysis(df, num_cols):
    """
    Perform multivariate analysis for numerical columns.
    
    Args:
        df (pd.DataFrame): Dataset.
        num_cols (list): List of numerical columns.
        
    Returns:
        None
    """
    # Correlation Heatmap
    corr_matrix = df[num_cols].corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Correlation Heatmap")
    plt.show()
    
    # Pairplot
    sns.pairplot(df[num_cols], diag_kind='kde', kind='reg', corner=True)
    plt.suptitle("Pair Plot", y=1.02)
    plt.show()


# In[ ]:


numerical_columns = ['age', 'salary', 'experience']
multivariate_analysis(df, numerical_columns)


# In[ ]:


from statsmodels.tsa.seasonal import seasonal_decompose

def time_series_analysis(df, time_col, value_col, freq='M'):
    """
    Perform time series decomposition.
    
    Args:
        df (pd.DataFrame): Dataset.
        time_col (str): Time column.
        value_col (str): Value column to analyze.
        freq (str): Frequency ('D', 'M', etc.).
        
    Returns:
        None
    """
    df[time_col] = pd.to_datetime(df[time_col])
    df = df.set_index(time_col)
    decomposition = seasonal_decompose(df[value_col], model='additive', period=12)
    decomposition.plot()
    plt.show()


# In[ ]:


time_series_analysis(df, 'date', 'sales')


# In[ ]:


def grouped_analysis(df, group_col, agg_col, agg_func='mean'):
    """
    Perform grouped analysis.
    
    Args:
        df (pd.DataFrame): Dataset.
        group_col (str): Column to group by.
        agg_col (str): Column to aggregate.
        agg_func (str): Aggregation function ('mean', 'sum', 'count', etc.).
        
    Returns:
        pd.DataFrame: Grouped summary.
    """
    grouped = df.groupby(group_col)[agg_col].agg(agg_func)
    print(grouped)
    grouped.plot(kind='bar', color='teal')
    plt.title(f"{agg_func.title()} of {agg_col} by {group_col}")
    plt.show()


# In[ ]:


grouped_analysis(df, 'department', 'salary', 'mean')


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
import seaborn as sns

def univariate_visualization(df, column):
    """
    Generate univariate visualizations for a column.
    
    Args:
        df (pd.DataFrame): Dataset.
        column (str): Column to visualize.
        
    Returns:
        None
    """
    if df[column].dtype in ['int64', 'float64']:
        # Numerical data
        plt.figure(figsize=(14, 6))
        
        plt.subplot(1, 2, 1)
        sns.histplot(df[column], kde=True, color='blue', bins=30)
        plt.title(f"Histogram of {column}")
        
        plt.subplot(1, 2, 2)
        sns.boxplot(x=df[column], color='blue')
        plt.title(f"Boxplot of {column}")
        
        plt.show()
    elif df[column].dtype == 'object':
        # Categorical data
        plt.figure(figsize=(10, 6))
        sns.countplot(y=df[column], palette='viridis', order=df[column].value_counts().index)
        plt.title(f"Bar Chart of {column}")
        plt.show()
        
        # Pie chart
        plt.figure(figsize=(8, 8))
        df[column].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, colors=sns.color_palette('pastel'))
        plt.title(f"Pie Chart of {column}")
        plt.ylabel("")  # Remove y-label for aesthetics
        plt.show()


# In[ ]:


# Numerical column
univariate_visualization(df, 'age')

# Categorical column
univariate_visualization(df, 'department')


# In[ ]:


def bivariate_visualization(df, col1, col2):
    """
    Generate bivariate visualizations for two columns.
    
    Args:
        df (pd.DataFrame): Dataset.
        col1 (str): First column.
        col2 (str): Second column.
        
    Returns:
        None
    """
    if df[col1].dtype in ['int64', 'float64'] and df[col2].dtype in ['int64', 'float64']:
        # Numerical vs Numerical
        plt.figure(figsize=(8, 6))
        sns.scatterplot(x=df[col1], y=df[col2], alpha=0.7, color='green')
        plt.title(f"Scatter Plot: {col1} vs {col2}")
        plt.show()
        
        # Linear Regression Plot
        sns.lmplot(x=col1, y=col2, data=df, line_kws={'color': 'red'})
        plt.title(f"Regression Plot: {col1} vs {col2}")
        plt.show()

    elif df[col1].dtype == 'object' and df[col2].dtype in ['int64', 'float64']:
        # Categorical vs Numerical
        plt.figure(figsize=(12, 6))
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
bivariate_visualization(df, 'age', 'salary')

# Categorical vs Numerical
bivariate_visualization(df, 'department', 'salary')

# Categorical vs Categorical
bivariate_visualization(df, 'gender', 'department')


# In[ ]:


def pair_plot(df, numerical_columns):
    """
    Generate a pair plot for numerical columns.
    
    Args:
        df (pd.DataFrame): Dataset.
        numerical_columns (list): List of numerical columns to include in the pair plot.
        
    Returns:
        None
    """
    sns.pairplot(df[numerical_columns], diag_kind='kde', kind='reg', corner=True)
    plt.suptitle("Pair Plot", y=1.02)
    plt.show()


# In[ ]:


pair_plot(df, ['age', 'salary', 'experience'])


# In[ ]:


def correlation_heatmap(df, numerical_columns):
    """
    Generate a correlation heatmap for numerical columns.
    
    Args:
        df (pd.DataFrame): Dataset.
        numerical_columns (list): List of numerical columns.
        
    Returns:
        None
    """
    plt.figure(figsize=(10, 8))
    corr_matrix = df[numerical_columns].corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
    plt.title("Correlation Heatmap")
    plt.show()


# In[ ]:


correlation_heatmap(df, ['age', 'salary', 'experience'])


# In[ ]:


def multi_variant_matrix(df, numerical_columns):
    """
    Generate a multi-variant matrix with KDE plots on the diagonal
    and regression scatter plots on the off-diagonal.
    
    Args:
        df (pd.DataFrame): Dataset.
        numerical_columns (list): List of numerical columns.
        
    Returns:
        None
    """
    sns.pairplot(df[numerical_columns], diag_kind="kde", kind="reg", corner=True)
    plt.suptitle("Multi-Variant Analysis Matrix", y=1.02)
    plt.show()


# In[ ]:


multi_variant_matrix(df, ['age', 'salary', 'experience'])


# In[ ]:


import plotly.express as px

def interactive_scatter_plot(df, x, y, color=None, size=None):
    """
    Generate an interactive scatter plot using Plotly.
    
    Args:
        df (pd.DataFrame): Dataset.
        x (str): X-axis variable.
        y (str): Y-axis variable.
        color (str): Column to color the points.
        size (str): Column to size the points.
        
    Returns:
        None
    """
    fig = px.scatter(df, x=x, y=y, color=color, size=size, title=f"{x} vs {y}")
    fig.show()


# In[ ]:


interactive_scatter_plot(df, x='age', y='salary', color='department', size='experience')


# In[ ]:


from pandas_profiling import ProfileReport

def generate_eda_report(df, report_name="eda_report.html"):
    """
    Generate an automated EDA report using pandas-profiling.
    
    Args:
        df (pd.DataFrame): Dataset.
        report_name (str): Name of the output HTML report.
        
    Returns:
        None
    """
    profile = ProfileReport(df, title="Exploratory Data Analysis Report", explorative=True)
    profile.to_file(report_name)


# In[ ]:


generate_eda_report(df, report_name="my_eda_report.html")


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def data_quality_report(df):
    """
    Generate a summary report of data quality issues.
    
    Args:
        df (pd.DataFrame): Dataset.
        
    Returns:
        pd.DataFrame: Summary of data quality issues.
    """
    report = pd.DataFrame({
        'Column': df.columns,
        'DataType': df.dtypes,
        'Non-Null Count': df.notnull().sum(),
        'Null Count': df.isnull().sum(),
        'Null Percentage': (df.isnull().sum() / len(df)) * 100,
        'Unique Values': df.nunique(),
        'Duplicate Rows': df.duplicated().sum()
    }).reset_index(drop=True)
    return report


# In[ ]:


report = data_quality_report(df)
print(report)


# In[ ]:


import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.impute import KNNImputer

def visualize_missing_data(df):
    """
    Visualize missing data using a heatmap.
    
    Args:
        df (pd.DataFrame): Dataset.
    """
    plt.figure(figsize=(12, 6))
    sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
    plt.title("Missing Data Heatmap")
    plt.show()

def handle_missing_values(df, strategy="mean", columns=None, knn_neighbors=5):
    """
    Handle missing values in the dataset.
    
    Args:
        df (pd.DataFrame): Dataset.
        strategy (str): Strategy for handling missing values ('mean', 'median', 'mode', 'drop', 'knn').
        columns (list): Specific columns to apply the strategy to. If None, applies to all columns.
        knn_neighbors (int): Number of neighbors for KNN imputation.
        
    Returns:
        pd.DataFrame: Dataset with missing values handled.
    """
    columns = columns if columns else df.columns
    
    if strategy == "drop":
        return df.dropna(subset=columns)
    
    for col in columns:
        if strategy == "mean":
            df[col].fillna(df[col].mean(), inplace=True)
        elif strategy == "median":
            df[col].fillna(df[col].median(), inplace=True)
        elif strategy == "mode":
            df[col].fillna(df[col].mode()[0], inplace=True)
        elif strategy == "knn":
            imputer = KNNImputer(n_neighbors=knn_neighbors)
            df[col] = imputer.fit_transform(df[[col]])
    
    return df


# In[ ]:


# Visualize missing data
visualize_missing_data(df)

# Handle missing values with mean imputation
df_cleaned = handle_missing_values(df, strategy="mean")

# Handle missing values using KNN
df_cleaned_knn = handle_missing_values(df, strategy="knn", knn_neighbors=3)


# In[ ]:


def remove_duplicates(df, subset=None):
    """
    Remove duplicate rows from the dataset.
    
    Args:
        df (pd.DataFrame): Dataset.
        subset (list): Columns to check for duplicates. If None, checks all columns.
        
    Returns:
        pd.DataFrame: Dataset without duplicates.
    """
    return df.drop_duplicates(subset=subset)


# In[ ]:


df_no_duplicates = remove_duplicates(df)


# In[ ]:


def detect_outliers_iqr(df, column):
    """
    Detect outliers using the IQR method.
    
    Args:
        df (pd.DataFrame): Dataset.
        column (str): Column to check for outliers.
        
    Returns:
        pd.DataFrame: Boolean mask where True indicates an outlier.
    """
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return (df[column] < lower_bound) | (df[column] > upper_bound)

def remove_outliers(df, column):
    """
    Remove outliers using the IQR method.
    
    Args:
        df (pd.DataFrame): Dataset.
        column (str): Column to check for outliers.
        
    Returns:
        pd.DataFrame: Dataset without outliers.
    """
    outliers = detect_outliers_iqr(df, column)
    return df[~outliers]


# In[ ]:


outliers_mask = detect_outliers_iqr(df, 'salary')
df_no_outliers = remove_outliers(df, 'salary')


# In[ ]:


def convert_dtypes(df):
    """
    Convert data types to optimize memory and ensure integrity.
    
    Args:
        df (pd.DataFrame): Dataset.
        
    Returns:
        pd.DataFrame: Dataset with optimized data types.
    """
    for col in df.select_dtypes(include=['object']).columns:
        try:
            df[col] = pd.to_datetime(df[col])
        except:
            pass
    for col in df.select_dtypes(include=['int', 'float']).columns:
        df[col] = pd.to_numeric(df[col], downcast='float')
    return df


# In[ ]:


df_cleaned = convert_dtypes(df)


# In[ ]:


def encode_categorical(df, columns, encoding_type="one_hot"):
    """
    Encode categorical columns.
    
    Args:
        df (pd.DataFrame): Dataset.
        columns (list): List of categorical columns to encode.
        encoding_type (str): Encoding type ('one_hot' or 'label').
        
    Returns:
        pd.DataFrame: Dataset with encoded columns.
    """
    if encoding_type == "one_hot":
        return pd.get_dummies(df, columns=columns, drop_first=True)
    elif encoding_type == "label":
        from sklearn.preprocessing import LabelEncoder
        le = LabelEncoder()
        for col in columns:
            df[col] = le.fit_transform(df[col])
    return df


# In[ ]:


df_encoded = encode_categorical(df, columns=['gender', 'department'], encoding_type='one_hot')


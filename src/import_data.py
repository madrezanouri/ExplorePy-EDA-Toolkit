#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

def import_local_file(file_path, file_type, **kwargs):
    """
    Import data from local files.
    
    Args:
        file_path (str): Path to the file.
        file_type (str): Type of the file ('csv', 'excel', 'json', 'parquet', etc.).
        **kwargs: Additional arguments for specific file readers.
        
    Returns:
        pd.DataFrame: Loaded dataset.
    """
    if file_type == 'csv':
        df = pd.read_csv(file_path, **kwargs)
    elif file_type == 'excel':
        df = pd.read_excel(file_path, **kwargs)
    elif file_type == 'json':
        df = pd.read_json(file_path, **kwargs)
    elif file_type == 'parquet':
        df = pd.read_parquet(file_path, **kwargs)
    else:
        raise ValueError(f"Unsupported file type: {file_type}")
    return df


# In[ ]:


# CSV
df_csv = import_local_file('data.csv', 'csv')

# Excel
df_excel = import_local_file('data.xlsx', 'excel')

# JSON
df_json = import_local_file('data.json', 'json')


# In[ ]:


import pandas as pd
import sqlite3

def import_from_sql(query, db_path):
    """
    Import data from an SQLite database.
    
    Args:
        query (str): SQL query to execute.
        db_path (str): Path to the SQLite database.
        
    Returns:
        pd.DataFrame: Resulting dataset.
    """
    conn = sqlite3.connect(db_path)
    df = pd.read_sql(query, conn)
    conn.close()
    return df


# In[ ]:


# SQL Query
query = "SELECT * FROM employees WHERE salary > 50000"
df_sql = import_from_sql(query, 'database.db')


# In[ ]:


import requests
import pandas as pd

def import_from_api(url, headers=None, params=None):
    """
    Import data from an API endpoint.
    
    Args:
        url (str): API endpoint URL.
        headers (dict): Headers for the API request.
        params (dict): Query parameters for the API request.
        
    Returns:
        pd.DataFrame: Data from the API as a DataFrame.
    """
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()  # Assuming the API returns JSON
        return pd.DataFrame(data)
    else:
        raise Exception(f"Failed to fetch data. Status code: {response.status_code}")


# In[ ]:


# Example API
api_url = "https://jsonplaceholder.typicode.com/posts"
df_api = import_from_api(api_url)


# In[ ]:


def import_large_csv(file_path, chunk_size=10000):
    """
    Import large CSV files in chunks.
    
    Args:
        file_path (str): Path to the CSV file.
        chunk_size (int): Number of rows per chunk.
        
    Returns:
        pd.DataFrame: Combined dataset after reading in chunks.
    """
    chunks = []
    for chunk in pd.read_csv(file_path, chunksize=chunk_size):
        chunks.append(chunk)
    return pd.concat(chunks, axis=0)


# In[ ]:


df_large = import_large_csv('large_file.csv', chunk_size=5000)


# In[ ]:


import boto3
import pandas as pd
from io import StringIO

def import_from_s3(bucket_name, file_key, aws_access_key, aws_secret_key):
    """
    Import data from an AWS S3 bucket.
    
    Args:
        bucket_name (str): Name of the S3 bucket.
        file_key (str): Key (path) to the file in the bucket.
        aws_access_key (str): AWS access key.
        aws_secret_key (str): AWS secret key.
        
    Returns:
        pd.DataFrame: Loaded dataset.
    """
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)
    obj = s3.get_object(Bucket=bucket_name, Key=file_key)
    data = obj['Body'].read().decode('utf-8')
    return pd.read_csv(StringIO(data))


# In[ ]:


df_s3 = import_from_s3(
    bucket_name='my-bucket',
    file_key='path/to/data.csv',
    aws_access_key='your-access-key',
    aws_secret_key='your-secret-key'
)


# In[ ]:


def data_summary(df):
    """
    Display basic information about the dataset.
    
    Args:
        df (pd.DataFrame): Dataset.
    """
    print("Shape of dataset:", df.shape)
    print("\nInfo:")
    print(df.info())
    print("\nSummary statistics:")
    print(df.describe(include='all'))


# In[ ]:


data_summary(df_csv)


# In[ ]:


def optimize_memory(df):
    """
    Reduce memory usage by optimizing data types.
    
    Args:
        df (pd.DataFrame): Dataset.
        
    Returns:
        pd.DataFrame: Optimized dataset.
    """
    for col in df.select_dtypes(include=['int', 'float']).columns:
        df[col] = pd.to_numeric(df[col], downcast='unsigned')
    return df


# In[ ]:


df_optimized = optimize_memory(df_csv)


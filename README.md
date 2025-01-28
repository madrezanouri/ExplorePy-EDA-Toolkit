# ExplorePy: An EDA Toolkit

<img width="640" alt="1696735515832" src="https://github.com/user-attachments/assets/9e6c335e-626a-48ef-83de-0346b9cccf7c" />

This end-to-end EDA toolkit provides a comprehensive set of tools and reusable code modules for importing, cleaning, analyzing, and visualizing data, enabling users to uncover valuable insights and make informed decisions efficiently.



# Introduction
**ExplorePy** is a comprehensive Python framework designed for Exploratory Data Analysis (EDA), which is the essential first step in any data science or machine learning project. The framework provides a step-by-step, modular, and reusable toolkit for importing, cleaning, analyzing, and visualizing datasets.


# The goal of ExplorePy is to:

. Simplify the EDA process for analysts and data scientists.

. Save time by automating routine EDA tasks.

. Provide advanced techniques and insights to make better data-driven decisions.

. Deliver professional visualizations and detailed summary reports.



# Key Features:

. Flexible data importing (from files, APIs, databases, etc.).

. Automated data cleaning and preprocessing.

. Comprehensive analysis methods: univariate, bivariate, and multivariate.

. Stunning visualizations using both static and interactive tools.

. Automated report generation for quick sharing of insights.


# Overview of Step 1

The data importing module supports:

**1. Local File Importing:**
   
Supports multiple formats: CSV, Excel, JSON, Parquet, etc.

```
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
```
```
# CSV
df_csv = import_local_file('data.csv', 'csv')

# Excel
df_excel = import_local_file('data.xlsx', 'excel')

# JSON
df_json = import_local_file('data.json', 'json')
  ```

 

**2. Database Integration:**
   
Import data directly from SQL databases using SQLite or SQLAlchemy.

```
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
```
```
# SQL Query
query = "SELECT * FROM employees WHERE salary > 50000"
df_sql = import_from_sql(query, 'database.db')
```
 

**3. API Data Importing:**
   
Fetch JSON data from APIs and convert it to a DataFrame.

```
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
```
```
# Example API
api_url = "https://jsonplaceholder.typicode.com/posts"
df_api = import_from_api(api_url)
```
 

**4. Cloud Data Handling:**
   
Load data from AWS S3 buckets or other cloud services.

```
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
```
```
df_s3 = import_from_s3(
    bucket_name='my-bucket',
    file_key='path/to/data.csv',
    aws_access_key='your-access-key',
    aws_secret_key='your-secret-key'
)
```
 

**5. Chunk Processing:**
   
Efficiently handle large datasets using chunk-based loading to avoid memory issues.

```
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
```
```
df_large = import_large_csv('large_file.csv', chunk_size=5000)
```
 



**6. Dataset Summary Function:**

This function displays three key aspects of the dataset:

1. Shape: The number of rows and columns in the dataset.
2. Info: The data types of each column, the number of non-null values, and memory usage.
3. Summary Statistics: Descriptive statistics for both numerical and categorical columns (e.g., mean, median, unique values).

   ```
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
```
data_summary(df_csv)
```

# Example Table: Output of data_summary()

**Dataset Shape**

Metric  | Value
------- | -------
Row     | 5
Columns | 4



**Dataset Info:**

Column Name  | Non-Null Count | Data Type
------------ | -------------  | ---------
Name         | 5              | object
Age          | 5              | int64
Department   | 5              | object
Salary       | 5              | int64



**Summary Statistics**

Metric     | Name | Age       |  Department | Salary
-------    | ---  |---------- | ----------- | ------
Count      | 5    | 5.000000  |    5        | 5.000000  
Unique     |   5  | 5         | int64       | NaN
Top        |Alice |    NaN    | Engineering | NaN
Frequency  |   1  | NaN       | 2           | NaN
Mean       | NaN  | 35.000000 |    NaN      | 68000.000000 
Std Dev    |  NaN | 7.905694  | NaN         | 11135.528725
Min        | NaN  | 25.000000 | NaN         |55000.000000
25%        |  NaN | 30.000000 | NaN         | 60000.000000
50%        |  NaN | 35.000000 | NaN         | 70000.000000
75%        | NaN  | 40.000000 | NaN         |  75000.000000
Max        |  NaN | 45.000000 | NaN         |  80000.000000


**7. Memory Optimization Function:**
1. Optimize Numerical Columns: Converts numerical columns (integers and floats) to more memory-efficient types, such as unsigned integers or smaller floating-point formats.

2.Improve Dataset Performance: Reduces the amount of memory required to store the dataset in RAM, making it easier to work with large datasets.

```
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
```
```
df_optimized = optimize_memory(df_csv)
```


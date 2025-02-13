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
2. Improve Dataset Performance: Reduces the amount of memory required to store the dataset in RAM, making it easier to work with large datasets.

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


# Step 2: Cleaning and Preprocessing the Data

After importing the dataset in Step 1, the next critical step in Exploratory Data Analysis (EDA) is data cleaning and preprocessing. This step ensures that the dataset is consistent, reliable, and ready for analysis by addressing common issues such as missing values, duplicates, outliers, and data type mismatches.

In ExplorePy, the cleaning and preprocessing module is designed to streamline this process by providing reusable, efficient, and flexible functions that can handle datasets of varying complexity.

**Overview of Step 2**
The data cleaning and preprocessing module includes:

**1. Data Quality Assessment:**
Generate a detailed data quality report to evaluate issues like missing values, null percentages, unique values, and duplicate rows.

```
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
```
```
report = data_quality_report(df)
print(report)
```

**2. Handling Missing Values:** 
Identifying and addressing missing values using multiple strategies like imputation, deletion, or advanced methods.

```
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
```
```
# Visualize missing data
visualize_missing_data(df)

# Handle missing values with mean imputation
df_cleaned = handle_missing_values(df, strategy="mean")

# Handle missing values using KNN
df_cleaned_knn = handle_missing_values(df, strategy="knn", knn_neighbors=3)
```

# Output Example:

![no missing values](https://github.com/user-attachments/assets/c15201dd-95f2-4a3b-959c-c479e859fa03)

**Fig1: Data sample with no missing valuse**


![missing valus](https://github.com/user-attachments/assets/80e935fe-788e-443b-8195-44196196d23f)

**Fig2: Data sample with missing values**



**3. Removing Duplicates:**
Identifying and removing duplicate rows to ensure data integrity.

```
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
```
```
df_no_duplicates = remove_duplicates(df)
```

**4. Outlier Detection and Handling:** 
Identifying outliers using statistical methods like the Interquartile Range (IQR) and addressing them appropriately.

```
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
```
```
outliers_mask = detect_outliers_iqr(df, 'salary')
df_no_outliers = remove_outliers(df, 'salary')
```

**5. Datatype Validation and Optimization:**
Ensuring the data types are correct and optimizing them for efficiency (as demonstrated in the optimize_memory function).

```
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
```
```
df_cleaned = convert_dtypes(df)
```

**6. Categorical Encoding:**
Converting categorical data into numerical formats for easier analysis and modeling.

```
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
```
```
df_encoded = encode_categorical(df, columns=['gender', 'department'], encoding_type='one_hot')
```

# Step 3: Analyzing the Data

With the dataset cleaned and preprocessed in Step 2, the next step is to dive into data analysis. This step involves exploring the data to uncover patterns, trends, and relationships between variables. By performing univariate, bivariate, and multivariate analyses, we can gain valuable insights that set the stage for modeling and decision-making.

**The data analysis module in ExplorePy includes:**

**Univariate Analysis:** 
Focuses on summarizing and visualizing individual variables to understand their distributions.

```
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
```
```
# Numerical column
univariate_analysis(df, 'age')

# Categorical column
univariate_analysis(df, 'gender')
```

# Univariate Analysis Output Example:

![Histogram Boxplot](https://github.com/user-attachments/assets/8d3c9c48-834e-420d-8480-4d2b06ee8869)

**Fig3: Histogram and Boxplot**


**Bivariate Analysis:** 
Examines relationships between two variables, such as correlations and comparisons.

![scatter plot](https://github.com/user-attachments/assets/856e2566-876f-45e0-a505-ac84deb66962)

**Fig4: Scatter Plot**


**Multivariate Analysis:** 
Explores relationships across multiple variables to understand higher-dimensional interactions.

![Correlation Heatmap](https://github.com/user-attachments/assets/3956d845-448f-4170-afdb-ec35c72715fd)

**Fig5: Correlation Heatmap**

![Pair Plot](https://github.com/user-attachments/assets/aeeda9da-0021-4e21-923d-f48d3e31e7ce)

![pairwise_scatter_plots](https://github.com/user-attachments/assets/3d4809d6-1b66-448b-9fdd-3d79388e1aae)


**Fig6: Pair Plots**

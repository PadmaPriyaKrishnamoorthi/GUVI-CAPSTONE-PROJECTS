import pandas as pd
stores_df = pd.read_csv("C:\Users\Vishwa\Desktop\GUVI captone\DATASPARK\DS\Stores.csv")
stores_df
stores_df.dtypes
stores_df['Open Date'] = pd.to_datetime(stores_df['Open Date'])
stores_df.isnull().sum()
stores_df['Square Meters'] = stores_df['Square Meters'].fillna(0)
stores_df.isnull().sum()
stores_df.to_csv('C:\Users\Vishwa\Desktop\GUVI captone\DATASPARK\DS\Cleaned_Stores.csv', index=False)
import pandas as pd
Cleaned_Stores=pd.read_csv('C:\Users\Vishwa\Desktop\GUVI captone\DATASPARK\DS\Cleaned_Stores.csv')
Cleaned_Stores
Products_df=pd.read_csv("C:\Users\Vishwa\Desktop\GUVI captone\DATASPARK\DS\Products.csv")
Products_df
Products_df.isnull().sum()
Products_df.dtypes
Products_df['Unit Cost USD'] = Products_df['Unit Cost USD'].astype(str)
Products_df['Unit Price USD'] = Products_df['Unit Price USD'].astype(str)

Products_df['Unit Cost USD'] = Products_df['Unit Cost USD'].str.replace('[\$,]', '', regex=True).astype(float)
Products_df['Unit Price USD'] = Products_df['Unit Price USD'].str.replace('[\$,]', '', regex=True).astype(float)
Products_df
Products_df.to_csv('C:\Users\Vishwa\Desktop\GUVI captone\DATASPARK\DS\Cleaned_Products.csv', index=False)
Cleaned_Products=pd.read_csv('C:\Users\Vishwa\Desktop\GUVI captone\DATASPARK\DS\Cleaned_Products.csv')
Cleaned_Products
import pandas as pd
Sales_df=pd.read_csv("C:\Users\Vishwa\Desktop\GUVI captone\DATASPARK\DS\Sales.csv")
Sales_df
Sales_df.isnull().sum()
Sales_df = Sales_df.drop(columns=['Delivery Date'])
Sales_df.dtypes

Sales_df['Order Date'] = pd.to_datetime(Sales_df['Order Date'])
Sales_df.to_csv('C:\Users\Vishwa\Desktop\GUVI captone\DATASPARK\DS\Cleaned_Sales.csv', index=False)
Cleaned_Sales=pd.read_csv('C:\Users\Vishwa\Desktop\GUVI captone\DATASPARK\DS\Cleaned_Sales.csv')
Cleaned_Sales
Exchange_Rates_df=pd.read_csv("C:\Users\Vishwa\Desktop\GUVI captone\DATASPARK\DS\Exchange_Rates.csv")
Exchange_Rates_df
Exchange_Rates_df.isnull().sum()
Exchange_Rates_df.dtypes
Exchange_Rates_df['Date'] = pd.to_datetime(Exchange_Rates_df['Date'])
Exchange_Rates_df.dtypes
Exchange_Rates_df.to_csv('C:\Users\Vishwa\Desktop\GUVI captone\DATASPARK\DS\Cleaned_Exchange_Rates.csv', index=False)
Cleaned_Exchange_Rates=pd.read_csv('C:\Users\Vishwa\Desktop\GUVI captone\DATASPARK\DS\Cleaned_Exchange_Rates.csv')
Cleaned_Exchange_Rates
Customers_df = pd.read_csv("C:\Users\Vishwa\Desktop\GUVI captone\DATASPARK\DS\Customers.csv")
Customers_df
Customers_df.isnull().sum()
Customers_df['State Code'] = Customers_df['State Code'].fillna('Unknown')
Customers_df.dtypes
Customers_df.rename(columns={'Birthday ': 'Birthday'}, inplace=True)

# Now convert 'Birthday' column to datetime
Customers_df['Birthday'] = pd.to_datetime(Customers_df['Birthday'])
Customers_df.rename(columns={'Zip Code ': 'Zip Code'}, inplace=True)

# Now convert 'Zip Code' column to numeric
Customers_df['Zip Code'] = pd.to_numeric(Customers_df['Zip Code'], errors='coerce')
Customers_df.loc[:, 'Zip Code'] = pd.to_numeric(Customers_df['Zip Code']).astype('Int64')
Customers_df.to_csv('C:\Users\Vishwa\Desktop\GUVI captone\DATASPARK\DS\Cleaned_Customers.csv', index=False)
Cleaned_Customers=pd.read_csv('C:\Users\Vishwa\Desktop\GUVI captone\DATASPARK\DS\Cleaned_Customers.csv')
Cleaned_Customers


import pandas as pd
import pymysql

# Define database connection details
user = 'root'
password = '1111'
host = 'localhost'
database = 'Dataspark'

# Connect to the database
connection = pymysql.connect(
    host=host,
    user=user,
    password=password,
    database=database
)
cursor = connection.cursor()

# Load and rename columns in each dataset
datasets = {
    'Cleaned_Stores': '"C:\Users\Vishwa\Desktop\GUVI captone\DATASPARK\DS\Cleaned_Stores_Renamed.csv',
    'Cleaned_Products': 'C:\Users\Vishwa\Desktop\GUVI captone\DATASPARK\DS\Cleaned_Products.csv',
    'Cleaned_Sales': 'C:\Users\Vishwa\Desktop\GUVI captone\DATASPARK\DS\Cleaned_Sales.csv',
    'Cleaned_Exchange_Rates': 'C:\Users\Vishwa\Desktop\GUVI captone\DATASPARK\DS\Cleaned_Exchange_Rates.csv',
    'Cleaned_Customers': 'C:\Users\Vishwa\Desktop\GUVI captone\DATASPARK\DS\Cleaned_Customers.csv'
}

# Define table creation queries
table_creation_queries = {
    'Cleaned_Stores': """
        CREATE TABLE IF NOT EXISTS Cleaned_Stores (
            StoreKey INT,
            Country VARCHAR(255),
            State VARCHAR(255),
            SquareMeters DECIMAL(10, 2),
                        OpenDate DATE
        )
    """,
    'Cleaned_Products': """
        CREATE TABLE IF NOT EXISTS Cleaned_Products (
            ProductKey INT,
            ProductName VARCHAR(255),
            Brand VARCHAR(255),
            Color VARCHAR(255),
            UnitCostUSD DECIMAL(10, 2),
            UnitPriceUSD DECIMAL(10, 2),
            SubcategoryKey INT,
            Subcategory VARCHAR(255),
            CategoryKey INT,
            Category VARCHAR(255)
        )
    """,
    'Cleaned_Sales': """
        CREATE TABLE IF NOT EXISTS Cleaned_Sales (
            OrderNumber INT,
            LineItem INT,
            OrderDate DATE,
            CustomerKey INT,
            StoreKey INT,
            ProductKey INT,
            Quantity INT,
            CurrencyCode VARCHAR(10)
        )
    """,
    'Cleaned_Exchange_Rates': """
        CREATE TABLE IF NOT EXISTS Cleaned_Exchange_Rates (
            Date DATE,
            Currency VARCHAR(255),
            Exchange DECIMAL(10, 4)
               )
    """,
    'Cleaned_Customers': """
        CREATE TABLE IF NOT EXISTS Cleaned_Customers (
            CustomerKey INT,
            Gender VARCHAR(10),
            Name VARCHAR(255),
            City VARCHAR(255),
            StateCode VARCHAR(10),
            State VARCHAR(255),
            ZipCode VARCHAR(20),
            Country VARCHAR(255),
            Continent VARCHAR(255),
            Birthday DATE
        )
    """
}

# Define insert queries
insert_queries = {
    'Cleaned_Stores': """
        INSERT INTO Cleaned_Stores (StoreKey, Country, State, SquareMeters, OpenDate)
        VALUES (%s, %s, %s, %s, %s)
    """,
    'Cleaned_Products': """
        INSERT INTO Cleaned_Products (ProductKey, ProductName, Brand, Color, UnitCostUSD, UnitPriceUSD, SubcategoryKey, Subcategory, CategoryKey, Category)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """,
    'Cleaned_Sales': """
        INSERT INTO Cleaned_Sales (OrderNumber, LineItem, OrderDate, CustomerKey, StoreKey, ProductKey, Quantity, CurrencyCode)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """,
    'Cleaned_Exchange_Rates': """
        INSERT INTO Cleaned_Exchange_Rates (Date, Currency, Exchange)
        VALUES (%s, %s, %s)
    """,
    'Cleaned_Customers': """
        INSERT INTO Cleaned_Customers (CustomerKey, Gender, Name, City, StateCode, State, ZipCode, Country, Continent, Birthday)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
}

# Insert data into the database
for table_name, file_path in datasets.items():
    print(f"Inserting data into table {table_name}:")
    
    # Load and rename columns if needed
    df = pd.read_csv(file_path)
    
    # Clean up column names if needed (e.g., removing spaces)
    df.columns = df.columns.str.strip().str.replace(' ', '_')
    
    # Create table
    cursor.execute(table_creation_queries[table_name])
    
    # Insert data
    insert_query = insert_queries[table_name]
    for _, row in df.iterrows():
        try:
            cursor.execute(insert_query, tuple(row))
        except pymysql.MySQLError as e:
            print(f"Error inserting data: {e}")
            print(f"Query: {insert_query}")
            print(f"Values: {tuple(row)}")

# Commit the transaction and close the connection
connection.commit()
cursor.close()
connection.close()

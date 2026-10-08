# Pandas - Pandas is a python library used for working with structured data.
# Pandas works on a data that looks like a table
# Eg: CSV files, Excel Files, Datbases, Data analysis project
# Syntax pandas as pd
# import pandas as pd
# # Pandas series - 1D labeled data structure 
# marks=pd.Series([80,90,70,75])
# print(marks)
# # print(marks.iloc[1])

# import pandas as pd
# marks=pd.Series(
#     [80,90,70],
#     index=['Apple','Banana','Carrot']
# )
# print(marks.iloc['Banana'])

# import pandas as pd
# marks=pd.Series([80,90,70])
# print(marks+5)
# print(marks*2)
# print(marks-10)

# DataFrame - 2D labeled data structure
# Series - One column
# DATFrame - 

# import pandas as pd
# data={
#     'Name': ['A','B','C'],
#     'Age': 23,
#     'Marks': [20,56,78]

# }
# df=pd.DataFrame(data)
# print(df)
# print(df[['Name','Marks']])
# print(df.iloc[0])
# print(df.loc[1,'Marks']) # It gives the marks of the index 1 
# print(df.shape)


# Reading CSV values
# Name,Age,Marks
# A,21,85
# B,23,99
# C,20,85

# import pandas as pd
# df=pd.read_csv('annual.csv')
# print(df.head(10)) # It prints first specified no of rows
# print(df.tail(10)) # It prints last specified no of rows
# print(df.info)  # Gives the basic info about the csv file
# print(df.describe) 

# Data Cleaning Basics
# Find the Missing Values
import pandas as pd
df=pd.read_csv('annual.csv')
# print(df.isnull()) # It checks whether 
# print(df.isnull().sum())

# Removing Missing Rows
# import pandas as pd
# df=pd.read_csv('annual.csv')
# df=df.dropna() # It removes the entire row which have missing values

# # Filling Missing Values
# import pandas as pd
# df=pd.read_csv('annual.csv')
# df['year']=df['year'].fillna(2026)
# # df['height']=df['height'].fillin(df['height'].mean()) # We can handle a specific missing values by using this method, here we are filling the missing values with mean data.


# # Duplicate Data
# import pandas as pd
# df=pd.read_csv('annual.csv')
# print(df.duplicated()) # Finding the duplicates syntax

# # Remove Duplicates
# import pandas as pd
# df=pd.read_csv('annual.csv')
# df=df.drop_duplicates()

# # Changing Columns Names
# import pandas as pd
# df=pd.read_csv('annual.csv')
# df=df.rename(columns={'industry_code_ANZSIC': 'ANZ'})
# print(df.head())

# Filter the data 
import pandas as pd
df=pd.read_csv('annual.csv')
result=df[df['year']>2011]
print(result)




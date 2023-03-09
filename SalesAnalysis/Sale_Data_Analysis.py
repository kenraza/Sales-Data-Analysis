#import libraries 
import pandas as pd 
import os 

#TASK 1: Merge 12 months of sale data into single csv file 
df = pd.read_csv('./Sales_Data/Sales_April_2019.csv')

files = [file for file in os.listdir('./Sales_Data')]

all_months_data = pd.DataFrame()

for file in files:
    df = pd.read_csv('./Sales_Data/'+file)
    all_months_data = pd.concat([all_months_data, df])
    
all_months_data.to_csv('all_month.csv', index = False)


    
     #read in updated dataframe

all_month = pd.read_csv("all_month.csv")
print(all_month.head())



#Cleam up the data!
     #find rows with NaN Data 
nan_df = all_month[all_month.isna().any(axis=1)]
print(nan_df.head(5))
     
     #Drop rows of Nan
all_month = all_month.dropna(how='all')
print(all_month.head(5))

    #Find "Or" and delet it 
all_month = all_month[all_month['Order Date'].str[0:2] != 'Or']
    
    
    #Convert Columns to the correct type 
all_month['Quantity Ordered'] = pd.to_numeric(all_month['Quantity Ordered'])  # Make int 
all_month['Price Each'] = pd.to_numeric(all_month['Price Each'])# Make Float

#Augment data with additional columns 

#TASK 2: Add Month Column
all_month['Month'] = all_month['Order Date'].str[0:2]
all_month['Month'] = all_month['Month'].astype('int32')
print(all_month.head(5))

#TASK 3: Add a sales column
all_month['Sales'] = all_month['Quantity Ordered']*all_month['Price Each']
print(all_month.head(5))


#Question 1: What was the best month for sale? How much was earned that month?



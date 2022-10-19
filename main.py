import pandas as pn
import numpy as np
import matplotlib.pyplot as plt

data = pn.read_csv('finance_liquor_sales 2016-2019.csv')
data2 = pn.DataFrame(data)

data2['zip_code'] = data2['zip_code'].astype(int)
data3 = data2[["zip_code", "item_description", "bottles_sold"]]

#find the most popular item by zip code
print("Most popular item by zip code")
data4 = data3.sort_values(['zip_code','bottles_sold'], ascending=[True,False]).groupby(['zip_code']).head(100)
print(data4.to_string(index=False))
#save the new csv file for solution 1
data4.to_csv('solution_1.csv',index=False)

#find percentage per store
print("Sales percentage per store")
data5 = data2[['store_number', 'sale_dollars']]
data6 = data5.sort_values(['store_number'], ascending=True).groupby(['store_number']).head(100)
total_sales = data6['sale_dollars'].sum()
data6['percentage'] = (data6.sale_dollars/total_sales)*100
print(data6.to_string(index=False))

#save the new csv file for solution 2 a
data6.to_csv('solution_2.csv', index=False)











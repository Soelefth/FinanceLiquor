import matplotlib.pyplot as plt
import numpy as np
import pandas as pn

#plot for percentage of sales per store

data = pn.read_csv('solution_2.csv')
data2 = pn.DataFrame(data)
print(data2.to_string())

colors = np.random.randint(100,size=(74))

plt.scatter(data2['store_number'], data2['percentage'], c = colors)
plt.xlabel("Store Number")
plt.ylabel("Percentage %")
plt.title("Percentage of Sales per Store")
plt.show()
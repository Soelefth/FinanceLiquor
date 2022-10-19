import matplotlib.pyplot as plt
import numpy as np
import pandas as pn

#plot for most popular item per zip code

data = pn.read_csv('solution_1.csv')
data2 = pn.DataFrame(data)
#print(data2.to_string())

colors = np.random.randint(100,size=(74))

plt.scatter(data2['zip_code'], data2['bottles_sold'], c = colors, alpha = 0.5, cmap = 'nipy_spectral')
plt.xlabel("Zip Codes")
plt.ylabel("Bottles Sold")
plt.title("Most Popular Item per Zip Code")
plt.show()
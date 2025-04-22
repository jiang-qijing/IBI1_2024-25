import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir('/Users/jiangqijing/Desktop/IBI               IBMS8011 Introduction to Biomedical Informatics/Practical/IBI1_2024-25/Practical10')
dalys_data=pd.read_csv('dalys-rate-from-all-causes.csv')
print(dalys_data.iloc[0:10,2])
print(dalys_data.loc[dalys_data['Year']==1990,'DALYs'])

uk=dalys_data.loc[dalys_data.Entity=='United Kingdom',['DALYs','Year']]
fr=dalys_data.loc[dalys_data.Entity=='France',['DALYs','Year']]
uk_mean=uk.mean()
fr_mean=fr.mean()
print('UK mean DALYs:',uk_mean)
print('France mean DALYs:',fr_mean)
#The mean DALYs in the UK was greater than France.

plt.plot(uk.Year,uk.DALYs,'b+')
plt.xticks(uk.Year,rotation=-90)
plt.title('DALYs Over Time in the UK')
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.show()

data_1990=dalys_data.loc[dalys_data['Year']==1990,'DALYs']
plt.boxplot(data_1990)
plt.title("Boxplot of DALYs Across Countries in 1990")
plt.ylabel("DALYs")
plt.show()

#Define a list named 'uk_countries' containing the population sizes of UK countries
#Define a list named 'zhejiang_neighbouring_provinces' containing the population sizes of provinces neighboring Zhejiang
#Sort the 'uk_countries' list and print the sorted list
#Sort the 'zhejiang_neighbouring_provinces' list and print the sorted list
#Import the 'matplotlib.pyplot' library to create visualizations
#Create a pie chart for the UK countries
#Set the title of the first pie chart
#Ensure the pie chart is circular by setting the axis to 'equal'
#Display the first pie chart
#Create a pie chart for the provinces neighboring Zhejiang
#Set the title of the second pie chart
#Ensure the pie chart is circular by setting the axis to 'equal'
#Display the second pie chart

uk_countries=[57.11,3.13,1.91,5.45]#Define a list named 'uk_countries' containing the population sizes of UK countries
zhejiang_neighbouring_provinces=[65.77,41.88,45.28,61.27,85.15]#Define a list named 'zhejiang_neighbouring_provinces' containing the population sizes of provinces neighboring Zhejiang
print(sorted(uk_countries))#Sort the 'uk_countries' list and print the sorted list
print(sorted(zhejiang_neighbouring_provinces))#Sort the 'zhejiang_neighbouring_provinces' list and print the sorted list
import matplotlib.pyplot as plt#Import the 'matplotlib.pyplot' library to create visualizations
plt.pie(uk_countries,labels=['England','Wales','Northern Ireland','Scotland'],autopct='%1.1f%%')#Create a pie chart for the UK countries
plt.title('Population Sizes in the UK')#Set the title of the first pie chart
plt.axis('equal')#Ensure the pie chart is circular by setting the axis to 'equal'
plt.show()#Display the first pie chart
plt.pie(zhejiang_neighbouring_provinces,labels=['Zhejiang','Fujian','Jiangxi','Anhui','Jiangsu'],autopct='%1.1f%%')#Create a pie chart for the provinces neighboring Zhejiang
plt.title('Population Sizes in provinces neighbouring Zhejiang')#Set the title of the second pie chart
plt.axis('equal')#Ensure the pie chart is circular by setting the axis to 'equal'
plt.show()#Display the second pie chart

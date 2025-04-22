#Define a dictionary named 'popularity' to store the popularity percentages of programming languages
#Print the dictionary to display the popularity percentages of the programming languages
#Import the 'matplotlib.pyplot' library to create visualizations
#Extract the keys from the 'popularity' dictionary and store them in a list named 'languages‘
#Extract the values from the 'popularity' dictionary and store them in a list named 'percentages‘
#Create a bar chart using the 'languages' list as the x-axis labels and the 'percentages' list as the y
#Set the label for the x-axis to 'languages'
#Set the title of the bar chart to 'Programming language popularity'
#Set the label for the y-axis to 'percentages'
#Display the bar chart
#Print the popularity percentage of 'JavaScript' by accessing its value in the 'popularity' dictionary

popularity={"JavaScript":62.3,"HTML":52.9,"Python":51,"SQL":51,"TypeScript":38.5}#Define a dictionary named 'popularity' to store the popularity percentages of programming languages
print(popularity)#Print the dictionary to display the popularity percentages of the programming languages
import matplotlib.pyplot as plt#Import the 'matplotlib.pyplot' library to create visualizations
languages = list(popularity.keys())#Extract the keys from the 'popularity' dictionary and store them in a list named 'languages‘
percentages = list(popularity.values())#Extract the values from the 'popularity' dictionary and store them in a list named 'percentages‘
plt.bar(languages, percentages)#Create a bar chart using the 'languages' list as the x-axis labels and the 'percentages' list as the y
plt.title('Programming language popularity')#Set the title of the bar chart to 'Programming language popularity'
plt.xlabel('languages')#Set the label for the x-axis to 'languages'
plt.ylabel('percentages')#Set the label for the y-axis to 'percentages'
plt.show()#Display the bar chart
javascript_popularity=popularity["JavaScript"]#Define the popularity percentage of 'JavaScript'
print(javascript_popularity)#Print the popularity percentage of 'JavaScript' by accessing its value in the 'popularity' dictionary

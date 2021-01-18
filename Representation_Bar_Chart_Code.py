#Code to create a directory and call the uploaded csv file
#Uses the data from the Species name and Over_Underrep value - Sheet1.csv, in the data section of our github
!mkdir data
!mkdir data/representation
data_path="./data/representation/Species name and Over_Underrep value - Sheet1.csv"
data = pd.read_csv(data_path)
data.head(5)

import matplotlib.pyplot as plt

#Naming the data from the relevant columns
Species_Name = data['Common Name'][0:84]
Representation = data['Difference (observed y - expected y)'][0:84]

plt.figure(figsize=(25,10))
#This loop is written to add the correct colour for each bar into the list of colours (c), without having to manually write out each colour in order
c = []
for item in Representation:
  if item <= 0:
    c.append('red')
    a.append(item)
  else:
    c.append('purple')
    b.append(item)
plt.bar(Species_Name, Representation, color=c, width = 0.8)
plt.title('Representation of Species', fontsize=14)
plt.xlabel('Species Name', fontsize=12)
plt.ylabel('Representation', fontsize=12)
#This sets the x axis labels to have the species names
plt.xticks(Species_Name, rotation=90)
plt.subplots_adjust(bottom=0.4, top=0.99)
plt.grid(True)
plt.show()

#Sources
#https://datatofish.com/bar-chart-python-matplotlib/ - Showed me how to use dataframes to make a bar chart and edit the colours
#https://www.pythonpool.com/matplotlib-figsize/ - Showed me how to edit figure size and set and rotate the x axis labels

!mkdir data
!mkdir data/representation

data_path="./data/representation/Species name and Over_Underrep value - Sheet1.csv"
data = pd.read_csv(data_path)
data.head(5)

#Uses the data from the Species name and Over_Underrep value - Sheet1.csv, in the data section of our github


import matplotlib.pyplot as plt
   
Species_Name = data['Common Name'][0:84]
Representation = data['Difference (observed y - expected y)'][0:84]

#a = []
#b = []
#c = []
plt.figure(figsize=(25,10))
for item in Representation:
  if item <= 0:
    c.append('red')
    a.append(item)
  else:
    c.append('purple')
    b.append(item)
#This loop is written to add the correct colour for each bar into the list of colours, without having to manually write out each colour in order
plt.bar(Species_Name, Representation, color=c, width = 0.8)
plt.title('Representation of Species', fontsize=14)
plt.xlabel('Species Name', fontsize=12)
plt.ylabel('Representation', fontsize=12)
plt.xticks(Species_Name, rotation=90)
plt.subplots_adjust(bottom=0.4, top=0.99)
plt.grid(True)
plt.show()
#print(a)
#print(b)
#print(c)

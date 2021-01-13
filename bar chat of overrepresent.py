import pandas as pd
import matplotlib.patches as mpatches
from matplotlib import pyplot as plt
data =  pd.read_excel('C:/Users\hp\Desktop\Life Span Variable Cleaned.xls')
data['Academic Articles per species']=data['Academic Articles per species']/10
data['indicator']=data['Overall Welfare']>data['Academic Articles per species']
data['color']='green'
data.loc[data.indicator==True,'color']='orange'
import numpy as np
from matplotlib import pyplot as plt
sp=np.arange(0,85)
welfare=np.array(data['Overall Welfare'])
color=np.array(data['color'])
popularity=np.array(data['Academic Articles per species'])
width = 0.4
fig,ax = plt.subplots()
ax.bar(sp,welfare,width,color=color)
ax.bar(sp+width,popularity,width,color=color)
plt.title('Welfare vs Popularity')
labels=['overrepresented','underrepresented']
color=['orange','green']
patches = [ mpatches.Patch(color=color[i], label="{:s}".format(labels[i]) ) for i in range(len(color)) ]
plt.legend(handles=patches)
plt.show()

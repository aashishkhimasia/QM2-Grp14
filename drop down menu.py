import tkinter as tk
from tkinter import ttk
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

data =  pd.read_excel('C:/Users\hp\Desktop\Life Span Variable Cleaned.xls')
data['article']=data['Academic Articles per species']/10
classtype=data['Class']
classtype.drop_duplicates(inplace=True)
classt=list(classtype.values)

species=data['Genus species']
species.drop_duplicates(inplace=True)
speciest=list(species.values)

def go(*arg):
   # clear_output()
    dt=data[data['Class']==comboxlist.get()]
    name=comboxlist.get()
    species=np.array(dt['Genus species'])
    article=dt['article']
    welfare=dt['Overall Welfare']
    ax=plt.subplot()
    lent=np.arange(len(article))
    width=0.5
    a=0.25
    ax.bar(lent-a,article,width=width,color='green')
    ax.bar(lent+a,welfare,width=width,color='orange')
    plt.xlabel('Genus species')
    plt.xticks(lent,species,rotation=60,fontsize=6)
    plt.title(name)
    plt.show()

def going(*arg):
   # clear_output()
    dt=data[data['Genus species']==comboxlist.get()]
    name=comboxlist.get()
    species=np.array(dt['Genus species'])
    article=dt['article']
    welfare=dt['Overall Welfare']
    ax=plt.subplot()
    lent=np.arange(len(article))
    width=0.4
    a=0.4/2
    ax.bar(lent-a,article,width=width,color='green')
    ax.bar(lent+a,welfare,width=width,color='orange')
    plt.xlabel('Genus species')
    plt.title(name)
    plt.show()


# By Class
#win=tk.Tk()
#comvalue=tk.StringVar()
#comboxlist=ttk.Combobox(win,textvariable=comvalue)
#comboxlist["values"]=classt
#comboxlist.current()
#comboxlist.bind("<<ComboboxSelected>>",go)
#comboxlist.pack()

win.mainloop()

# By Species
win=tk.Tk()
comvalue=tk.StringVar()
comboxlist=ttk.Combobox(win,textvariable=comvalue)
comboxlist["values"]=speciest
comboxlist.current()
comboxlist.bind("<<ComboboxSelected>>",going)
comboxlist.pack()

win.mainloop()

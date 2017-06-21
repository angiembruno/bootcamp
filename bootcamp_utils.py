import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#set up jb's preferred style
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728',
          '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
          '#bcbd22', '#17becf']
sns.set(style='whitegrid', palette=colors,
        rc={'axes.labelsize': 20, 'axes.titlesize': 20})


#load in data
xa_low = np.loadtxt('data/xa_low_food.csv', comments='#')
xa_high = np.loadtxt('data/xa_high_food.csv', comments='#')

#format data
x = np.sort(xa_low)
y = np.arange (1, len(xa_low)+1 / len(xa_low))

xh = np.sort(xa_high)
yh = np.arange (1, len(xa_high)+1 / len(xa_high))


#paint data
fig, ax = plt.subplots(1,1, figsize=(10,3))
ax.set_title('Awesome plot')
_ = ax.plot(x, y, marker='o', markersize=10, linestyle='none')
_ = ax.plot(xh,yh, marker='o', markersize=10, linestyle='none')
plt.show()

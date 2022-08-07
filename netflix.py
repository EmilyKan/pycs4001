import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 資料來源: https://www.kaggle.com/datasets/victorsoeiro/netflix-tv-shows-and-movies?select=credits.csv
df = pd.read_csv("./netflix_titles.csv")


df.head(10)

df.info()
x=df.groupby(['type'])['type'].count()
y=len(df)
r=((x/y)).round(2)

mt_ratio = pd.DataFrame(r).T
fig, ax = plt.subplots(1,1,figsize=(4, 1.5))
#Axes.barh()函數用於製作水平條形圖
ax.barh(mt_ratio.index, mt_ratio['Movie'], 
        color='#07b29e')
ax.barh(mt_ratio.index, mt_ratio['TV Show'], left=mt_ratio['Movie'], 
        color='#eb923f')



# movie percentage
for i in mt_ratio.index:
    ax.annotate(f"{int(mt_ratio['Movie'][i]*100)}%", 
                   xy=(mt_ratio['Movie'][i]/2, i),
                   va = 'center', ha='center',fontsize=25, fontweight='light', fontfamily='serif',
                   color='white')

    ax.annotate("Movie", 
                   xy=(mt_ratio['Movie'][i]/2, -0.25),
                   va = 'center', ha='center',fontsize=10, fontweight='light', fontfamily='serif',
                   color='white')
    
    
for i in mt_ratio.index:
    ax.annotate(f"{int(mt_ratio['TV Show'][i]*100)}%", 
                   xy=(mt_ratio['Movie'][i]+mt_ratio['TV Show'][i]/2, i),
                   va = 'center', ha='center',fontsize=25, fontweight='light', fontfamily='serif',
                   color='white')
    ax.annotate("TV Show", 
                   xy=(mt_ratio['Movie'][i]+mt_ratio['TV Show'][i]/2, -0.25),
                   va = 'center', ha='center',fontsize=10, fontweight='light', fontfamily='serif',
                   color='white')






# Title & Subtitle
fig.text(0.125,1.03,'Movie & TV Show distribution', fontfamily='serif',fontsize=10, fontweight='bold')
fig.text(0.125,0.92,'We see vastly more movies than TV shows on Netflix.',fontfamily='serif',fontsize=8)  

    

ax.legend().set_visible(False)





df['count'] = 1

df['first_country'] = df['country'].apply(lambda x: x.split(",")[0])
df['first_country'].head()





data = df.groupby('first_country')['count'].sum().sort_values(ascending=False)[:10]

# Plot

color_map = ['#f5f5f1' for _ in range(10)]
color_map[0] = color_map[1] = color_map[2] =  '#b20710' # color highlight

fig, ax = plt.subplots(1,1, figsize=(12, 6))
ax.bar(data.index, data, width=0.5, 
       edgecolor='darkgray',
       linewidth=0.6,color=color_map)

#annotations
for i in data.index:
    ax.annotate(f"{data[i]}", 
                   xy=(i, data[i] + 150),
                   va = 'center', ha='center',fontweight='light', fontfamily='serif')





# Title and sub-title

fig.text(0.09, 1, 'Top 10 countries on Netflix', fontsize=15, fontweight='bold', fontfamily='serif')
fig.text(0.09, 0.95, 'The three most frequent countries have been highlighted.', fontsize=12, fontweight='light', fontfamily='serif')

fig.text(1.1, 1.01, 'Insight', fontsize=15, fontweight='bold', fontfamily='serif')


ax.grid(axis='y', linestyle='-', alpha=0.4)   

grid_y_ticks = np.arange(0, 4000, 500) # y ticks, min, max, then step
ax.set_yticks(grid_y_ticks)
ax.set_axisbelow(True)

plt.axhline(y = 0, color = 'black', linewidth = 1.3, alpha = .7)

ax.tick_params(axis='both', which='major', labelsize=12)


import matplotlib.lines as lines
l1 = lines.Line2D([1, 1], [0, 1], transform=fig.transFigure, figure=fig,color='black',lw=0.2)
fig.lines.extend([l1])

ax.tick_params(axis=u'both', which=u'both',length=0)

plt.show()


 


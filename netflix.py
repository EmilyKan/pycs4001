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


plt.show()


 


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

oo = pd.read_csv('Olympics.csv', skiprows=4)

gy = oo[oo.NOC == 'USA'].groupby(['Edition','Athlete', 'Medal']).size().unstack('Medal', fill_value=0)
print(gy)
gy['Total'] = gy['Gold'] + gy['Silver'] + gy['Bronze']
print(gy)
gy.reset_index(inplace=True)
print(gy.groupby('Edition'))
for year, group in gy.groupby('Edition') :
    print(group.sort_values('Total', ascending=False).head(1))


print(oo[oo.Edition == 2008].groupby('NOC').size())
lo = oo[oo.Edition == 2008].groupby(['NOC', 'Medal']).size()
print(lo)
print(lo.unstack(fill_value=0))
g = lo.unstack(fill_value=0)
g = g.sort_values(['Gold', 'Silver', 'Bronze'], ascending=False)[['Gold', 'Silver', 'Bronze']]
sns.heatmap(g);
plt.show()

g = g.transpose()
print(g)
plt.figure(figsize=(16,5))
sns.heatmap(g)
plt.show()
top5 = oo.groupby(['Athlete', 'Medal']).size().unstack('Medal', fill_value=0).sort_values(['Gold', 'Silver', 'Bronze'], ascending=False)[['Gold', 'Silver', 'Bronze']].head(5)
print(top5)
top5.plot(kind='bar')
plt.show()

from matplotlib.colors import ListedColormap
sns.color_palette()
sns.palplot(sns.color_palette())
plt.show()

#gsb = ['$dbb40c', '#c5c9c7', '#a87900']
#sns.palplot(sns.color_palette(gsb))
#plt.show()


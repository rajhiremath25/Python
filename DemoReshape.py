import pandas as pd

oo = pd.read_csv('Olympics.csv', skiprows=4)
print(oo.head(3))

mw2008ht = oo[(oo.Edition == 2008) & ((oo.Event == '100m') | (oo.Event == '200m') )]
print(mw2008ht)
g = mw2008ht.groupby(['NOC', 'Gender', 'Discipline', 'Event']).size()
print(g)

df = g.unstack(['Discipline', 'Event'])
print(df)
print(df.stack('Event'))
print(df.unstack())
print(df.unstack('Gender'))

mwusg = oo[(oo.Medal == 'Gold') & (oo.NOC == 'USA')]
myplot = mwusg.groupby(['Edition', 'Gender']).agg({'Medal' : ['count']})
print(myplot)
finalPlot = myplot.unstack('Gender', fill_value=0)
print(finalPlot)

import matplotlib.pyplot as plt
finalPlot.plot(kind='bar')
plt.show()

mostMedals = oo.groupby(['Athlete', 'Medal']).size().unstack('Medal', fill_value=0)
top5 = mostMedals.sort_values(['Gold', 'Silver', 'Bronze'], ascending=False)[['Gold', 'Silver', 'Bronze']].head(5)
print(top5)
top5.plot(kind='bar')
plt.show()

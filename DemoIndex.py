import pandas as pd

oo = pd.read_csv('Olympics.csv', skiprows=4)
oo.head()
print(type(oo.index))
print(oo.index[100])
# oo.index[100] = 5 Index is immutable
print(oo.set_index('Athlete').head(3))
print(oo.head(3))
print(oo.set_index('Athlete', inplace=True))
print(oo.head(3))
oo.reset_index(inplace=True)
print(oo.head(3))
ath = oo.set_index('Athlete')
print(ath.head(3))
ath.sort_index(inplace=True)
print(ath.head(3))
ath.sort_index(inplace=True, ascending=False)
print(ath.head(3))
print(ath.loc['BOLT, Usain'])
print(oo[oo.Athlete =='BOLT, Usain'])
print(oo.loc[oo.Athlete =='BOLT, Usain'])
print(oo.iloc[1700])
print(oo.iloc[[152, 6000, 15000, 1700]])
print(oo.iloc[1:4])

import matplotlib.pyplot as plt
oo.Edition.value_counts().sort_index().plot()
plt.show()

lo = oo[oo.Edition == 2008]
print(lo.head(3))

noc = pd.read_csv('Summer Olympic medallists 1896 to 2008 - IOC COUNTRY CODES.csv')
print(noc.head(3))

print(noc[noc['Country'] != noc['Country1']])
noc.set_index('Int Olympic Committee code', inplace=True)
print(noc.head(3))

medals_2008 = lo.NOC.value_counts()
print(medals_2008)
noc['medals_2008'] = medals_2008
print(noc.head())
# print(noc[noc.medals_2008.isNull])


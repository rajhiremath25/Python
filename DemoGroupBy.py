import pandas as pd

oo = pd.read_csv('Olympics.csv', skiprows=4)
oo.head()

print(oo.groupby('Edition'))
print(type(oo.groupby('Edition')))
print(list(oo.groupby('Edition')))

for group_key, group_value in oo.groupby('Edition') :
    print('key : ' ,group_key)
    print('vaue : ' , group_value)

print(type(group_value))
print(oo.groupby('Edition').size())
print(oo.groupby(['Edition', 'NOC', 'Medal']).agg(['min', 'max', 'count']))
print(oo.groupby(['Edition', 'NOC', 'Medal']).agg(['count']))
print(oo.groupby(['Edition', 'NOC', 'Medal']).size())
print(oo.groupby(['Edition', 'NOC', 'Medal']).agg({'Edition' : ['min', 'max', 'count']}))
print(oo[oo.Athlete == 'LEWIS, Carl'].groupby('Athlete').agg({'Edition' : ['min', 'max', 'count']}))

import matplotlib.pyplot as plt

oo.groupby('Edition').size().plot(kind='bar')
plt.show()

print(oo.groupby('NOC').size())
print(oo.groupby('NOC').agg({'Edition' : ['count', 'min', 'max']}))



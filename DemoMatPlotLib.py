import pandas as pd

oo = pd.read_csv('Olympics.csv', skiprows=4)
oo.head()

import matplotlib.pyplot as plt

fo = oo[oo.Edition == 1896]
fo.head()
obj = fo.Sport.value_counts()
print(obj)
obj.plot()
obj.plot(kind='line');
obj.plot(kind='bar', color='green');
plt.show()

obj.plot(kind='line', figsize=(10,3));
plt.show()


obj.plot(kind='barh');
plt.show()

obj.plot(kind='pie', colormap='Pastel1');
plt.show()

import seaborn as sns
sns.countplot(x='Medal', data=oo, hue='Gender');
plt.show()

chineseMedals = oo[(oo.NOC == 'CHN') & (oo.Edition == 2008)]
print(chineseMedals)
chineseMedals.head()
chineseMedals.Gender.value_counts().plot(kind='bar')
plt.show()

sns.countplot(x='Gender', data=chineseMedals);
plt.show()

sns.countplot(x='Gender', data=chineseMedals, palette='bwr');
plt.show()

sns.countplot(x='Medal', data=chineseMedals, hue='Gender');
plt.show()

sns.countplot(x='Medal', data=chineseMedals, hue='Gender', palette='bwr', order=['Gold', 'Silver', 'Bronze']);
plt.show()






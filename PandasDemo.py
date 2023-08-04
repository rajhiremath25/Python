import pandas as pd

oo = pd.read_csv('Olympics.csv', skiprows=4)
print(oo.head())
print(oo['City'])
print(oo['Athlete'])
print(oo.Athlete)
print(oo[['City', 'Edition', 'Athlete']])
print(type(oo[['City', 'Edition', 'Athlete']]))
print(oo.NOC)
print(oo['NOC'])
print(type(oo['NOC']))
print(oo.shape)
print(oo.shape[0], oo.shape[1])
print(oo.head(2))
print(oo.tail(2))
print(oo.Edition.value_counts())
print(oo.Gender.value_counts())
print(oo.Gender.value_counts(ascending=True))
ath = oo.Athlete.sort_values()
print(ath)
ath = oo.sort_values(by=['Edition', 'Athlete'])
print(ath)
print(oo[(oo.Medal == 'Gold') & (oo.Gender == 'Women')])
print(oo[oo.Athlete.str.contains('OWENS, Jesse')]['Event'].value_counts())
maleBadmintonGolds = oo[(oo.Gender =='Men') & (oo.Medal == 'Gold') & (oo.Sport == 'Badminton') & (oo.Event == 'singles')]
print(maleBadmintonGolds.NOC.value_counts())
print(maleBadmintonGolds.sort_values(by=['Athlete']))
rec = oo[(oo.Edition >= 1982)]
print(rec.NOC.value_counts().head(3))
mgh = oo[(oo.Gender =='Men') & (oo.Medal == 'Gold') & (oo.Event == '100m')]
mghByEdition = mgh.sort_values('Edition', ascending=False)
print(mghByEdition[['City','Edition', 'Athlete', 'NOC']])










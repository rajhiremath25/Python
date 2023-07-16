#Set is unordered and undexed collection of elements enclosed with {}
#Duplicates are not allowed in set

s1 = {1, "a", True, 2.15}
print(s1)

s1 = {1, "a", 1, True, 2.15}
print(s1) #duplicates not allowed

s1.add(3+5j)
print(s1)

s1.update([10, 20, 30])
print(s1)

s1.remove(30)
print(s1)

s1 = {1, 2, 3, "b"}
s2 = {"a", "b", "c"}
s3 = s1.union(s2)
print(s3)
s3 = s1.intersection(s2)
print(s3)



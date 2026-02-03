#Do lists lo aur common elements find karo (use set).
list1 = [1,4,2,6,3,7,8,4, 3, 8]
list2 = [8,3,5,2,6,0,1]
set1 = set(list1)
set2 = set(list2)
print(f"commonelements are: {set1.intersection(set2)}")

#Set me se duplicates automatically kaise remove hote hain – example ke saath show karo.
print(f"whenever you print the set,, it will only show the unique valuesof set like in list1 we have duplicate elems but when we convert it in set it will remove internally duplicate values: {set1}")

#Two sets ka:
#union
print(f"union is: {set1.union(set2)}")

#intersection
print(f"intersection is: {set1.intersection(set2)}")

#difference find karo.
print(f"difference is: {set1.difference(set2)}")
print(f"difference2 is: {set2.difference(set1)}")
list1 = [1, 2, 3, 4, 5]
steps = input()
list2 = list1[int(steps):len(list1)] + list1[0:int(steps)]
print(list2)
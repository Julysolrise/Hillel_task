set1 = {1, 2, 3, 4}
set2 = {2, 3, 5, 6}
set3 = {3, 4, 6, 7}

set_intersected = set.intersection(set1, set2, set3)
print(set_intersected)

set_diference_done = set1.difference(set2).difference(set3)
print(set_diference_done)

set_union = set1.union(set2).union(set3)
print(set_union)

sampleSet = {"Yellow", "Orange", "Black"}
sampleList = ["Blue", "Green", "Red"]
sampleSet.update(set(sampleList))
print(sampleSet)

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set_res = set1.intersection(set2)
print(set_res)

set_union = set1.union(set2)
print(set_union)

set1 = {10, 20, 30}
set2 = {20, 40, 50}
set1.difference_update(set2)
print(set1)

set1 = {10, 20, 30, 40, 50}
set1.difference_update({10, 20, 30})
print(set1)


set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
set_intersected = set1.intersection(set2)
if set_intersected:
    print(f'Commont elements in {set1} and {set2} are: ', set_intersected)
else:
    print('There are not common elements')

set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

set1.update(set2)
print(set1)

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set1.intersection_update(set2)
print(set1)

import random
import time
def binary_search (list, target, low=None, high=None):
    if low is None:
        low = 0
        
    if high is None:
        high = len(list) - 1
        
    if high < low:
        return -1
    midpoint = (high + low) // 2
##    print(f"midpoint {midpoint}")
    if target == list[midpoint]:
        return midpoint
    elif target < list[midpoint]:
##        print(f"min {list[low:midpoint - 1]}")
        return binary_search (list, target, low, midpoint - 1)
    else:
##        print(f" max {list[midpoint +1: high]}")
        return binary_search (list, target, midpoint + 1, high)



length = 10000
    # build a sorted list of length 10000
sorted_list = set()

while len(sorted_list) < length:
    sorted_list.add(random.randint(-3*length, 3*length))
    
sorted_list = sorted(list(sorted_list))
start = time.time()
for target in sorted_list:
     binary_search(sorted_list ,target)

end = time.time()
print(f"binary search time: {end-start} seconds")

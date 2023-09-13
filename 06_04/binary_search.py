import random


def binary_search(data, target):
    low_idx = 0
    high_idx = len(data)-1
    # while True:
    #     middle_idx = (low_idx+high_idx)//2
    #     print(low_idx, middle_idx, high_idx)

    #     if data[middle_idx] > target:
    #         high_idx=middle_idx
    #     elif data[middle_idx] < target:
    #         low_idx=middle_idx
    #     elif data[middle_idx] == target:
    #         return middle_idx
        
    #     if high_idx-low_idx<=1:
    #         if data[high_idx] == target:
    #             return high_idx
    #         elif data[low_idx] == target:
    #             return low_idx
    #         else:
    #             return -1
    while low_idx <= high_idx:
        middle_idx = (low_idx+high_idx)//2
        if data[middle_idx] == target:
            return middle_idx
        elif data[middle_idx] < target:
            low_idx=middle_idx+1
        else:
            high_idx=middle_idx-1
    return -1

n = 10
max_val = 50
data = [random.randint(1, max_val) for i in range(n)]
data.sort()
#data = [2, 14, 16, 19, 21, 28, 30, 31, 32, 33]
print("Data:", data)
# target = int(input("Enter target value: "))
target_pos = binary_search(data, 33)
print(target_pos)
# if target_pos == -1:
#     print("Your target value is not in the list.")
# else:
#     print("You target value has been found at index", target_pos)
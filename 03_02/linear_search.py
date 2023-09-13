# def linear_search(data, target):
#     for i in range(0,len(data)):
#         if data[i] == target:
#             return i
#     return -1


def linear_search(data, target):
<<<<<<< HEAD
    for idx,val in enumerate(data):
        if val == target:
            return idx
    return -1

=======
    for idx, val in enumerate(data):
        if val == target:
            return idx  # Early exit if item is found.
    return -1
>>>>>>> 03_04


data = [4, 5, 2, 7, 1, 8]
target = 1
result = linear_search(data, target)
if result == -1:
    print("Item not found.")
else:
    print(f"Item found at position {result}.")

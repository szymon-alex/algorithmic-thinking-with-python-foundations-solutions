def find_min(l):
    min_index=0
    for idx, val in enumerate(l):
        if l[idx] < l[min_index]:
            min_index = idx
    return min_index

def selection_sort(xs):
    xs_size = len(xs)
    for idx in range(xs_size-1):
        min_idx = find_min(xs[idx+1:])+idx
        if xs[idx] > xs[min_idx+1]:
            xs[idx], xs[min_idx+1] = xs[min_idx+1], xs[idx]
    return xs



xs = [3, 2, 1, 5, 4]

print(xs)
selection_sort(xs)
print(xs)

# A nice Pythonic way to check  a list is sorted
# without relying on using Python's own sorting methods to compare.
print(all(xs[i] <= xs[i + 1] for i in range(len(xs) - 1)))

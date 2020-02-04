# merge two sorted lists
def merge(l, r):
    result = []
    # left and right indices of sorted lists
    l_idx, r_idx = 0, 0
    while l_idx < len(l) and r_idx < len(r):
        if l[l_idx] < r[r_idx]:
            result.append(l[l_idx])
            l_idx += 1
        else:
            result.append(r[r_idx])
            r_idx += 1
    if l_idx == len(l):
        result.extend(r[r_idx:])
    else:
        result.extend(l[l_idx:])
    return result


def merge_sort(arr):
    # Recursive base case
    if len(arr) <= 1:
        return arr

    # Recursively split input
    left = merge_sort(arr[:len(arr)//2])
    right = merge_sort(arr[len(arr)//2:])

    return merge(left, right)




test = [3, 5, 7, 2, 1, 8, 6, 4]

a = merge_sort(test)
print(a)
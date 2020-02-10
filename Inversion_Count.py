# Sort and count inversions of array of distinct integers
def sort_count_inv(arr):
    n = len(arr)
    if n == 0 or n == 1:
        return arr, 0
    else:
        (left, left_inv) = sort_count_inv(arr[:n // 2])
        (right, right_inv) = sort_count_inv(arr[n // 2:])
        (result, split_inv) = merge_count_split_inv(left, right)
    print(result, left_inv + right_inv + split_inv)
    return result, left_inv + right_inv + split_inv


# Input: sorted arrays C and D of length n/2 with distinct integer
# Output: sorted array B of length n and the number of split inversions
def merge_count_split_inv(left, right):
    result = []
    i, j, inversions = 0, 0, 0
    # Merge and count inversions advancing appropriate pointer
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            inversions += len(left) - i
    # Append elements still present
    if i == len(left):
        result.extend(right[j:])
    else:
        result.extend(left[i:])
    return result, inversions


sort_count_inv([4, 3, 5, 7, 8, 1])
# merge_count_split_inv([4, 5, 6], [1, 2, 3])

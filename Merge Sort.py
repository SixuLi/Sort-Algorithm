# Time Complexities:
# Worst Case Complexity: O(nlogn)
# Best Case Complexity: O(nlogn)
# Average Case Complexity: O(nlogn)

# Space Complexity: O(n)

# Stable or not: Yes

def MergeSort(nums, l, r):
    if l < r:
        m = (l+r) // 2
        MergeSort(nums, l, m)
        MergeSort(nums, m+1, r)
        merge(nums, l, m, r)
    return nums

def merge(nums, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L, M = n1*[0], n2*[0]
    for i in range(n1):
        L[i] = nums[l+i]
    for j in range(n2):
        M[j] = nums[m+1+j]
    i, j, k = 0, 0, l
    while i < n1 and j < n2:
        if L[i] < M[j]:
            nums[k] = L[i]
            i += 1
        else:
            nums[k] = M[j]
            j += 1
        k += 1
    while i < n1:
        nums[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        nums[k] = M[j]
        j += 1
        k += 1

nums = [-2, 45, 0, 11, -9]
print('Sorted Array in Ascending Order:')
print(MergeSort(nums, 0, len(nums)-1))
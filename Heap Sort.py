# Time Complexities:
# Worst Case Complexity: O(nlogn)
# Best Case Complexity: O(nlogn)
# Average Case Complexity: O(nlogn)

# Space Complexity: O(1)

# Stable or not: No

def heapify(nums, n, i):
    # Find largest among root and children.
    largest = i
    lc = 2*i + 1
    rc = 2*i + 2
    if lc < n and nums[lc] > nums[largest]:
        largest = lc
    if rc < n and nums[rc] > nums[largest]:
        largest = rc

    # If root is not largest, swap with largest and continue heapifying.
    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i]
        heapify(nums, n, largest)

def BuildHeap(nums):
    n = len(nums)
    for i in range(n, -1, -1):
        heapify(nums, n, i)

def HeapSort(nums):
    BuildHeap(nums)
    n = len(nums)
    for i in range(n-1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)
    return nums

nums = [12, 11, 13, 5, 6, 7]
sort_nums = HeapSort(nums)
print('Sorted Array in Ascending Order:')
print(sort_nums)

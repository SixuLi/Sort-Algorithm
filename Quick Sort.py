# Time Complexities:
# Worst Case Complexity: O(n^2)
# Best Case Complexity: O(nlogn)
# Average Case Complexity: O(nlogn)

# Space Complexity: O(logn)

# Stable or not: No

def QuickSort(nums, left, right):
    if left < right:
        pivot = partition(nums, left, right)
        QuickSort(nums, left, pivot-1)
        QuickSort(nums, pivot+1, right)
    return nums

def partition(nums, left, right):
    pivot = right
    index_small = left
    for i in range(left, right):
        if nums[i] < nums[pivot]:
            nums[index_small], nums[i] = nums[i], nums[index_small]
            index_small += 1
    nums[pivot], nums[index_small] = nums[index_small], nums[pivot]
    return index_small

#nums = [5, 4, 3, 2, 1]
#nums = [9, 5, 1, 4, 3]
nums = [8, 7, 2, 1, 0, 9, 6, 7, 9, 1]
sort_nums = QuickSort(nums, 0, len(nums)-1)
print('Sorted Array in Ascending Order:')
print(sort_nums)

# Optimize the Original Quick Sort
# Consider the case that the target array contains a lot of duplicate numbers, in such a case,
# the original Quick Sort Algorithm may easily fall into the Worst Case, because of unbalanced partition.
# Hence, we can use Three-Way Quick Sort to solve this problem.
# Given a pivot number, we divide the original array(nums[left,right]) into three part:
# 1. nums[left, lt-1]: All the elements here smaller than pivot.
# 2. nums[lt, gt]: All the elements here equal to pivot.
# 3. nums[gt+1, right]: All the elements here larger than pivot.

# Specific Method: We scan the array from left to right. When Scanning current ith element:
# 1. Let pointer lt satisfy that all the elements in nums[left, lt-1] are less than pivot.
# 2. Let pointer gt satisfy that all the elements in nums[gt+1, right] are larger than pivot.
# 3. Let point i satisfy that all the elements in nums[lt, i-1] are equal to pivot and nums[i, gt] remaining under scan.

def ThreeWayQuickSort(nums, left, right):
    if left < right:
        lt, gt = ThreeWayPartition(nums, left, right)
        ThreeWayQuickSort(nums, left, lt-1)
        ThreeWayQuickSort(nums, gt+1, right)
    return nums

def ThreeWayPartition(nums, left, right):
    lt, gt, i = left, right, left+1
    pivot = nums[left]
    while i <= gt:
        if nums[i] > pivot:
            nums[i], nums[gt] = nums[gt], nums[i]
            gt -= 1
        elif nums[i] < pivot:
            nums[i], nums[lt] = nums[lt], nums[i]
            i += 1
            lt += 1
        else:
            i += 1
    return lt, gt

nums = [8, 7, 2, 1, 0, 9, 6, 7, 9, 1]
sort_nums = ThreeWayQuickSort(nums, 0, len(nums)-1)
print('Sorted Array in Ascending Order:')
print(sort_nums)














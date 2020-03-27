# Time Complexities:
# Worst Case Complexity: O(n^2)
# Best Case Complexity: O(n)
# Average Case Complexity: O(n^2)

# Space Complexity: O(1)

# Stability: Stable sort Algorithms sort repeated elements in the same order that they appear in the input.
# Stable or not: Yes

def BubbleSort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

def OptimizeBubbleSort(nums):
    n = len(nums)
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
        if swapped == False:
            break
    return nums


nums = [-2, 45, 0, 11, -9]
sort_nums = OptimizeBubbleSort(nums)
print('Sorted Array in Ascending Order:')
print(sort_nums)
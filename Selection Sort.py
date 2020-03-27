def SelectionSort(nums):
    n = len(nums)
    for i in range(n-1):
        index = i
        for j in range(i+1,n):
            if nums[index] > nums[j]:
                index = j
        nums[i], nums[index] = nums[index], nums[i]
    return nums

nums = [-2, 45, 0, 11, -9]
sort_nums = SelectionSort(nums)
print('Sorted Array in Ascending Order:')
print(sort_nums)

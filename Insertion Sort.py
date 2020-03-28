def InsertionSort(nums):
    n = len(nums)
    for i in range(1, n):
        cur = nums[i]
        j = i-1
        while j >= 0 and cur < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = cur
    return nums

nums = [5, 4, 3, 2, 1]
#nums = [9, 5, 1, 4, 3]
sort_nums = InsertionSort(nums)
print('Sorted Array in Ascending Order:')
print(sort_nums)
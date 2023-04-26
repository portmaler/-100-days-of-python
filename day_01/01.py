def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    left = 0
    right = len(nums) - 1
    mid = int((left + right) / 2)
    print(len(nums))
    while left <= right:
        print(mid)
        if nums[mid] == target: return mid

        if target > nums[mid]:
            left = mid + 1
        elif target < nums[mid]:
            right = mid - 1
        mid = int((left + right) / 2)

    return mid+1


if __name__ == '__main__':
    lst = [0, 1, 2, 4, 7, 9, 12, 16, 18, 22, 44, 55, 68, 96, 99, 123, 125, 126, 147, 148, 159]
    print(searchInsert(lst, 15))

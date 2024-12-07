class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # Pointer for the position of the next unique element
        k = 0

        for i in range(len(nums)):
            # Only update nums[k] when we find a new unique element
            if i == 0 or nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k

def test_remove_duplicates():
    solution = Solution()

    # Test case 1
    nums = [1, 1, 2]
    expectedNums = [1, 2]
    k = solution.removeDuplicates(nums)
    assert k == len(expectedNums), f"Test failed for input: {nums}. Expected length {len(expectedNums)}, got {k}."
    assert nums[:k] == expectedNums, f"Test failed for input: {nums}. Expected {expectedNums}, got {nums[:k]}."

    # Test case 2
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    expectedNums = [0, 1, 2, 3, 4]
    k = solution.removeDuplicates(nums)
    assert k == len(expectedNums), f"Test failed for input: {nums}. Expected length {len(expectedNums)}, got {k}."
    assert nums[:k] == expectedNums, f"Test failed for input: {nums}. Expected {expectedNums}, got {nums[:k]}."

    # Test case 3
    nums = [1, 1, 1, 1, 1]
    expectedNums = [1]
    k = solution.removeDuplicates(nums)
    assert k == len(expectedNums), f"Test failed for input: {nums}. Expected length {len(expectedNums)}, got {k}."
    assert nums[:k] == expectedNums, f"Test failed for input: {nums}. Expected {expectedNums}, got {nums[:k]}."

    # Test case 4
    nums = []
    expectedNums = []
    k = solution.removeDuplicates(nums)
    assert k == len(expectedNums), f"Test failed for input: {nums}. Expected length {len(expectedNums)}, got {k}."
    assert nums[:k] == expectedNums, f"Test failed for input: {nums}. Expected {expectedNums}, got {nums[:k]}."

    # Test case 5
    nums = [1, 2, 3, 4, 5]
    expectedNums = [1, 2, 3, 4, 5]
    k = solution.removeDuplicates(nums)
    assert k == len(expectedNums), f"Test failed for input: {nums}. Expected length {len(expectedNums)}, got {k}."
    assert nums[:k] == expectedNums, f"Test failed for input: {nums}. Expected {expectedNums}, got {nums[:k]}."

    print("All test cases passed!")

# Run the tests
test_remove_duplicates()


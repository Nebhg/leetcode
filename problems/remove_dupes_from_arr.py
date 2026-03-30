from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Remove duplicates from a sorted array in-place.
        Modify nums so each unique element appears once, maintaining order.
        Return the number of unique elements.
        
        Constraint: Must modify array in-place with O(1) extra space.
        Use two pointers: one for write position, one for read position.
        """
        #check if the list is empty
        if not nums:
            return 0  # also fix: return 0, not None

        write = 1  # next position to write a unique value

        for read in range(1, len(nums)):
            if nums[read] != nums[read - 1]:  # new unique value found
                nums[write] = nums[read]       # write it to the front
                write += 1

        return write
# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Array with duplicates
    nums1 = [1, 1, 2]
    result1 = sol.removeDuplicates(nums1)
    print(f"Test 1 - Result: {result1}, Array: {nums1[:result1]}")  # Expected: 2, [1, 2]
    
    # Test 2: Array with more duplicates
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    result2 = sol.removeDuplicates(nums2)
    print(f"Test 2 - Result: {result2}, Array: {nums2[:result2]}")  # Expected: 5, [0, 1, 2, 3, 4]
    
    # Test 3: Empty array
    nums3 = []
    result3 = sol.removeDuplicates(nums3)
    print(f"Test 3 - Result: {result3}, Array: {nums3[:result3]}")  # Expected: 0, []
    
    # Test 4: Single element
    nums4 = [1]
    result4 = sol.removeDuplicates(nums4)
    print(f"Test 4 - Result: {result4}, Array: {nums4[:result4]}")  # Expected: 1, [1]
    
    # Test 5: No duplicates
    nums5 = [1, 2, 3, 4, 5]
    result5 = sol.removeDuplicates(nums5)
    print(f"Test 5 - Result: {result5}, Array: {nums5[:result5]}")  # Expected: 5, [1, 2, 3, 4, 5]
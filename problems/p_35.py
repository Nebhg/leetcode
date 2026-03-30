from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Search Insert Position
        Given a sorted array of distinct integers and a target value,
        return the index if the target is found. If not, return the index
        where it would be if it were inserted in order.
        Must use O(log n) runtime complexity (binary search).
        
        Constraints:
        - 1 <= nums.length <= 10^4
        - -10^4 <= nums[i] <= 10^4
        - nums contains distinct values sorted in ascending order
        - -10^4 <= target <= 10^4
        """
        #base case, if the list is empty then it would be inserted at index 0
        if not nums:
            return 0
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid -1
        return left
        #iterative approach
        # for i in range(len(nums)):
        #     # does i = target?
        #     if nums[i] == target:
        #         return i
        #     elif nums[i] > target:
        #         return i
        # return len(nums)  
      
            


# Test cases
def test_searchInsert():
    sol = Solution()
    
    # Example 1: target found in array
    assert sol.searchInsert([1, 3, 5, 6], 5) == 2
    
    # Example 2: target inserted at beginning
    assert sol.searchInsert([1, 3, 5, 6], 2) == 1
    
    # Example 3: target inserted at end
    assert sol.searchInsert([1, 3, 5, 6], 7) == 4
    
    # Edge case: single element array, target found
    assert sol.searchInsert([1], 1) == 0
    
    # Edge case: single element array, target before
    assert sol.searchInsert([1], 0) == 0
    
    # Edge case: single element array, target after
    assert sol.searchInsert([1], 2) == 1
    
    # Target at start
    assert sol.searchInsert([1, 3, 5, 6], 1) == 0
    
    # Target at end
    assert sol.searchInsert([1, 3, 5, 6], 6) == 3
    
    print("All tests passed!")

if __name__ == "__main__":
    test_searchInsert()
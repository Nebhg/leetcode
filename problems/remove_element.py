from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        
        write = 0  # next position to write a non-val value
        for read in range(len(nums)):
            if nums[read] != val:  # found a non-val value
                nums[write] = nums[read]  # write it to the front
                write += 1
        return write


# Test cases
def test_removeElement():
    solution = Solution()
    
    # Example 1: nums = [3,2,2,3], val = 3
    nums1 = [3, 2, 2, 3]
    k1 = solution.removeElement(nums1, 3)
    assert k1 == 2, f"Expected k=2, got k={k1}"
    assert sorted(nums1[:k1]) == [2, 2], f"Expected [2, 2], got {sorted(nums1[:k1])}"
    
    # Example 2: nums = [0,1,2,2,3,0,4,2], val = 2
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    k2 = solution.removeElement(nums2, 2)
    assert k2 == 5, f"Expected k=5, got k={k2}"
    assert sorted(nums2[:k2]) == [0, 0, 1, 3, 4], f"Expected [0, 0, 1, 3, 4], got {sorted(nums2[:k2])}"
    
    # Edge case: empty array
    nums3 = []
    k3 = solution.removeElement(nums3, 0)
    assert k3 == 0, f"Expected k=0, got k={k3}"
    
    # Edge case: all elements are val
    nums4 = [1, 1, 1, 1]
    k4 = solution.removeElement(nums4, 1)
    assert k4 == 0, f"Expected k=0, got k={k4}"
    
    # Edge case: no elements are val
    nums5 = [1, 2, 3, 4]
    k5 = solution.removeElement(nums5, 5)
    assert k5 == 4, f"Expected k=4, got k={k5}"
    assert sorted(nums5[:k5]) == [1, 2, 3, 4], f"Expected [1, 2, 3, 4], got {sorted(nums5[:k5])}"
    
    # Single element that matches val
    nums6 = [5]
    k6 = solution.removeElement(nums6, 5)
    assert k6 == 0, f"Expected k=0, got k={k6}"
    
    # Single element that doesn't match val
    nums7 = [5]
    k7 = solution.removeElement(nums7, 3)
    assert k7 == 1, f"Expected k=1, got k={k7}"
    assert nums7[0] == 5, f"Expected 5, got {nums7[0]}"
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_removeElement()
    
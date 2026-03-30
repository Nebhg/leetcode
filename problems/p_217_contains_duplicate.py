from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counts = {}

        if not nums:
            return False

        for i in nums:
            if i in counts: 
                counts[i] += 1
                if counts[i] >= 2:
                    return True
            else:
                counts[i] = 1
        return False

def testSolution():
    solution = Solution()
    
    # Example 1: has duplicate (1 appears twice)
    assert solution.containsDuplicate([1, 2, 3, 1]) == True
    
    # Example 2: all elements distinct
    assert solution.containsDuplicate([1, 2, 3, 4]) == False
    
    # Example 3: multiple duplicates
    assert solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True
    
    # Edge case: single element
    assert solution.containsDuplicate([1]) == False
    
    # Edge case: two same elements
    assert solution.containsDuplicate([1, 1]) == True
    
    print("All test cases passed!")

if __name__ == "__main__":
    testSolution()
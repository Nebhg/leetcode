from typing import List
from collections import defaultdict


class Solution:

    def get_name(self, input):
        #get user to input their name
        name = input("Please enter your name: ")
        return name


    def twoSum(self, nums, target):
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i

    def contains_duplicate(self, input):
        seen = set()        
        for c in input:
            if c in seen:
                return True
            seen.add(c)
        return False
    
    def validParentheses(self, input: str) -> bool:
        #take an input of a list of type string that contains 
        # what type of data can we use to solve this problem? a stack
        stack = []
        opening = ['(', '{', '[']
        closing = [')', '}', ']']

        # iterate over the input str
        # push all elements on to the stack
        for c in input:
            stack.append(c)
        
        # pop the top of the stack and check the 


    def group_anagrams(self, strs: List[str]) -> List[List[str]]:

        result = defaultdict(list)
        # for each s in the list
        # loop over each character
        # first order then count each char
        # then use the ordered version of each grouping as the key and return the values for those keys
        # for s in strs:
        #     # sort it and add it to that key as a value
        #     key = " ".join(sorted(s))
            
        #     result[key].append(s)
        # return list(result.values())
        for s in strs:
            count = [0] * 26 # a .... z
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            result[key].append(s)
        return list(result.values())

    def top_k(self, nums: List[int], k: int) -> List[int]:
        # use bucket sort to solve this problem
        # use index to count groups of items that have this value
        # then return the k items starting form the end of the list 
        # what type of data structure do we want here? a hashmap to count the frequency
        
        # count the frequency of using a hashmap
        # create bucket lists where the index = frequency 
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]     
        for num, freq in count.items():
            buckets[freq].append(num)
        
        result = []
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
            return result


        #use bucket sort 
        # create the key of the index to be the count of how many of each elements there is
        #  1 = [10,1]
        #  2 = [11,2,4]
        #  3 =  [6]
        # if k = 5 we return [10,1,11,2,4]
            # for each number in the list we want to track how many times it appears in the list, then return the top k frequency elements
            # need to intialise the index of the array to be a representation oh how many times each number appears so that we dont have to di the other way of having an index for every element in the nums list with many be empty if the last vlaue is larger

    def twoSum1(self, nums, target):
        # need to scan the list of nums and find the pair that makes the target
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        


if __name__ == "__main__":
    solution = Solution()

    #need test casses for contains_duplicate and twoSum
    assert solution.twoSum1([2, 7, 11, 15], 9) == [0, 1]
    assert solution.twoSum1([3, 2, 4], 6) == [1, 2]
    # assert solution.contains_duplicate([1, 2, 3, 1]) == True
    # assert solution.contains_duplicate([1, 2, 3, 4]) == False

    #create tests for gorup anagrams
    assert solution.group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]  

    print("All test cases passed!")
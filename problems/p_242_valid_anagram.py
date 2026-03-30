class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_map = {}
        t_map = {}

        if not s or not t:
            return False
        
        # loop through s and count characters into s_map
        for i in s:
            if i in s_map:
                s_map[i] += 1
            else:
                s_map[i] = 1
            
        
        for i in t:
            if i in t_map:
                t_map[i] += 1
            else:
                t_map[i] = 1
        
        return s_map == t_map

            
            
        # loop through t and count characters into t_map

        # then compare


def test_solution():
    sol = Solution()

    assert sol.isAnagram("anagram", "nagaram") == True

    print("All tests passed")

if __name__ == "__main__":
    test_solution()
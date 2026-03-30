class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1


def test_strStr():
    sol = Solution()
    
    # Example 1: needle occurs at index 0 and 6, return first occurrence
    assert sol.strStr("sadbutsad", "sad") == 0
    
    # Example 2: needle not found in haystack
    assert sol.strStr("leetcode", "leeto") == -1
    
    # Edge case: needle is single character at the beginning
    assert sol.strStr("abc", "a") == 0
    
    # Edge case: needle is single character in the middle
    assert sol.strStr("abc", "b") == 1
    
    # Edge case: needle is single character at the end
    assert sol.strStr("abc", "c") == 2
    
    # Edge case: single character needle not found
    assert sol.strStr("abc", "d") == -1
    
    # Edge case: needle equals haystack
    assert sol.strStr("hello", "hello") == 0
    
    # Edge case: needle at the end of haystack
    assert sol.strStr("mississippi", "pi") == 9
    
    # Edge case: needle appears multiple times, return first
    assert sol.strStr("aaaa", "aa") == 0
    
    # Edge case: repeated characters, needle not found
    assert sol.strStr("aaa", "aaaa") == -1
    
    # Edge case: needle longer than haystack
    assert sol.strStr("a", "ab") == -1
    
    # Constraint check: overlapping pattern
    assert sol.strStr("abab", "ab") == 0
    
    # Constraint check: needle at the very end
    assert sol.strStr("abcdef", "ef") == 4
    
    print("All tests passed!")


if __name__ == "__main__":
    test_strStr()
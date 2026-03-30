class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Length of Last Word
        Given a string s consisting of words and spaces, return the length of the last word in the string.
        A word is a maximal substring consisting of non-space characters only.
        
        Constraints:
        - 1 <= s.length <= 10^4
        - s consists of only English letters and spaces ' '
        - There will be at least one word in s
        
        Examples:
        - Input: s = "Hello World" -> Output: 5
        - Input: s = "   fly me   to   the moon  " -> Output: 4
        - Input: s = "luffy is still joyboy" -> Output: 6
        """
        # find the final " " char and take any chars to the right of it
        # Start from end, skip trailing spaces
        i = len(s) - 1
        while i >= 0 and s[i] == ' ':
            i -= 1
        
        # Count non-space characters going backwards
        count = 0
        while i >= 0 and s[i] != ' ':
            count += 1
            i -= 1
        
        return count


def test_lengthOfLastWord():
    sol = Solution()
    
    # Example 1: simple two words
    result = sol.lengthOfLastWord("Hello World")
    print(f"Result for 'Hello World': {result}, Expected: 5")
    assert result == 5
    
    # Example 2: multiple spaces before/after
    assert sol.lengthOfLastWord("   fly me   to   the moon  ") == 4
    
    # Example 3: multiple words
    assert sol.lengthOfLastWord("luffy is still joyboy") == 6
    
    # Edge case: single word
    assert sol.lengthOfLastWord("a") == 1
    
    # Edge case: single word with leading spaces
    assert sol.lengthOfLastWord("   a") == 1
    
    # Edge case: single word with trailing spaces
    assert sol.lengthOfLastWord("a   ") == 1
    
    # Edge case: longer single word
    assert sol.lengthOfLastWord("longerword") == 10
    
    print("All tests passed!")


if __name__ == "__main__":
    test_lengthOfLastWord()
        
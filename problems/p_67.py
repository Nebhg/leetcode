class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        Binary Addition
        Given two binary strings a and b, return their sum as a binary string.
        
        Constraints:
        - 1 <= a.length, b.length <= 10^4
        - a and b consist only of '0' or '1' characters
        - Each string does not contain leading zeros except for the zero itself
        
        Examples:
        - Input: a = "11", b = "1" -> Output: "100"
        - Input: a = "1010", b = "1011" -> Output: "10101"
        """
        #use 2 pointers and shift along each string to add each pair together
        pntr1 = len(a) - 1
        pntr2 = len(b) - 1
            #need to implment the following rules
            # 0 + 0 = 0
            # 1 + 0 = 1
            # 1 + 1 = 10, carry the 1
            # 1 + 1 + 1 = 11
        while pntr1 >= 0:
            pass
            # take end of a and end of b and check it agasint the rules
            #after applying cases continue looping until the addition is complete 

def test_addBinary():
    sol = Solution()
    
    # Example 1: simple binary addition
    assert sol.addBinary("11", "1") == "100"
    
    # Example 2: longer binary strings
    assert sol.addBinary("1010", "1011") == "10101"
    
    # Edge case: single digits
    assert sol.addBinary("0", "0") == "0"
    
    # Edge case: adding with zero
    assert sol.addBinary("1", "0") == "1"
    
    # Edge case: same length strings with carry
    assert sol.addBinary("1", "1") == "10"
    
    # Edge case: longer string with multiple carries
    assert sol.addBinary("1111", "1111") == "11110"
    
    # Edge case: different lengths
    assert sol.addBinary("1", "1111") == "10000"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_addBinary()
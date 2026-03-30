from typing import List
import unittest


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # how many digits is the number?
        i = len(digits) - 1
        #dpeending on how long th enumber is we ahve rules for adding 1
        #if its a 9 and then we set curr digit to 0 and set the previous digit to 1
        # elif its not 9 then we just add 1 to the current digit 
        while i >= 0:
            if digits[i] != 9:
                digits[i] += 1
                return digits
            
            digits[i] = 0
            i -= 1
        # if we exit the loop, it means all digits were 9, so we need to add a new digit at the front
        return [1] + digits

class TestPlusOne(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_example_1(self):
        self.assertEqual(self.solution.plusOne([1, 2, 3]), [1, 2, 4])

    def test_example_2(self):
        self.assertEqual(self.solution.plusOne([4, 3, 2, 1]), [4, 3, 2, 2])

    def test_example_3(self):
        self.assertEqual(self.solution.plusOne([9]), [1, 0])

    def test_no_carry_single_digit(self):
        self.assertEqual(self.solution.plusOne([5]), [6])

    def test_no_carry_multi_digit(self):
        self.assertEqual(self.solution.plusOne([1, 2, 8]), [1, 2, 9])

    def test_single_carry_at_end(self):
        self.assertEqual(self.solution.plusOne([1, 2, 9]), [1, 3, 0])

    def test_multiple_carry(self):
        self.assertEqual(self.solution.plusOne([2, 9, 9]), [3, 0, 0])

    def test_all_nines_short(self):
        self.assertEqual(self.solution.plusOne([9, 9]), [1, 0, 0])

    def test_all_nines_long(self):
        self.assertEqual(self.solution.plusOne([9, 9, 9, 9]), [1, 0, 0, 0, 0])

    def test_internal_zeros(self):
        self.assertEqual(self.solution.plusOne([1, 0, 0, 9]), [1, 0, 1, 0])

    def test_large_length_near_constraint(self):
        digits = [1] + [0] * 98 + [9]
        expected = [1] + [0] * 97 + [1, 0]
        self.assertEqual(self.solution.plusOne(digits), expected)


if __name__ == "__main__":
    unittest.main()
    
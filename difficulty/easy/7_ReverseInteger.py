"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321


Example 2:

Input: -123
Output: -321


Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range.
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        isLessZero = False if x > 0 else True
        result = 0
        for index, value in enumerate(str(abs(x))):
            result += int(value) * (10 ** index)
        if len(bin(result)) - 2 >= 32:
            return 0
        return result if not isLessZero else -result


sol = Solution()
print(sol.reverse(-2147483412))
print(len(bin(1)))

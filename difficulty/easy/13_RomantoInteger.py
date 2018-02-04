"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

Some Hits:

Hit 1:
    I - 1
    V - 5
    X - 10
    L - 50
    C - 100
    D - 500
    M - 1000

Hit 2:
    Rules:
    * If I comes before V or X, subtract 1 eg: IV = 4 and IX = 9
    * If X comes before L or C, subtract 10 eg: XL = 40 and XC = 90
    * If C comes before D or M, subtract 100 eg: CD = 400 and CM = 900
"""


class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        rules = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        result = 0
        for index, value in enumerate(s):
            if index == len(s) - 1:
                result += rules[value]
                continue
            if value == 'I' and s[index + 1] == 'V':
                result = 4
            else:
                result += rules[value]
        return result


sol = Solution()
print(sol.romanToInt('IV'))

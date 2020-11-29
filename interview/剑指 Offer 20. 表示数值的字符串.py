#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100"、"5e2"、"-123"、"3.1416"、"-1E-16"、"0123"都表示数值，但"12e"、"1a3.14"、"1.2.3"、"+-5"及"12e+5.4"都不是。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Author: Thomas Young
Date: 2020-09-02 08:18:05
LastEditors: Thomas Young
LastEditTime: 2020-09-02 08:43:07
'''

import re

class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            float(s)
        except:
            return False
        else:
            return True

        # if not s:
        #     return False
        # s = s.strip()
        # m = re.match('[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?', s)
        # return m is not None and m.end() == len(s)

if __name__ == "__main__":
    solution = Solution()
    print(solution.isNumber("+100"))
    print(solution.isNumber("3.1416"))
    print(solution.isNumber("1a3.14"))
    print(solution.isNumber("1 "))
    print(solution.isNumber(".1 "))
    print(solution.isNumber("1. "))
    print(solution.isNumber(" 005047e+6"))

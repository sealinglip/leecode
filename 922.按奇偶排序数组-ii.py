#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-11-12 08:42:08
LastEditors: Thomas Young
LastEditTime: 2020-11-12 09:01:51
'''
#
# @lc app=leetcode.cn id=922 lang=python3
#
# [922] 按奇偶排序数组 II
#
# 给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。
# 对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。
# 你可以返回任何满足上述条件的数组作为答案。

# 示例：
# 输入：[4, 2, 5, 7]
# 输出：[4, 5, 2, 7]
# 解释：[4, 7, 2, 5]，[2, 5, 4, 7]，[2, 7, 4, 5] 也会被接受。

# 提示：
# 2 <= A.length <= 20000
# A.length % 2 == 0
# 0 <= A[i] <= 1000

from typing import List
# @lc code=start
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        if not A:
            return A
        
        newA = [None] * len(A)
        oddPtr, evenPtr = 1, 0
        
        for n in A:
            if (n & 1): #奇数
                newA[oddPtr] = n
                oddPtr += 2
            else:
                newA[evenPtr] = n
                evenPtr += 2
                
        return newA
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.sortArrayByParityII([4, 2, 5, 7])) # [4, 5, 2, 7]
    print(solution.sortArrayByParityII([2, 3])) # [2, 3]

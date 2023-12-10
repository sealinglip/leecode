#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-13 08:34:05
@LastEditors: Thomas Young
@LastEditTime: 2020-06-13 08:59:01
'''
#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
 
# 示例 1：
# 输入：n = 2
# 输出：2
# 解释：有两种方法可以爬到楼顶。
# 1. 1 阶 + 1 阶
# 2. 2 阶

# 示例 2：
# 输入：n = 3
# 输出：3
# 解释：有三种方法可以爬到楼顶。
# 1. 1 阶 + 1 阶 + 1 阶
# 2. 1 阶 + 2 阶
# 3. 2 阶 + 1 阶
 

# 提示：
# 1 <= n <= 45

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # 爬n级台阶的方法就是爬n-1级和爬n-2级方法之和
        # 所以实际是个斐波那契数列问题
        # 初始值
        if n <= 2:
            return n
        else:
            pre = 1
            cur = 2
            for i in range(2, n):
                tmp = cur
                cur = tmp + pre
                pre = tmp
            return cur
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.climbStairs(2)) # 2
    print(solution.climbStairs(3)) # 3
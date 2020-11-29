#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-08-30 11:20:56
LastEditors: Thomas Young
LastEditTime: 2020-08-30 22:09:55
'''
#
# @lc app=leetcode.cn id=557 lang=python3
#
# [557] 反转字符串中的单词 III
#
# 给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

# 示例：

# 输入："Let's take LeetCode contest"
# 输出："s'teL ekat edoCteeL tsetnoc"

# 提示：
# 在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return s
        
        return " ".join([part[::-1] for part in s.split(" ")])
        
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.reverseWords("Let's take LeetCode contest"))
    print(solution.reverseWords("  Let's take LeetCode contest"))

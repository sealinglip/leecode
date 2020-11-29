#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-11-22 08:34:15
LastEditors: Thomas Young
LastEditTime: 2020-11-22 08:41:06
'''
#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

# 示例 1:
# 输入: s = "anagram", t = "nagaram"
# 输出: true

# 示例 2:
# 输入: s = "rat", t = "car"
# 输出: false

# 说明:
# 你可以假设字符串只包含小写字母。

# 进阶:
# 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s:
            return True if not t else False
        
        cnt = [0] * 26
        base = ord('a')
        for c in s:
            cnt[ord(c) - base] += 1

        for c in t:
            cnt[ord(c) - base] -= 1

        return not any(cnt)

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.isAnagram("anagram", "nagaram"))
    print(solution.isAnagram("rat", "car"))

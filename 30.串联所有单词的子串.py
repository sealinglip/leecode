#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-20 16:38:45
@LastEditors: Thomas Young
@LastEditTime: 2020-06-21 11:00:50
'''
#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
#
# 给定一个字符串 s 和一些 长度相同 的单词 words 。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。

# 注意子串要与 words 中的单词完全匹配，中间不能有其他字符 ，但不需要考虑 words 中单词串联的顺序。


# 示例 1：
# 输入：s = "barfoothefoobarman", words = ["foo", "bar"]
# 输出：[0, 9]
# 解释：
# 从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
# 输出的顺序不重要, [9, 0] 也是有效答案。

# 示例 2：
# 输入：s = "wordgoodgoodgoodbestword", words = ["word", "good", "best", "word"]
# 输出：[]

# 示例 3：
# 输入：s = "barfoofoobarthefoobarman", words = ["bar", "foo", "the"]
# 输出：[6, 9, 12]


# 提示：
# 1 <= s.length <= 10^4
# s 由小写英文字母组成
# 1 <= words.length <= 5000
# 1 <= words[i].length <= 30
# words[i] 由小写英文字母组成

# Hard
from typing import List
# @lc code=start
from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        w_len, s_len = len(words[0]), len(s)
        t_len = w_len * len(words)  # 所有词加一块的长度
        if s_len < t_len:
            return []

        requirement = Counter(words)  # 对要求的单词进行计数

        res = []
        for i in range(w_len):  # 总共过这么多轮，每轮偏移i
            l, lb = i, s_len - t_len
            while l <= lb:
                tmp_dict = dict(requirement)
                r = l + t_len
                match = True
                while r > l:
                    word = s[r - w_len: r]
                    if word not in tmp_dict or tmp_dict[word] == 0:
                        match = False
                        break
                    else:
                        tmp_dict[word] -= 1

                    r -= w_len
                if match:
                    res.append(l)
                    l += w_len
                else:  # 到这说明当前word不满足条件，所以下一个尝试点即从r开始即可
                    l = r

        return res


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.findSubstring("wordgoodgoodgoodbestword",
                                 ["word", "good", "best", "good"]))
    print(solution.findSubstring("barfoothefoobarman", ["foo", "bar"]))
    print(solution.findSubstring("wordgoodgoodgoodbestword",
                                 ["word", "good", "best", "word"]))

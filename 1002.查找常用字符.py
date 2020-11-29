#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-10-14 08:53:28
LastEditors: Thomas Young
LastEditTime: 2020-10-14 09:09:22
'''
#
# @lc app=leetcode.cn id=1002 lang=python3
#
# [1002] 查找常用字符
#
# 给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。
# 例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。
# 你可以按任意顺序返回答案。

# 示例 1：
# 输入：["bella", "label", "roller"]
# 输出：["e", "l", "l"]

# 示例 2：
# 输入：["cool", "lock", "cook"]
# 输出：["c", "o"]

# 提示：
# 1 <= A.length <= 100
# 1 <= A[i].length <= 100
# A[i][j] 是小写字母

from typing import List
# @lc code=start
from collections import Counter
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if not A:
            return []
        
        cnt = Counter(A[0])
        for i in range(1, len(A)):
            cnt1 = Counter(A[i])
            keys = list(cnt.keys())
            for c in keys:
                if c in cnt1:
                    cnt[c] = min(cnt[c], cnt1[c])
                else:
                    del cnt[c]

        res = []
        for c in cnt:
            res.extend([c] * cnt[c])
        return res
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.commonChars(["bella", "label", "roller"]))

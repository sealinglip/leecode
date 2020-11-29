#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-10-19 08:58:16
LastEditors: Thomas Young
LastEditTime: 2020-10-19 09:45:30
'''
#
# @lc app=leetcode.cn id=844 lang=python3
#
# [844] 比较含退格的字符串
#
# 给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。  # 代表退格字符。
# 注意：如果对空文本输入退格字符，文本继续为空。


# 示例 1：
# 输入：S = "ab#c", T = "ad#c"
# 输出：true
# 解释：S 和 T 都会变成 “ac”。

# 示例 2：
# 输入：S = "ab##", T = "c#d#"
# 输出：true
# 解释：S 和 T 都会变成 “”。

# 示例 3：
# 输入：S = "a##c", T = "#a#c"
# 输出：true
# 解释：S 和 T 都会变成 “c”。

# 示例 4：
# 输入：S = "a#c", T = "b"
# 输出：false
# 解释：S 会变成 “c”，但 T 仍然是 “b”。

# 提示：
# 1 <= S.length <= 200
# 1 <= T.length <= 200
# S 和 T 只含有小写字母以及字符 '#'。

# 进阶：
# 你可以用 O(N) 的时间复杂度和 O(1) 的空间复杂度解决该问题吗？

# @lc code=start
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        if S and T:
            i, j = len(S) - 1, len(T) - 1
            skipS = skipT = 0

            while i >= 0 or j >= 0:
                while i >= 0:
                    if S[i] == '#':
                        skipS += 1
                        i -= 1
                    elif skipS:
                        skipS -= 1
                        i -= 1
                    else:
                        break
                while j >= 0:
                    if T[j] == '#':
                        skipT += 1
                        j -= 1
                    elif skipT:
                        skipT -= 1
                        j -= 1
                    else:
                        break
                if i >= 0 and j >= 0:
                    if S[i] != T[j]:
                        return False
                elif i >= 0 or j >= 0:
                    return False
                    
                i -= 1
                j -= 1

            return True
        else:
            return S == T
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.backspaceCompare("nzp#o#g", "b#nzp#o#g"))
    # print(solution.backspaceCompare("ab#c", "ad#c"))
    # print(solution.backspaceCompare("ab##", "c#d#"))
    # print(solution.backspaceCompare("a##c", "#a#c"))
    # print(solution.backspaceCompare("a#c", "b"))

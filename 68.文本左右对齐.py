#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-09-04 08:41:11
LastEditors: Thomas Young
LastEditTime: 2020-09-04 10:09:27
'''
#
# @lc app=leetcode.cn id=68 lang=python3
#
# [68] 文本左右对齐
#
# 给定一个单词数组和一个长度 maxWidth，重新排版单词，使其成为每行恰好有 maxWidth 个字符，且左右两端对齐的文本。
# 你应该使用“贪心算法”来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 ' ' 填充，使得每行恰
# 好有 maxWidth 个字符。

# 要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。
# 文本的最后一行应为左对齐，且单词之间不插入额外的空格。

# 说明:
# 单词是指由非空格字符组成的字符序列。
# 每个单词的长度大于 0，小于等于 maxWidth。
# 输入单词数组 words 至少包含一个单词。

# 示例:
# 输入:
# words = ["This", "is", "an", "example", "of", "text", "justification."]
# maxWidth = 16
# 输出:
# [
#     "This    is    an",
#     "example  of text",
#     "justification.  "
# ]

# 示例 2:
# 输入:
# words = ["What", "must", "be", "acknowledgment", "shall", "be"]
# maxWidth = 16
# 输出:
# [
#     "What   must   be",
#     "acknowledgment  ",
#     "shall be        "
# ]
# 解释: 注意最后一行的格式应为 "shall be    " 而不是 "shall     be",
# 因为最后一行应为左对齐，而不是左右两端对齐。
# 第二行同样为左对齐，这是因为这行只包含一个单词。

# 示例 3:
# 输入:
# words = ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain",
#          "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"]
# maxWidth = 20
# 输出:
# [
#     "Science  is  what we",
#     "understand      well",
#     "enough to explain to",
#     "a  computer.  Art is",
#     "everything  else  we",
#     "do                  "
# ]

from typing import List
# @lc code=start
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        if not words:
            return []

        res = []

        def generateLine(start: int, end: int, space: int) -> str:
            if end - start == 1:
                return words[start] + " " * space
                
            avggap = round(space / (end - start - 1))
            delta = space - avggap * (end - start - 1)
            gap = [avggap] * (end - start - 1)

            if delta > 0:
                for i in range(delta):
                    gap[i] += 1
            elif delta < 0:
                for i in range(len(gap)-1, len(gap) - 1 + delta, -1):
                    gap[i] -= 1
            line = ""
            for i in range(len(gap)):
                line += words[start + i]
                line += " " * gap[i]
            line += words[end - 1]
            return line

        start = 0
        accumulate = -1
        i, end, wordCnt = 0, 0, len(words)
        while i < wordCnt:
            wordLen = len(words[i])
            accumulate += wordLen + 1
            if accumulate >= maxWidth:
                if accumulate > maxWidth:
                    end = i
                    accumulate -= wordLen + 1
                else:
                    end = i + 1
                res.append(generateLine(start, end, maxWidth - accumulate + end - start - 1))
                start = end
                i = end
                accumulate = -1
            else:
                i += 1

        if end < wordCnt:
            line = " ".join(words[end:])
            if len(line) < maxWidth:
                line += " " * (maxWidth - len(line))
            res.append(line)

        return res


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.fullJustify(["Don\'t", "go", "around", "saying", "the", "world", "owes", "you",
                                "a", "living;", "the", "world", "owes", "you", "nothing;", "it", "was", "here", "first."], 30))
    print(solution.fullJustify(["a"], 2))
    print(solution.fullJustify(
        ["This", "is", "an", "example", "of", "text", "justification."], 16))
    print(solution.fullJustify(
        ["What", "must", "be", "acknowledgment", "shall", "be"], 16))
    print(solution.fullJustify(
        ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain",
            "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"], 20))

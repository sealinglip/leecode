#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-11-05 08:16:37
LastEditors: Thomas Young
LastEditTime: 2020-11-05 08:40:17
'''
#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#
# 给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：

# 每次转换只能改变一个字母。
# 转换过程中的中间单词必须是字典中的单词。
# 说明:

# 如果不存在这样的转换序列，返回 0。
# 所有单词具有相同的长度。
# 所有单词只由小写字母组成。
# 字典中不存在重复的单词。
# 你可以假设 beginWord 和 endWord 是非空的，且二者不相同。

# 示例 1:
# 输入:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
# 输出: 5
# 解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# 返回它的长度 5。

# 示例 2:
# 输入:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot", "dot", "dog", "lot", "log"]
# 输出: 0
# 解释: endWord "cog" 不在字典中，所以无法进行转换。

from typing import List
from collections import defaultdict, deque
# @lc code=start
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordLen = len(beginWord)
        wordList.append(beginWord)
        # 构造hash映射，key是带一个通配符的Pattern，value是匹配词列表
        hash = defaultdict(list)
        for word in set(wordList):
            for i in range(wordLen):
                hash[word[:i] + '*' + word[i+1:]].append(word)

        visited = {beginWord: 0}  # word和level
        wordQueue = deque([(beginWord, 0)])
        while wordQueue:
            curWord, level = wordQueue.popleft()
            for i in range(wordLen):
                for word in hash[curWord[:i] + '*' + curWord[i+1:]]:
                    if word not in visited:
                        wordQueue.append((word, level + 1))
                        visited[word] = level + 1  # 表示从beginWord到word的最短距离
            # 表明从beginWord到endWord的最短距离就是level，那么再高的层次就不用遍历了
            if endWord in visited and visited[endWord] <= level:
                return visited[endWord] + 1 # + 1是长度包含起点
        return 0

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.ladderLength("hit", "cog", [
          "hot", "dot", "dog", "lot", "log", "cog"]))
    print(solution.ladderLength("hit", "cog", [
          "hot", "dot", "dog", "lot", "log"]))

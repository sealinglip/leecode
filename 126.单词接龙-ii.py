#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-11-05 08:25:17
LastEditors: Thomas Young
LastEditTime: 2020-11-05 08:31:02
'''
#
# @lc app=leetcode.cn id=126 lang=python3
#
# [126] 单词接龙 II
#
# 给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。转换需遵循如下规则：

# 每次转换只能改变一个字母。
# 转换后得到的单词必须是字典中的单词。
# 说明:

# 如果不存在这样的转换序列，返回一个空列表。
# 所有单词具有相同的长度。
# 所有单词只由小写字母组成。
# 字典中不存在重复的单词。
# 你可以假设 beginWord 和 endWord 是非空的，且二者不相同。

# 示例 1:
# 输入:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
# 输出:
# [
#     ["hit", "hot", "dot", "dog", "cog"],
#     ["hit", "hot", "lot", "log", "cog"]
# ]

# 示例 2:
# 输入:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot", "dot", "dog", "lot", "log"]
# 输出: []
# 解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。

# 提示：
# 1 <= beginWord.length <= 5
# endWord.length == beginWord.length
# 1 <= wordList.length <= 5000
# wordList[i].length == beginWord.length
# beginWord、endWord 和 wordList[i] 由小写英文字母组成
# beginWord != endWord
# wordList 中的所有单词 互不相同

# Hard
from typing import List
# @lc code=start
from collections import defaultdict, deque


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordLen = len(beginWord)
        wordList.append(beginWord)
        # 构造hash映射，key是带一个通配符的Pattern，value是匹配词列表
        hash = defaultdict(list)
        for word in set(wordList):
            for i in range(wordLen):
                hash[word[:i] + '*' + word[i+1:]].append(word)

        visited = {beginWord: 0}  # word和level
        preWords = defaultdict(list)  # 保存word的前导word
        wordQueue = deque([(beginWord, 0)])
        while wordQueue:
            curWord, level = wordQueue.popleft()
            for i in range(wordLen):
                for word in hash[curWord[:i] + '*' + curWord[i+1:]]:
                    if word not in visited:
                        wordQueue.append((word, level + 1))
                        visited[word] = level + 1  # 表示从beginWord到word的最短距离
                    if visited[word] == level + 1:  # 加这个判断才能求出全部的最短路径
                        preWords[word].append(curWord)
            # 表明从beginWord到endWord的最短距离就是level，那么再高的层次就不用遍历了
            if endWord in visited and visited[endWord] <= level:
                break
        if endWord in visited:
            # 从endWord 倒查 直到 找到beginWord
            res = [[endWord]]
            while res[0][0] != beginWord:
                res = [[preWord] + w for w in res for preWord in preWords[w[0]]]
            return res
        else:
            return []
# @lc code=end

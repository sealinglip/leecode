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
# 字典 wordList 中从单词 beginWord 和 endWord 的 转换序列 是一个按下述规格形成的序列 beginWord -> s1 -> s2 -> ... -> sk：

# 每一对相邻的单词只差一个字母。
# 对于 1 <= i <= k 时，每个 si 都在 wordList 中。注意， beginWord 不需要在 wordList 中。
# sk == endWord
# 给你两个单词 beginWord 和 endWord 和一个字典 wordList ，返回 从 beginWord 到 endWord 的 最短转换序列 中的 单词数目 。如果不存在这样的转换序列，返回 0 。


# 示例 1：
# 输入：beginWord = "hit", endWord = "cog", wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
# 输出：5
# 解释：一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog", 返回它的长度 5。

# 示例 2：
# 输入：beginWord = "hit", endWord = "cog", wordList = ["hot", "dot", "dog", "lot", "log"]
# 输出：0
# 解释：endWord "cog" 不在字典中，所以无法进行转换。


# 提示：
# 1 <= beginWord.length <= 10
# endWord.length == beginWord.length
# 1 <= wordList.length <= 5000
# wordList[i].length == beginWord.length
# beginWord、endWord 和 wordList[i] 由小写英文字母组成
# beginWord != endWord
# wordList 中的所有字符串 互不相同

# Hard
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
                return visited[endWord] + 1  # + 1是长度包含起点
        return 0

# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.ladderLength("hit", "cog", [
          "hot", "dot", "dog", "lot", "log", "cog"]))
    print(solution.ladderLength("hit", "cog", [
          "hot", "dot", "dog", "lot", "log"]))

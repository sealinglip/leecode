#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2021-09-16 20:12:48
LastEditors: Thomas Young
LastEditTime: 2021-09-16 20:27:16
'''
#
# @lc app=leetcode.cn id=212 lang=python3
#
# [212] 单词搜索 II
#
# 给定一个 m x n 二维字符网格 board 和一个单词（字符串）列表 words，找出所有同时在二维网格和字典中出现的单词。
# 单词必须按照字母顺序，通过 相邻的单元格 内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。


# 示例 1：
# 输入：board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]], words = ["oath", "pea", "eat", "rain"]
# 输出：["eat", "oath"]

# 示例 2：
# 输入：board = [["a", "b"], ["c", "d"]], words = ["abcb"]
# 输出：[]

# 提示：
# m == board.length
# n == board[i].length
# 1 <= m, n <= 12
# board[i][j] 是一个小写英文字母
# 1 <= words.length <= 3 * 10^4
# 1 <= words[i].length <= 10
# words[i] 由小写英文字母组成
# words 中的所有字符串互不相同

from typing import List
# @lc code=start
from collections import defaultdict
class Trie:
    def __init__(self) -> None:
        self.children = defaultdict(Trie)
        self.isWord = False

    def insert(self, word: str) -> None:
        cur = self
        for c in word:
            cur = cur.children[c]
        cur.isWord = True
        cur.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        trie = Trie()
        for w in words:
            trie.insert(w)

        res = set()
        def dfs(node: Trie, x:int, y:int):
            if board[x][y] not in node.children:
                return

            c = board[x][y]
            node = node.children[c]
            if node.isWord:
                res.add(node.word)

            board[x][y] = "*"
            for x2, y2 in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= x2 < m and 0 <= y2 < n:
                    dfs(node, x2, y2)
            board[x][y] = c
        
        for i in range(m):
            for j in range(n):
                dfs(trie, i, j)
        return list(res)
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.findWords([["o", "a", "a", "n"], ["e", "t", "a", "e"], [
          "i", "h", "k", "r"], ["i", "f", "l", "v"]], ["oath", "pea", "eat", "rain"]))
    print(solution.findWords([["a", "b"], ["c", "d"]], ["abcb"]))

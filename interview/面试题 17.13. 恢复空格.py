#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-07-09 11:23:39
@LastEditors: Thomas Young
@LastEditTime: 2020-07-09 14:35:22
'''
# 哦，不！你不小心把一个长篇文章中的空格、标点都删掉了，并且大写也弄成了小写。
# 像句子"I reset the computer. It still didn’t boot!"已经变成了"iresetthecomputeritstilldidntboot"。
# 在处理标点符号和大小写之前，你得先把它断成词语。当然了，你有一本厚厚的词典dictionary，不过，有些词没在词典里。
# 假设文章用sentence表示，设计一个算法，把文章断开，要求未识别的字符最少，返回未识别的字符数。
# 注意：本题相对原题稍作改动，只需返回未识别的字符数

# 示例：

# 输入：
# dictionary = ["looked", "just", "like", "her", "brother"]
# sentence = "jesslookedjustliketimherbrother"
# 输出： 7
# 解释： 断句后为"jess looked just like tim her brother"，共7个未识别字符。
# 提示：

# 0 <= len(sentence) <= 1000
# dictionary中总字符数不超过 150000。
# 你可以认为dictionary和sentence中只包含小写字母。

from typing import List, Set

class Trie:
    def __init__(self):
        self.child = {}
        self.wordEnd = False

class Solution:
    def createTree(self, dictionary: Set[str]):
        self.root = Trie()
        for word in dictionary:
            node = self.root
            for c in word:
                if c not in node.child:
                    node.child[c] = Trie()
                node = node.child[c]
            node.wordEnd = True

    def respace(self, dictionary: List[str], sentence: str) -> int:
        if not sentence:
            return 0
        # 去掉不在字符串中的单词
        dictionary = set([w for w in dictionary if sentence.find(w) != -1])
        self.createTree(dictionary)

        sLen = len(sentence)
        dp = [0 for i in range(sLen + 1)] # dp[i] 代表第i个字符（含）之后不可识别的字符数
        for i in range(sLen - 1, -1, -1):
            dp[i] = dp[i + 1] + 1 # 默认为本字符未匹配的最坏情况
            node = self.root
            for j in range(i, sLen):
                if sentence[j] in node.child:
                    node = node.child[sentence[j]]
                    if node.wordEnd:
                        dp[i] = min(dp[i], dp[j + 1])
                else:
                    break
                
        return dp[0]

if __name__ == "__main__":
    solution = Solution()
    print(solution.respace(["ouf", "uucuocucoouoffcpuuf", "pf", "o", "fofopupoufuofffffocpocfccuofuupupcouocpocoooupcuu", "cf", "cffooccccuoocpfupuucufoocpocucpuouofffpoupu", "opoffuoofpupcpfouoouufpcuocufo", "fopuupco", "upocfucuucfucofufu", "ufoccopopuouccupooc", "fffu", "uuopuccfocopooupooucfoufop", "occ", "ppfcuu", "o", "fpp", "o", "oououpuccuppuococcpoucccffcpcucoffupcoppoc", "ufc", "coupo", "ufuoufofopcpfoufoouppffofffuupfco", "focfcfcfcfpuouoccupfccfpcooup", "ffupfffccpffufuuo", "cufoupupppocou", "upopupopccffuofpcopouofpoffopcfcuooocppofofuuc", "oo", "pccc", "oupupcccppuuucuuouocu", "fuop", "ppuocfuppff", "focofooffpfcpcupupuuooufu", "uofupoocpf", "opufcuffopcpcfcufpcpufuupffpp", "f", "opffp", "fpccopc"],
                           "fofopupoufuofffffocpocfccuofuupupcouocpocoooupcuufffufffufpccopc"))
    print(solution.respace(["looked", "just", "like",
                            "her", "brother"], 'jesslookedjustliketimherbrother'))

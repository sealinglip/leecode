#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2020-10-12 08:58:59
LastEditors: Thomas Young
LastEditTime: 2020-10-13 17:33:56
'''
#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原IP地址
#
# 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
# 有效的 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。
# 例如："0.1.2.201" 和 "192.168.1.1" 是 有效的 IP 地址，但是 "0.011.255.245"、
# "192.168.1.312" 和 "192.168@1.1" 是 无效的 IP 地址。

# 示例 1：
# 输入：s = "25525511135"
# 输出：["255.255.11.135", "255.255.111.35"]

# 示例 2：
# 输入：s = "0000"
# 输出：["0.0.0.0"]

# 示例 3：
# 输入：s = "1111"
# 输出：["1.1.1.1"]

# 示例 4：
# 输入：s = "010010"
# 输出：["0.10.0.10", "0.100.1.0"]

# 示例 5：
# 输入：s = "101023"
# 输出：["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]

# 提示：
# 0 <= s.length <= 3000
# s 仅由数字组成

from typing import List
# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if not s:
            return []
        
        res = []
        
        def dfs(ca: str, split: List[str]):
            """递归求解

            Args:
                ca (str): 尝试分解的字符串
                split (List[str]): 已经切分的前缀数组
            """
            rest = 4 - len(split)
            l = len(ca)
            if rest == 0 and ca == '':
                res.append(".".join(split))
                return
            elif l > 3 * rest or l == 0: # 合法的ip不能这么长或者ca为空
                return
            
            # 尝试切一位
            dfs(ca[1:], split + [ca[0]])
            # 尝试切两位
            if ca[0] != '0' and l > 1:
                dfs(ca[2:], split + [ca[:2]])
                # 尝试切三位
                if ca[:3] < '256' and l > 2:
                    dfs(ca[3:], split + [ca[:3]])

        dfs(s, [])
        return res 
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.restoreIpAddresses("25525511135"))
    print(solution.restoreIpAddresses("0000"))
    print(solution.restoreIpAddresses("1111"))
    print(solution.restoreIpAddresses("010010"))
    print(solution.restoreIpAddresses("101023"))

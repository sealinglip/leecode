#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-22 09:23:20
@LastEditors: Thomas Young
@LastEditTime: 2020-06-22 16:14:01
'''
from collections import Counter

class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        if not pattern:
            return False if value else True
        
        p_len, v_len = len(pattern), len(value)
        counter = Counter(pattern)
        if len(counter) == 1: # 只有一种模式
            a_len = v_len // p_len
            if a_len * p_len != v_len:
                return False
            else:
                a, i = value[0:a_len], a_len
                while i < v_len:
                    if value[i : i + a_len] != a:
                        return False
                    i += a_len
                return True
        else:
            a_len_max = v_len // counter['a'] # 模式a匹配的子串最大可能长度
            for a_len in range(a_len_max + 1):
                b_len = (v_len - counter['a'] * a_len) // counter['b']
                # 如果不能被整除，那么试下一种可能
                if a_len * counter['a'] + b_len * counter['b'] != v_len:
                    continue
                # 验证是不是靠谱
                a, b, i = '', '', 0
                match = True
                for p in pattern:
                    if p == 'a':
                        if a:
                            if a != value[i : i + a_len]:
                                match = False
                                break
                        elif a_len != 0:
                            a = value[i : i + a_len]
                    else:
                        if b:
                            if b != value[i : i + b_len]:
                                match = False
                                break
                        elif b_len != 0:
                            b = value[i : i + b_len]
                            
                    i += a_len if p == 'a' else b_len
                if match and a != b:
                    return True

            return False


if __name__ == "__main__":
    solution = Solution()
    print(solution.patternMatching("abba", "dogcatcatdog"))
    print(solution.patternMatching("abba", "dogcatcatfish"))
    print(solution.patternMatching("aaaa", "dogcatcatdog"))
    print(solution.patternMatching("abba", "dogdogdogdog"))

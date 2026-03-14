#
# @lc app=leetcode.cn id=756 lang=python3
#
# [756] 金字塔转换矩阵
#
# https://leetcode.cn/problems/pyramid-transition-matrix/description/
#
# algorithms
# Medium (49.74%)
# Likes:    108
# Dislikes: 0
# Total Accepted:    10.9K
# Total Submissions: 20.6K
# Testcase Example:  '"BCD"\n["BCC","CDE","CEA","FFF"]'
#
# 你正在把积木堆成金字塔。每个块都有一个颜色，用一个字母表示。每一行的块比它下面的行 少一个块 ，并且居中。
# 
# 为了使金字塔美观，只有特定的 三角形图案 是允许的。一个三角形的图案由 两个块 和叠在上面的 单个块 组成。模式是以三个字母字符串的列表形式
# allowed 给出的，其中模式的前两个字符分别表示左右底部块，第三个字符表示顶部块。
# 
# 例如，"ABC" 表示一个三角形图案，其中一个 “C” 块堆叠在一个 'A' 块(左)和一个 'B' 块(右)之上。请注意，这与 "BAC" 不同，"B"
# 在左下角，"A" 在右下角。
# 
# 你从作为单个字符串给出的底部的一排积木 bottom 开始，必须 将其作为金字塔的底部。
# 
# 在给定 bottom 和 allowed 的情况下，如果你能一直构建到金字塔顶部，使金字塔中的 每个三角形图案 都是在 allowed 中的，则返回
# true ，否则返回 false 。
# 
# 
# 示例 1：
# 输入：bottom = "BCD", allowed = ["BCC","CDE","CEA","FFF"]
# 输出：true
# 解释：允许的三角形图案显示在右边。
# 从最底层(第 3 层)开始，我们可以在第 2 层构建“CE”，然后在第 1 层构建“E”。
# 金字塔中有三种三角形图案，分别是 “BCC”、“CDE” 和 “CEA”。都是允许的。
# 
# 示例 2：
# 输入：bottom = "AAAA", allowed = ["AAB","AAC","BCD","BBE","DEF"]
# 输出：false
# 解释：允许的三角形图案显示在右边。
# 从最底层(即第 4 层)开始，创造第 3 层有多种方法，但如果尝试所有可能性，你便会在创造第 1 层前陷入困境。
# 
# 
# 提示：
# 2 <= bottom.length <= 6
# 0 <= allowed.length <= 216
# allowed[i].length == 3
# 所有输入字符串中的字母来自集合 {'A', 'B', 'C', 'D', 'E', 'F'}。
# allowed 中所有值都是 唯一的
# 
# 复习
#

from collections import defaultdict
from functools import cache
from typing import Iterable, List
# @lc code=start
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        pattern = defaultdict(set)
        for a in allowed:
            pattern[a[:2]].add(a[2:])

        # dfs
        @cache
        def dfs(row: str) -> bool:
            if len(row) == 1: # 已经到顶
                return True
            
            return any(dfs(upperRow) for upperRow in permute(row, [], 0))
        
        def permute(row: str, arr: List[str], idx: int) -> Iterable[str]:
            if idx + 1 == len(row):
                yield "".join(arr)
            else:
                for ca in pattern[row[idx] + row[idx+1]]:
                    arr.append(ca)
                    for p in permute(row, arr, idx+1):
                        yield p
                    arr.pop()

        return dfs(bottom)
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.pyramidTransition("ABBBBA", ["ACA","ACF","ACE","ACD","ABA","ABF","ABE","ABD","FCA","FCF","FCE","FCD","FBA","FBF","FBE","FBD","ECA","ECF","ECE","ECD","EBA","EBF","EBE","EBD","DCA","DCF","DCE","DCD","DBA","DBF","DBE","DBD","CAA","CAF","CAE","CAD","CFA","CFF","CFE","CFD","CEA","CEF","CEE","CED","CDA","CDF","CDE","CDD","BAA","BAF","BAE","BAD","BFA","BFF","BFE","BFD","BEA","BEF","BEE","BED","BDA","BDF","BDE","BDD","CCA","CCF","CCE","CCD","CBA","CBF","CBE","CBD","BCA","BCF","BCE","BCD","BBA","BBF","BBE","BBD","CCC","CCB","CBC","CBB","BCC","BCB","BBC","BBB"])) # False
    print(solution.pyramidTransition("BCD", ["BCC","CDE","CEA","FFF"])) # True
    print(solution.pyramidTransition("AAAA", ["AAB","AAC","BCD","BBE","DEF"])) # False

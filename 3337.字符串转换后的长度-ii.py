#
# @lc app=leetcode.cn id=3337 lang=python3
#
# [3337] 字符串转换后的长度 II
#
# https://leetcode.cn/problems/total-characters-in-string-after-transformations-ii/description/
#
# algorithms
# Hard (44.56%)
# Likes:    14
# Dislikes: 0
# Total Accepted:    5.6K
# Total Submissions: 9.8K
# Testcase Example:  '"abcyy"\n2\n[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]'
#
# 给你一个由小写英文字母组成的字符串 s，一个整数 t 表示要执行的 转换 次数，以及一个长度为 26 的数组 nums。每次 转换
# 需要根据以下规则替换字符串 s 中的每个字符：
# 
# 
# 将 s[i] 替换为字母表中后续的 nums[s[i] - 'a'] 个连续字符。例如，如果 s[i] = 'a' 且 nums[0] = 3，则字符
# 'a' 转换为它后面的 3 个连续字符，结果为 "bcd"。
# 如果转换超过了 'z'，则 回绕 到字母表的开头。例如，如果 s[i] = 'y' 且 nums[24] = 3，则字符 'y' 转换为它后面的 3
# 个连续字符，结果为 "zab"。
# 
# 返回 恰好 执行 t 次转换后得到的字符串的 长度。
# 
# 由于答案可能非常大，返回其对 10^9 + 7 取余的结果。
# 
# 
# 示例 1：
# 输入： s = "abcyy", t = 2, nums =
# [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]
# 输出： 7
# 解释：
# 第一次转换 (t = 1)
# 'a' 变为 'b' 因为 nums[0] == 1
# 'b' 变为 'c' 因为 nums[1] == 1
# 'c' 变为 'd' 因为 nums[2] == 1
# 'y' 变为 'z' 因为 nums[24] == 1
# 'y' 变为 'z' 因为 nums[24] == 1
# 第一次转换后的字符串为: "bcdzz"
# 
# 第二次转换 (t = 2)
# 'b' 变为 'c' 因为 nums[1] == 1
# 'c' 变为 'd' 因为 nums[2] == 1
# 'd' 变为 'e' 因为 nums[3] == 1
# 'z' 变为 'ab' 因为 nums[25] == 2
# 'z' 变为 'ab' 因为 nums[25] == 2
# 第二次转换后的字符串为: "cdeabab"
# 字符串最终长度： 字符串为 "cdeabab"，长度为 7 个字符。
# 
# 
# 示例 2：
# 输入： s = "azbk", t = 1, nums =
# [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
# 输出： 8
# 解释：
# 第一次转换 (t = 1)
# 'a' 变为 'bc' 因为 nums[0] == 2
# 'z' 变为 'ab' 因为 nums[25] == 2
# 'b' 变为 'cd' 因为 nums[1] == 2
# 'k' 变为 'lm' 因为 nums[10] == 2
# 第一次转换后的字符串为: "bcabcdlm"
# 字符串最终长度： 字符串为 "bcabcdlm"，长度为 8 个字符。
# 
# 
# 提示：
# 1 <= s.length <= 10^5
# s 仅由小写英文字母组成。
# 1 <= t <= 10^9
# nums.length == 26
# 1 <= nums[i] <= 25
# 
#

from typing import List
# @lc code=start
MOD = 10 ** 9 + 7
L = 26

class Matrix:
    def __init__(self, clone: "Matrix" = None) -> None:
        self.a = [[0] * L for _ in range(L)]
        if clone:
            for i in range(L):
                for j in range(L):
                    self.a[i][j] = clone.a[i][j]

    def __mul__(self, other: "Matrix") -> "Matrix":
        res = Matrix()
        for i in range(L):
            for j in range(L):
                res.a[i][j] = sum(self.a[i][k] * other.a[k][j] for k in range(L)) % MOD
        return res
    
    def quickmul(self, e: int) -> "Matrix":
        res = Matrix.I()
        cur = Matrix(self)
        while e:
            if e & 1:
                res = cur * res
            cur *= cur
            e >>= 1
        return res
    
    @staticmethod
    def I() -> "Matrix":
        eye = Matrix()
        for i in range(L):
            eye.a[i][i] = 1
        return eye

class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        # 构建转换矩阵
        trans = Matrix()
        for i in range(L):
            for j in range(1, nums[i] + 1):
                trans.a[(i+j) % L][i] = 1

        trans = trans.quickmul(t)

        vec = [0] * L
        for c in s:
            vec[ord(c) - ord('a')] += 1

        res = 0
        for i in range(L):
            res = (res + sum(trans.a[i][j] * vec[j] for j in range(L))) % MOD
        return res

        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthAfterTransformations("abcyy", 2, [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2])) # 7
    print(solution.lengthAfterTransformations("azbk", 1, [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2])) # 8

# 给你一个整数 n 和一个二维数组 requirements ，其中 requirements[i] = [endi, cnti] 表示这个要求中的末尾下标和 逆序对 的数目。

# 整数数组 nums 中一个下标对 (i, j) 如果满足以下条件，那么它们被称为一个 逆序对 ：

# i < j 且 nums[i] > nums[j]
# 请你返回 [0, 1, 2, ..., n - 1] 的 
# 排列
#  perm 的数目，满足对 所有 的 requirements[i] 都有 perm[0..endi] 恰好有 cnti 个逆序对。

# 由于答案可能会很大，将它对 109 + 7 取余 后返回。


# 示例 1：
# 输入：n = 3, requirements = [[2,2],[0,0]]
# 输出：2
# 解释：
# 两个排列为：
# [2, 0, 1]
# 前缀 [2, 0, 1] 的逆序对为 (0, 1) 和 (0, 2) 。
# 前缀 [2] 的逆序对数目为 0 个。
# [1, 2, 0]
# 前缀 [1, 2, 0] 的逆序对为 (0, 2) 和 (1, 2) 。
# 前缀 [1] 的逆序对数目为 0 个。

# 示例 2：
# 输入：n = 3, requirements = [[2,2],[1,1],[0,0]]
# 输出：1
# 解释：
# 唯一满足要求的排列是 [2, 0, 1] ：
# 前缀 [2, 0, 1] 的逆序对为 (0, 1) 和 (0, 2) 。
# 前缀 [2, 0] 的逆序对为 (0, 1) 。
# 前缀 [2] 的逆序对数目为 0 。

# 示例 3：
# 输入：n = 2, requirements = [[0,0],[1,0]]
# 输出：1
# 解释：
# 唯一满足要求的排列为 [0, 1] ：
# 前缀 [0] 的逆序对数目为 0 。
# 前缀 [0, 1] 的逆序对为 (0, 1) 。
 
# 提示：
# 2 <= n <= 300
# 1 <= requirements.length <= n
# requirements[i] = [endi, cnti]
# 0 <= endi <= n - 1
# 0 <= cnti <= 400
# 输入保证至少有一个 i 满足 endi == n - 1 。
# 输入保证所有的 endi 互不相同。

# Hard
# 复习

from functools import cache
from typing import List
class Solution:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7

        # 动规
        # 定义dp(i,j)为i+1个不同的数组成的数组，恰好有j个逆序对的排列数
        # 考虑最后一个数是整个数组中的最大值、次大值、……，最小值
        # 如果是最大值，本身对逆序对没贡献，逆序对只能靠前i个数
        # 如果是次大值，贡献一对，
        # 依次类推，如果是最小值，贡献i对
        # 那么得到状态转移方程：
        # dp(i, j) = sum(dp(i-1, j-k) for k in range(min(i,j)))
        # 边界条件 dp(0,0) = 1, dp(0, x) = 0 if x > 0

        reqMap = {0: 0}
        for e, c in requirements:
            reqMap[e] = c
        if reqMap[0]: # dp(0, x) = 0 if x > 0
            return 0
        
        @cache
        def dfs(e: int, c: int) -> int:
            if c < 0:
                return 0
            if e == 0:
                return 1
            if e - 1 in reqMap:
                r = reqMap[e-1]
                if r <= c <= e + r:
                    return dfs(e-1, r)
                else:
                    return 0
            else:
                if c > e:
                    return (dfs(e, c-1) - dfs(e-1, c-1-e) + dfs(e-1, c)) % MOD
                else:
                    return (dfs(e, c-1) + dfs(e-1, c)) % MOD
                
        return dfs(n-1, reqMap[n-1])



if __name__ == "__main__":
    solution = Solution()
    print(solution.numberOfPermutations(3, [[2,2],[0,0]])) # 2
    print(solution.numberOfPermutations(3, [[2,2],[1,1],[0,0]])) # 1
    print(solution.numberOfPermutations(2, [[0,0],[1,0]])) # 1

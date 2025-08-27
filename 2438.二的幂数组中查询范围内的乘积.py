#
# @lc app=leetcode.cn id=2438 lang=python3
#
# [2438] 二的幂数组中查询范围内的乘积
#
# https://leetcode.cn/problems/range-product-queries-of-powers/description/
#
# algorithms
# Medium (44.37%)
# Likes:    32
# Dislikes: 0
# Total Accepted:    10.8K
# Total Submissions: 22.7K
# Testcase Example:  '15\n[[0,1],[2,2],[0,3]]'
#
# 给你一个正整数 n ，你需要找到一个下标从 0 开始的数组 powers ，它包含 最少 数目的 2 的幂，且它们的和为 n 。powers 数组是
# 非递减 顺序的。根据前面描述，构造 powers 数组的方法是唯一的。
# 
# 同时给你一个下标从 0 开始的二维整数数组 queries ，其中 queries[i] = [lefti, righti] ，其中 queries[i]
# 表示请你求出满足 lefti <= j <= righti 的所有 powers[j] 的乘积。
# 
# 请你返回一个数组 answers ，长度与 queries 的长度相同，其中 answers[i]是第 i
# 个查询的答案。由于查询的结果可能非常大，请你将每个 answers[i] 都对 10^9 + 7 取余 。
# 
# 
# 示例 1：
# 输入：n = 15, queries = [[0,1],[2,2],[0,3]]
# 输出：[2,4,64]
# 解释：
# 对于 n = 15 ，得到 powers = [1,2,4,8] 。没法得到元素数目更少的数组。
# 第 1 个查询的答案：powers[0] * powers[1] = 1 * 2 = 2 。
# 第 2 个查询的答案：powers[2] = 4 。
# 第 3 个查询的答案：powers[0] * powers[1] * powers[2] * powers[3] = 1 * 2 * 4 * 8 = 64 。
# 每个答案对 10^9 + 7 得到的结果都相同，所以返回 [2,4,64] 。
# 
# 示例 2：
# 输入：n = 2, queries = [[0,0]]
# 输出：[2]
# 解释：
# 对于 n = 2, powers = [2] 。
# 唯一一个查询的答案是 powers[0] = 2 。答案对 10^9 + 7 取余后结果相同，所以返回 [2] 。
# 
# 
# 提示：
# 1 <= n <= 10^9
# 1 <= queries.length <= 10^5
# 0 <= starti <= endi < powers.length
# 
# 
#

from typing import List
# @lc code=start
from itertools import accumulate
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10 ** 9 + 7
        # 没必要真的把power算出来，可以把power转换为对2求对数的数组（即只存幂）
        p = [i for i, x in enumerate(bin(n)[:1:-1]) if x == '1']
        preSum = [0] + list(accumulate(p)) # 转为前缀和

        res = []
        for l, r in queries:
            pSum = preSum[r+1] - preSum[l]
            res.append((1 << pSum) % MOD)
        return res
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.productQueries(15, [[0,1],[2,2],[0,3]])) # [2,4,64]
    print(solution.productQueries(2, [[0,0]])) # [2]
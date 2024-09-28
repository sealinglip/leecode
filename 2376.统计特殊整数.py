#
# @lc app=leetcode.cn id=2376 lang=python3
#
# [2376] 统计特殊整数
#
# 如果一个正整数每一个数位都是 互不相同 的，我们称它是 特殊整数 。

# 给你一个 正 整数 n ，请你返回区间 [1, n] 之间特殊整数的数目。

# 示例 1：
# 输入：n = 20
# 输出：19
# 解释：1 到 20 之间所有整数除了 11 以外都是特殊整数。所以总共有 19 个特殊整数。

# 示例 2：
# 输入：n = 5
# 输出：5
# 解释：1 到 5 所有整数都是特殊整数。

# 示例 3：
# 输入：n = 135
# 输出：110
# 解释：从 1 到 135 总共有 110 个整数是特殊整数。
# 不特殊的部分数字为：22 ，114 和 131 。
 

# 提示：
# 1 <= n <= 2 * 10^9

# Hard

# @lc code=start
from functools import cache

class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        # 数位DP
        # 将n转成字符串
        s = str(n)

        @cache
        def dfs(pos: int, state: int, limit: bool, filled: bool) -> int:
            """
            pos: 第pos个数位（从左到右）
            state: 选过的数字集合
            limit: 当前位选择是否受限。true，则当前位最大为s[pos]；false，则当前位最大为9
            filled: 表示前面的数位是否已经填了数字。true，表示前面填了，当前位也必须填；false，表示前面没填，当前位也可不填
            return： 构造第pos位及之后所有数位的合法方案数
            """
            if pos == len(s):
                # 排列结束，判断当前方案是否为特殊整数，‘是’返回1，‘否’返回0
                # 从未填过数不算合法方案数
                return int(filled)
            
            res = 0
            if not filled:
                # 当前位可以跳过，那么直接叠加跳过当前位的合法方案数
                res = dfs(pos+1, state, False, False)

            # 如果前一位没有填数字，则最小为1（不能含前导0）；否则为0
            minX = 0 if filled else 1
            # 如果选择受限，则最大为s[pos]；否则为9
            maxX = int(s[pos]) if limit else 9

            # 枚举可选择的数字
            for x in range(minX, maxX + 1):
                if (state >> x) & 1 == 0:
                    # 这个数还没被选过
                    res += dfs(pos + 1, state | (1 << x), limit and x == maxX, True)

            return res

        return dfs(0, 0, True, False)
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.countSpecialNumbers(20)) # 19
    print(solution.countSpecialNumbers(5)) # 5
    print(solution.countSpecialNumbers(135)) # 110

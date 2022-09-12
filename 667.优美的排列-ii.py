#
# @lc app=leetcode.cn id=667 lang=python3
#
# [667] 优美的排列 II
#
# 给你两个整数 n 和 k ，请你构造一个答案列表 answer ，该列表应当包含从 1 到 n 的 n 个不同正整数，并同时满足下述条件：

# 假设该列表是 answer = [a1, a2, a3, ..., an] ，那么列表 [ | a1 - a2|, | a2 - a3|, | a3 - a4|, ..., | an-1 - an|] 中应该有且仅有 k 个不同整数。
# 返回列表 answer 。如果存在多种答案，只需返回其中 任意一种 。


# 示例 1：
# 输入：n = 3, k = 1
# 输出：[1, 2, 3]
# 解释：[1, 2, 3] 包含 3 个范围在 1-3 的不同整数，并且[1, 1] 中有且仅有 1 个不同整数：1

# 示例 2：
# 输入：n = 3, k = 2
# 输出：[1, 3, 2]
# 解释：[1, 3, 2] 包含 3 个范围在 1-3 的不同整数，并且[2, 1] 中有且仅有 2 个不同整数：1 和 2


# 提示：
# 1 <= k < n <= 10^4

from typing import List
# @lc code=start


class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        # 如果按[1, 2, ..., n]这样构造呢，差值只有一种
        # 如果按[1, n, 2, n-1, ..., ]这样构造呢，差值有n-1种
        # 所以k小于n的情况都是可以构造出来的
        # 构造方法可以通过摆动法先搞出k-1种不同来，后续剩余的数字都升序排列或降序排列（取决于前面的state
        res = []
        l = 1
        r = n
        accu = 0
        state = 0  # 0 动左边界，1 动右边界
        while l < r and accu < k:
            if state == 0:
                res.append(l)
                l += 1
            else:
                res.append(r)
                r -= 1
            state = 1 - state
            accu += 1

        if l <= r:
            if state:
                res.extend(range(l, r+1))
            else:
                res.extend(range(r, l-1, -1))

        return res


# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.constructArray(3, 1))  # [1, 2, 3]
    print(solution.constructArray(3, 2))  # [1, 3, 2]
    print(solution.constructArray(4, 2))  # [1, 4, 3, 2]
    print(solution.constructArray(4, 3))  # [1, 4, 2, 3]
    print(solution.constructArray(4, 1))  # [1, 2, 3, 4]

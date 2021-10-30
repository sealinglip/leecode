#
# @lc app=leetcode.cn id=869 lang=python3
#
# [869] 重新排序得到 2 的幂
#
# 给定正整数 N ，我们按任何顺序（包括原始顺序）将数字重新排序，注意其前导数字不能为零。

# 如果我们可以通过上述方式得到 2 的幂，返回 true；否则，返回 false。


# 示例 1：
# 输入：1
# 输出：true

# 示例 2：
# 输入：10
# 输出：false

# 示例 3：
# 输入：16
# 输出：true

# 示例 4：
# 输入：24
# 输出：false

# 示例 5：
# 输入：46
# 输出：true


# 提示：
# 1 <= N <= 10 ^ 9

from typing import Tuple
# @lc code=start


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        # 10 ^ 9 < 2 ^ 30
        # 把2^30之内2的幂的数字组合存起来
        def countDigit(x: int) -> Tuple[int]:
            cnt = [0] * 10
            while x:
                cnt[x % 10] += 1
                x //= 10
            return tuple(cnt)

        powerCache = set([countDigit(1 << i) for i in range(30)])
        return countDigit(n) in powerCache

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.reorderedPowerOf2(1))  # True
    print(solution.reorderedPowerOf2(10))  # False
    print(solution.reorderedPowerOf2(16))  # True
    print(solution.reorderedPowerOf2(24))  # False
    print(solution.reorderedPowerOf2(46))  # True

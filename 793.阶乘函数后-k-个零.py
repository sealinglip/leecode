#
# @lc app=leetcode.cn id=793 lang=python3
#
# [793] 阶乘函数后 K 个零
#
# f(x) 是 x! 末尾是 0 的数量。回想一下 x! = 1 * 2 * 3 * ... * x，且 0! = 1 。

# 例如， f(3) = 0 ，因为 3! = 6 的末尾没有 0 ；而 f(11) = 2 ，因为 11! = 39916800 末端有 2 个 0 。
# 给定 k，找出返回能满足 f(x) = k 的非负整数 x 的数量。


# 示例 1：
# 输入：k = 0
# 输出：5
# 解释：0!, 1!, 2!, 3!, 和 4! 均符合 k = 0 的条件。

# 示例 2：
# 输入：k = 5
# 输出：0
# 解释：没有匹配到这样的 x!，符合 k = 5 的条件。

# 示例 3:
# 输入: k = 3
# 输出: 5

# 提示:
# 0 <= k <= 10^9

# Hard

# @lc code=start
class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        # 结尾有几个零，就是数经过的5和10的数量，每过一个5的倍数，就加一个0，每过一个25的倍数，就再加一个0，以此类推
        # 所以k的取值范围并不是连续的整数
        # 本方法返回值要么是5，要么是0，即，如果能找到满足条件的x，那么至少能找到5个；要么就是1个也找不到
        # 设满足f(x) = k 的最小x为x0，那么x0 % 5 == 0
        # x0 // 5 + x0 // 25 + ... = k，等比数列求和有 极限情况下 x0 * (1 / 4) = k
        # 4 * k < x0 <= 5 * k
        # 如此，则可用二分查找法了

        def zeroCnt(x: int) -> int:
            '''
            x! 末尾的0个数
            '''
            cnt = 0
            while x:
                x //= 5
                cnt += x
            return cnt

        lb, rb = 4 * k, 5 * k
        while lb <= rb:
            mid = (lb + rb) >> 1
            zc = zeroCnt(mid)
            if zc == k:
                return 5
            elif zc < k:
                lb = mid + 1
            else:
                rb = mid - 1

        return 0


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.preimageSizeFZF(0))  # 5
    print(solution.preimageSizeFZF(5))  # 0
    print(solution.preimageSizeFZF(3))  # 5

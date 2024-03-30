#
# @lc app=leetcode.cn id=1969 lang=python3
#
# [1969] 数组元素的最小非零乘积
#
# 给你一个正整数 p 。你有一个下标从 1 开始的数组 nums ，这个数组包含范围 [1, 2^p - 1] 内所有整数的二进制形式（两端都 包含）。你可以进行以下操作 任意 次：

# 从 nums 中选择两个元素 x 和 y  。
# 选择 x 中的一位与 y 对应位置的位交换。对应位置指的是两个整数 相同位置 的二进制位。
# 比方说，如果 x = 1101 且 y = 0011 ，交换右边数起第 2 位后，我们得到 x = 1111 和 y = 0001 。

# 请你算出进行以上操作 任意次 以后，nums 能得到的 最小非零 乘积。将乘积对 10^9 + 7 取余 后返回。

# 注意：答案应为取余 之前 的最小值。


# 示例 1：
# 输入：p = 1
# 输出：1
# 解释：nums = [1] 。
# 只有一个元素，所以乘积为该元素。

# 示例 2：
# 输入：p = 2
# 输出：6
# 解释：nums = [01, 10, 11] 。
# 所有交换要么使乘积变为 0 ，要么乘积与初始乘积相同。
# 所以，数组乘积 1 * 2 * 3 = 6 已经是最小值。

# 示例 3：
# 输入：p = 3
# 输出：1512
# 解释：nums = [001, 010, 011, 100, 101, 110, 111]
# - 第一次操作中，我们交换第二个和第五个元素最左边的数位。
#     - 结果数组为 [001, 110, 011, 100, 001, 110, 111] 。
# - 第二次操作中，我们交换第三个和第四个元素中间的数位。
#     - 结果数组为 [001, 110, 001, 110, 001, 110, 111] 。
# 数组乘积 1 * 6 * 1 * 6 * 1 * 6 * 7 = 1512 是最小乘积。
 

# 提示：
# 1 <= p <= 60

# @lc code=start
class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        MOD = 10 ** 9 + 7
        
        # [1, 2^p - 1]这个区间中，每一位上累计的1的个数为2^(p-1)，要让乘积尽可能小（还要大于零）
        # 策略就是尽量把1放到集中的数上，让数两级分化
        # 所有应该有 (2^(p-1) - 1) 个 1，(2^(p-1) - 1) 个 (2^p - 2)，一个(2^p - 1)
        res = (1 << p) - 1

        # 下面的解法竟然会TLE（p 跑到 27 就跑不过去了）
        # 总结：一个一个乘确实太耗辰光，分治比较好
        # multiplier = (1 << p) - 2
        # for _ in range(1, 1 << (p-1)):
        #     res = res * multiplier
        #     if res > MOD:
        #         res %= MOD
        multiplier = (1 << p) - 2
        for _ in range(p-1):
            res = res * multiplier
            if res > MOD:
                res %= MOD
            multiplier **= 2
            if multiplier > MOD:
                multiplier %= MOD

        return res


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.minNonZeroProduct(27)) # 821184946
    print(solution.minNonZeroProduct(1)) # 1
    print(solution.minNonZeroProduct(2)) # 6
    print(solution.minNonZeroProduct(3)) # 1512
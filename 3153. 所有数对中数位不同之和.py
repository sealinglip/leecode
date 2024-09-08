# 你有一个数组 nums ，它只包含 正 整数，所有正整数的数位长度都 相同 。
# 两个整数的 数位不同 指的是两个整数 相同 位置上不同数字的数目。
# 请你返回 nums 中 所有 整数对里，数位不同之和。

# 示例 1：
# 输入：nums = [13,23,12]
# 输出：4
# 解释：
# 计算过程如下：
# - 13 和 23 的数位不同为 1 。
# - 13 和 12 的数位不同为 1 。
# - 23 和 12 的数位不同为 2 。
# 所以所有整数数对的数位不同之和为 1 + 1 + 2 = 4 。

# 示例 2：
# 输入：nums = [10,10,10,10]
# 输出：0
# 解释：
# 数组中所有整数都相同，所以所有整数数对的数位不同之和为 0 。

# 提示：
# 2 <= nums.length <= 10^5
# 1 <= nums[i] < 10^9
# nums 中的整数都有相同的数位长度。

from typing import List

class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        digits = len(str(nums[0])) # 每个数数位的长度
        n = len(nums) # 数组长度

        # 方法1：总数 - 相同 = 不同
        # # 所有的整数对 * 数位长度 （不管数位相同还是不相同的总数位数）
        # total = ((n * (n-1)) >> 1) * digits
        # # 统计每个数位上的数字
        # stat = [[0] * 10 for _ in range(digits)]
        # for num in nums:
        #     for i, c in enumerate(str(num)):
        #         stat[i][int(c)] += 1

        # # 计算相同数位个数
        # same = 0
        # for s in stat:
        #     for cnt in s:
        #         if cnt > 0:
        #             same += (cnt * (cnt-1)) >> 1

        # return total - same

        # 方法2：直接算不同
        res = 0
        for i in range(digits):
            cnt = [0] * 10
            k = 10 ** i
            for num in nums:
                cnt[(num // k) % 10] += 1

            s = n
            for c in cnt:
                s -= c
                res += c * s

        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.sumDigitDifferences([13,23,12])) # 4
    print(solution.sumDigitDifferences([10,10,10,10])) # 0

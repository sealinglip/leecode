# 给你一个数组 nums 和一个整数 k 。你需要找到 nums 的一个子数组，满足子数组中所有元素按位或运算 OR 的值与 k 的 绝对差 尽可能 小 。
# 换言之，你需要选择一个子数组 nums[l..r] 满足 |k - (nums[l] OR nums[l + 1] ... OR nums[r])| 最小。

# 请你返回 最小 的绝对差值。

# 子数组 是数组中连续的 非空 元素序列。

# 示例 1：
# 输入：nums = [1,2,4,5], k = 3
# 输出：0
# 解释：
# 子数组 nums[0..1] 的按位 OR 运算值为 3 ，得到最小差值 |3 - 3| = 0 。

# 示例 2：
# 输入：nums = [1,3,1,3], k = 2
# 输出：1
# 解释：
# 子数组 nums[1..1] 的按位 OR 运算值为 3 ，得到最小差值 |3 - 2| = 1 。

# 示例 3：
# 输入：nums = [1], k = 10
# 输出：9
# 解释：
# 只有一个子数组，按位 OR 运算值为 1 ，得到最小差值 |10 - 1| = 9 。

# 提示：
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9
# 1 <= k <= 10^9

# Hard
# 复习

from typing import List
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # 子数组是连续区间，用滑动窗口，双指针
        # 难点在于左边界向右滑动时怎么更新区间的 OR 值
        # 变化一下思路，还是窗口，右边界滑动，然后对于每一个确定的右边界
        # 窗口左边界从右边界向左延伸，跳跃式遍历会发生或值变化的点
        n = len(nums)
        # 记录每一位最后出现的位置
        bitLastPos = [-1] * 31
        res = 10 ** 9

        for r in range(n):
            for i in range(31):
                if nums[r] >> i & 1:
                    bitLastPos[i] = r # 更新最后出现的位置

            # 对于出现过的1，以及最后出现的位置构建列表，进行降序排序
            posAndBit = sorted([(b, i) for i, b in enumerate(bitLastPos) if b != -1], reverse=True)

            # 遍历以r为右边界（包含），所有可能的或值
            i = orVal = 0
            while i < len(posAndBit):
                l = posAndBit[i][0]
                while i < len(posAndBit) and posAndBit[i][0] == l:
                    orVal |= 1 << posAndBit[i][1]
                    i += 1
                res = min(res, abs(orVal - k))

        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumDifference([1,2,4,5], 3)) # 0
    print(solution.minimumDifference([1,3,1,3], 2)) # 1
    print(solution.minimumDifference([1], 10)) # 9
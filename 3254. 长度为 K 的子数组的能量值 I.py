# 给你一个长度为 n 的整数数组 nums 和一个正整数 k 。

# 一个数组的 能量值 定义为：

# 如果 所有 元素都是依次 连续 且 上升 的，那么能量值为 最大 的元素。
# 否则为 -1 。
# 你需要求出 nums 中所有长度为 k 的 子数组的能量值。

# 请你返回一个长度为 n - k + 1 的整数数组 results ，其中 results[i] 是子数组 nums[i..(i + k - 1)] 的能量值。


# 示例 1：
# 输入：nums = [1,2,3,4,3,2,5], k = 3
# 输出：[3,4,-1,-1,-1]
# 解释：
# nums 中总共有 5 个长度为 3 的子数组：
# [1, 2, 3] 中最大元素为 3 。
# [2, 3, 4] 中最大元素为 4 。
# [3, 4, 3] 中元素 不是 连续的。
# [4, 3, 2] 中元素 不是 上升的。
# [3, 2, 5] 中元素 不是 连续的。

# 示例 2：
# 输入：nums = [2,2,2,2,2], k = 4
# 输出：[-1,-1]

# 示例 3：
# 输入：nums = [3,2,3,2,3,2], k = 2
# 输出：[-1,3,-1,3,-1]


# 提示：
# 1 <= n == nums.length <= 500
# 1 <= nums[i] <= 10^5
# 1 <= k <= n

from typing import List

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = []
        # MD. 是连续且上升，不是连续上升
        # 移动窗口 + 单调栈 —— 直接改成计数好了
        cnt = 1
        # 初始化窗口
        for i in range(1, k-1):
            if nums[i-1] != nums[i]-1:
                cnt = 0
            cnt += 1

        for i in range(k-1, len(nums)):
            if nums[i-1] != nums[i]-1:
                cnt = 0
            cnt += 1

            res.append(-1 if cnt < k else nums[i])
        
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.resultsArray([1,3,4], 2)) # [-1,4]
    print(solution.resultsArray([1,2,3,4,3,2,5], 3)) # [3,4,-1,-1,-1]
    print(solution.resultsArray([2,2,2,2,2], 4)) # [-1,-1]
    print(solution.resultsArray([3,2,3,2,3,2], 2)) # [-1,3,-1,3,-1]

#
# @lc app=leetcode.cn id=3013 lang=python3
#
# [3013] 将数组分成最小总代价的子数组 II
#
# https://leetcode.cn/problems/divide-an-array-into-subarrays-with-minimum-cost-ii/description/
#
# algorithms
# Hard (36.28%)
# Likes:    24
# Dislikes: 0
# Total Accepted:    4K
# Total Submissions: 8.9K
# Testcase Example:  '[1,3,2,6,4,2]\n3\n3'
#
# 给你一个下标从 0 开始长度为 n 的整数数组 nums 和两个 正 整数 k 和 dist 。
# 
# 一个数组的 代价 是数组中的 第一个 元素。比方说，[1,2,3] 的代价为 1 ，[3,4,1] 的代价为 3 。
# 
# 你需要将 nums 分割成 k 个 连续且互不相交 的子数组，满足 第二 个子数组与第 k 个子数组中第一个元素的下标距离 不超过 dist
# 。换句话说，如果你将 nums 分割成子数组 nums[0..(i1 - 1)], nums[i1..(i2 - 1)], ...,
# nums[ik-1..(n - 1)] ，那么它需要满足 ik-1 - i1 <= dist 。
# 
# 请你返回这些子数组的 最小 总代价。
# 
# 
# 示例 1：
# 输入：nums = [1,3,2,6,4,2], k = 3, dist = 3
# 输出：5
# 解释：将数组分割成 3 个子数组的最优方案是：[1,3] ，[2,6,4] 和 [2] 。这是一个合法分割，因为 ik-1 - i1 等于 5 - 2 =
# 3 ，等于 dist 。总代价为 nums[0] + nums[2] + nums[5] ，也就是 1 + 2 + 2 = 5 。
# 5 是分割成 3 个子数组的最小总代价。
# 
# 示例 2：
# 输入：nums = [10,1,2,2,2,1], k = 4, dist = 3
# 输出：15
# 解释：将数组分割成 4 个子数组的最优方案是：[10] ，[1] ，[2] 和 [2,2,1] 。这是一个合法分割，因为 ik-1 - i1 等于 3 -
# 1 = 2 ，小于 dist 。总代价为 nums[0] + nums[1] + nums[2] + nums[3] ，也就是 10 + 1 + 2 +
# 2 = 15 。
# 分割 [10] ，[1] ，[2,2,2] 和 [1] 不是一个合法分割，因为 ik-1 和 i1 的差为 5 - 1 = 4 ，大于 dist 。
# 15 是分割成 4 个子数组的最小总代价。
# 
# 示例 3：
# 输入：nums = [10,8,18,9], k = 3, dist = 1
# 输出：36
# 解释：将数组分割成 4 个子数组的最优方案是：[10] ，[8] 和 [18,9] 。这是一个合法分割，因为 ik-1 - i1 等于 2 - 1 = 1
# ，等于 dist 。总代价为 nums[0] + nums[1] + nums[2] ，也就是 10 + 8 + 18 = 36 。
# 分割 [10] ，[8,18] 和 [9] 不是一个合法分割，因为 ik-1 和 i1 的差为 3 - 1 = 2 ，大于 dist 。
# 36 是分割成 3 个子数组的最小总代价。
# 
# 
# 提示：
# 3 <= n <= 10^5
# 1 <= nums[i] <= 10^9
# 3 <= k <= n
# k - 2 <= dist <= n - 2
# 
# 
#

from typing import List
# @lc code=start
class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        # 除了 nums[0] 以外，再选出 k-1 个数
        target = k - 1
        base_cost = nums[0]
        
        # 初始窗口
        init_window = nums[1 : dist + 2]
        
        # 维护窗口内最小的 target 个数
        selected = SortedList(init_window)
        # 维护窗口内剩余的数
        candidates = SortedList()
        
        # 当前 selected 中所有元素的和
        cur_sum = sum(init_window)
        
        # 平衡，将 selected 中多余的较大元素移动到 candidates
        while len(selected) > target:
            max_val = selected.pop()
            cur_sum -= max_val
            candidates.add(max_val)
        
        ans = base_cost + cur_sum
        # i 指向即将进入窗口的新元素下标
        for i in range(dist + 2, len(nums)):
            # 移除
            removed_val = nums[i - dist - 1]
            
            # 判断要移除的元素是在 selected 中还是 candidates 中
            if removed_val in selected:
                selected.remove(removed_val)
                cur_sum -= removed_val
            else:
                candidates.remove(removed_val)
            
            # 进入
            added_val = nums[i]
            
            # 新元素比 selected 中最大的还小，说明它属于 selected
            if len(selected) > 0 and added_val < selected[-1]:
                selected.add(added_val)
                cur_sum += added_val
            else:
                candidates.add(added_val)
            
            # 维护 selected 的大小为 target
            if len(selected) < target:
                # 缺元素：从 candidates 中拿最小的补进来
                min_candidate = candidates.pop(0)
                selected.add(min_candidate)
                cur_sum += min_candidate
            elif len(selected) > target:
                # 多元素：把 selected 中最大的踢到 candidates
                max_selected = selected.pop()
                cur_sum -= max_selected
                candidates.add(max_selected)
            
            ans = min(ans, base_cost + cur_sum)
        
        return ans
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumCost([1,3,2,6,4,2], 3, 3)) # 5
    print(solution.minimumCost([10,1,2,2,2,1], 4, 3)) # 15
    print(solution.minimumCost([10,8,18,9], 3, 1)) # 36

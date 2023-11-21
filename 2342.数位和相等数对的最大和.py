#
# @lc app=leetcode.cn id=2342 lang=python3
#
# [2342] 数位和相等数对的最大和
#
# 给你一个下标从 0 开始的数组 nums ，数组中的元素都是 正 整数。请你选出两个下标 i 和 j（i != j），且 nums[i] 的数位和 与  nums[j] 的数位和相等。

# 请你找出所有满足条件的下标 i 和 j ，找出并返回 nums[i] + nums[j] 可以得到的 最大值 。

# 示例 1：
# 输入：nums = [18,43,36,13,7]
# 输出：54
# 解释：满足条件的数对 (i, j) 为：
# - (0, 2) ，两个数字的数位和都是 9 ，相加得到 18 + 36 = 54 。
# - (1, 4) ，两个数字的数位和都是 7 ，相加得到 43 + 7 = 50 。
# 所以可以获得的最大和是 54 。

# 示例 2：
# 输入：nums = [10,12,19,14]
# 输出：-1
# 解释：不存在满足条件的数对，返回 -1 。
 

# 提示：
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9


from typing import List
# @lc code=start
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def digitSum(num: int) -> int:
            '''
            返回数位和
            '''
            return sum(int(c) for c in str(num))
        
        def record(num: int, arr: List[int]) -> None:
            if arr:
                if num < arr[1]:
                    return
                elif num < arr[0]:
                    arr[1] = num
                else:
                    arr[1] = arr[0]
                    arr[0] = num
            else:
                arr.append(num)

        
        d = {}
        for n in nums:
            s = digitSum(n)
            if s not in d:
                d[s] = [0, 0]
            record(n, d[digitSum(n)])

        ca = [sum(v) for v in d.values() if v[1] > 0]

        return max(ca) if ca else -1

# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumSum([18,43,36,13,7])) # 54
    print(solution.maximumSum([10,12,19,14])) # -1
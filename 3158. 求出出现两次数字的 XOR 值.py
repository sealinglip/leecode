# 给你一个数组 nums ，数组中的数字 要么 出现一次，要么 出现两次。

# 请你返回数组中所有出现两次数字的按位 XOR 值，如果没有数字出现过两次，返回 0 。

# 示例 1：
# 输入：nums = [1,2,1,3]
# 输出：1
# 解释：
# nums 中唯一出现过两次的数字是 1 。

# 示例 2：
# 输入：nums = [1,2,3]
# 输出：0
# 解释：
# nums 中没有数字出现两次。

# 示例 3：
# 输入：nums = [1,2,2,1]
# 输出：3
# 解释：
# 数字 1 和 2 出现过两次。1 XOR 2 == 3 。

# 提示：
# 1 <= nums.length <= 50
# 1 <= nums[i] <= 50
# nums 中每个数字要么出现过一次，要么出现过两次。

from typing import List

class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        cnt = set()
        res = 0
        for n in nums:
            if n in cnt:
                res ^= n
            else:
                cnt.add(n)
        
        return res


if __name__ == "__main__":
    solution = Solution()
    print(solution.duplicateNumbersXOR([1,2,1,3])) # 1
    print(solution.duplicateNumbersXOR([1,2,3])) # 0
    print(solution.duplicateNumbersXOR([1,2,2,1])) # 3

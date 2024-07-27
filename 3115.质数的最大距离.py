#
# @lc app=leetcode.cn id=3115 lang=python3
#
# [3115] 质数的最大距离
#
# 给你一个整数数组 nums。

# 返回两个（不一定不同的）质数在 nums 中 下标 的 最大距离。

 

# 示例 1：
# 输入： nums = [4,2,9,5,3]
# 输出： 3
# 解释： nums[1]、nums[3] 和 nums[4] 是质数。因此答案是 |4 - 1| = 3。

# 示例 2：
# 输入： nums = [4,8,2,8]
# 输出： 0
# 解释： nums[2] 是质数。因为只有一个质数，所以答案是 |2 - 2| = 0。


# 提示：
# 1 <= nums.length <= 3 * 10^5
# 1 <= nums[i] <= 100
# 输入保证 nums 中至少有一个质数。

from typing import List
# @lc code=start
from math import sqrt
class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        primes = set()

        def _isPrime(num: int) -> bool:
            if num < 2:
                return False
            elif num in primes:
                return True
            elif num < 4:
                primes.add(num)
                return True
            else:
                limit = int(sqrt(num))
                for i in primes:
                    if i > limit:
                        break
                    if num % i == 0:
                        return False
                primes.add(num)
                return True
        
        for i in range(2, 101):
            _isPrime(i)

        mi, ma = len(nums), -1
        for i, num in enumerate(nums):
            if _isPrime(num):
                mi = min(mi, i)
                ma = max(ma, i)
        
        return ma - mi
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumPrimeDifference([4,2,9,5,3])) # 3
    print(solution.maximumPrimeDifference([4,8,2,8])) # 0
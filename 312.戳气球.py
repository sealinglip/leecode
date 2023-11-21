#
# @lc app=leetcode.cn id=312 lang=python3
#
# [312] 戳气球
#
# 有 n 个气球，编号为0 到 n - 1，每个气球上都标有一个数字，这些数字存在数组 nums 中。
# 现在要求你戳破所有的气球。戳破第 i 个气球，你可以获得 nums[i - 1] * nums[i] * nums[i + 1] 枚硬币。 这里的 i - 1 和 i + 1 代表和 i 相邻的两个气球的序号。如果 i - 1或 i + 1 超出了数组的边界，那么就当它是一个数字为 1 的气球。
# 求所能获得硬币的最大数量。


# 示例 1：
# 输入：nums = [3,1,5,8]
# 输出：167
# 解释：
# nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
# coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167

# 示例 2：
# 输入：nums = [1,5]
# 输出：10
 

# 提示：
# n == nums.length
# 1 <= n <= 300
# 0 <= nums[i] <= 100

# Hard
import random
from typing import List
# @lc code=start
from functools import lru_cache

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        val = [1] + nums + [1]
        
        @lru_cache(None)
        def solve(left: int, right: int) -> int:
            if left >= right - 1:
                return 0
            
            best = 0
            for i in range(left + 1, right):
                total = val[left] * val[i] * val[right]
                total += solve(left, i) + solve(i, right)
                best = max(best, total)
            return best

        return solve(0, n + 1)
    
# @lc code=end

def randomArray(n: int) -> List[int]:
    randomArr = []
    for _ in range(n):
        randomArr.append(random.randint(0, 100))
    return randomArr

class Balloon:
    def __init__(self, val: int, prev: 'Balloon'=None, next: 'Balloon'=None) -> None:
        self.val = val
        self.prev = prev
        self.next = next

    def burst(self) -> int:
        prod = self.val * self.prev.val * self.next.val
        self.prev.next = self.next
        self.next.prev = self.prev
        return prod
    
class Solution2:
    def maxCoins(self, nums: List[int]) -> int:
        # 长度大于3的时候，先戳掉小的，剩三个的时候先戳中间的，剩下两个先戳小的，然后打完收工
        # 构造一个链表方便戳
        head = Balloon(1)
        tail = Balloon(1)
        n = len(nums)

        balloons = []
        prev = head
        for num in nums:
            b = Balloon(num, prev)
            balloons.append(b)
            prev.next = b
            prev = b
        prev.next = tail
        tail.prev = prev

        # 对balloons进行排序
        balloons.sort(key=lambda b: b.val, reverse=True)

        # 开戳
        res = 0
        if n > 3:
            for _ in range(n-3):
                b = balloons.pop()
                res += b.burst()
        if n >= 3:
            res += head.next.next.burst() # 戳中间那个
        if n >= 2:
            b = tail.prev if head.next.val > tail.prev.val else head.next
            res += b.burst()

        res += head.next.burst()
        return res
    

if __name__ == "__main__":
    solution = Solution()
    solution2 = Solution2()
    print(solution.maxCoins([52, 41, 3, 59, 95, 23])) # 554470
    print(solution.maxCoins([1,3,1,5,8,1])) # 178
    print(solution.maxCoins([3,1,5,8])) # 167
    print(solution.maxCoins([1,5])) # 10
    # for _ in range(1000):
    #     n = random.randint(1, 30)
    #     arr = randomArray(n)
    #     s1 = solution.maxCoins(arr)
    #     s2 = solution2.maxCoins(arr)
    #     if s1 != s2:
    #         print(arr)
    #         print("s1: %d, s2: %d" % (s1, s2))
    #         break



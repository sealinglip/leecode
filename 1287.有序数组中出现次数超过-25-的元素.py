#
# @lc app=leetcode.cn id=1287 lang=python3
#
# [1287] 有序数组中出现次数超过25%的元素
#
# 给你一个非递减的 有序 整数数组，已知这个数组中恰好有一个整数，它的出现次数超过数组元素总数的 25%。
# 请你找到并返回这个整数

 

# 示例：

# 输入：arr = [1,2,2,6,6,6,6,7,10]
# 输出：6
 

# 提示：

# 1 <= arr.length <= 10^4
# 0 <= arr[i] <= 10^5

from typing import List
# @lc code=start
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        limit = (n >> 2)
        prev = cnt = 0
        for x in arr:
            if x == prev:
                cnt += 1
            else:
                cnt = 1
                prev = x
            if cnt > limit:
                return prev
            
        return None
        
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.findSpecialInteger([1,2,3,3])) # 3
    print(solution.findSpecialInteger([1,2,2,6,6,6,6,7,10])) # 6

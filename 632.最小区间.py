#
# @lc app=leetcode.cn id=632 lang=python3
#
# [632] 最小区间
#
# 你有 k 个 非递减排列 的整数列表。找到一个 最小 区间，使得 k 个列表中的每个列表至少有一个数包含在其中。
# 我们定义如果 b-a < d-c 或者在 b-a == d-c 时 a < c，则区间 [a,b] 比 [c,d] 小。


# 示例 1：
# 输入：nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
# 输出：[20,24]
# 解释： 
# 列表 1：[4, 10, 15, 24, 26]，24 在区间 [20,24] 中。
# 列表 2：[0, 9, 12, 20]，20 在区间 [20,24] 中。
# 列表 3：[5, 18, 22, 30]，22 在区间 [20,24] 中。

# 示例 2：
# 输入：nums = [[1,2,3],[1,2,3],[1,2,3]]
# 输出：[1,1]
 
# 提示：
# nums.length == k
# 1 <= k <= 3500
# 1 <= nums[i].length <= 50
# -10^5 <= nums[i][j] <= 10^5
# nums[i] 按非递减顺序排列

# Hard

from typing import List
import heapq 
# @lc code=start
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # 归并排序 + 滑动窗口计数
        k = len(nums)
        # cnt = [0] * k # 窗口内各列表计数
        ptr = [0] * k # 窗口内各列表索引
        # win = [] # 窗口
        hq = [] # 小顶堆，每个系列一个元素
        max_ = nums[0][0]

        def push(i: int) -> bool:
            nonlocal max_
            if ptr[i] >= len(nums[i]):
                # 这个序列已经没数了
                return False
            tmp = nums[i][ptr[i]]
            max_ = max(max_, tmp)
            heapq.heappush(hq, (tmp, i))
            ptr[i] += 1
            return True

        # 初始化
        for i in range(k):
            push(i)
        
        res = [hq[0][0], max_] # 初始区间（包含每个列表一个数）
        span = res[1] - res[0]
        while True:
            _, i = heapq.heappop(hq) # 出堆
            if not push(i):
                # 这个序列已经没数了
                break
            if max_ - hq[0][0] < span:
                res = [hq[0][0], max_]
                span = res[1] - res[0]

        return res
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.smallestRange([[-1,1],[-2,2],[-3,3],[-4,4],[-5,5],[-6,6],[-7,7],[-8,8],[-9,9],[-10,10],[-11,11],[-12,12],[-13,13],[-14,14],[-15,15],[-16,16],[-17,17],[-18,18],[-19,19],[-20,20],[-21,21],[-22,22],[-23,23],[-24,24],[-25,25],[-26,26],[-27,27],[-28,28],[-29,29],[-30,30],[-31,31],[-32,32],[-33,33],[-34,34],[-35,35],[-36,36],[-37,37],[-38,38],[-39,39],[-40,40],[-41,41],[-42,42],[-43,43],[-44,44],[-45,45],[-46,46],[-47,47],[-48,48],[-49,49],[-50,50],[-51,51],[-52,52],[-53,53],[-54,54],[-55,55]])) # [-55,-1]
    print(solution.smallestRange([[4,10,15,24,26], [0,9,12,20], [5,18,22,30]])) # [20,24]
    print(solution.smallestRange([[1,2,3],[1,2,3],[1,2,3]])) # [1,1]

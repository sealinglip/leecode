#
# @lc app=leetcode.cn id=2071 lang=python3
#
# [2071] 你可以安排的最多任务数目
#
# https://leetcode.cn/problems/maximum-number-of-tasks-you-can-assign/description/
#
# algorithms
# Hard (34.60%)
# Likes:    132
# Dislikes: 0
# Total Accepted:    12K
# Total Submissions: 30.6K
# Testcase Example:  '[3,2,1]\n[0,3,3]\n1\n1'
#
# 给你 n 个任务和 m 个工人。每个任务需要一定的力量值才能完成，需要的力量值保存在下标从 0 开始的整数数组 tasks 中，第 i 个任务需要
# tasks[i] 的力量才能完成。每个工人的力量值保存在下标从 0 开始的整数数组 workers 中，第 j 个工人的力量值为 workers[j]
# 。每个工人只能完成 一个 任务，且力量值需要 大于等于 该任务的力量要求值（即 workers[j] >= tasks[i] ）。
# 
# 除此以外，你还有 pills 个神奇药丸，可以给 一个工人的力量值 增加 strength 。你可以决定给哪些工人使用药丸，但每个工人 最多 只能使用
# 一片 药丸。
# 
# 给你下标从 0 开始的整数数组tasks 和 workers 以及两个整数 pills 和 strength ，请你返回 最多
# 有多少个任务可以被完成。
# 
# 
# 示例 1：
# 输入：tasks = [3,2,1], workers = [0,3,3], pills = 1, strength = 1
# 输出：3
# 解释：
# 我们可以按照如下方案安排药丸：
# - 给 0 号工人药丸。
# - 0 号工人完成任务 2（0 + 1 >= 1）
# - 1 号工人完成任务 1（3 >= 2）
# - 2 号工人完成任务 0（3 >= 3）
# 
# 
# 示例 2：
# 输入：tasks = [5,4], workers = [0,0,0], pills = 1, strength = 5
# 输出：1
# 解释：
# 我们可以按照如下方案安排药丸：
# - 给 0 号工人药丸。
# - 0 号工人完成任务 0（0 + 5 >= 5）
# 
# 
# 示例 3：
# 输入：tasks = [10,15,30], workers = [0,10,10,10,10], pills = 3, strength = 10
# 输出：2
# 解释：
# 我们可以按照如下方案安排药丸：
# - 给 0 号和 1 号工人药丸。
# - 0 号工人完成任务 0（0 + 10 >= 10）
# - 1 号工人完成任务 1（10 + 10 >= 15）
# 
# 
# 示例 4：
# 输入：tasks = [5,9,8,5,9], workers = [1,6,4,2,6], pills = 1, strength = 5
# 输出：3
# 解释：
# 我们可以按照如下方案安排药丸：
# - 给 2 号工人药丸。
# - 1 号工人完成任务 0（6 >= 5）
# - 2 号工人完成任务 2（4 + 5 >= 8）
# - 4 号工人完成任务 3（6 >= 5）
# 
# 
# 提示：
# n == tasks.length
# m == workers.length
# 1 <= n, m <= 5 * 10^4
# 0 <= pills <= m
# 0 <= tasks[i], workers[j], strength <= 10^9
#

from collections import deque
from typing import List
# @lc code=start
class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        n, m = len(tasks), len(workers)
        tasks.sort() # 将任务按所需力量从小到大排列
        workers.sort() # 将工人从弱到强排列

        def check(x: int) -> bool:
            '''
            用最强的x名工人是否可以完成最容易的x个任务？
            '''
            i = 0 # 待分配任务索引
            pi = pills # 💊数
            achievable = deque() # 可完成的任务

            for j in range(m-x, m):
                w = workers[j]

                # 吃药的情况下，当前工人能完成的任务加入队列
                while i < x and tasks[i] <= w + strength:
                    achievable.append(tasks[i])
                    i += 1

                # 吃药都搞不定
                if not achievable:
                    return False
                
                # 不吃药就能搞定最简单的任务，优先
                if w >= achievable[0]:
                    achievable.popleft()
                    continue

                # 冇💊了
                if pi <= 0:
                    return False
                
                pi -= 1
                achievable.pop()

            return True

        # 二分查找
        l, r = 0, min(n, m)
        res = 0
        while l <= r:
            mid = (l + r) >> 1
            if check(mid):
                res = mid
                l = mid + 1
            else:
                r = mid - 1

        return res
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxTaskAssign([3,2,1], [0,3,3], 1, 1)) # 3
    print(solution.maxTaskAssign([5,4], [0,0,0], 1, 5)) # 1
    print(solution.maxTaskAssign([10,15,30], [0,10,10,10,10], 3, 10)) # 2
    print(solution.maxTaskAssign([5,9,8,5,9], [1,6,4,2,6], 1, 5)) # 3

#
# @lc app=leetcode.cn id=621 lang=python3
#
# [621] 任务调度器
#
# 给你一个用字符数组 tasks 表示的 CPU 需要执行的任务列表。其中每个字母表示一种不同种类的任务。
# 任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。在任何一个单位时间，CPU 
# 可以完成一个任务，或者处于待命状态。

# 然而，两个 相同种类 的任务之间必须有长度为整数 n 的冷却时间，因此至少有连续 n 个单位时间内 
# CPU 在执行不同的任务，或者在待命状态。

# 你需要计算完成所有任务所需要的 最短时间 。

# 示例 1：
# 输入：tasks = ["A","A","A","B","B","B"], n = 2
# 输出：8
# 解释：A -> B -> (待命) -> A -> B -> (待命) -> A -> B
#      在本示例中，两个相同类型任务之间必须间隔长度为 n = 2 的冷却时间，而执行一个任务只需要一个单位时间，所以中间出现了（待命）状态。 

# 示例 2：
# 输入：tasks = ["A","A","A","B","B","B"], n = 0
# 输出：6
# 解释：在这种情况下，任何大小为 6 的排列都可以满足要求，因为 n = 0
# ["A","A","A","B","B","B"]
# ["A","B","A","B","A","B"]
# ["B","B","B","A","A","A"]
# ...
# 诸如此类

# 示例 3：
# 输入：tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
# 输出：16
# 解释：一种可能的解决方案是：
#      A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> (待命) -> (待命) -> A -> (待命) -> (待命) -> A
 
# 提示：
# 1 <= task.length <= 10^4
# tasks[i] 是大写英文字母
# n 的取值范围为 [0, 100]

from typing import List
# @lc code=start
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:
            return 0
        elif n == 0:
            return len(tasks)
        else:
            cnt = Counter(tasks)
            taskStats = cnt.most_common()

            # 方法1：实际排任务
            # time = 0 # 总耗时
            # limit = [0] * len(taskStats) # 记录每个任务的最早开始时间
            # hasTaskLeft = True
            # while hasTaskLeft:
            #     hasTaskLeft = False
            #     for i in range(len(taskStats)):
            #         task = taskStats[i]
            #         if task[1] == 0: # 剩余次数为0，跳过
            #             break
            #         else:
            #             hasTaskLeft = True
            #             if time >= limit[i]:
            #                 time += 1
            #                 taskStats[i] = (task[0], task[1] - 1)
            #                 limit[i] += n + 1 # 下一次该任务能开始的最早时间
            #             else:
            #                 time += 1
            #                 break
            
            # return time

            # 方法2：推导最少需要的时长
            taskCntHasMaxExecs = 0 # 有最多执行次数的任务数
            maxExecs = taskStats[0][1] # 任务最多的执行次数
            for task in taskStats:
                if task[1] < maxExecs:
                    break
                taskCntHasMaxExecs += 1
            return max(len(tasks), (maxExecs - 1) * (n + 1) + taskCntHasMaxExecs)


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.leastInterval(["A","A","A","B","B","B"], 2))
    print(solution.leastInterval(["A","A","A","B","B","B"], 0))
    print(solution.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"], 2))
#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#
# 你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。

# 在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，
# 表示如果要学习课程 ai 则 必须 先学习课程  bi 。

# 例如，先修课程对[0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
# 请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。

# 示例 1：
# 输入：numCourses = 2, prerequisites = [[1, 0]]
# 输出：true
# 解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。

# 示例 2：
# 输入：numCourses = 2, prerequisites = [[1, 0], [0, 1]]
# 输出：false
# 解释：总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。


# 提示：
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# prerequisites[i] 中的所有课程对 互不相同

from collections import defaultdict, deque
from typing import List
# @lc code=start


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 拓扑排序
        subsequent = defaultdict(list)
        inDegree = [0] * numCourses
        for p, q in prerequisites:
            subsequent[q].append(p)
            inDegree[p] += 1

        finished = 0
        queue = deque(c for c in range(numCourses) if inDegree[c] == 0)
        while queue:
            c = queue.popleft()
            finished += 1
            if c in subsequent:
                for s in subsequent[c]:
                    inDegree[s] -= 1
                    if inDegree[s] == 0:
                        queue.append(s)

        return finished == numCourses

        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.canFinish(2, [[1, 0]]))  # True
    print(solution.canFinish(2, [[1, 0], [0, 1]]))  # False

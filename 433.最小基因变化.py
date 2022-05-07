#
# @lc app=leetcode.cn id=433 lang=python3
#
# [433] 最小基因变化
#
# 基因序列可以表示为一条由 8 个字符组成的字符串，其中每个字符都是 'A'、'C'、'G' 和 'T' 之一。

# 假设我们需要调查从基因序列 start 变为 end 所发生的基因变化。一次基因变化就意味着这个基因序列中的一个字符发生了变化。

# 例如，"AACCGGTT" - -> "AACCGGTA" 就是一次基因变化。
# 另有一个基因库 bank 记录了所有有效的基因变化，只有基因库中的基因才是有效的基因序列。

# 给你两个基因序列 start 和 end ，以及一个基因库 bank ，请你找出并返回能够使 start 变化为 end 所需的最少变化次数。如果无法完成此基因变化，返回 - 1 。

# 注意：起始基因序列 start 默认是有效的，但是它并不一定会出现在基因库中。


# 示例 1：
# 输入：start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]
# 输出：1

# 示例 2：
# 输入：start = "AACCGGTT", end = "AAACGGTA", bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
# 输出：2

# 示例 3：
# 输入：start = "AAAAACCC", end = "AACCCCCC", bank = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
# 输出：3


# 提示：
# start.length == 8
# end.length == 8
# 0 <= bank.length <= 10
# bank[i].length == 8
# start、end 和 bank[i] 仅由字符['A', 'C', 'G', 'T'] 组成


from typing import List
# @lc code=start
from collections import defaultdict, deque


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        def diff(g1: str, g2: str) -> int:
            # 求所有不同的位置
            return sum([1 if x != y else 0 for x, y in zip(g1, g2)])
        endIdx = -1
        if end not in bank:
            # end 必须在基因库中
            return -1
        else:
            endIdx = bank.index(end)

        diffDict = defaultdict(list)
        startIdx = -1
        bn = len(bank)
        if start in bank:
            startIdx = bank.index(start)
        else:
            for i in range(bn):
                if diff(start, bank[i]) == 1:
                    diffDict[startIdx].append(i)
                    diffDict[i].append(startIdx)
        for i in range(bn):
            for j in range(i, bn):
                if diff(bank[i], bank[j]) == 1:
                    diffDict[i].append(j)
                    diffDict[j].append(i)

        # bfs
        queue = deque([(startIdx, 0)])
        visited = set([startIdx])
        while queue:
            g, s = queue.popleft()
            if g == endIdx:
                return s
            visited.add(g)
            s += 1
            for t in diffDict[g]:
                if t not in visited:
                    queue.append((t, s))

        return -1


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]))  # 1
    print(solution.minMutation("AACCGGTT", "AAACGGTA",
                               ["AACCGGTA", "AACCGCTA", "AAACGGTA"]))  # 2
    print(solution.minMutation("AAAAACCC", "AACCCCCC",
                               ["AAAACCCC", "AAACCCCC", "AACCCCCC"]))  # 3

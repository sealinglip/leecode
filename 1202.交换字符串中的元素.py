#
# @lc app=leetcode.cn id=1202 lang=python3
#
# [1202] 交换字符串中的元素
#
# 给你一个字符串 s，以及该字符串中的一些「索引对」数组 pairs，其中 pairs[i] = [a, b] 表示字符串中的两个索引（编号从 0 开始）。
# 你可以 任意多次交换 在 pairs 中任意一对索引处的字符。
# 返回在经过若干次交换后，s 可以变成的按字典序最小的字符串。


# 示例 1:
# 输入：s = "dcab", pairs = [[0, 3], [1, 2]]
# 输出："bacd"
# 解释：
# 交换 s[0] 和 s[3], s = "bcad"
# 交换 s[1] 和 s[2], s = "bacd"

# 示例 2：
# 输入：s = "dcab", pairs = [[0, 3], [1, 2], [0, 2]]
# 输出："abcd"
# 解释：
# 交换 s[0] 和 s[3], s = "bcad"
# 交换 s[0] 和 s[2], s = "acbd"
# 交换 s[1] 和 s[2], s = "abcd"

# 示例 3：
# 输入：s = "cba", pairs = [[0, 1], [1, 2]]
# 输出："abc"
# 解释：
# 交换 s[0] 和 s[1], s = "bca"
# 交换 s[1] 和 s[2], s = "bac"
# 交换 s[0] 和 s[1], s = "abc"

# 提示：
# 1 <= s.length <= 10 ^ 5
# 0 <= pairs.length <= 10 ^ 5
# 0 <= pairs[i][0], pairs[i][1] < s.length
# s 中只含有小写英文字母

from typing import List
# @lc code=start
from collections import defaultdict


class UnionFind:
    def __init__(self, s):
        self.father = {i: i for i in range(len(s))}

    def find(self, x):
        root = x

        while self.father[root] != root:
            root = self.father[root]

        # 路径压缩
        while x != root:
            original_father = self.father[x]
            self.father[x] = root
            x = original_father

        return root

    def merge(self, x, y):
        root_x, root_y = self.find(x), self.find(y)

        if root_x != root_y:
            self.father[root_x] = root_y


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        if not s or not pairs:
            return s

        # 处理pairs得到连通集
        # 并查集建图
        uf = UnionFind(s)
        for x, y in pairs:
            uf.merge(x, y)

        # 获取连通节点
        connectedSets = defaultdict(list)
        for i in range(len(s)):
            connectedSets[uf.find(i)].append(i)

        sArr = list(s)  # 离散化字符串
        for l in connectedSets.values():
            if len(l) == 1:
                continue
            l.sort()
            subS = [sArr[i] for i in l]
            subS.sort()  # 本连通集内排序
            for i in range(len(l)):
                sArr[l[i]] = subS[i]

        return "".join(sArr)


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.smallestStringWithSwaps(
        "pwqlmqm", [[5, 3], [3, 0], [5, 1], [1, 1], [1, 5], [3, 0], [0, 2]]))
    print(solution.smallestStringWithSwaps(
        "udyyek", [[3, 3], [3, 0], [5, 1], [3, 1], [3, 4], [3, 5]]))
    print(solution.smallestStringWithSwaps("dcab", [[0, 3], [1, 2]]))
    print(solution.smallestStringWithSwaps("dcab", [[0, 3], [1, 2], [0, 2]]))
    print(solution.smallestStringWithSwaps("cba", [[0, 1], [1, 2]]))

#
# @lc app=leetcode.cn id=699 lang=python3
#
# [699] 掉落的方块
#
# 在二维平面上的 x 轴上，放置着一些方块。

# 给你一个二维整数数组 positions ，其中 positions[i] = [lefti, sideLengthi] 表示：第 i 个方块边长为 sideLengthi ，其左侧边与 x 轴上坐标点 lefti 对齐。

# 每个方块都从一个比目前所有的落地方块更高的高度掉落而下。方块沿 y 轴负方向下落，直到着陆到 另一个正方形的顶边 或者是 x 轴上 。
# 一个方块仅仅是擦过另一个方块的左侧边或右侧边不算着陆。一旦着陆，它就会固定在原地，无法移动。

# 在每个方块掉落后，你必须记录目前所有已经落稳的 方块堆叠的最高高度 。

# 返回一个整数数组 ans ，其中 ans[i] 表示在第 i 块方块掉落后堆叠的最高高度。


# 示例 1：
# 输入：positions = [[1, 2], [2, 3], [6, 1]]
# 输出：[2, 5, 5]
# 解释：
# 第 1 个方块掉落后，最高的堆叠由方块 1 组成，堆叠的最高高度为 2 。
# 第 2 个方块掉落后，最高的堆叠由方块 1 和 2 组成，堆叠的最高高度为 5 。
# 第 3 个方块掉落后，最高的堆叠仍然由方块 1 和 2 组成，堆叠的最高高度为 5 。
# 因此，返回[2, 5, 5] 作为答案。


# 示例 2：
# 输入：positions = [[100, 100], [200, 100]]
# 输出：[100, 100]
# 解释：
# 第 1 个方块掉落后，最高的堆叠由方块 1 组成，堆叠的最高高度为 100 。
# 第 2 个方块掉落后，最高的堆叠可以由方块 1 组成也可以由方块 2 组成，堆叠的最高高度为 100 。
# 因此，返回[100, 100] 作为答案。
# 注意，方块 2 擦过方块 1 的右侧边，但不会算作在方块 1 上着陆。


# 提示：
# 1 <= positions.length <= 1000
# 1 <= lefti <= 10^8
# 1 <= sideLengthi <= 10^6

# 复习

from typing import List
# @lc code=start


class Node:
    def __init__(self) -> None:
        self.ls = self.rs = None
        self.val = self.add = 0


class SegmentTree:
    def __init__(self):
        self.root = Node()

    @staticmethod
    def update(node: Node, lc: int, rc: int, l: int, r: int, v: int) -> None:
        if l <= lc and rc <= r:
            node.add = v
            node.val = v
            return
        SegmentTree.pushdown(node)
        mid = (lc + rc) >> 1
        if l <= mid:
            SegmentTree.update(node.ls, lc, mid, l, r, v)
        if r > mid:
            SegmentTree.update(node.rs, mid + 1, rc, l, r, v)
        SegmentTree.pushup(node)

    @staticmethod
    def query(node: Node, lc: int, rc: int, l: int, r: int) -> int:
        if l <= lc and rc <= r:
            return node.val
        # 先确保所有关联的懒标记下沉下去
        SegmentTree.pushdown(node)
        mid, ans = (lc + rc) >> 1, 0
        if l <= mid:
            ans = SegmentTree.query(node.ls, lc, mid, l, r)
        if r > mid:
            # 同样为不同题目中的更新方式
            ans = max(ans, SegmentTree.query(node.rs, mid + 1, rc, l, r))
        return ans

    @staticmethod
    def pushdown(node: Node) -> None:
        # 懒标记, 在需要的时候才开拓节点和赋值
        if node.ls is None:
            node.ls = Node()
        if node.rs is None:
            node.rs = Node()
        if not node.add:
            return
        node.ls.add, node.rs.add, node.ls.val, node.rs.val = [node.add] * 4
        node.add = 0

    @staticmethod
    def pushup(node: Node) -> None:
        # 动态更新方式：此处为最大值
        node.val = max(node.ls.val, node.rs.val)


class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        # 线段树
        ans, st, max_range = [], SegmentTree(), int(1e9)
        for a, length in positions:
            SegmentTree.update(st.root, 0, max_range, a, a + length - 1,
                               SegmentTree.query(st.root, 0, max_range, a, a + length - 1) + length)
            ans.append(st.root.val)
        return ans


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.fallingSquares([[1, 2], [2, 3], [6, 1]]))  # [2,5,5]
    print(solution.fallingSquares([[100, 100], [200, 100]]))  # [100, 100]

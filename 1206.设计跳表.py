#
# @lc app=leetcode.cn id=1206 lang=python3
#
# [1206] 设计跳表
#
# 不使用任何库函数，设计一个 跳表 。

# 跳表 是在 O(log(n)) 时间内完成增加、删除、搜索操作的数据结构。跳表相比于树堆与红黑树，其功能与性能相当，并且跳表的代码长度相较下更短，其设计思想与链表相似。

# 例如，一个跳表包含[30, 40, 50, 60, 70, 90] ，然后增加 80、45 到跳表中，以下图的方式操作：


# Artyom Kalinin[CC BY-SA 3.0], via Wikimedia Commons

# 跳表中有很多层，每一层是一个短的链表。在第一层的作用下，增加、删除和搜索操作的时间复杂度不超过 O(n)。跳表的每一个操作的平均时间复杂度是 O(log(n))，空间复杂度是 O(n)。

# 了解更多: https: // en.wikipedia.org/wiki/Skip_list

# 在本题中，你的设计应该要包含这些函数：

# bool search(int target): 返回target是否存在于跳表中。
# void add(int num): 插入一个元素到跳表。
# bool erase(int num): 在跳表中删除一个值，如果 num 不存在，直接返回false. 如果存在多个 num ，删除其中任意一个即可。
# 注意，跳表中可能存在多个相同的值，你的代码需要处理这种情况。


# 示例 1:
# 输入
# ["Skiplist", "add", "add", "add", "search",
#     "add", "search", "erase", "erase", "search"]
# [[], [1], [2], [3], [0], [4], [1], [0], [1], [1]]
# 输出
# [null, null, null, null, false, null, true, false, true, false]

# 解释
# Skiplist skiplist = new Skiplist()
# skiplist.add(1)
# skiplist.add(2)
# skiplist.add(3)
# skiplist.search(0)
# // 返回 false
# skiplist.add(4)
# skiplist.search(1)
# // 返回 true
# skiplist.erase(0)
# // 返回 false，0 不在跳表中
# skiplist.erase(1)
# // 返回 true
# skiplist.search(1)
# // 返回 false，1 已被擦除


# 提示:
# 0 <= num, target <= 2 * 104
# 调用search, add,  erase操作次数不大于 5 * 10^4

# Hard
# 复习

from typing import List
# @lc code=start
import random

MAX_LEVEL = 32
P_FACTOR = 0.25


def randomLevel() -> int:
    lv = 1
    while lv < MAX_LEVEL and random.random() < P_FACTOR:
        lv += 1
    return lv


class Node:
    __slots__ = ('val', 'forwards')

    def __init__(self, val: int, maxLevel: int = MAX_LEVEL):
        self.val = val
        self.forwards = [None] * maxLevel


class Skiplist:

    def __init__(self):
        self.dummyHead = Node(-1)
        self.level = 0  # 记录当前最大层数

    def search(self, target: int) -> bool:
        cur = self.dummyHead
        for i in range(self.level - 1, -1, -1):
            # 逐层找，找到本层小于target的最大节点，进到更细的一层
            while cur.forwards[i] and cur.forwards[i].val < target:
                cur = cur.forwards[i]
        cur = cur.forwards[0]
        return cur is not None and cur.val == target

    def add(self, num: int) -> None:
        update = [self.dummyHead] * MAX_LEVEL  # 用于构造新节点的forwards
        cur = self.dummyHead
        for i in range(self.level - 1, -1, -1):
            # 逐层找，找到本层小于num的最大节点，进到更细的一层
            while cur.forwards[i] and cur.forwards[i].val < num:
                cur = cur.forwards[i]
            update[i] = cur
        lv = randomLevel()  # 新节点层数
        self.level = max(self.level, lv)
        newNode = Node(num, lv)
        for i in range(lv):
            newNode.forwards[i] = update[i].forwards[i]
            update[i].forwards[i] = newNode

    def erase(self, num: int) -> bool:
        update = [None] * MAX_LEVEL
        cur = self.dummyHead
        for i in range(self.level - 1, -1, -1):
            # 逐层找，找到本层小于num的最大节点，进到更细的一层
            while cur.forwards[i] and cur.forwards[i].val < num:
                cur = cur.forwards[i]
            update[i] = cur
        cur = cur.forwards[0]
        if cur is not None and cur.val == num:
            # 要删掉cur
            for i in range(self.level):
                if update[i].forwards[i] != cur:
                    break
                update[i].forwards[i] = cur.forwards[i]
            # 更新level，如果必要的话
            while self.level > 1 and self.dummyHead.forwards[self.level - 1] is None:
                self.level -= 1
            return True
        return False  # 没有找到

        # Your Skiplist object will be instantiated and called as such:
        # obj = Skiplist()
        # param_1 = obj.search(target)
        # obj.add(num)
        # param_3 = obj.erase(num)
        # @lc code=end

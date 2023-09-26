#
# @lc app=leetcode.cn id=460 lang=python3
#
# [460] LFU 缓存
#
# 请你为 最不经常使用（LFU）缓存算法设计并实现数据结构。

# 实现 LFUCache 类：

# LFUCache(int capacity) - 用数据结构的容量 capacity 初始化对象
# int get(int key) - 如果键 key 存在于缓存中，则获取键的值，否则返回 - 1 。
# void put(int key, int value) - 如果键 key 已存在，则变更其值；如果键不存在，请插入键值对。
# 当缓存达到其容量 capacity 时，则应该在插入新项之前，移除最不经常使用的项。
# 在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，应该去除 最近最久未使用 的键。
# 为了确定最不常使用的键，可以为缓存中的每个键维护一个 使用计数器 。使用计数最小的键是最久未使用的键。

# 当一个键首次插入到缓存中时，它的使用计数器被设置为 1 (由于 put 操作)。对缓存中的键执行 get 或 put 操作，使用计数器的值将会递增。

# 函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。


# 示例：
# 输入：
# ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
# 输出：
# [null, null, null, 1, null, -1, 3, null, -1, 3, 4]
# 解释：
# // cnt(x) = 键 x 的使用计数
# // cache = [] 将显示最后一次使用的顺序（最左边的元素是最近的）
# LFUCache lfu = new LFUCache(2)
# lfu.put(1, 1)
# // cache = [1, _], cnt(1) = 1
# lfu.put(2, 2)
# // cache = [2, 1], cnt(2) = 1, cnt(1) = 1
# lfu.get(1)
# // 返回 1
# // cache = [1, 2], cnt(2) = 1, cnt(1) = 2
# lfu.put(3, 3)
# // 去除键 2 ，因为 cnt(2) = 1 ，使用计数最小
# // cache = [3, 1], cnt(3) = 1, cnt(1) = 2
# lfu.get(2)
# // 返回 - 1（未找到）
# lfu.get(3)
# // 返回 3
# // cache = [3, 1], cnt(3) = 2, cnt(1) = 2
# lfu.put(4, 4)
# // 去除键 1 ，1 和 3 的 cnt 相同，但 1 最久未使用
# // cache = [4, 3], cnt(4) = 1, cnt(3) = 2
# lfu.get(1)
# // 返回 - 1（未找到）
# lfu.get(3)
# // 返回 3
# // cache = [3, 4], cnt(4) = 1, cnt(3) = 3
# lfu.get(4)
# // 返回 4
# // cache = [3, 4], cnt(4) = 2, cnt(3) = 3


# 提示：
# 1 <= capacity <= 10^4
# 0 <= key <= 10^5
# 0 <= value <= 10^9
# 最多调用 2 * 10^5 次 get 和 put 方法

# Hard
# 复习

# @lc code=start
from collections import defaultdict


class Node:
    def __init__(self, key: int, value: int, prev: 'Node' = None, next: 'Node' = None, freq: int = 0) -> None:
        self.key = key
        self.value = value
        self.freq = freq
        self.prev = prev
        self.next = next

    def insert(self, next: 'Node') -> None:
        next.next = self.next
        next.prev = self
        self.next.prev = next
        self.next = next


def createLinkedList():
    head = Node(0, 0)
    tail = Node(0, 0)
    head.next = tail
    tail.prev = head
    return (head, tail)


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.freqMap = defaultdict(createLinkedList)
        self.minFreq = 0

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.increaseAccess(node)
            return node.value

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.increaseAccess(node)
            node.value = value
            return
        elif len(self.cache) == self.capacity:  # 满了
            # 删一个节点
            _, tail = self.freqMap[self.minFreq]
            node = tail.prev
            node.prev.next = tail
            tail.prev = node.prev
            del self.cache[node.key]

        # 插入新节点
        node = Node(key, value)
        self.increaseAccess(node)
        self.cache[key] = node

    def increaseAccess(self, node: Node) -> None:
        # 更新访问次数
        node.freq += 1
        # 从旧链表中删除
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        # 插入新链表
        head, _ = self.freqMap[node.freq]
        head.next.prev = node
        node.next = head.next
        node.prev = head
        head.next = node
        # 更新最少访问次数
        if self.minFreq == node.freq - 1:
            head, tail = self.freqMap[self.minFreq]
            if head.next == tail:  # 空了
                self.minFreq += 1
        else:
            self.minFreq = min(self.minFreq, node.freq)

        # Your LFUCache object will be instantiated and called as such:
        # obj = LFUCache(capacity)
        # param_1 = obj.get(key)
        # obj.put(key,value)
        # @lc code=end
if __name__ == "__main__":
    lfu = LFUCache(2)
    lfu.put(1, 1)
    lfu.put(2, 2)
    print(lfu.get(1))  # 1
    lfu.put(3, 3)
    print(lfu.get(2))  # -1
    print(lfu.get(3))  # 3
    lfu.put(4, 4)
    print(lfu.get(1))  # -1
    print(lfu.get(3))  # 3
    print(lfu.get(4))  # 4

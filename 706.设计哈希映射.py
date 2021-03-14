#
# @lc app=leetcode.cn id=706 lang=python3
#
# [706] 设计哈希映射
#
# 不使用任何内建的哈希表库设计一个哈希映射（HashMap）。

# 实现 MyHashMap 类：

# MyHashMap() 用空映射初始化对象
# void put(int key, int value) 向 HashMap 插入一个键值对(key, value) 。如果 key 已经存在于映射中，则更新其对应的值 value 。
# int get(int key) 返回特定的 key 所映射的 value ；如果映射中不包含 key 的映射，返回 - 1 。
# void remove(key) 如果映射中存在 key 的映射，则移除 key 和它所对应的 value 。

# 示例：
# 输入：
# ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
# [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
# 输出：
# [null, null, null, 1, -1, null, 1, null, -1]

# 解释：
# MyHashMap myHashMap = new MyHashMap()
# myHashMap.put(1, 1)
# // myHashMap 现在为[[1, 1]]
# myHashMap.put(2, 2)
# // myHashMap 现在为[[1, 1], [2, 2]]
# myHashMap.get(1)
# // 返回 1 ，myHashMap 现在为[[1, 1], [2, 2]]
# myHashMap.get(3)
# // 返回 - 1（未找到），myHashMap 现在为[[1, 1], [2, 2]]
# myHashMap.put(2, 1)
# // myHashMap 现在为[[1, 1], [2, 1]]（更新已有的值）
# myHashMap.get(2)
# // 返回 1 ，myHashMap 现在为[[1, 1], [2, 1]]
# myHashMap.remove(2)
# // 删除键为 2 的数据，myHashMap 现在为[[1, 1]]
# myHashMap.get(2)
# // 返回 - 1（未找到），myHashMap 现在为[[1, 1]]


# 提示：
# 0 <= key, value <= 10^6
# 最多调用 10^4 次 put、get 和 remove 方法

# @lc code=start
class Node:
    def __init__(self, key, val, nxt=None):
        self.key = key
        self.val = val
        self.next = nxt


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.capacity = 769
        self.A = [Node(-1, -1) for _ in range(self.capacity)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        i = key % self.capacity
        cur = self.A[i].next
        while cur:
            if cur.key == key:
                cur.val = value
                return
            cur = cur.next
        new_node = Node(key, value)
        head = self.A[i]
        new_node.next = head.next
        head.next = new_node

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        i = key % self.capacity
        cur = self.A[i].next
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        i = key % self.capacity
        cur = self.A[i].next
        pre = self.A[i]
        while cur:
            if cur.key == key:
                pre.next = cur.next
            cur = cur.next
            pre = pre.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end
if __name__ == "__main__":
    hashMap = MyHashMap()
    hashMap.put(1, 1)
    hashMap.put(2, 2)
    print(hashMap.get(1))
    print(hashMap.get(2))
    print(hashMap.get(3))
    hashMap.put(2, 1)
    print(hashMap.get(2))
    hashMap.remove(2)
    print(hashMap.get(2))

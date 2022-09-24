#
# @lc app=leetcode.cn id=707 lang=python3
#
# [707] 设计链表
#
# 设计链表的实现。您可以选择使用单链表或双链表。单链表中的节点应该具有两个属性：val 和 next。val 是当前节点的值，next 是指向下一个节点的指针/引用。如果要使用双向链表，则还需要一个属性 prev 以指示链表中的上一个节点。假设链表中的所有节点都是 0-index 的。

# 在链表类中实现这些功能：

# get(index)：获取链表中第 index 个节点的值。如果索引无效，则返回-1。
# addAtHead(val)：在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
# addAtTail(val)：将值为 val 的节点追加到链表的最后一个元素。
# addAtIndex(index, val)：在链表中的第 index 个节点之前添加值为 val  的节点。如果 index 等于链表的长度，则该节点将附加到链表的末尾。如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
# deleteAtIndex(index)：如果索引 index 有效，则删除链表中的第 index 个节点。


# 示例：
# MyLinkedList linkedList = new MyLinkedList()
# linkedList.addAtHead(1)
# linkedList.addAtTail(3)
# linkedList.addAtIndex(1, 2)
# //链表变为1 -> 2 -> 3
# linkedList.get(1)
# //返回2
# linkedList.deleteAtIndex(1)
# //现在链表是1 -> 3
# linkedList.get(1)
# //返回3


# 提示：
# 所有val值都在[1, 1000] 之内。
# 操作次数将在[1, 1000] 之内。
# 请不要使用内置的 LinkedList 库。


# @lc code=start
class Node:
    def __init__(self, val: int, next: 'Node') -> None:
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.dummy = Node(-1, None)
        self.tail = self.dummy

    def get(self, index: int) -> int:
        i = 0
        node = self.dummy
        while i <= index and node:
            node = node.next
            i += 1
        return node.val if node else -1

    def addAtHead(self, val: int) -> None:
        node = Node(val, self.dummy.next)
        self.dummy.next = node
        if self.tail == self.dummy:
            self.tail = node

    def addAtTail(self, val: int) -> None:
        node = Node(val, None)
        self.tail.next = node
        self.tail = node

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            self.addAtHead(val)
        else:
            i = 0
            node = self.dummy
            while i < index and node:
                node = node.next
                i += 1
            if node:
                newNode = Node(val, node.next)
                node.next = newNode
                if self.tail == node:
                    self.tail = newNode

    def deleteAtIndex(self, index: int) -> None:
        if index >= 0:
            i = 0
            node = self.dummy
            while i < index and node:
                node = node.next
                i += 1
            if node and node.next:
                if self.tail == node.next:
                    self.tail = node
                node.next = node.next.next


        # Your MyLinkedList object will be instantiated and called as such:
        # obj = MyLinkedList()
        # param_1 = obj.get(index)
        # obj.addAtHead(val)
        # obj.addAtTail(val)
        # obj.addAtIndex(index,val)
        # obj.deleteAtIndex(index)
        # @lc code=end
if __name__ == "__main__":
    linkedList = MyLinkedList()
    linkedList.addAtHead(1)
    linkedList.addAtTail(3)
    linkedList.addAtIndex(1, 2)
    # 链表变为1 -> 2 -> 3
    print(linkedList.get(1))  # 返回2

    linkedList.deleteAtIndex(1)
    # 现在链表是1 -> 3
    print(linkedList.get(1))  # 3

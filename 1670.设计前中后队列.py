#
# @lc app=leetcode.cn id=1670 lang=python3
#
# [1670] 设计前中后队列
#
# 请你设计一个队列，支持在前，中，后三个位置的 push 和 pop 操作。

# 请你完成 FrontMiddleBack 类：

# FrontMiddleBack() 初始化队列。
# void pushFront(int val) 将 val 添加到队列的 最前面 。
# void pushMiddle(int val) 将 val 添加到队列的 正中间 。
# void pushBack(int val) 将 val 添加到队里的 最后面 。
# int popFront() 将 最前面 的元素从队列中删除并返回值，如果删除之前队列为空，那么返回 -1 。
# int popMiddle() 将 正中间 的元素从队列中删除并返回值，如果删除之前队列为空，那么返回 -1 。
# int popBack() 将 最后面 的元素从队列中删除并返回值，如果删除之前队列为空，那么返回 -1 。
# 请注意当有 两个 中间位置的时候，选择靠前面的位置进行操作。比方说：

# 将 6 添加到 [1, 2, 3, 4, 5] 的中间位置，结果数组为 [1, 2, 6, 3, 4, 5] 。
# 从 [1, 2, 3, 4, 5, 6] 的中间位置弹出元素，返回 3 ，数组变为 [1, 2, 4, 5, 6] 。
 

# 示例 1：
# 输入：
# ["FrontMiddleBackQueue", "pushFront", "pushBack", "pushMiddle", "pushMiddle", "popFront", "popMiddle", "popMiddle", "popBack", "popFront"]
# [[], [1], [2], [3], [4], [], [], [], [], []]
# 输出：
# [null, null, null, null, null, 1, 3, 4, 2, -1]

# 解释：
# FrontMiddleBackQueue q = new FrontMiddleBackQueue();
# q.pushFront(1);   // [1]
# q.pushBack(2);    // [1, 2]
# q.pushMiddle(3);  // [1, 3, 2]
# q.pushMiddle(4);  // [1, 4, 3, 2]
# q.popFront();     // 返回 1 -> [4, 3, 2]
# q.popMiddle();    // 返回 3 -> [4, 2]
# q.popMiddle();    // 返回 4 -> [2]
# q.popBack();      // 返回 2 -> []
# q.popFront();     // 返回 -1 -> [] （队列为空）
 

# 提示：
# 1 <= val <= 10^9
# 最多调用 1000 次 pushFront， pushMiddle， pushBack， popFront， popMiddle 和 popBack 。

# @lc code=start
from collections import deque


class FrontMiddleBackQueue:

    def __init__(self):
        self._front = deque()
        self._back = deque()

    def pushFront(self, val: int) -> None:
        self._front.appendleft(val)
        # 判断是否要把前半个队列的末尾放到后半个队列的开头
        self._balance()

    def pushMiddle(self, val: int) -> None:
        if len(self._front) < len(self._back):
            self._front.append(val)
        else:
            self._back.appendleft(val)

    def pushBack(self, val: int) -> None:
        self._back.append(val)
        self._balance()

    def popFront(self) -> int:
        res = -1
        if self._front:
            res = self._front.popleft()
        elif self._back:
            res = self._back.popleft()
        self._balance()
        return res

    def popMiddle(self) -> int:
        f, b = len(self._front), len(self._back)
        res = -1
        if f == b:
            if self._front:
                res = self._front.pop()
        else:
            res = self._back.popleft()
        self._balance()
        return res

    def popBack(self) -> int:
        res = -1
        if self._back:
            res = self._back.pop()
        self._balance()
        return res

    def _balance(self) -> None:
        f, b = len(self._front), len(self._back)
        if f == b or f == b-1:
            return
        elif f > b:
            self._back.appendleft(self._front.pop())
        elif b > f:
            self._front.append(self._back.popleft())


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
# @lc code=end

if __name__ == "__main__":
    q = FrontMiddleBackQueue()
    q.pushFront(1)
    q.pushBack(2)
    q.pushMiddle(3)
    q.pushMiddle(4)
    print(q.popFront()) # 1
    print(q.popMiddle()) # 3
    print(q.popMiddle()) # 4
    print(q.popBack()) # 2
    print(q.popFront()) # -1

#
# @lc app=leetcode.cn id=284 lang=python3
#
# [284] 窥探迭代器
#
# 请你设计一个迭代器，除了支持 hasNext 和 next 操作外，还支持 peek 操作。

# 实现 PeekingIterator 类：

# PeekingIterator(int[] nums) 使用指定整数数组 nums 初始化迭代器。
# int next() 返回数组中的下一个元素，并将指针移动到下个元素处。
# bool hasNext() 如果数组中存在下一个元素，返回 true ；否则，返回 false 。
# int peek() 返回数组中的下一个元素，但 不 移动指针。


# 示例：
# 输入：
# ["PeekingIterator", "next", "peek", "next", "next", "hasNext"]
# [[[1, 2, 3]], [], [], [], [], []]
# 输出：
# [null, 1, 2, 2, 3, false]

# 解释：
# PeekingIterator peekingIterator = new PeekingIterator([1, 2, 3])
# // [1, 2, 3]
# peekingIterator.next()
# // 返回 1 ，指针移动到下一个元素[1, 2, 3]
# peekingIterator.peek()
# // 返回 2 ，指针未发生移动[1, 2, 3]
# peekingIterator.next()
# // 返回 2 ，指针移动到下一个元素[1, 2, 3]
# peekingIterator.next()
# // 返回 3 ，指针移动到下一个元素[1, 2, 3]
# peekingIterator.hasNext()
# // 返回 False


# 提示：
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 1000
# 对 next 和 peek 的调用均有效
# next、hasNext 和 peek 最多调用  1000 次

# 进阶：你将如何拓展你的设计？使之变得通用化，从而适应所有的类型，而不只是整数型？

class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self.data = nums
        self.idx = 0

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        return self.idx < len(self.data)

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        ret = self.data[self.idx]
        self.idx += 1
        return ret


# @lc code=start
# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.it = iterator
        self.peekValue = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.peekValue:
            return self.peekValue
        elif self.it.hasNext():
            self.peekValue = self.it.next()
            return self.peekValue
        else:
            return None

    def next(self):
        """
        :rtype: int
        """
        if self.peekValue:
            ret = self.peekValue
            self.peekValue = None
            return ret
        else:
            return self.it.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.peekValue:
            return True
        else:
            return self.it.hasNext()


# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
# @lc code=end
if __name__ == "__main__":
    iter = PeekingIterator(Iterator([1, 2, 3]))
    print(iter.next())
    print(iter.peek())
    print(iter.next())
    print(iter.next())
    print(iter.hasNext())

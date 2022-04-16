#
# @lc app=leetcode.cn id=385 lang=python3
#
# [385] 迷你语法分析器
#
# 给定一个字符串 s 表示一个整数嵌套列表，实现一个解析它的语法分析器并返回解析的结果 NestedInteger 。

# 列表中的每个元素只可能是整数或整数嵌套列表


# 示例 1：
# 输入：s = "324",
# 输出：324
# 解释：你应该返回一个 NestedInteger 对象，其中只包含整数值 324。

# 示例 2：
# 输入：s = "[123,[456,[789]]]",
# 输出：[123,[456,[789]]]
# 解释：返回一个 NestedInteger 对象包含一个有两个元素的嵌套列表：
# 1. 一个 integer 包含值 123
# 2. 一个包含两个元素的嵌套列表：
#     i.  一个 integer 包含值 456
#     ii. 一个包含一个元素的嵌套列表
#          a. 一个 integer 包含值 789


# 提示：
# 1 <= s.length <= 5 * 10^4
# s 由数字、方括号 "[]"、负号 '-' 、逗号 ','组成
# 用例保证 s 是可解析的 NestedInteger
# 输入中的所有值的范围是 [-10^6, 10^6]

class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """
        self.value = self.list = None
        if value:
            self.value = value
        else:
            self.list = []

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        return self.value is not None

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """
        if self.list is None:
            self.list = []
        if self.value is not None:
            self.list.append(NestedInteger(self.value))
            self.value = None
        self.list.append(elem)

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """
        self.value = value

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        if self.list is not None:
            return None
        return self.value

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        if self.value is not None:
            return None
        return self.list

    def __str__(self) -> str:
        if self.value is not None:
            return str(self.value)
        elif self.list is not None:
            return '[' + ','.join([str(item) for item in self.list]) + ']'
        else:
            return 'None'

# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        stack = []
        pointer = 0
        for i, c in enumerate(s):
            if c.isdigit() or c == '-':
                # 数字的一部分
                pass
            else:
                if i > pointer:
                    num = int(s[pointer:i])
                    ni = NestedInteger(num)
                    if stack:
                        stack[-1].add(ni)
                    else:
                        stack.append(ni)
                pointer = i+1
                if c == '[':
                    ni = NestedInteger()
                    if stack:
                        stack[-1].add(ni)
                    stack.append(ni)
                elif c == ']':
                    if len(stack) > 1:
                        # 最后一个保持不出栈
                        stack.pop()

        if pointer < len(s):
            num = int(s[pointer:])
            stack.append(NestedInteger(num))
        return stack[0]

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.deserialize("324"))
    print(solution.deserialize("[123,[456,[789]]]"))

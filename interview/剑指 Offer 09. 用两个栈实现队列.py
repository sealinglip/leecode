#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: 
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。
(若队列中没有元素，deleteHead 操作返回 -1 )


示例 1：

输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]
示例 2：

输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]
提示：

1 <= values <= 10000
最多会对 appendTail、deleteHead 进行 10000 次调用

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

@Author: Thomas Young
@Date: 2020-06-30 10:26:34
@LastEditors: Thomas Young
@LastEditTime: 2020-06-30 10:26:35
'''


class CQueue:

    def __init__(self):
        self.s_in = []
        self.s_out = []

    def appendTail(self, value: int) -> None:
        self.s_in.append(value)

    def deleteHead(self) -> int:
        if self.s_out:
            return self.s_out.pop()
        elif self.s_in:
            while self.s_in:
                self.s_out.append(self.s_in.pop())
            return self.deleteHead()
        else:
            return -1

if __name__ == "__main__":
    # Your CQueue object will be instantiated and called as such:
    # obj = CQueue()
    # obj.appendTail(value)
    # param_2 = obj.deleteHead()
    pass

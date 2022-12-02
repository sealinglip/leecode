#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Description: file content
Author: Thomas Young
Date: 2022-11-30 08:59:55
LastEditors: Thomas Young
LastEditTime: 2022-11-30 22:38:00
'''
#
# @lc app=leetcode.cn id=895 lang=python3
#
# [895] 最大频率栈
#
# 设计一个类似堆栈的数据结构，将元素推入堆栈，并从堆栈中弹出出现频率最高的元素。

# 实现 FreqStack 类:

# FreqStack() 构造一个空的堆栈。
# void push(int val) 将一个整数 val 压入栈顶。
# int pop() 删除并返回堆栈中出现频率最高的元素。
# 如果出现频率最高的元素不只一个，则移除并返回最接近栈顶的元素。
 

# 示例 1：
# 输入：
# ["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
# [[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
# 输出：[null,null,null,null,null,null,null,5,7,5,4]
# 解释：
# FreqStack = new FreqStack();
# freqStack.push (5);//堆栈为 [5]
# freqStack.push (7);//堆栈是 [5,7]
# freqStack.push (5);//堆栈是 [5,7,5]
# freqStack.push (7);//堆栈是 [5,7,5,7]
# freqStack.push (4);//堆栈是 [5,7,5,7,4]
# freqStack.push (5);//堆栈是 [5,7,5,7,4,5]
# freqStack.pop ();//返回 5 ，因为 5 出现频率最高。堆栈变成 [5,7,5,7,4]。
# freqStack.pop ();//返回 7 ，因为 5 和 7 出现频率最高，但7最接近顶部。堆栈变成 [5,7,5,4]。
# freqStack.pop ();//返回 5 ，因为 5 出现频率最高。堆栈变成 [5,7,4]。
# freqStack.pop ();//返回 4 ，因为 4, 5 和 7 出现频率最高，但 4 是最接近顶部的。堆栈变成 [5,7]。
 

# 提示：
# 0 <= val <= 10^9
# push 和 pop 的操作数不大于 2 * 10^4。
# 输入保证在调用 pop 之前堆栈中至少有一个元素。

# Hard

from collections import defaultdict

# @lc code=start

class FreqStack:

    def __init__(self):
        self.cnt = defaultdict(int)
        self.buckets = defaultdict(list)
        self.maxFreq = 0

    def push(self, val: int) -> None:
        curCnt = self.cnt[val] + 1
        self.buckets[curCnt].append(val) # 添加到数量对应桶里
        self.cnt[val] = curCnt
        self.maxFreq = max(self.maxFreq, curCnt)

    def pop(self) -> int:
        val = self.buckets[self.maxFreq].pop()
        if not self.buckets[self.maxFreq]:
            # 已经空了的话
            self.maxFreq -= 1
        self.cnt[val] -= 1
        return val




# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
# @lc code=end

if __name__ == "__main__":
    st = FreqStack()
    st.push(5)
    st.push(7)
    st.push(5)
    st.push(7)
    st.push(4)
    st.push(5)
    print(st.pop()) # 5
    print(st.pop()) # 7
    print(st.pop()) # 5
    print(st.pop()) # 4

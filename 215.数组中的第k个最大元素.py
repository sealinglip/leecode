#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@Description: file content
@Author: Thomas Young
@Date: 2020-06-29 10:15:43
@LastEditors: Thomas Young
@LastEditTime: 2020-06-29 12:09:09
'''
#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#
from typing import List
# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums or not k:
            return None
        # 采用小顶堆来解决
        topK, size = [None for i in range(k)], 0
        def siftup(i: int, n: int):
            while i > 0:
                parent = (i - 1) >> 1
                p = topK[parent]
                if n >= p:
                    break
                topK[i] = p
                i = parent
            topK[i] = n

        def siftdown(i: int, n: int):
            half = k >> 1
            while i < half:
                child = (i << 1) + 1
                c = topK[child]
                right = child + 1
                if right < size and c > topK[right]: # 取左右节点里的小值
                    child = right
                    c = topK[right]
                if n <= c:
                    break
                topK[i] = c
                i = child
            topK[i] = n

        def offer(n: int):
            nonlocal size
            i = size
            if size < k:
                size += 1
            if i == 0:
                topK[0] = n
            elif i < k:
                siftup(i, n)
            elif n > topK[0]:
                siftdown(0, n)

        for num in nums:
            offer(num)
        
        return topK[0]

# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.findKthLargest([3, 1, 2, 4], 2))
    # print(solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
    # print(solution.findKthLargest([3, 2, 1, 5, 6, 4], 2))

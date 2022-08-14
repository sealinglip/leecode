#
# @lc app=leetcode.cn id=768 lang=python3
#
# [768] 最多能完成排序的块 II
#
# 这个问题和“最多能完成排序的块”相似，但给定数组中的元素可以重复，输入数组最大长度为2000，其中的元素最大为10^8。

# arr是一个可能包含重复元素的整数数组，我们将这个数组分割成几个“块”，并将这些块分别进行排序。之后再连接起来，使得连接的结果和按升序排序后的原数组相同。

# 我们最多能将数组分成多少块？

# 示例 1:
# 输入: arr = [5, 4, 3, 2, 1]
# 输出: 1
# 解释:
# 将数组分成2块或者更多块，都无法得到所需的结果。
# 例如，分成[5, 4], [3, 2, 1] 的结果是[4, 5, 1, 2, 3]，这不是有序的数组。

# 示例 2:
# 输入: arr = [2, 1, 3, 4, 4]
# 输出: 4
# 解释:
# 我们可以把它分成两块，例如[2, 1], [3, 4, 4]。
# 然而，分成[2, 1], [3], [4], [4] 可以得到最多的块数。

# 注意:
# arr的长度在[1, 2000]之间。
# arr[i]的大小在[0, 10**8]之间。

# Hard

from inspect import stack
from typing import List
# @lc code=start


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # 方法1：计数
        # sortedArr = sorted(arr)  # 排序
        # cnt = 0
        # diff = {}
        # for s, c in zip(arr, sortedArr):
        #     diff[s] = diff.get(s, 0) + 1
        #     if diff[s] == 0:
        #         del diff[s]
        #     diff[c] = diff.get(c, 0) - 1
        #     if diff[c] == 0:
        #         del diff[c]
        #     if len(diff) == 0:
        #         cnt += 1

        # return cnt

        # 方法2：单调栈
        # 复习
        # 一个可行的切割，每一块中的每个元素都应该大于等于前一块中的最大元素
        # 对于一个已经分好块的数组，如果在其末尾添加一个数字，新的分块该如何？
        # 如果添加的数大于等于最后一个块的最大值，那么新添加的可以自成一块；
        # 如果添加的数小于最后一块的最大值，它必须合并到已经存在的块中，究竟是要合并前面的多少块，就要看
        # 添加的数和前面的块依次去比较的结果而定，只要最大值比添加数大的块，都需要合并。
        # 所以，维护一个栈记录当前划分的每一块中最大的数，从头往后推
        stack = []
        for n in arr:
            if not stack or n >= stack[-1]:
                stack.append(n)
            else:
                top = stack.pop()  # 当前划分最后一块的最大值
                while stack and stack[-1] > n:
                    stack.pop()
                stack.append(top)

        return len(stack)


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxChunksToSorted([5, 4, 3, 2, 1]))  # 1
    print(solution.maxChunksToSorted([2, 1, 3, 4, 4]))  # 4

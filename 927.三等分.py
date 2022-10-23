#
# @lc app=leetcode.cn id=927 lang=python3
#
# [927] 三等分
#
# 给定一个由 0 和 1 组成的数组 arr ，将数组分成  3 个非空的部分 ，使得所有这些部分表示相同的二进制值。

# 如果可以做到，请返回任何[i, j]，其中 i+1 < j，这样一来：

# arr[0], arr[1], ..., arr[i] 为第一部分；
# arr[i + 1], arr[i + 2], ..., arr[j - 1] 为第二部分；
# arr[j], arr[j + 1], ..., arr[arr.length - 1] 为第三部分。
# 这三个部分所表示的二进制值相等。
# 如果无法做到，就返回[-1, -1]。

# 注意，在考虑每个部分所表示的二进制时，应当将其看作一个整体。例如，[1, 1, 0] 表示十进制中的 6，而不会是 3。
# 此外，前导零也是被允许的，所以[0, 1, 1] 和[1, 1] 表示相同的值。


# 示例 1：
# 输入：arr = [1, 0, 1, 0, 1]
# 输出：[0, 3]

# 示例 2：
# 输入：arr = [1, 1, 0, 1, 1]
# 输出：[-1, -1]

# 示例 3:
# 输入：arr = [1, 1, 0, 0, 1]
# 输出：[0, 2]


# 提示：
# 3 <= arr.length <= 3 * 10^4
# arr[i] 是 0 或 1

# Hard
# 复习

from typing import List
# @lc code=start


class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        n = len(arr)
        # 每个分段中1的个数应该是一样的
        ones = arr.count(1)  # 1的个数
        if ones % 3 != 0:  # 不能均分的情况
            return [-1, -1]
        elif ones == 0:
            # 全是0，糊弄一下算了
            return [0, n-1]

        onePiece = ones // 3
        tailZero = cntOne = 0  # 默尾零的个数，一的个数

        # 从后往前，找onePiece个1，确认够不够位置留末尾的零
        zero = True
        i = j = iMax = jMax = -1
        for k in range(n-1, -1, -1):
            bit = arr[k]
            if bit == 0:
                if zero:
                    tailZero += 1
            else:
                zero = False
                cntOne += 1
                if cntOne == onePiece:
                    jMax = k
                elif cntOne == onePiece + 1:
                    j = k + tailZero + 1
                    if j > jMax:  # 第二段不够摆末尾的零
                        return [-1, -1]
                if cntOne == (onePiece << 1):
                    iMax = k - 1
                elif cntOne == (onePiece << 1) + 1:
                    i = k + tailZero
                    if i > iMax:
                        return [-1, -1]  # 第一段不够摆末尾的零
                    break
        if arr[jMax:] != arr[iMax+1:j] or arr[jMax:] != arr[i+1-n+jMax:i+1]:
            return [-1, -1]
        return [i, j]


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.threeEqualParts([1, 0, 1, 0, 1]))  # [0,3]
    print(solution.threeEqualParts([1, 1, 0, 1, 1]))  # [-1,-1]
    print(solution.threeEqualParts([1, 1, 0, 0, 1]))  # [0,2]
    print(solution.threeEqualParts([0, 0, 0, 0, 0]))  # [0,4]

#
# @lc app=leetcode.cn id=1073 lang=python3
#
# [1073] 负二进制数相加
#
# 给出基数为 - 2 的两个数 arr1 和 arr2，返回两数相加的结果。

# 数字以 数组形式 给出：数组由若干 0 和 1 组成，按最高有效位到最低有效位的顺序排列。例如，arr = [1, 1, 0, 1] 表示数字(-2) ^ 3 + (-2) ^ 2 + (-2) ^ 0 = -3。数组形式 中的数字 arr 也同样不含前导零：即 arr == [0] 或 arr[0] == 1。

# 返回相同表示形式的 arr1 和 arr2 相加的结果。两数的表示形式为：不含前导零、由若干 0 和 1 组成的数组。


# 示例 1：
# 输入：arr1 = [1, 1, 1, 1, 1], arr2 = [1, 0, 1]
# 输出：[1, 0, 0, 0, 0]
# 解释：arr1 表示 11，arr2 表示 5，输出表示 16 。

# 示例 2：
# 输入：arr1 = [0], arr2 = [0]
# 输出：[0]

# 示例 3：
# 输入：arr1 = [0], arr2 = [1]
# 输出：[1]


# 提示：
# 1 <= arr1.length, arr2.length <= 1000
# arr1[i] 和 arr2[i] 都是 0 或 1
# arr1 和 arr2 都没有前导0


from typing import List
# @lc code=start


class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        i, j = len(arr1) - 1, len(arr2) - 1
        carry = 0  # 进位
        res = []

        while i >= 0 or j >= 0 or carry:
            tmp = carry
            if i >= 0:
                tmp += arr1[i]
            if j >= 0:
                tmp += arr2[j]

            if tmp >= 2:  # 有进位
                res.append(tmp - 2)
                carry = -1
            elif tmp >= 0:
                res.append(tmp)
                carry = 0
            else:  # 小于0的情况，只能是-1
                res.append(1)  # 设为1，那么实际还有-2，进位就变成1
                carry = 1
            i -= 1
            j -= 1

        # 去掉前端0
        while len(res) > 1 and res[-1] == 0:
            res.pop()

        return res[::-1]

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.addNegabinary([1, 1, 1, 1, 1], [1, 0, 1]))  # [1,0,0,0,0]
    print(solution.addNegabinary([0], [0]))  # [0]
    print(solution.addNegabinary([0], [1]))  # [1]

#
# @lc app=leetcode.cn id=1089 lang=python3
#
# [1089] 复写零
#
# 给你一个长度固定的整数数组 arr，请你将该数组中出现的每个零都复写一遍，并将其余的元素向右平移。

# 注意：请不要在超过该数组长度的位置写入元素。

# 要求：请对输入的数组 就地 进行上述修改，不要从函数返回任何东西。


# 示例 1：
# 输入：[1, 0, 2, 3, 0, 4, 5, 0]
# 输出：null
# 解释：调用函数后，输入的数组将被修改为：[1, 0, 0, 2, 3, 0, 0, 4]

# 示例 2：
# 输入：[1, 2, 3]
# 输出：null
# 解释：调用函数后，输入的数组将被修改为：[1, 2, 3]


# 提示：
# 1 <= arr.length <= 10000
# 0 <= arr[i] <= 9


from typing import List
# @lc code=start


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        # 从头往后扫一遍，看看能装到多少
        i = -1
        top = 0
        while top < n:
            i += 1
            top += 1 if arr[i] else 2
        # 此时 i 指向复写零后数组的最后一个元素当前的位置
        j = n - 1
        if top == n + 1:  # 最后一个元素是0
            arr[j] = 0
            j -= 1
            i -= 1

        while i >= 0:
            arr[j] = arr[i]
            j -= 1
            if arr[i] == 0:
                arr[j] = 0
                j -= 1
            i -= 1


# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    l = [0, 1, 7, 6, 0, 2, 0, 7]
    solution.duplicateZeros(l)
    print(l)  # [0,0,1,7,6,0,0,2]
    l = [1, 0, 2, 3, 0, 4, 5, 0]
    solution.duplicateZeros(l)
    print(l)  # [1, 0, 0, 2, 3, 0, 0, 4]
    l = [1, 2, 3]
    solution.duplicateZeros(l)
    print(l)  # [1, 2, 3]

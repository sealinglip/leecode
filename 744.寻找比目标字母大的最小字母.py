#
# @lc app=leetcode.cn id=744 lang=python3
#
# [744] 寻找比目标字母大的最小字母
#
# 给你一个排序后的字符列表 letters ，列表中只包含小写英文字母。另给出一个目标字母 target，请你寻找在这一有序列表里比目标字母大的最小字母。

# 在比较时，字母是依序循环出现的。举个例子：

# 如果目标字母 target = 'z' 并且字符列表为 letters = ['a', 'b']，则答案返回 'a'


# 示例 1：

# 输入: letters = ["c", "f", "j"]，target = "a"
# 输出: "c"
# 示例 2:

# 输入: letters = ["c", "f", "j"], target = "c"
# 输出: "f"
# 示例 3:

# 输入: letters = ["c", "f", "j"], target = "d"
# 输出: "f"


# 提示：
# 2 <= letters.length <= 104
# letters[i] 是一个小写字母
# letters 按非递减顺序排序
# letters 最少包含两个不同的字母
# target 是一个小写字母


from typing import List
# @lc code=start
from bisect import bisect_right


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        i = bisect_right(letters, target)
        if i == len(letters):
            i = 0
        return letters[i]


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.nextGreatestLetter(['a', 'b'], 'z'))  # a
    print(solution.nextGreatestLetter(["c", "f", "j"], "a"))  # c
    print(solution.nextGreatestLetter(["c", "f", "j"], "c"))  # f
    print(solution.nextGreatestLetter(["c", "f", "j"], "d"))  # f

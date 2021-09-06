#
# @lc app=leetcode.cn id=171 lang=python3
#
# [171] Excel表列序号
#
# 给定一个Excel表格中的列名称，返回其相应的列序号。

# 例如，

# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28
# ...

# 示例 1:
# 输入: "A"
# 输出: 1

# 示例 2:
# 输入: "AB"
# 输出: 28

# 示例 3:
# 输入: "ZY"
# 输出: 701

# @lc code=start
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        idx = 0
        for c in columnTitle:
            idx = (idx * 26) + ord(c) - ord('A') + 1
        return idx

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.titleToNumber('A'))
    print(solution.titleToNumber('AB'))
    print(solution.titleToNumber('ZY'))

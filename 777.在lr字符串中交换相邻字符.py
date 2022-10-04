#
# @lc app=leetcode.cn id=777 lang=python3
#
# [777] 在LR字符串中交换相邻字符
#
# 在一个由 'L', 'R' 和 'X' 三个字符组成的字符串（例如"RXXLRXRXL"）中进行移动操作。一次移动操作指用一个"LX"替换一个"XL"，或者用一个"XR"替换一个"RX"。现给定起始字符串start和结束字符串end，请编写代码，当且仅当存在一系列移动操作使得start可以转换成end时， 返回True。


# 示例:
# 输入: start = "RXXLRXRXL", end = "XRLXXRRLX"
# 输出: True
# 解释:
# 我们可以通过以下几步将start转换成end:
# RXXLRXRXL ->
# XRXLRXRXL ->
# XRLXRXRXL ->
# XRLXXRRXL ->
# XRLXXRRLX


# 提示：
# 1 <= len(start) = len(end) <= 10000。
# start和end中的字符串仅限于'L', 'R'和'X'。


# @lc code=start
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        # 从交换规则可知，L和R没有办法变相地交换前后顺序
        # L只能向左移动，R只能向右移动
        # 从左至右遍历，非x字符是否为L、R且对应位置要相同
        n = len(start)
        if n == len(end):
            i = j = 0  # 分别对应两个指针，指向start和end
            while i < n and j < n:
                while i < n and start[i] == 'X':
                    i += 1
                while j < n and end[j] == 'X':
                    j += 1
                if i < n and j < n:
                    if start[i] != end[j]:
                        return False
                    c = start[i]
                    if (c == 'L' and i < j) or (c == 'R' and i > j):
                        # 对应 L只能往左，R只能往右
                        return False
                    i += 1
                    j += 1
            while i < n:
                # 剩余必须都是X
                if start[i] != 'X':
                    return False
                i += 1
            while j < n:
                if end[j] != 'X':
                    return False
                j += 1
            return True
        else:
            return False


# @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.canTransform("XXXXXLXXXX", "LXXXXXXXXX"))  # True
    print(solution.canTransform("LXXLXRLXXL", "XLLXRXLXLX"))  # False
    print(solution.canTransform("XLLR", "LXLX"))  # False
    print(solution.canTransform("X", "L"))  # False
    print(solution.canTransform("RXXLRXRXL", "XRLXXRRLX"))  # True
    print(solution.canTransform("RXXLRXRXL", "XLLXXRRLX"))  # False

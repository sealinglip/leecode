#
# @lc app=leetcode.cn id=1542 lang=python3
#
# [1542] 找出最长的超赞子字符串
#
# 给你一个字符串 s 。请返回 s 中最长的 超赞子字符串 的长度。

# 「超赞子字符串」需满足满足下述两个条件：

# 该字符串是 s 的一个非空子字符串
# 进行任意次数的字符交换后，该字符串可以变成一个回文字符串
 

# 示例 1：
# 输入：s = "3242415"
# 输出：5
# 解释："24241" 是最长的超赞子字符串，交换其中的字符后，可以得到回文 "24142"

# 示例 2：
# 输入：s = "12345678"
# 输出：1

# 示例 3：
# 输入：s = "213123"
# 输出：6
# 解释："213123" 是最长的超赞子字符串，交换其中的字符后，可以得到回文 "231132"

# 示例 4：
# 输入：s = "00"
# 输出：2

# 提示：
# 1 <= s.length <= 10^5
# s 仅由数字组成

# Hard

# @lc code=start
class Solution:
    def longestAwesome(self, s: str) -> int:
        # 就十个数，用十个bit来表示前缀字符串中各数字数量的奇偶性
        flag = 0 # 起始为0
        posMap = {0: -1}
        res = 0
        for i, c in enumerate(s):
            d = 1 << int(c)
            flag ^= d
            if flag in posMap:
                res = max(res, i - posMap[flag])
            else:
                posMap[flag] = i
            # 遍历跟flag只差1位的数 —— 这样搞会TLE
            # for f in posMap.keys():
            # 换个思路，只遍历跟flag差一位的数，看看posMap里有没有
            for j in range(10):
                f = flag ^ (1 << j)
                if f in posMap:
                    res = max(res, i - posMap[f])
        return res
    
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.longestAwesome("3242415")) # 5
    print(solution.longestAwesome("12345678")) # 1
    print(solution.longestAwesome("213123")) # 6
    print(solution.longestAwesome("00")) # 2
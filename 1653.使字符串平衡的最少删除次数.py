#
# @lc app=leetcode.cn id=1653 lang=python3
#
# [1653] 使字符串平衡的最少删除次数
#
# 给你一个字符串 s ，它仅包含字符 'a' 和 'b'​​​​ 。

# 你可以删除 s 中任意数目的字符，使得 s 平衡 。当不存在下标对 (i,j) 满足 i < j ，且 s[i] = 'b' 的同时 s[j]= 'a' ，此时认为 s 是 平衡 的。

# 请你返回使 s 平衡 的 最少 删除次数。


# 示例 1：
# 输入：s = "aababbab"
# 输出：2
# 解释：你可以选择以下任意一种方案：
# 下标从 0 开始，删除第 2 和第 6 个字符（"aababbab" -> "aaabbb"），
# 下标从 0 开始，删除第 3 和第 6 个字符（"aababbab" -> "aabbbb"）。

# 示例 2：
# 输入：s = "bbaaaaabb"
# 输出：2
# 解释：唯一的最优解是删除最前面两个字符。


# 提示：
# 1 <= s.length <= 10^5
# s[i] 要么是 'a' 要么是 'b'。

# 复习
# 把删理解成翻转，本题就类似[926]题

# @lc code=start
class Solution:
    def minimumDeletions(self, s: str) -> int:
        # # 贪心：本质上是求最长非递减子序列长度
        # a, b = 0, 0
        # for c in s:
        #     if c == 'b':
        #         b += 1
        #     else:
        #         if b > 0:
        #             b -= 1
        #         a += 1
        # return len(s) - a - b

        # 动态规划
        # 把删除当成翻转来处理，等效的
        dpa = dpb = 0
        for c in s:
            dpaTmp, dpbTmp = dpa, min(dpa, dpb)
            if c == 'b':
                dpaTmp += 1
            else:
                dpbTmp += 1
            dpa, dpb = dpaTmp, dpbTmp
        return min(dpa, dpb)

        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumDeletions("aaabbb"))  # 0
    print(solution.minimumDeletions("aababbab"))  # 2
    print(solution.minimumDeletions("bbaaaaabb"))  # 2

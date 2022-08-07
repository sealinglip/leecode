#
# @lc app=leetcode.cn id=899 lang=python3
#
# [899] 有序队列
#
# 给定一个字符串 s 和一个整数 k 。你可以从 s 的前 k 个字母中选择一个，并把它加到字符串的末尾。
# 返回 在应用上述步骤的任意数量的移动后，字典上最小的字符串 。


# 示例 1：
# 输入：s = "cba", k = 1
# 输出："acb"
# 解释：
# 在第一步中，我们将第一个字符（“c”）移动到最后，获得字符串 “bac”。
# 在第二步中，我们将第一个字符（“b”）移动到最后，获得最终结果 “acb”。

# 示例 2：
# 输入：s = "baaca", k = 3
# 输出："aaabc"
# 解释：
# 在第一步中，我们将第一个字符（“b”）移动到最后，获得字符串 “aacab”。
# 在第二步中，我们将第三个字符（“c”）移动到最后，获得最终结果 “aaabc”。


# 提示：
# 1 <= k <= S.length <= 1000
# s 只由小写字母组成。

# Hard
# @lc code=start


class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        # 大顶堆不行吗？还真不行，因为并不是把前k个里最大的拿出来，放到最后就可以；这样能保证s[:k]是最小的，但s[k:]保证不了是最小的
        # 但如果k大于1，是否就可以获得最佳排列呢？因为k大于1就能交换相邻两个元素——这是冒泡排序的充要条件
        if k == 1:
            res = s
            for _ in range(len(s) - 1):
                s = s[1:] + s[0:1]
                res = min(res, s)
            return res
        else:
            return "".join(sorted(s))

            # @lc code=end

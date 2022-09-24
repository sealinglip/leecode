#
# @lc app=leetcode.cn id=854 lang=python3
#
# [854] 相似度为 K 的字符串
#
# 对于某些非负整数 k ，如果交换 s1 中两个字母的位置恰好 k 次，能够使结果字符串等于 s2 ，则认为字符串 s1 和 s2 的 相似度为 k 。

# 给你两个字母异位词 s1 和 s2 ，返回 s1 和 s2 的相似度 k 的最小值。


# 示例 1：
# 输入：s1 = "ab", s2 = "ba"
# 输出：1

# 示例 2：
# 输入：s1 = "abc", s2 = "bca"
# 输出：2


# 提示：
# 1 <= s1.length <= 20
# s2.length == s1.length
# s1 和 s2  只包含集合 {'a', 'b', 'c', 'd', 'e', 'f'} 中的小写字母
# s2 是 s1 的一个字母异位词

# Hard
# 复习

# @lc code=start
class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        # 拟采用广度优先遍历算法
        step, n = 0, len(s1)
        q, vis = [(s1, 0)], {s1}
        while True:
            tmp = q
            q = []
            for s, i in tmp:
                if s == s2:
                    return step
                while i < n and s[i] == s2[i]:
                    i += 1
                for j in range(i + 1, n):
                    if s[j] == s2[i] != s2[j]:
                        t = list(s)
                        t[i], t[j] = t[j], t[i]
                        t = ''.join(t)
                        if t not in vis:
                            vis.add(t)
                            q.append((t, i + 1))
            step += 1

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.kSimilarity("ab", "ba"))  # 1
    print(solution.kSimilarity("abc", "bca"))  # 2

#
# @lc app=leetcode.cn id=1147 lang=python3
#
# [1147] 段式回文
#
# 你会得到一个字符串 text 。你应该把它分成 k 个子字符串(subtext1, subtext2，…， subtextk) ，要求满足:

# subtexti 是 非空 字符串
# 所有子字符串的连接等于 text(即subtext1 + subtext2 + ... + subtextk == text)
# 对于所有 i 的有效值(即 1 <= i <= k) ，subtexti == subtextk - i + 1 均成立
# 返回k可能最大值。


# 示例 1：
# 输入：text = "ghiabcdefhelloadamhelloabcdefghi"
# 输出：7
# 解释：我们可以把字符串拆分成 "(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)"。

# 示例 2：
# 输入：text = "merchant"
# 输出：1
# 解释：我们可以把字符串拆分成 "(merchant)"。

# 示例 3：
# 输入：text = "antaprezatepzapreanta"
# 输出：11
# 解释：我们可以把字符串拆分成 "(a)(nt)(a)(pre)(za)(tpe)(za)(pre)(a)(nt)(a)"。


# 提示：
# 1 <= text.length <= 1000
# text 仅由小写英文字符组成

# Hard
# 复习

# @lc code=start
class Solution:
    def longestDecomposition(self, text: str) -> int:
        n = len(text)
        # 双指针回溯，变相dfs
        # 下面的解法会TLE——实际上不需要回溯，无需stack
        # 能判断出无需回溯才是需要功力的啊
        l = s = 0
        r = n - 1
        res = 0
        # stack = []
        stack = 0
        while l <= r:
            # 从位置l（含）往后找text[r]
            tmp = text.find(text[r], s)
            if tmp == r:
                # 划分完毕
                res = max(res, stack * 2 + 1)
                break
            elif text[l:tmp+1] == text[r-tmp+l:r+1]:
                # 判断text[l:tmp+1] == text[r-tmp+l:r+1]
                # print(text[l:tmp+1])
                if (tmp << 1) == l + r - 1:  # 划分完毕
                    res = max(res, stack * 2 + 2)
                    break
                else:
                    stack += 1
                    l, r, s = tmp+1, l+r-tmp-1, tmp+1
            else:
                s = tmp+1

        return res

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.longestDecomposition(
        "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))  # 1000
    print(solution.longestDecomposition(
        "bqrcnnqrcb"))  # 6
    print(solution.longestDecomposition(
        "vnviixzsftjnsxyhjkziucnqvoeldaxwkmmgtozuopjzzmdzodebgegdzjhvnbkxwbgwxwtqgsxijnjkhebqidvoemogjmytfyxabywywmlrergrpseqlmjyglddncxiqjizebgxiwpeinukyqdtktgdlgxyqvslfpdwnqnlppqjiqlhlaosmlmogsmkubfviqmdgx"))  # 1
    print(solution.longestDecomposition(
        "elvtoelvto"))  # 2
    print(solution.longestDecomposition(
        "aaa"))  # 3
    print(solution.longestDecomposition(
        "ghiabcdefhelloadamhelloabcdefghi"))  # 7
    print(solution.longestDecomposition("merchant"))  # 1
    print(solution.longestDecomposition("antaprezatepzapreanta"))  # 11

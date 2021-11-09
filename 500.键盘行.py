#
# @lc app=leetcode.cn id=500 lang=python3
#
# [500] 键盘行
#
# 给你一个字符串数组 words ，只返回可以使用在 美式键盘 同一行的字母打印出来的单词。键盘如下图所示。

# 美式键盘 中：

# 第一行由字符 "qwertyuiop" 组成。
# 第二行由字符 "asdfghjkl" 组成。
# 第三行由字符 "zxcvbnm" 组成。
# American keyboard

# 示例 1：
# 输入：words = ["Hello", "Alaska", "Dad", "Peace"]
# 输出：["Alaska", "Dad"]

# 示例 2：
# 输入：words = ["omk"]
# 输出：[]

# 示例 3：
# 输入：words = ["adsdf", "sfd"]
# 输出：["adsdf", "sfd"]

# 提示：
# 1 <= words.length <= 20
# 1 <= words[i].length <= 100
# words[i] 由英文字母（小写和大写字母）组成


from typing import List
# @lc code=start


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        lines = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
        res = []
        for w in words:
            # 先找第一个字母在哪一行
            lw = w.lower()
            l = -1
            for line in lines:
                l += 1
                if lw[0] in line:
                    break

            line = lines[l]
            match = True
            for c in lw[1:]:
                if c not in line:
                    match = False
                    break

            if match:
                res.append(w)

        return res


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    # ["Alaska","Dad"]
    print(solution.findWords(["Hello", "Alaska", "Dad", "Peace"]))
    print(solution.findWords(["omk"]))  # []
    print(solution.findWords(["adsdf", "sfd"]))  # ["adsdf","sfd"]

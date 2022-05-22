#
# @lc app=leetcode.cn id=691 lang=python3
#
# [691] 贴纸拼词
#
# 我们有 n 种不同的贴纸。每个贴纸上都有一个小写的英文单词。

# 您想要拼写出给定的字符串 target ，方法是从收集的贴纸中切割单个字母并重新排列它们。如果你愿意，你可以多次使用每个贴纸，每个贴纸的数量是无限的。

# 返回你需要拼出 target 的最小贴纸数量。如果任务不可能，则返回 - 1 。

# 注意：在所有的测试用例中，所有的单词都是从 1000 个最常见的美国英语单词中随机选择的，并且 target 被选择为两个随机单词的连接。


# 示例 1：
# 输入： stickers = ["with", "example", "science"], target = "thehat"
# 输出：3
# 解释：
# 我们可以使用 2 个 "with" 贴纸，和 1 个 "example" 贴纸。
# 把贴纸上的字母剪下来并重新排列后，就可以形成目标 “thehat“ 了。
# 此外，这是形成目标字符串所需的最小贴纸数量。

# 示例 2:
# 输入：stickers = ["notice", "possible"], target = "basicbasic"
# 输出：- 1
# 解释：我们不能通过剪切给定贴纸的字母来形成目标“basicbasic”。


# 提示:
# n == stickers.length
# 1 <= n <= 50
# 1 <= stickers[i].length <= 10
# 1 <= target <= 15
# stickers[i] 和 target 由小写英文单词组成


# Hard
# 复习
from functools import cache
from typing import List
from collections import Counter
# @lc code=start


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        # 因为target的长度小于15，所以可以用整型来描述其子序列，mask
        n = len(target)

        @cache
        def dp(mask: int) -> int:
            '''
            mask代表的子序列的最优解（最少贴纸数）
            mask的某位为1代表这一位对应的字符在子序列中
            '''
            if mask == 0:
                return 0
            res = n + 1  # 这里将初始值设为n+1是如果该题有解，贴纸数最多也就是总字符数n，所以初始值设为一个可以表征无解的情况
            for sticker in stickers:
                left = mask  # 剩下没匹配的
                cnt = Counter(sticker)
                for i, c in enumerate(target):
                    if (mask >> i) & 1 and cnt[c]:
                        cnt[c] -= 1
                        left ^= 1 << i
                if left < mask:
                    res = min(res, dp(left) + 1)
            return res

        res = dp((1 << n) - 1)  # 起始mask 为(1 << n) - 1
        return res if res <= n else -1

        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.minStickers(
        ["with", "example", "science"], "thehat"))  # 3
    print(solution.minStickers(
        ["notice", "possible"], "basicbasic"))  # -1

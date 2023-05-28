#
# @lc app=leetcode.cn id=2423 lang=python3
#
# [2423] 删除字符使频率相同
#
# 给你一个下标从 0 开始的字符串 word ，字符串只包含小写英文字母。你需要选择 一个 下标并 删除 下标处的字符，使得 word 中剩余每个字母出现 频率 相同。

# 如果删除一个字母后，word 中剩余所有字母的出现频率都相同，那么返回 true ，否则返回 false 。

# 注意：

# 字母 x 的 频率 是这个字母在字符串中出现的次数。
# 你 必须 恰好删除一个字母，不能一个字母都不删除。


# 示例 1：
# 输入：word = "abcc"
# 输出：true
# 解释：选择下标 3 并删除该字母，word 变成 "abc" 且每个字母出现频率都为 1 。

# 示例 2：
# 输入：word = "aazz"
# 输出：false
# 解释：我们必须删除一个字母，所以要么 "a" 的频率变为 1 且 "z" 的频率为 2 ，要么两个字母频率反过来。所以不可能让剩余所有字母出现频率相同。


# 提示：
# 2 <= word.length <= 100
# word 只包含小写英文字母。

# 复习
# @lc code=start
from collections import Counter


class Solution:
    def equalFrequency(self, word: str) -> bool:
        cnt = Counter(word)
        ma = cnt.most_common(1)[0][1]

        # 情况1：一个字母出现m+1次，其他字母都是m次—— 不能用(len(word) == (ma - 1) * len(cnt) + 1) 判断
        # 情况2：有一个字母出现1次，其他字母m次（m也可以为1）
        # 情况3：所有字母均相同
        return len(cnt) == 1 or (len(set(cnt.values())) <= 2 and ((len(word) - 1 == ma * (len(cnt) - 1)) or (len(word) == (ma - 1) * len(cnt) + 1)))

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.equalFrequency("abbcccfff"))  # False
    print(solution.equalFrequency("aaacccd"))  # True
    print(solution.equalFrequency("cccd"))  # True
    print(solution.equalFrequency("abbcc"))  # True
    print(solution.equalFrequency("bac"))  # True
    print(solution.equalFrequency("abcc"))  # True
    print(solution.equalFrequency("aacc"))  # False

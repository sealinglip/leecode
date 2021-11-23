#
# @lc app=leetcode.cn id=859 lang=python3
#
# [859] 亲密字符串
#
# 给你两个字符串 s 和 goal ，只要我们可以通过交换 s 中的两个字母得到与 goal 相等的结果，就返回 true ；否则返回 false 。
# 交换字母的定义是：取两个下标 i 和 j （下标从 0 开始）且满足 i != j ，接着交换 s[i] 和 s[j] 处的字符。
# 例如，在 "abcd" 中交换下标 0 和下标 2 的元素可以生成 "cbad" 。


# 示例 1：
# 输入：s = "ab", goal = "ba"
# 输出：true
# 解释：你可以交换 s[0] = 'a' 和 s[1] = 'b' 生成 "ba"，此时 s 和 goal 相等。

# 示例 2：
# 输入：s = "ab", goal = "ab"
# 输出：false
# 解释：你只能交换 s[0] = 'a' 和 s[1] = 'b' 生成 "ba"，此时 s 和 goal 不相等。

# 示例 3：
# 输入：s = "aa", goal = "aa"
# 输出：true
# 解释：你可以交换 s[0] = 'a' 和 s[1] = 'a' 生成 "aa"，此时 s 和 goal 相等。

# 示例 4：
# 输入：s = "aaaaaaabc", goal = "aaaaaaacb"
# 输出：true


# 提示：
# 1 <= s.length, goal.length <= 2 * 10^4
# s 和 goal 由小写英文字母组成

# @lc code=start
from collections import Counter


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if s and goal and len(s) == len(goal):
            p1, p2 = None, None
            for i in range(len(s)):
                if s[i] != goal[i]:
                    if p1 is None:
                        p1 = i
                    elif p2 is None:
                        p2 = i
                    else:
                        return False

            # 如果两个字符相等，如果它们中有重复字符，那么也能满足要求
            if p1 is None:
                cnt = Counter(s)
                return cnt.most_common(1)[0][1] > 1
            else:
                return (p2 is not None) and s[p1] == goal[p2] and s[p2] == goal[p1]
        else:
            return False


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.buddyStrings("ab", "ba"))  # True
    print(solution.buddyStrings("ab", "ab"))  # False
    print(solution.buddyStrings("aa", "aa"))  # True
    print(solution.buddyStrings("aaaaaaabc", "aaaaaaacb"))  # True

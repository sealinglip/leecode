#
# @lc app=leetcode.cn id=2516 lang=python3
#
# [2516] 每种字符至少取 K 个
#
# 给你一个由字符 'a'、'b'、'c' 组成的字符串 s 和一个非负整数 k 。每分钟，你可以选择取走 s 最左侧 还是 最右侧 的那个字符。
# 你必须取走每种字符 至少 k 个，返回需要的 最少 分钟数；如果无法取到，则返回 -1 。

# 示例 1：
# 输入：s = "aabaaaacaabc", k = 2
# 输出：8
# 解释：
# 从 s 的左侧取三个字符，现在共取到两个字符 'a' 、一个字符 'b' 。
# 从 s 的右侧取五个字符，现在共取到四个字符 'a' 、两个字符 'b' 和两个字符 'c' 。
# 共需要 3 + 5 = 8 分钟。
# 可以证明需要的最少分钟数是 8 。

# 示例 2：
# 输入：s = "a", k = 1
# 输出：-1
# 解释：无法取到一个字符 'b' 或者 'c'，所以返回 -1 。
 
# 提示：
# 1 <= s.length <= 10^5
# s 仅由字母 'a'、'b'、'c' 组成
# 0 <= k <= s.length

from collections import Counter
from typing import List

# @lc code=start
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        cnt = Counter(s)
        if any(cnt[c] < k for c in "abc"):
            # 无解的情况
            return -1
        
        def valid(c: List[int]) -> bool:
            return all(v >= k for v in c)

        base = ord('a')
        n = len(s)
        # 先假设全去左侧的
        cnt = [0] * 3
        i = j = 0
        while j < n and not valid(cnt):
            cnt[ord(s[j]) - base] += 1
            j += 1
            
        res = j - i # 初始窗口大小
        # 左移j和i，找其他满足条件的窗口
        while j > 0:
            while j > 0 and valid(cnt):
                j -= 1
                cnt[ord(s[j]) - base] -= 1

            res = min(res, j - i + 1) # [i:j+1] 是满足条件的窗口
            # 移动i
            while not valid(cnt):
                i -= 1
                cnt[ord(s[i]) - base] += 1
                
            res = min(res, j - i) # [i:j] 是满足条件的窗口

        return res


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.takeCharacters("a", 0)) # 0
    print(solution.takeCharacters("aabaaaacaabc", 2)) # 8
    print(solution.takeCharacters("a", 1)) # -1

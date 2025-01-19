# 给你一个字符串数组 words 和一个字符串 target。
# 如果字符串 x 是 words 中 任意 字符串的 前缀，则认为 x 是一个 有效 字符串。

# 现计划通过 连接 有效字符串形成 target ，请你计算并返回需要连接的 最少 字符串数量。如果无法通过这种方式形成 target，则返回 -1。


# 示例 1：
# 输入： words = ["abc","aaaaa","bcdef"], target = "aabcdabc"
# 输出： 3
# 解释：
# target 字符串可以通过连接以下有效字符串形成：
# words[1] 的长度为 2 的前缀，即 "aa"。
# words[2] 的长度为 3 的前缀，即 "bcd"。
# words[0] 的长度为 3 的前缀，即 "abc"。

# 示例 2：
# 输入： words = ["abababab","ab"], target = "ababaababa"
# 输出： 2
# 解释：
# target 字符串可以通过连接以下有效字符串形成：
# words[0] 的长度为 5 的前缀，即 "ababa"。
# words[0] 的长度为 5 的前缀，即 "ababa"。

# 示例 3：
# 输入： words = ["abcdef"], target = "xyz"
# 输出： -1

# 提示：
# 1 <= words.length <= 100
# 1 <= words[i].length <= 5 * 10^4
# 输入确保 sum(words[i].length) <= 10^5.
# words[i]  只包含小写英文字母。
# 1 <= target.length <= 5 * 10^4
# target  只包含小写英文字母。

# Hard

from bisect import bisect_left
from random import randint
from typing import List
    
class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        n = len(target)
        # 多项式字符串哈希（方便计算子串哈希值）
        # 哈希函数 hash(s) = s[0] * BASE^(n-1) + s[1] * BASE^(n-2) + ... + s[n-2] * BASE + s[n-1]
        MOD = 1_070_777_777
        BASE = randint(8 * 10 ** 8, 9 * 10 ** 8)  # 随机 BASE，防止 hack
        pow_base = [1] + [0] * n  # pow_base[i] = BASE^i
        pre_hash = [0] * (n + 1)  # 前缀哈希值 pre_hash[i] = hash(s[:i])
        for i, b in enumerate(target):
            pow_base[i + 1] = pow_base[i] * BASE % MOD
            pre_hash[i + 1] = (pre_hash[i] * BASE + ord(b)) % MOD  # 秦九韶算法计算多项式哈希

        # 计算子串 target[l:r] 的哈希值，注意这是左闭右开区间 [l,r)
        # 计算方法类似前缀和
        def sub_hash(l: int, r: int) -> int:
            return (pre_hash[r] - pre_hash[l] * pow_base[r - l]) % MOD

        # 保存每个 words[i] 的每个前缀的哈希值，按照长度分组
        max_len = max(map(len, words))
        sets = [set() for _ in range(max_len)]
        for w in words:
            h = 0
            for j, b in enumerate(w):
                h = (h * BASE + ord(b)) % MOD
                sets[j].add(h)  # 注意 j 从 0 开始

        ans = 0
        cur_r = 0  # 已建造的桥的右端点
        nxt_r = 0  # 下一座桥的右端点的最大值
        for i in range(n):
            while nxt_r < n and nxt_r - i < max_len and sub_hash(i, nxt_r + 1) in sets[nxt_r - i]:
                nxt_r += 1
            if i == cur_r:  # 到达已建造的桥的右端点
                if i == nxt_r:  # 无论怎么造桥，都无法从 i 到 i+1
                    return -1
                cur_r = nxt_r  # 建造下一座桥
                ans += 1
        return ans
        

if __name__ == "__main__":
    solution = Solution()
    print(solution.minValidStrings(["abc","aaaaa","bcdef"], "aabcdabc")) # 3
    print(solution.minValidStrings(["abababab","ab"], "ababaababa")) # 2
    print(solution.minValidStrings(["abcdef"], "xyz")) # -1

#
# @lc app=leetcode.cn id=1079 lang=python3
#
# [1079] 活字印刷
#
# 你有一套活字字模 tiles，其中每个字模上都刻有一个字母 tiles[i]。返回你可以印出的非空字母序列的数目。

# 注意：本题中，每个活字字模只能使用一次。


# 示例 1：
# 输入："AAB"
# 输出：8
# 解释：可能的序列为 "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA"。

# 示例 2：
# 输入："AAABBC"
# 输出：188

# 示例 3：
# 输入："V"
# 输出：1


# 提示：
# 1 <= tiles.length <= 7
# tiles 由大写英文字母组成

# 复习

# @lc code=start
from collections import Counter


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        cnt = Counter(tiles)
        letter = set(cnt.keys())

        def dfs(i: int) -> int:
            if i == 0:
                return 1
            res = 1  # 代表后面什么都拼，到此为止的情况
            for t in letter:
                if cnt[t] > 0:
                    cnt[t] -= 1
                    res += dfs(i-1)
                    cnt[t] += 1
            return res

        return dfs(len(tiles)) - 1


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.numTilePossibilities("AAB"))  # 8
    print(solution.numTilePossibilities("AAABBC"))  # 188
    print(solution.numTilePossibilities("V"))  # 1

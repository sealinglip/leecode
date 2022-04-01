#
# @lc app=leetcode.cn id=954 lang=python3
#
# [954] 二倍数对数组
#
# 给定一个长度为偶数的整数数组 arr，只有对 arr 进行重组后可以满足 “对于每个 0 <= i < len(arr) / 2，
# 都有 arr[2 * i + 1] = 2 * arr[2 * i]” 时，返回 true；否则，返回 false。


# 示例 1：
# 输入：arr = [3, 1, 3, 6]
# 输出：false

# 示例 2：
# 输入：arr = [2, 1, 2, 6]
# 输出：false

# 示例 3：
# 输入：arr = [4, -2, 2, -4]
# 输出：true
# 解释：可以用[-2, -4] 和[2, 4] 这两组组成[-2, -4, 2, 4] 或是[2, 4, -2, -4]


# 提示：
# 0 <= arr.length <= 3 * 10^4
# arr.length 是偶数
# -10^5 <= arr[i] <= 10^5


from typing import List
# @lc code=start
from collections import Counter


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        cnt = Counter(arr)
        for k in sorted(cnt.keys()):
            c = cnt[k]
            if c == 0:
                continue
            elif c < 0:
                break
            elif k < 0:
                # k 必须是偶数
                if k & 1 == 1 or cnt[k // 2] < c:
                    break
                cnt[k // 2] -= c
            elif k > 0:
                if cnt[k << 1] < c:
                    break
                cnt[k << 1] -= c
            else:  # k == 0
                if c & 1 == 1:
                    break
        else:
            return True

        return False


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.canReorderDoubled([3, 1, 3, 6]))  # False
    print(solution.canReorderDoubled([2, 1, 2, 6]))  # False
    print(solution.canReorderDoubled([4, -2, 2, -4]))  # True

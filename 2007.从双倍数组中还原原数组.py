#
# @lc app=leetcode.cn id=2007 lang=python3
#
# [2007] 从双倍数组中还原原数组
#
# 一个整数数组 original 可以转变成一个 双倍 数组 changed ，转变方式为将 original 中每个元素 值乘以 2 加入数组中，然后将所有元素 随机打乱 。

# 给你一个数组 changed ，如果 change 是 双倍 数组，那么请你返回 original数组，否则请返回空数组。original 的元素可以以 任意 顺序返回。


# 示例 1：
# 输入：changed = [1,3,4,2,6,8]
# 输出：[1,3,4]
# 解释：一个可能的 original 数组为 [1,3,4] :
# - 将 1 乘以 2 ，得到 1 * 2 = 2 。
# - 将 3 乘以 2 ，得到 3 * 2 = 6 。
# - 将 4 乘以 2 ，得到 4 * 2 = 8 。
# 其他可能的原数组方案为 [4,3,1] 或者 [3,1,4] 。

# 示例 2：
# 输入：changed = [6,3,0,1]
# 输出：[]
# 解释：changed 不是一个双倍数组。

# 示例 3：
# 输入：changed = [1]
# 输出：[]
# 解释：changed 不是一个双倍数组。
 

# 提示：
# 1 <= changed.length <= 10^5
# 0 <= changed[i] <= 10^5

from collections import Counter
from typing import List
# @lc code=start
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        cnt = Counter(changed)
        res = []
        for k in sorted(cnt.keys()):
            if cnt[k]:
                if (k > 0 and cnt[k << 1] >= cnt[k]) or (k == 0 and (cnt[k] & 1) == 0):
                    if k == 0:
                        res.extend([k] * (cnt[k] >> 1))
                    else:
                        cnt[k << 1] -= cnt[k]
                        res.extend([k] * cnt[k])
                else:
                    return []
                    
        return res
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.findOriginalArray([4,2,0])) # [0]
    print(solution.findOriginalArray([0,0,0,0])) # [0, 0]
    print(solution.findOriginalArray([1,3,4,2,6,8])) # [1,3,4]
    print(solution.findOriginalArray([6,3,0,1])) # []
    print(solution.findOriginalArray([8,4,2,1,1,2,2,4])) # []
    print(solution.findOriginalArray([1])) # []
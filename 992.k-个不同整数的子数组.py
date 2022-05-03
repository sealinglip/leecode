#
# @lc app=leetcode.cn id=992 lang=python3
#
# [992] K 个不同整数的子数组
#
# 给定一个正整数数组 A，如果 A 的某个子数组中不同整数的个数恰好为 K，则称 A 的这个连续、不一定独立的子数组为好子数组。
# （例如，[1, 2, 3, 1, 2] 中有 3 个不同的整数：1，2，以及 3。）
# 返回 A 中好子数组的数目。

# 示例 1：
# 输入：A = [1, 2, 1, 2, 3], K = 2
# 输出：7
# 解释：恰好由 2 个不同整数组成的子数组：[1, 2], [2, 1], [1, 2], [2, 3], [1, 2, 1], [2, 1, 2], [1, 2, 1, 2].

# 示例 2：
# 输入：A = [1, 2, 1, 3, 4], K = 3
# 输出：3
# 解释：恰好由 3 个不同整数组成的子数组：[1, 2, 1, 3], [2, 1, 3], [1, 3, 4].


# 提示：
# 1 <= A.length <= 20000
# 1 <= A[i] <= A.length
# 1 <= K <= A.length

# Hard

from typing import List
# @lc code=start


class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        # 双指针
        # 初始化
        l = 0
        r = 0
        cCnt = {}
        subArrCnt = 0

        N = len(A)
        while r <= N:
            # 如果当前cCnt长度小于K且r小于N，右指针移动，更新cCnt
            # 如果当前cCnt长度等于K，subArrCnt加1，如果r小于N且A[r] in cCnt，右指针移动，更新cCnt；否则如果r-l>K，左指针移动，更新cCnt；否则如果r == N，break
            # 如果当前cCnt长度大于K，左指针移动，更新cCnt
            if len(cCnt) < K:
                if r < N:
                    cCnt[A[r]] = cCnt.get(A[r], 0) + 1
                    r += 1
                else:
                    break
            elif len(cCnt) == K:
                subArrCnt += 1
                if r < N and A[r] in cCnt:
                    # 右移之前先尝试左移边界
                    lMark = l
                    clone = dict(cCnt)
                    while l < r:
                        clone[A[l]] = clone.get(A[l], 0) - 1
                        if clone[A[l]] <= 0:
                            clone.pop(A[l])
                        l += 1
                        if len(clone) == K:
                            subArrCnt += 1
                        else:
                            break
                    l = lMark
                    cCnt[A[r]] = cCnt.get(A[r], 0) + 1
                    r += 1
                elif r - l >= K:
                    cCnt[A[l]] = cCnt.get(A[l], 0) - 1
                    if cCnt[A[l]] <= 0:
                        cCnt.pop(A[l])
                    l += 1
                elif r == N:
                    break
            else:
                cCnt[A[l]] = cCnt.get(A[l], 0) - 1
                if cCnt[A[l]] <= 0:
                    cCnt.pop(A[l])
                l += 1

        return subArrCnt

# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.subarraysWithKDistinct([1, 2, 1, 2, 3], 2))
    print(solution.subarraysWithKDistinct([1, 2, 1, 3, 4], 3))

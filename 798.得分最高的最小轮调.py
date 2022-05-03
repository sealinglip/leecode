#
# @lc app=leetcode.cn id=798 lang=python3
#
# [798] 得分最高的最小轮调
#
# 给你一个数组 nums，我们可以将它按一个非负整数 k 进行轮调，这样可以使数组变为[nums[k], nums[k + 1], ... nums[nums.length - 1], nums[0], nums[1], ..., nums[k-1]] 的形式。此后，任何值小于或等于其索引的项都可以记作一分。

# 例如，数组为 nums = [2, 4, 1, 3, 0]，我们按 k = 2 进行轮调后，它将变成[1, 3, 0, 2, 4]。这将记为 3 分，因为 1 > 0 [不计分]、3 > 1 [不计分]、0 <= 2 [计 1 分]、2 <= 3 [计 1 分]，4 <= 4 [计 1 分]。
# 在所有可能的轮调中，返回我们所能得到的最高分数对应的轮调下标 k 。如果有多个答案，返回满足条件的最小的下标 k 。


# 示例 1：
# 输入：nums = [2, 3, 1, 4, 0]
# 输出：3
# 解释：
# 下面列出了每个 k 的得分：
# k = 0,  nums = [2, 3, 1, 4, 0],    score 2
# k = 1,  nums = [3, 1, 4, 0, 2],    score 3
# k = 2,  nums = [1, 4, 0, 2, 3],    score 3
# k = 3,  nums = [4, 0, 2, 3, 1],    score 4
# k = 4,  nums = [0, 2, 3, 1, 4],    score 3
# 所以我们应当选择 k = 3，得分最高。

# 示例 2：
# 输入：nums = [1, 3, 0, 2, 4]
# 输出：0
# 解释：
# nums 无论怎么变化总是有 3 分。
# 所以我们将选择最小的 k，即 0。


# 提示：
# 1 <= nums.length <= 10^5
# 0 <= nums[i] < nums.length

# Hard

from typing import List


def rotateArr(nums: List[int], k: int) -> None:
    newNums = nums[k:] + nums[0:k]
    count = 0
    for i, num in enumerate(newNums):
        if num <= i:
            count += 1
    print("rotate %d, score %d" % (k, count))

# @lc code=start


class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)
        myCriticalK = [0] * n  # myCriticalK[i]记录轮转i时，刚才不能得分的点的数量
        # 考虑0元素所在的位置，在数学上是严谨，但其实不区分0元素，其效果也是对的，比如下面的代码
        # 这是因为，第一步中0值也会记录一个不得分的位置（设为i)，但是在第二步遍历中一定会遍历到这个0处于第一位的时候，
        # 然后会进行-1操作（即myCriticalK[i] += myCriticalK[i-1] - 1）会把第一步中多算的不得分的位置给减去了
        # 可以理解为myCriticalK[i]本来多记了个1，然后现在将1减去了。
        # for i, num in enumerate(nums):
        #     myCriticalK[(i - num + 1 + n) % n] += 1

        # resK = 0
        # for i in range(1, n):
        #     myCriticalK[i] += myCriticalK[i-1] - 1
        #     if myCriticalK[i] < myCriticalK[resK]:
        #         resK = i

        zeroPos = set()  # 记录0元素的位置

        for i, num in enumerate(nums):
            # 第i个数num轮转k恰好不得分，则 k = (i - num + 1 + n) % n
            if num == 0:
                zeroPos.add(i)
            else:
                myCriticalK[(i - num + 1 + n) % n] += 1

        resK = 0
        for i in range(1, n):
            # 上面myCriticalK记录的是刚好不得分的点位，要得到所有不得分的点位，需要累加
            # 记轮转 k 时所有不得分的点位 f(k)，则有f(k+1) = f(k) - (1 if k != zeroPos else 0) + myCriticalK[k]
            # 因为轮转k不得分的点，轮转k+1也不会得分，但最左边的点移到了最右边，从不得分变成得分（如果它不是零的话——零的话在哪都得分）
            myCriticalK[i] += myCriticalK[i-1] - (0 if (i-1) in zeroPos else 1)
            if myCriticalK[i] < myCriticalK[resK]:
                resK = i

        return resK

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    nums = [18, 69, 56, 0, 39, 8, 2, 83, 18, 61, 14, 80, 58, 8, 72, 15, 38, 88, 38, 67, 6, 80, 70, 87, 62, 20, 4, 39, 81, 63, 46, 92, 52, 47, 57, 22, 33, 63, 97, 41, 76, 89, 79, 62, 12, 57, 48,
            75, 28, 74, 36, 17, 9, 95, 37, 78, 10, 86, 16, 44, 57, 81, 74, 50, 59, 77, 36, 0, 5, 14, 4, 99, 49, 56, 25, 70, 70, 56, 15, 78, 64, 93, 82, 63, 56, 3, 79, 40, 42, 0, 68, 14, 46, 69, 78, 81, 69, 14, 34, 39]
    rotateArr(nums, 62)
    rotateArr(nums, 63)
    rotateArr(nums, 77)

    print(solution.bestRotation(nums))  # 62
    print(solution.bestRotation([2, 3, 1, 4, 0]))  # 3
    print(solution.bestRotation([1, 3, 0, 2, 4]))  # 0

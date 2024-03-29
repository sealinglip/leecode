#
# @lc app=leetcode.cn id=825 lang=python3
#
# [825] 适龄的朋友
#
# 在社交媒体网站上有 n 个用户。给你一个整数数组 ages ，其中 ages[i] 是第 i 个用户的年龄。

# 如果下述任意一个条件为真，那么用户 x 将不会向用户 y（x != y）发送好友请求：

# age[y] <= 0.5 * age[x] + 7
# age[y] > age[x]
# age[y] > 100 & & age[x] < 100
# 否则，x 将会向 y 发送一条好友请求。

# 注意，如果 x 向 y 发送一条好友请求，y 不必也向 x 发送一条好友请求。另外，用户不会向自己发送好友请求。

# 返回在该社交媒体网站上产生的好友请求总数。


# 示例 1：
# 输入：ages = [16, 16]
# 输出：2
# 解释：2 人互发好友请求。

# 示例 2：
# 输入：ages = [16, 17, 18]
# 输出：2
# 解释：产生的好友请求为 17 -> 16 ，18 -> 17 。

# 示例 3：
# 输入：ages = [20, 30, 100, 110, 120]
# 输出：3
# 解释：产生的好友请求为 110 -> 100 ，120 -> 110 ，120 -> 100 。


# 提示：
# n == ages.length
# 1 <= n <= 2 * 10^4
# 1 <= ages[i] <= 120


from typing import List
# @lc code=start


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        # 条件3是冗余条件，满足条件3则一定会满足条件2
        # x <= 14 时，y无解
        # y 的有效范围为  floor(0.5 * x + 8) <= y <= x
        # 计数
        cnt = [0] * 121
        for age in ages:
            cnt[age] += 1

        # 求前缀和
        preSum = [0] * 121
        for i in range(1, 121):
            preSum[i] = preSum[i-1] + cnt[i]

        res = 0
        for i in range(15, 121):
            if cnt[i] > 0:
                lb = int(0.5 * i + 8)
                res += (preSum[i] - preSum[lb - 1] - 1) * cnt[i]
        return res

        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.numFriendRequests([16, 16]))  # 2

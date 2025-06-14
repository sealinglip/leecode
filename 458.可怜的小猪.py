#
# @lc app=leetcode.cn id=458 lang=python3
#
# [458] 可怜的小猪
#
# 有 buckets 桶液体，其中 正好 有一桶含有毒药，其余装的都是水。它们从外观看起来都一样。为了弄清楚哪只水桶含有毒药，
# 你可以喂一些猪喝，通过观察猪是否会死进行判断。不幸的是，你只有 minutesToTest 分钟时间来确定哪桶液体是有毒的。

# 喂猪的规则如下：

# 选择若干活猪进行喂养
# 可以允许小猪同时饮用任意数量的桶中的水，并且该过程不需要时间。
# 小猪喝完水后，必须有 minutesToDie 分钟的冷却时间。在这段时间里，你只能观察，而不允许继续喂猪。
# 过了 minutesToDie 分钟后，所有喝到毒药的猪都会死去，其他所有猪都会活下来。
# 重复这一过程，直到时间用完。
# 给你桶的数目 buckets ，minutesToDie 和 minutesToTest ，返回在规定时间内判断哪个桶有毒所需的 最小 猪数。


# 示例 1：
# 输入：buckets = 1000, minutesToDie = 15, minutesToTest = 60
# 输出：5

# 示例 2：
# 输入：buckets = 4, minutesToDie = 15, minutesToTest = 15
# 输出：2

# 示例 3：
# 输入：buckets = 4, minutesToDie = 15, minutesToTest = 30
# 输出：2


# 提示：
# 1 <= buckets <= 1000
# 1 <= minutesToDie <= minutesToTest <= 100

# 复习
# Hard

# @lc code=start
from math import ceil, log


class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        M = minutesToTest // minutesToDie  # 能进行测试的轮数
        # 每只猪最多可以验证M次，区分M+1种情况。每只小🐷对应一位，进制为(M+1)，设需要n只
        # 那么有 n = ceil(log(buckets)/log(M+1))
        # 将桶从0开始编号，将编号转为(M+1)进制的数
        # 对于第i位的小猪，第j轮（j <= M)它需要饮用编号的第i位值为j的所有桶
        # 要注意浮点数的精度问题
        return ceil(log(buckets)/log(M+1) - 1e-5)
        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.poorPigs(1000, 15, 60))  # 5
    print(solution.poorPigs(4, 15, 15))  # 2
    print(solution.poorPigs(4, 15, 30))  # 2

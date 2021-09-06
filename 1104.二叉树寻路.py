#
# @lc app=leetcode.cn id=1104 lang=python3
#
# [1104] 二叉树寻路
#
# 在一棵无限的二叉树上，每个节点都有两个子节点，树中的节点 逐行 依次按 “之” 字形进行标记。
# 如下图所示，在奇数行（即，第一行、第三行、第五行……）中，按从左到右的顺序进行标记；
# 而偶数行（即，第二行、第四行、第六行……）中，按从右到左的顺序进行标记。


# 给你树上某一个节点的标号 label，请你返回从根节点到该标号为 label 节点的路径，该路径是由途经的节点标号所组成的。


# 示例 1：
# 输入：label = 14
# 输出：[1, 3, 4, 14]

# 示例 2：
# 输入：label = 26
# 输出：[1, 2, 6, 10, 26]


# 提示：
# 1 <= label <= 10^6

from typing import List

# @lc code=start
from math import log2, floor


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        # 第i行编号的区间是 [2 ^ i, 2 ^ (i + 1) - 1]，i从0开始
        # 不考虑“之”字形编码的话，节点与子节点关系应该是 n的子节点是 2n 和 2n + 1
        # 先将label转换为不考虑“之”字形编码的编号
        l = floor(log2(label))
        # l为奇数的话，label要处理一下
        if (l & 1) == 1:
            label = (2 ** l) * 3 - 1 - label

        res = [label]
        while res[-1] > 1:
            res.append(res[-1] >> 1)

        res.reverse()  # 翻转数组
        # 将偶数位置的编号按“之”字形规则进行转换
        for i in range(1, len(res), 2):
            res[i] = (2 ** i) * 3 - 1 - res[i]

        return res


        # @lc code=end
if __name__ == "__main__":
    solution = Solution()
    print(solution.pathInZigZagTree(14))
    print(solution.pathInZigZagTree(26))

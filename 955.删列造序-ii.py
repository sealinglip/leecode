#
# @lc app=leetcode.cn id=955 lang=python3
#
# [955] 删列造序 II
#
# https://leetcode.cn/problems/delete-columns-to-make-sorted-ii/description/
#
# algorithms
# Medium (36.75%)
# Likes:    101
# Dislikes: 0
# Total Accepted:    8.6K
# Total Submissions: 21.7K
# Testcase Example:  '["ca","bb","ac"]'
#
# 给定由 n 个字符串组成的数组 strs，其中每个字符串长度相等。
# 
# 选取一个删除索引序列，对于 strs 中的每个字符串，删除对应每个索引处的字符。
# 
# 比如，有 strs = ["abcdef", "uvwxyz"]，删除索引序列 {0, 2, 3}，删除后 strs 为["bef", "vyz"]。
# 
# 假设，我们选择了一组删除索引 answer，那么在执行删除操作之后，最终得到的数组的元素是按 字典序（strs[0] ）排列的，然后请你返回
# answer.length 的最小可能值。
# 
# 
# 示例 1：
# 输入：strs = ["ca","bb","ac"]
# 输出：1
# 解释： 
# 删除第一列后，strs = ["a", "b", "c"]。
# 现在 strs 中元素是按字典排列的 (即，strs[0] 
# 
# 示例 2：
# 输入：strs = ["xc","yb","za"]
# 输出：0
# 解释：
# strs 的列已经是按字典序排列了，所以我们不需要删除任何东西。
# 注意 strs 的行不需要按字典序排列。
# 也就是说，strs[0][0] 
# 
# 示例 3：
# 输入：strs = ["zyx","wvu","tsr"]
# 输出：3
# 解释：
# 我们必须删掉每一列。
# 
# 
# 提示：
# n == strs.length
# 1 <= n <= 100
# 1 <= strs[i].length <= 100
# strs[i] 由小写英文字母组成
# 
# 复习
#

from typing import List
# @lc code=start
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        cuts = [False] * n # 记录区段信息，cuts[i]=True代表i处为区段边界

        res = 0
        for col in zip(*strs):
            # 判断col是否区间有序
            valid = all(cuts[i] or col[i-1] <= col[i] for i in range(1, n))
            if valid:
                # 更新cuts
                for i in range(1, n):
                    if not cuts[i] and col[i-1] < col[i]:
                        cuts[i] = True
            else:
                res += 1
        
        return res
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.minDeletionSize(["abx","agz","bgc","bfc"])) # 1
    print(solution.minDeletionSize(["ca","bb","ac"])) # 1
    print(solution.minDeletionSize(["xc","yb","za"])) # 0
    print(solution.minDeletionSize(["zyx","wvu","tsr"])) # 3

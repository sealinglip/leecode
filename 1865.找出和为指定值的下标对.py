#
# @lc app=leetcode.cn id=1865 lang=python3
#
# [1865] 找出和为指定值的下标对
#
# https://leetcode.cn/problems/finding-pairs-with-a-certain-sum/description/
#
# algorithms
# Medium (51.42%)
# Likes:    26
# Dislikes: 0
# Total Accepted:    10.1K
# Total Submissions: 18.6K
# Testcase Example:  '["FindSumPairs","count","add","count","count","add","add","count"]\n' +
# '[[[1,1,2,2,2,3],[1,4,5,2,5,4]],[7],[3,2],[8],[4],[0,1],[1,1],[7]]'
#
# 给你两个整数数组 nums1 和 nums2 ，请你实现一个支持下述两类查询的数据结构：
# 
# 累加 ，将一个正整数加到 nums2 中指定下标对应元素上。
# 计数 ，统计满足 nums1[i] + nums2[j] 等于指定值的下标对 (i, j) 数目（0  且 0 ）。
# 
# 实现 FindSumPairs 类：
# FindSumPairs(int[] nums1, int[] nums2) 使用整数数组 nums1 和 nums2 初始化 FindSumPairs对象。
# void add(int index, int val) 将 val 加到 nums2[index] 上，即，执行 nums2[index] += val。
# int count(int tot) 返回满足 nums1[i] + nums2[j] == tot 的下标对 (i, j) 数目。
# 
# 
# 示例：
# 输入：
# ["FindSumPairs", "count", "add", "count", "count", "add", "add", "count"]
# [[[1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]], [7], [3, 2], [8], [4], [0, 1], [1,
# 1], [7]]
# 输出：
# [null, 8, null, 2, 1, null, null, 11]
# 解释：
# FindSumPairs findSumPairs = new FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2,
# 5, 4]);
# findSumPairs.count(7);  // 返回 8 ; 下标对 (2,2), (3,2), (4,2), (2,4), (3,4),
# (4,4) 满足 2 + 5 = 7 ，下标对 (5,1), (5,5) 满足 3 + 4 = 7
# findSumPairs.add(3, 2); // 此时 nums2 = [1,4,5,4,5,4]
# findSumPairs.count(8);  // 返回 2 ；下标对 (5,2), (5,4) 满足 3 + 5 = 8
# findSumPairs.count(4);  // 返回 1 ；下标对 (5,0) 满足 3 + 1 = 4
# findSumPairs.add(0, 1); // 此时 nums2 = [2,4,5,4,5,4]
# findSumPairs.add(1, 1); // 此时 nums2 = [2,5,5,4,5,4]
# findSumPairs.count(7);  // 返回 11 ；下标对 (2,1), (2,2), (2,4), (3,1), (3,2),
# (3,4), (4,1), (4,2), (4,4) 满足 2 + 5 = 7 ，下标对 (5,3), (5,5) 满足 3 + 4 = 7
# 
# 
# 提示：
# 1 <= nums1.length <= 1000
# 1 <= nums2.length <= 10^5
# 1 <= nums1[i] <= 10^9
# 1 <= nums2[i] <= 10^5
# 0 <= index < nums2.length
# 1 <= val <= 10^5
# 1 <= tot <= 10^9 
# 最多调用 add 和 count 函数各 1000 次
# 
#

from collections import Counter
from typing import List
# @lc code=start
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.cnt1 = Counter(nums1)
        self.cnt2 = Counter(nums2)
        self.nums2 = nums2        

    def add(self, index: int, val: int) -> None:
        oldVal = self.nums2[index]
        newVal = oldVal + val
        self.nums2[index] = newVal
        self.cnt2[oldVal] -= 1
        if self.cnt2[oldVal] == 0:
            del self.cnt2[oldVal]
        self.cnt2[newVal] += 1        

    def count(self, tot: int) -> int:
        c1, c2 = self.cnt1, self.cnt2
        if len(c1) > len(c2):
            c1, c2 = c2, c1
        pairs = 0
        for k, v in c1.items():
            k2 = tot - k
            if k2 in c2:
                pairs += v * c2[k2]
        return pairs
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
# @lc code=end

if __name__ == "__main__":
    findSumPairs = FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4])
    print(findSumPairs.count(7)) # 8
    findSumPairs.add(3, 2)
    print(findSumPairs.count(8)) # 2
    print(findSumPairs.count(4)) # 1
    findSumPairs.add(0, 1)
    findSumPairs.add(1, 1)
    print(findSumPairs.count(7)) # 11

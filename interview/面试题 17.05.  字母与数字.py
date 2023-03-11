# 给定一个放有字母和数字的数组，找到最长的子数组，且包含的字母和数字的个数相同。

# 返回该子数组，若存在多个最长子数组，返回左端点下标值最小的子数组。若不存在这样的数组，返回一个空数组。

# 示例 1:
# 输入: ["A", "1", "B", "C", "D", "2", "3", "4", "E", "5",
#      "F", "G", "6", "7", "H", "I", "J", "K", "L", "M"]
# 输出: ["A", "1", "B", "C", "D", "2", "3", "4", "E", "5", "F", "G", "6", "7"]

# 示例 2:
# 输入: ["A", "A"]
# 输出: []

# 提示：
# array.length <= 100000

from typing import List


class Solution:
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        deltaMap = {0: 0}  # 字母数字差异记录表，只记最早的
        delta = 0
        start = 0
        span = 0
        for i, c in enumerate(array):
            if c.isdigit():
                delta -= 1
            else:
                delta += 1
            if delta in deltaMap:
                s = i + 1 - deltaMap[delta]
                if s > span:
                    start = deltaMap[delta]
                    span = s
            else:
                deltaMap[delta] = i + 1

        return array[start:start+span]


if __name__ == "__main__":
    solution = Solution()
    print(solution.findLongestSubarray(["A", "1", "B", "C", "D", "2", "3", "4", "E", "5",
                                             "F", "G", "6", "7", "H", "I", "J", "K", "L", "M"]))  # ["A", "1", "B", "C", "D", "2", "3", "4", "E", "5", "F", "G", "6", "7"]
    print(solution.findLongestSubarray(["A", "A"]))  # []

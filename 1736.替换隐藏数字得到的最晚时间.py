#
# @lc app=leetcode.cn id=1736 lang=python3
#
# [1736] 替换隐藏数字得到的最晚时间
#

# @lc code=start
class Solution:
    def maximumTime(self, time: str) -> str:
        arr = [t for t in time]

        if arr[0] == '?':
            if arr[1] == '?':
                arr[0], arr[1] = '2', '3'
            else:
                arr[0] = '2' if arr[1] < '4' else '1'

        if arr[1] == '?':
            arr[1] = '9' if arr[0] < '2' else '3'

        if arr[3] == '?':
            arr[3] = '5'

        if arr[4] == '?':
            arr[4] = '9'

        return "".join(arr)

        # @lc code=end


if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumTime("2?:?0"))
    print(solution.maximumTime("0?:3?"))
    print(solution.maximumTime("1?:22"))

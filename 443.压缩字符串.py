#
# @lc app=leetcode.cn id=443 lang=python3
#
# [443] 压缩字符串
#
# 给你一个字符数组 chars ，请使用下述算法压缩：
# 从一个空字符串 s 开始。对于 chars 中的每组 连续重复字符 ：

# 如果这一组长度为 1 ，则将字符追加到 s 中。
# 否则，需要向 s 追加字符，后跟这一组的长度。
# 压缩后得到的字符串 s 不应该直接返回 ，需要转储到字符数组 chars 中。需要注意的是，如果组长度为 10 或 10 以上，则在 chars 数组中会被拆分为多个字符。

# 请在 修改完输入数组后 ，返回该数组的新长度。
# 你必须设计并实现一个只使用常量额外空间的算法来解决此问题。


# 示例 1：
# 输入：chars = ["a", "a", "b", "b", "c", "c", "c"]
# 输出：返回 6 ，输入数组的前 6 个字符应该是：["a", "2", "b", "2", "c", "3"]
# 解释：
# "aa" 被 "a2" 替代。"bb" 被 "b2" 替代。"ccc" 被 "c3" 替代。

# 示例 2：
# 输入：chars = ["a"]
# 输出：返回 1 ，输入数组的前 1 个字符应该是：["a"]
# 解释：
# 没有任何字符串被替代。

# 示例 3：
# 输入：chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
# 输出：返回 4 ，输入数组的前 4 个字符应该是：["a", "b", "1", "2"]。
# 解释：
# 由于字符 "a" 不重复，所以不会被压缩。"bbbbbbbbbbbb" 被 “b12” 替代。
# 注意每个数字在数组中都有它自己的位置。


# 提示：
# 1 <= chars.length <= 2000
# chars[i] 可以是小写英文字母、大写英文字母、数字或符号

from typing import List
# @lc code=start


class Solution:
    def compress(self, chars: List[str]) -> int:
        def reverse(left: int, right: int) -> None:
            while left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
        # 双指针表示读位置和写位置
        r, w, l, N = 0, 0, 0, len(chars)
        if N < 2:
            return N

        while r < N:
            if r == N - 1 or chars[r] != chars[r + 1]:
                chars[w] = chars[r]
                w += 1
                cnt = r - l + 1
                if cnt > 1:
                    # 写入数字 —— 这样写不符合题意O(1)
                    # for c in str(cnt):
                    #     chars[w] = c
                    #     w += 1
                    mark = w
                    while cnt:
                        chars[w] = str(cnt % 10)
                        cnt //= 10
                        w += 1
                    # reverse chars[mark:w]
                    reverse(mark, w - 1)
                l = r + 1
            r += 1
        return w


# @lc code=end
if __name__ == "__main__":
    solution = Solution()

    chars = ["a", "b", "c"]
    print(solution.compress(chars))
    print(chars)

    chars = ["a", "a", "b", "b", "c", "c", "c"]
    print(solution.compress(chars))
    print(chars)

    chars = ["a"]
    print(solution.compress(chars))
    print(chars)

    chars = ["a", "b", "b", "b", "b",
             "b", "b", "b", "b", "b", "b", "b", "b"]
    print(solution.compress(chars))
    print(chars)

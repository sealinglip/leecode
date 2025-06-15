#
# @lc app=leetcode.cn id=2434 lang=python3
#
# [2434] 使用机器人打印字典序最小的字符串
#
# https://leetcode.cn/problems/using-a-robot-to-print-the-lexicographically-smallest-string/description/
#
# algorithms
# Medium (45.24%)
# Likes:    74
# Dislikes: 0
# Total Accepted:    10.4K
# Total Submissions: 21.7K
# Testcase Example:  '"zza"'
#
# 给你一个字符串 s 和一个机器人，机器人当前有一个空字符串 t 。执行以下操作之一，直到 s 和 t 都变成空字符串：
# 
# 删除字符串 s 的 第一个 字符，并将该字符给机器人。机器人把这个字符添加到 t 的尾部。
# 删除字符串 t 的 最后一个 字符，并将该字符给机器人。机器人将该字符写到纸上。
# 
# 请你返回纸上能写出的字典序最小的字符串。
# 
# 
# 示例 1：
# 输入：s = "zza"
# 输出："azz"
# 解释：用 p 表示写出来的字符串。
# 一开始，p="" ，s="zza" ，t="" 。
# 执行第一个操作三次，得到 p="" ，s="" ，t="zza" 。
# 执行第二个操作三次，得到 p="azz" ，s="" ，t="" 。
# 
# 示例 2：
# 输入：s = "bac"
# 输出："abc"
# 解释：用 p 表示写出来的字符串。
# 执行第一个操作两次，得到 p="" ，s="c" ，t="ba" 。
# 执行第二个操作两次，得到 p="ab" ，s="c" ，t="" 。
# 执行第一个操作，得到 p="ab" ，s="" ，t="c" 。
# 执行第二个操作，得到 p="abc" ，s="" ，t="" 。
# 
# 示例 3：
# 输入：s = "bdda"
# 输出："addb"
# 解释：用 p 表示写出来的字符串。
# 一开始，p="" ，s="bdda" ，t="" 。
# 执行第一个操作四次，得到 p="" ，s="" ，t="bdda" 。
# 执行第二个操作四次，得到 p="addb" ，s="" ，t="" 。
# 
# 
# 提示：
# 1 <= s.length <= 10^5
# s 只包含小写英文字母。
# 
# 

# @lc code=start
class Solution:
    def robotWithString(self, s: str) -> str:
        n = len(s)
        # 先尽可能输出'a'，然后是'b'，依此类推
        c = 'a'
        pos = 0
        t = []
        res = []
        while pos < n:
            while (np := s.find(c, pos)) != -1:
                res.append(c)
                # 将s[pos:np]之间的字符加入t
                t.extend(s[pos:np])
                pos = np + 1
            # 没有c了，找比c大一的字符
            c = chr(ord(c)+1)
            # 从栈里看看有没有小于等于c的在顶上，有就出栈，加入到结果中
            while t and t[-1] <= c:
                res.append(t.pop())
                
        res.extend(t[::-1])

        return ''.join(res)
        
# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    print(solution.robotWithString("vzhofnpo")) # "fnohopzv"
    print(solution.robotWithString("zza")) # "azz"
    print(solution.robotWithString("bac")) # "abc"
    print(solution.robotWithString("bdda")) # "addb"


# 字符串有三种编辑操作: 插入一个字符、删除一个字符或者替换一个字符。 给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑。


# 示例 1:
# 输入:
# first = "pale"
# second = "ple"
# 输出: True

# 示例 2:
# 输入:
# first = "pales"
# second = "pal"
# 输出: False

class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        # 长度差必须在1以下
        n, m = len(first), len(second)
        if abs(n - m) > 1:
            return False
        else:
            if n < m:
                # 把长的放前面
                n, m = m, n
                first, second = second, first

            for i, (a, b) in enumerate(zip(first, second)):
                if a != b:
                    return (first[i+1:] == second[i+1:]) if n == m else (first[i+1:] == second[i:])
            return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.oneEditAway("pale", "ple"))  # True
    print(solution.oneEditAway("pales", "pal"))  # False

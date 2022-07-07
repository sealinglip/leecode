#
# @lc app=leetcode.cn id=535 lang=python3
#
# [535] TinyURL 的加密与解密
#
# TinyURL 是一种 URL 简化服务， 比如：当你输入一个 URL https: // leetcode.com/problems/design-tinyurl 时，它将返回一个简化的URL http: // tinyurl.com/4e9iAk 。请你设计一个类来加密与解密 TinyURL 。

# 加密和解密算法如何设计和运作是没有限制的，你只需要保证一个 URL 可以被加密成一个 TinyURL ，并且这个 TinyURL 可以用解密方法恢复成原本的 URL 。

# 实现 Solution 类：

# Solution() 初始化 TinyURL 系统对象。
# String encode(String longUrl) 返回 longUrl 对应的 TinyURL 。
# String decode(String shortUrl) 返回 shortUrl 原本的 URL 。题目数据保证给定的 shortUrl 是由同一个系统对象加密的。


# 示例：
# 输入：url = "https://leetcode.com/problems/design-tinyurl"
# 输出："http://tinyurl.com/4e9iAk"

# 解释：
# Solution obj = new Solution()
# string tiny = obj.encode(url)
# // 返回加密后得到的 TinyURL 。
# string ans = obj.decode(tiny)
# // 返回解密后得到的原本的 URL 。


# 提示：
# 1 <= url.length <= 10^4
# 题目数据保证 url 是一个有效的 URL

# @lc code=start
class Codec:
    def __init__(self) -> None:
        self.__db = {}
        self.__url2Id = {}
        self.__seed = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl in self.__url2Id:
            id = self.__url2Id[longUrl]
        else:
            id = self.__seed
            self.__db[id] = longUrl
            self.__url2Id[longUrl] = id
            self.__seed += 1
        return "http: // tinyurl.com/" + str(id)

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        i = shortUrl.rfind('/')
        id = int(shortUrl[i+1:])
        return self.__db[id]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
# @lc code=end
if __name__ == "__main__":
    codec = Codec()
    print(codec.decode(codec.encode("https://leetcode.com/problems/design-tinyurl")))

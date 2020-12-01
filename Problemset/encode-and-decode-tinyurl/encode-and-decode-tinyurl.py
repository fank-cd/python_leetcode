
# @Title: TinyURL 的加密与解密 (Encode and Decode TinyURL)
# @Author: 2464512446@qq.com
# @Date: 2019-07-16 10:44:52
# @Runtime: 36 ms
# @Memory: 11.4 MB

class Codec:
    def __init__(self):

        self.d1 = {}
        self.d2 = {}
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        INDEX = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
        TINYURL = "http://tinyurl.com/"
        import random
        tiny_url = ""
        for i in range(6):
            tiny_url += random.choice(INDEX)

        self.d1[longUrl] = TINYURL + tiny_url
        self.d2[TINYURL + tiny_url] = longUrl
        return TINYURL + tiny_url
    
    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.d2[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

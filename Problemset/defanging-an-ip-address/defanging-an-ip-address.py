
# @Title: IP 地址无效化 (Defanging an IP Address)
# @Author: 2464512446@qq.com
# @Date: 2019-07-16 10:23:09
# @Runtime: 24 ms
# @Memory: 11.6 MB

class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return address.replace(".","[.]")

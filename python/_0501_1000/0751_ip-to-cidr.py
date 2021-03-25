#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-31 15:05:25
# @Last Modified : 2020-07-31 15:05:25
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个起始 IP 地址 ip 和一个我们需要包含的 IP 的数量 n，返回用列表（最小可能的长度）表示的 CIDR块的范围。 
# 
#  CIDR 块是包含 IP 的字符串，后接斜杠和固定长度。例如：“123.45.67.89/20”。固定长度 “20” 表示在特定的范围中公共前缀位的长度。
#  
# 
#  示例 1： 
# 
#  输入：ip = "255.0.0.7", n = 10
# 输出：["255.0.0.7/32","255.0.0.8/29","255.0.0.16/32"]
# 解释：
# 转换为二进制时，初始IP地址如下所示（为清晰起见添加了空格）：
# 255.0.0.7 -> 11111111 00000000 00000000 00000111
# 地址 "255.0.0.7/32" 表示与给定地址有相同的 32 位前缀的所有地址，
# 在这里只有这一个地址。
# 
# 地址 "255.0.0.8/29" 表示与给定地址有相同的 29 位前缀的所有地址：
# 255.0.0.8 -> 11111111 00000000 00000000 00001000
# 有相同的 29 位前缀的地址如下：
# 11111111 00000000 00000000 00001000
# 11111111 00000000 00000000 00001001
# 11111111 00000000 00000000 00001010
# 11111111 00000000 00000000 00001011
# 11111111 00000000 00000000 00001100
# 11111111 00000000 00000000 00001101
# 11111111 00000000 00000000 00001110
# 11111111 00000000 00000000 00001111
# 
# 地址 "255.0.0.16/32" 表示与给定地址有相同的 32 位前缀的所有地址，
# 这里只有 11111111 00000000 00000000 00010000。
# 
# 总之，答案指定了从 255.0.0.7 开始的 10 个 IP 的范围。
# 
# 有一些其他的表示方法，例如：
# ["255.0.0.7/32","255.0.0.8/30", "255.0.0.12/30", "255.0.0.16/32"],
# 但是我们的答案是最短可能的答案。
# 
# 另外请注意以 "255.0.0.7/30" 开始的表示不正确，
# 因为其包括了 255.0.0.4 = 11111111 00000000 00000000 00000100 这样的地址，
# 超出了需要表示的范围。
#  
# 
#  
# 
#  注： 
# 
#  
#  ip 是有效的 IPv4 地址。 
#  每一个隐含地址 ip + x (其中 x < n) 都是有效的 IPv4 地址。 
#  n 为整数，范围为 [1, 1000]。 
#  
# 
#  
#  Related Topics 位运算 
#  👍 10 👎 0

"""
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        """
        Medium
        GOOD TODO
        """

        def ipToInt(ip):
            res = 0
            for x in ip.split("."):
                res = 256 * res + int(x)
            return res

        def intToIp(x):
            return ".".join(str((x >> i) & 255) for i in (24, 16, 8, 0))

        ans = []
        if ip == "0.0.0.0":
            ip = "0.0.0.1"
            n -= 1
            ans = ['0.0.0.0/32']
        start = ipToInt(ip)
        # print(start)
        # 方式1
        while n > 0:
            step = start & -start
            while step > n:
                step //= 2
            ans.append(intToIp(start) + "/" + str(33 - step.bit_length()))
            start += step
            n -= step
        # 方式2
        # while n:
        #     # 我们使用 n 和 start&-start（start 的最低位）的位长度来计算能表示 2**(32-mask)个 ip 地址的掩码
        #     # bin(12&(-12))==bin(12&~(12-1)) = '0b100'
        #     mask = 33 - min(n.bit_length(), (start & ~(start - 1)).bit_length())
        #     ans.append(intToIp(start) + "/" + str(mask))
        #     start += 1 << (32 - mask)
        #     n -= 1 << (32 - mask)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(ip="255.0.0.7", n=10), ["255.0.0.7/32", "255.0.0.8/29", "255.0.0.16/32"]],
    [dict(ip="0.0.0.0", n=1), ["0.0.0.0/32"]],
])
def test_solutions(kw, expected):
    assert Solution().ipToCIDR(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

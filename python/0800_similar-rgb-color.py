#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-31 16:44:52
# @Last Modified : 2020-07-31 16:44:52
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# RGB 颜色用十六进制来表示的话，每个大写字母都代表了某个从 0 到 f 的 16 进制数。 
# 
#  RGB 颜色 "#AABBCC" 可以简写成 "#ABC" 。例如，"#15c" 其实是 "#1155cc" 的简写。 
# 
#  现在，假如我们分别定义两个颜色 "#ABCDEF" 和 "#UVWXYZ"，则他们的相似度可以通过这个表达式 -(AB - UV)^2 - (CD - W
# X)^2 - (EF - YZ)^2 来计算。 
# 
#  那么给定颜色 "#ABCDEF"，请你返回一个与 #ABCDEF 最相似的 7 个字符代表的颜色，并且它是可以被简写形式表达的。（比如，可以表示成类似 "
# #XYZ" 的形式） 
# 
#  示例 1：
# 输入：color = "#09f166"
# 输出："#11ee66"
# 解释： 
# 因为相似度计算得出 -(0x09 - 0x11)^2 -(0xf1 - 0xee)^2 - (0x66 - 0x66)^2 = -64 -9 -0 = -7
# 3
# 这已经是所有可以简写的颜色中最相似的了
#  
# 
#  注意： 
# 
#  
#  color 是一个长度为 7 的字符串 
#  color 是一个有效的 RGB 颜色：对于仍和 i > 0，color[i] 都是一个在 0 到 f 范围的 16 进制数 
#  假如答案具有相同的（最大）相似度的话，都是可以被接受的 
#  所有输入、输出都必须使用小写字母，并且输出为 7 个字符 
#  
#  Related Topics 数学 字符串 
#  👍 6 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def similarRGB(self, color: str) -> str:
        """
        对于 AB，我们要在 00 到 ff 中找到一个相似度最大的。我们知道，00 到 ff 均为 17 的倍数，
        因此我们需要找到一个 17 的倍数，使得其与 AB 的差的绝对值最小。显然，当 AB mod 17 > 8 时，
        取刚好比 AB 大的那个数；当 AB mod 17 <= 8 时，取刚好比 AB 小或与 AB 相等的那个数
         ^-^数学题目
        """

        def f(comp):
            q, r = divmod(int(comp, 16), 17)
            if r > 16 // 2:
                q += 1
            return '{:02x}'.format(17 * q)

        return '#' + f(color[1:3]) + f(color[3:5]) + f(color[5:])


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def similarRGB(self, color: str) -> str:
        """AC"""
        a, b, c = color[1:3], color[3:5], color[5:7]
        choices = [char * 2 for char in "0123456789abcdef"]
        max_a = min(choices, key=lambda x: (int(x, 16) - int(a, 16)) ** 2)
        max_b = min(choices, key=lambda x: (int(x, 16) - int(b, 16)) ** 2)
        max_c = min(choices, key=lambda x: (int(x, 16) - int(c, 16)) ** 2)
        return "#{}{}{}".format(max_a, max_b, max_c)


@pytest.mark.parametrize("kw,expected", [
    [dict(color="#09f166"), "#11ee66"],
])
def test_solutions(kw, expected):
    assert Solution().similarRGB(**kw) == expected
    assert Solution1().similarRGB(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

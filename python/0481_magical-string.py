#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 神奇的字符串 S 只包含 '1' 和 '2'，并遵守以下规则： 
# 
#  字符串 S 是神奇的，因为串联字符 '1' 和 '2' 的连续出现次数会生成字符串 S 本身。 
# 
#  字符串 S 的前几个元素如下：S = “1221121221221121122 ......” 
# 
#  如果我们将 S 中连续的 1 和 2 进行分组，它将变成： 
# 
#  1 22 11 2 1 22 1 22 11 2 11 22 ...... 
# 
#  并且每个组中 '1' 或 '2' 的出现次数分别是： 
# 
#  1 2 2 1 1 2 1 2 2 1 2 2 ...... 
# 
#  你可以看到上面的出现次数就是 S 本身。 
# 
#  给定一个整数 N 作为输入，返回神奇字符串 S 中前 N 个数字中的 '1' 的数目。 
# 
#  注意：N 不会超过 100,000。 
# 
#  示例： 
# 
#  输入：6
# 输出：3
# 解释：神奇字符串 S 的前 6 个元素是 “12211”，它包含三个 1，因此返回 3。
#  
# 
#  
# 

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def magicalString(self, n: int) -> int:
        s = "122"
        p = 2
        while len(s) < n:
            # print(s,p,s[p])
            s += str((3 - int(s[-1]))) * int(s[p])
            p += 1
        return s[:n].count("1")


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    (6, 3),
    (66, 32),
])
def test_solutions(args, expected):
    assert Solution().magicalString(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

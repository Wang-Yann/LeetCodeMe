#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个有效的 IPv4 地址 address，返回这个 IP 地址的无效化版本。 
# 
#  所谓无效化 IP 地址，其实就是用 "[.]" 代替了每个 "."。 
# 
#  
# 
#  示例 1： 
# 
#  输入：address = "1.1.1.1"
# 输出："1[.]1[.]1[.]1"
#  
# 
#  示例 2： 
# 
#  输入：address = "255.100.50.0"
# 输出："255[.]100[.]50[.]0"
#  
# 
#  
# 
#  提示： 
# 
#  
#  给出的 address 是一个有效的 IPv4 地址 
#  
#  Related Topics 字符串

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")


# leetcode submit region end(Prohibit modification and deletion)
@pytest.mark.parametrize("kw,expected", [
    [dict(address="1.1.1.1"), "1[.]1[.]1[.]1"],
    [dict(address="255.100.50.0"), "255[.]100[.]50[.]0"],
])
def test_solutions(kw, expected):
    assert Solution().defangIPaddr(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

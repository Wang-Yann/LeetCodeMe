#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给定一个整数，将其转化为7进制，并以字符串形式输出。 
# 
#  示例 1: 
# 
#  
# 输入: 100
# 输出: "202"
#  
# 
#  示例 2: 
# 
#  
# 输入: -7
# 输出: "-10"
#  
# 
#  注意: 输入范围是 [-1e7, 1e7] 。 
# 

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def convertToBase7(self, num: int) -> str:
        if num < 0:
            return "-" + self.convertToBase7(-num)
        if num < 7:
            return str(num)
        return self.convertToBase7(num // 7) + str(num % 7)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    (100, "202"),
    pytest.param(-7, "-10"),
])
def test_solutions(args, expected):
    assert Solution().convertToBase7(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

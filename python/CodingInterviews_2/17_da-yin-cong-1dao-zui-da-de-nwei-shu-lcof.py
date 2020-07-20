#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-05-02 22:01:25
# @Last Modified : 2020-05-02 22:01:25
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。
#
#  示例 1:
#
#  输入: n = 1
# 输出: [1,2,3,4,5,6,7,8,9]
#
#
#
#
#  说明：
#
#
#  用返回一个整数列表来代替打印
#  n 为正整数
#
#  Related Topics 数学
#  👍 36 👎 0


import traceback
import pytest
from typing import List

class Solution:
    def printNumbers(self, n: int) -> List[int]:
        return list(range(1,10**n))

@pytest.mark.parametrize("args,expected", [
    (1, [1,2,3,4,5,6,7,8,9]),
])
def test_solutions(args, expected):
    assert Solution().printNumbers(args) == expected





if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])



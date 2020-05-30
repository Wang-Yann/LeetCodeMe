#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个整数 n, 返回从 1 到 n 的字典顺序。 
# 
#  例如， 
# 
#  给定 n =1 3，返回 [1,10,11,12,13,2,3,4,5,6,7,8,9] 。 
# 
#  请尽可能的优化算法的时间复杂度和空间复杂度。 输入的数据 n 小于等于 5,000,000。 
# 

"""
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def lexicalOrder(self, n: int) -> List[int]:
        lst = list(range(1, n + 1))
        return sorted(lst, key=str)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    (13, [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]),
])
def test_solutions(args, expected):
    assert Solution().lexicalOrder(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

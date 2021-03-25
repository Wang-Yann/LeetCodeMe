#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定两个正整数 x 和 y，如果某一整数等于 x^i + y^j，其中整数 i >= 0 且 j >= 0，那么我们认为该整数是一个强整数。 
# 
#  返回值小于或等于 bound 的所有强整数组成的列表。 
# 
#  你可以按任何顺序返回答案。在你的回答中，每个值最多出现一次。 
# 
#  
# 
#  示例 1： 
# 
#  输入：x = 2, y = 3, bound = 10
# 输出：[2,3,4,5,7,9,10]
# 解释： 
# 2 = 2^0 + 3^0
# 3 = 2^1 + 3^0
# 4 = 2^0 + 3^1
# 5 = 2^1 + 3^1
# 7 = 2^2 + 3^1
# 9 = 2^3 + 3^0
# 10 = 2^0 + 3^2
#  
# 
#  示例 2： 
# 
#  输入：x = 3, y = 5, bound = 15
# 输出：[2,4,6,8,10,14]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= x <= 100 
#  1 <= y <= 100 
#  0 <= bound <= 10^6 
#  
#  Related Topics 哈希表 数学

"""

import math
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        ans = set()
        # 2**20 > bound
        N = math.floor(math.log(10 ** 6, 2))+1
        for i in range(N):
            for j in range(N):
                v = x ** i + y ** j
                if v <= bound:
                    ans.add(v)
        return list(ans)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(x=2, y=3, bound=10), [2, 3, 4, 5, 7, 9, 10]],
    [dict(x=3, y=5, bound=15), [2, 4, 6, 8, 10, 14]],
])
def test_solutions(kw, expected):
    assert Solution().powerfulIntegers(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

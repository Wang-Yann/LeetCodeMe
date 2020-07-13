#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-13 18:28:57
# @Last Modified : 2020-07-13 18:28:57
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定两个整数数组，请交换一对数值（每个数组中取一个数值），使得两个数组所有元素的和相等。 
# 
#  返回一个数组，第一个元素是第一个数组中要交换的元素，第二个元素是第二个数组中要交换的元素。若有多个答案，返回任意一个均可。若无满足条件的数值，返回空数组。
#  
# 
#  示例: 
# 
#  输入: array1 = [4, 1, 2, 1, 1, 2], array2 = [3, 6, 3, 3]
# 输出: [1, 3]
#  
# 
#  示例: 
# 
#  输入: array1 = [1, 2, 3], array2 = [4, 5, 6]
# 输出: [] 
# 
#  提示： 
# 
#  
#  1 <= array1.length, array2.length <= 100000 
#  
#  Related Topics 排序 数组 
#  👍 8 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findSwapValues(self, array1: List[int], array2: List[int]) -> List[int]:
        sum1 = sum(array1)
        sum2 = sum(array2)
        diff = sum1 - sum2
        if diff % 2 != 0:
            return []
        delta = diff // 2
        lookup = set(array1)
        for v2 in array2:
            if v2 + delta in lookup:
                return [v2 + delta, v2]
        return []


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(array1=[4, 1, 2, 1, 1, 2], array2=[3, 6, 3, 3]), [1, 3]],
    [dict(array1=[1, 2, 3], array2=[4, 5, 6]), []],
])
def test_solutions(kw, expected):
    assert Solution().findSwapValues(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

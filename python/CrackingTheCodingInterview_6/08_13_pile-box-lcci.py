#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-13 11:49:44
# @Last Modified : 2020-07-13 11:49:44
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 堆箱子。给你一堆n个箱子，箱子宽 wi、深 di、高 hi。箱子不能翻转，将箱子堆起来时，下面箱子的宽度、高度和深度必须大于上面的箱子。实现一种方法，搭出最
# 高的一堆箱子。箱堆的高度为每个箱子高度的总和。 
# 
#  输入使用数组[wi, di, hi]表示每个箱子。 
# 
#  示例1: 
# 
#   输入：box = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
#  输出：6
#  
# 
#  示例2: 
# 
#   输入：box = [[1, 1, 1], [2, 3, 4], [2, 6, 7], [3, 4, 5]]
#  输出：10
#  
# 
#  提示: 
# 
#  
#  箱子的数目不大于3000个。 
#  
#  Related Topics 动态规划 回溯算法 
#  👍 16 👎 0

"""

import functools
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def pileBox(self, box: List[List[int]]) -> int:
        @functools.lru_cache(maxsize=None)
        def dp(w, d, h):
            inners = [(iw, id, ih) for iw, id, ih in box if iw < w and id < d and ih < h]
            if not inners:
                return h
            return max((dp(iw, id, ih) for iw, id, ih in inners)) + h

        return max(dp(w, d, h) for w, d, h in box)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(box=[[1, 1, 1], [2, 2, 2], [3, 3, 3]]), 6],
    [dict(box=[[1, 1, 1], [2, 3, 4], [2, 6, 7], [3, 4, 5]]), 10],
])
def test_solutions(kw, expected):
    assert Solution().pileBox(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

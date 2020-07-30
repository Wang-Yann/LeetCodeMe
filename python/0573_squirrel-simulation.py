#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-30 15:26:39
# @Last Modified : 2020-07-30 15:26:39
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 现在有一棵树，一只松鼠和一些坚果。位置由二维网格的单元格表示。你的目标是找到松鼠收集所有坚果的最小路程，且坚果是一颗接一颗地被放在树下。松鼠一次最多只能携带
# 一颗坚果，松鼠可以向上，向下，向左和向右四个方向移动到相邻的单元格。移动次数表示路程。 
# 
#  输入 1: 
# 
#  输入: 
# 高度 : 5
# 宽度 : 7
# 树的位置 : [2,2]
# 松鼠 : [4,4]
# 坚果 : [[3,0], [2,5]]
# 输出: 12
# 解释:
# ​​​​​
#  
# 
#  注意: 
# 
#  
#  所有给定的位置不会重叠。 
#  松鼠一次最多只能携带一颗坚果。 
#  给定的坚果位置没有顺序。 
#  高度和宽度是正整数。 3 <= 高度 * 宽度 <= 10,000。 
#  给定的网格至少包含一颗坚果，唯一的一棵树和一只松鼠。 
#  
#  Related Topics 数学 
#  👍 12 👎 0

"""

import math
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        """
        数学应用题
        GOOD
        """

        def distance(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])

        ans = math.inf
        sum_dis = sum(distance(nut, tree) for nut in nuts) * 2
        for first_nut in nuts:
            cur = sum_dis - distance(first_nut, tree) + distance(first_nut, squirrel)
            ans = min(cur, ans)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ((5, 7, [2, 2], [4, 4], [[3, 0], [2, 5]]), 12),
])
def test_solutions(args, expected):
    assert Solution().minDistance(*args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 我们把玻璃杯摆成金字塔的形状，其中第一层有1个玻璃杯，第二层有2个，依次类推到第100层，每个玻璃杯(250ml)将盛有香槟。 
# 
#  从顶层的第一个玻璃杯开始倾倒一些香槟，当顶层的杯子满了，任何溢出的香槟都会立刻等流量的流向左右两侧的玻璃杯。当左右两边的杯子也满了，就会等流量的流向它们左
# 右两边的杯子，依次类推。（当最底层的玻璃杯满了，香槟会流到地板上） 
# 
#  例如，在倾倒一杯香槟后，最顶层的玻璃杯满了。倾倒了两杯香槟后，第二层的两个玻璃杯各自盛放一半的香槟。在倒三杯香槟后，第二层的香槟满了 - 此时总共有三个满
# 的玻璃杯。在倒第四杯后，第三层中间的玻璃杯盛放了一半的香槟，他两边的玻璃杯各自盛放了四分之一的香槟，如下图所示。 
# 
#  
# 
#  现在当倾倒了非负整数杯香槟后，返回第 i 行 j 个玻璃杯所盛放的香槟占玻璃杯容积的比例（i 和 j都从0开始）。 
# 
#  
# 
#  
# 示例 1:
# 输入: poured(倾倒香槟总杯数) = 1, query_glass(杯子的位置数) = 1, query_row(行数) = 1
# 输出: 0.0
# 解释: 我们在顶层（下标是（0，0））倒了一杯香槟后，没有溢出，因此所有在顶层以下的玻璃杯都是空的。
# 
# 示例 2:
# 输入: poured(倾倒香槟总杯数) = 2, query_glass(杯子的位置数) = 1, query_row(行数) = 1
# 输出: 0.5
# 解释: 我们在顶层（下标是（0，0）倒了两杯香槟后，有一杯量的香槟将从顶层溢出，位于（1，0）的玻璃杯和（1，1）的玻璃杯平分了这一杯香槟，所以每个玻璃杯有
# 一半的香槟。
#  
# 
#  注意: 
# 
#  
#  poured 的范围[0, 10 ^ 9]。 
#  query_glass 和query_row 的范围 [0, 99]。 
#  
# 

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        res = [[0] * k for k in range(1, 102)]
        res[0][0] = poured
        for r in range(query_row + 1):
            for c in range(r+1):
                q = (res[r][c] - 1.0) / 2.0
                if q > 0:
                    res[r + 1][c] += q
                    res[r + 1][c + 1] += q
        return min(1, res[query_row][query_glass])


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(poured=1, query_glass=1, query_row=1), 0),
    pytest.param(dict(poured=2, query_glass=1, query_row=1), 0.5),
    pytest.param(dict(poured=2, query_glass=0, query_row=0), 1),
])
def test_solutions(kwargs, expected):
    assert Solution().champagneTower(**kwargs) == pytest.approx(expected, 1e-4)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

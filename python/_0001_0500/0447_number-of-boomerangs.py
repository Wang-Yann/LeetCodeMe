#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给定平面上 n 对不同的点，“回旋镖” 是由点表示的元组 (i, j, k) ，其中 i 和 j 之间的距离和 i 和 k 之间的距离相等（需要考虑元组的顺
# 序）。 
# 
#  找到所有回旋镖的数量。你可以假设 n 最大为 500，所有点的坐标在闭区间 [-10000, 10000] 中。 
# 
#  示例: 
# 
#  
# 输入:
# [[0,0],[1,0],[2,0]]
# 
# 输出:
# 2
# 
# 解释:
# 两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]
#  
#  Related Topics 哈希表

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        dist = lambda x, y:(x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2
        length = len(points)
        ans = 0

        for i in range(length):
            col = collections.defaultdict(int)
            for j in range(length):
                if i==j:
                    continue
                dis = dist(points[i], points[j])
                col[dis] += 1
            for k, vs in col.items():
                if vs > 1:
                    ans += vs * (vs - 1)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ([[0, 0], [1, 0], [2, 0]], 2),
    ([[0,0],[1,0],[-1,0],[0,1],[0,-1]], 20),
])
def test_solutions(args, expected):
    assert Solution().numberOfBoomerangs(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

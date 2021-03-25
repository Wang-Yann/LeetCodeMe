#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-29 14:08:18
# @Last Modified : 2020-07-29 14:08:18
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个按顺序连接的多边形的顶点，判断该多边形是否为凸多边形。（凸多边形的定义） 
# 
#  注： 
# 
#  
#  顶点个数至少为 3 个且不超过 10,000。 
#  坐标范围为 -10,000 到 10,000。 
#  你可以假定给定的点形成的多边形均为简单多边形（简单多边形的定义）。换句话说，保证每个顶点处恰好是两条边的汇合点，并且这些边 互不相交 。 
#  
# 
#  
# 
#  示例 1： 
# 
#  [[0,0],[0,1],[1,1],[1,0]]
# 
# 输出： True
# 
# 解释：
#  
# 
#  示例 2： 
# 
#  [[0,0],[0,10],[10,10],[10,0],[5,5]]
# 
# 输出： False
# 
# 解释：
#  
#  Related Topics 数学 
#  👍 12 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isConvex(self, points: List[List[int]]) -> bool:
        """检查叉积结果是否变化　"""
        N = len(points)
        pre = 0
        for i in range(N):
            x1 = points[(i + 1) % N][0] - points[i][0]
            y1 = points[(i + 1) % N][1] - points[i][1]
            x2 = points[(i + 2) % N][0] - points[i][0]
            y2 = points[(i + 2) % N][1] - points[i][1]
            cur = x1 * y2 - x2 * y1
            if cur:
                if cur * pre < 0:
                    return False
                pre = cur
        return True


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ([[0, 0], [0, 1], [1, 1], [1, 0]], True),
    ([[0, 0], [0, 10], [10, 10], [10, 0], [5, 5]], False),
])
def test_solutions(args, expected):
    assert Solution().isConvex(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

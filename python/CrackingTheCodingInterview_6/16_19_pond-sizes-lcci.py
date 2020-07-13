#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-13 18:09:46
# @Last Modified : 2020-07-13 18:09:46
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 你有一个用于表示一片土地的整数矩阵land，该矩阵中每个点的值代表对应地点的海拔高度。若值为0则表示水域。由垂直、水平或对角连接的水域为池塘。池塘的大小是指
# 相连接的水域的个数。编写一个方法来计算矩阵中所有池塘的大小，返回值需要从小到大排序。 
#  示例： 
#  输入：
# [
#   [0,2,1,0],
#   [0,1,0,1],
#   [1,1,0,1],
#   [0,1,0,1]
# ]
# 输出： [1,2,4]
#  
#  提示： 
#  
#  0 < len(land) <= 1000 
#  0 < len(land[i]) <= 1000 
#  
#  Related Topics 深度优先搜索 广度优先搜索 
#  👍 14 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        R, C = len(land), len(land[0])
        res = []

        def dfs(i, j):
            if 0 <= i <= R - 1 and 0 <= j <= C - 1 and land[i][j] == 0:
                land[i][j] = 0x7fffffff
                ans = 1
                for x, y in [(i, j + 1), (i, j - 1), (i - 1, j), (i + 1, j), (i - 1, j - 1), (i - 1, j + 1),
                             (i + 1, j - 1), (i + 1, j + 1)]:
                    ans += dfs(x, y)
                return ans
            return 0

        for i in range(R):
            for j in range(C):
                if land[i][j] == 0:
                    res.append(dfs(i, j))
        return sorted(res)


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(
        land=[
            [0, 2, 1, 0],
            [0, 1, 0, 1],
            [1, 1, 0, 1],
            [0, 1, 0, 1]
        ]
    ), [1, 2, 4]],
])
def test_solutions(kw, expected):
    assert Solution().pondSizes(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

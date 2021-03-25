#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-29 17:33:23
# @Last Modified : 2020-07-29 17:33:23
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一幅黑白像素组成的图像, 计算黑色孤独像素的数量。 
# 
#  图像由一个由‘B’和‘W’组成二维字符数组表示, ‘B’和‘W’分别代表黑色像素和白色像素。 
# 
#  黑色孤独像素指的是在同一行和同一列不存在其他黑色像素的黑色像素。 
# 
#  示例: 
# 
#  输入: 
# [['W', 'W', 'B'],
#  ['W', 'B', 'W'],
#  ['B', 'W', 'W']]
# 
# 输出: 3
# 解析: 全部三个'B'都是黑色孤独像素。
#  
# 
#  
# 
#  注意: 
# 
#  
#  输入二维数组行和列的范围是 [1,500]。 
#  
# 
#  
#  Related Topics 深度优先搜索 数组 
#  👍 8 👎 0

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        """
        AC
        Success: Runtime:516 ms, faster than 100.00% of Python3 online submissions.
        Memory Usage:14.7 MB, less than 100.00% of Python3 online submissions.
        """
        rows = collections.defaultdict(list)
        cols = collections.defaultdict(list)
        R, C = len(picture), len(picture[0])
        for i in range(R):
            for j in range(C):
                if picture[i][j] == "B":
                    rows[i].append(j)
                    cols[j].append(i)
        ans = 0
        for r, cs in rows.items():
            if len(cs) > 1:
                continue
            col = cs[0]
            if len(cols[col]) == 1:
                ans += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)


class Solution1(object):
    def findLonelyPixel(self, picture):
        return sum(col.count('B') == 1 == picture[col.index('B')].count('B') for col in zip(*picture))


class Solution2(object):
    def findLonelyPixel(self, picture):
        rows, cols = [0] * len(picture), [0] * len(picture[0])
        for i in range(len(picture)):
            for j in range(len(picture[0])):
                if picture[i][j] == 'B':
                    rows[i] += 1
                    cols[j] += 1

        result = 0
        for i in range(len(picture)):
            if rows[i] == 1:
                for j in range(len(picture[0])):
                    result += picture[i][j] == 'B' and cols[j] == 1
        return result


@pytest.mark.parametrize("kw,expected", [
    [dict(
        picture=
        [['W', 'W', 'B'],
         ['W', 'B', 'W'],
         ['B', 'W', 'W']]

    ), 3],
])
def test_solutions(kw, expected):
    assert Solution().findLonelyPixel(**kw) == expected
    assert Solution1().findLonelyPixel(**kw) == expected
    assert Solution2().findLonelyPixel(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-05 14:33:22
# @Last Modified : 2020-08-05 14:33:22
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 现在有一个尺寸为 width * height 的矩阵 M，矩阵中的每个单元格的值不是 0 就是 1。 
# 
#  而且矩阵 M 中每个大小为 sideLength * sideLength 的 正方形 子阵中，1 的数量不得超过 maxOnes。 
# 
#  请你设计一个算法，计算矩阵中最多可以有多少个 1。 
# 
#  
# 
#  示例 1： 
# 
#  输入：width = 3, height = 3, sideLength = 2, maxOnes = 1
# 输出：4
# 解释：
# 题目要求：在一个 3*3 的矩阵中，每一个 2*2 的子阵中的 1 的数目不超过 1 个。
# 最好的解决方案中，矩阵 M 里最多可以有 4 个 1，如下所示：
# [1,0,1]
# [0,0,0]
# [1,0,1]
#  
# 
#  示例 2： 
# 
#  输入：width = 3, height = 3, sideLength = 2, maxOnes = 2
# 输出：6
# 解释：
# [1,0,1]
# [1,0,1]
# [1,0,1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= width, height <= 100 
#  1 <= sideLength <= width, height 
#  0 <= maxOnes <= sideLength * sideLength 
#  
#  Related Topics 排序 数学 
#  👍 17 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
        """
         https://leetcode.jp/leetcode-1183-maximum-number-of-ones-%e8%a7%a3%e9%a2%98%e6%80%9d%e8%b7%af%e5%88%86%e6%9e%90/
        """
        if width < height:
            width, height = height, width

        # 1. split matrix by SxS tiles
        # 2. split each SxS tile into four parts
        #    (r, c), (r, S-c), (S-r, c), (S-r, S-c)
        # 3. for each count of tile part in matrix is
        #    (R+1)*(C+1), (R+1)*C, R*(C+1), R*C (already in descending order)
        # 4. fill one into matrix by tile part of which count is in descending order
        #    until number of ones in a tile comes to maxOnes
        #
        # ps. area of a tile and its count in matrix are as follows:
        #
        #  |<---- c ---->|<-- S-c -->|
        #  ^             |           |
        #  |             |           |
        #  r (R+1)*(C+1) |  (R+1)*C  |
        #  |             |           |
        #  v             |           |
        #  ---------------------------
        #  ^             |           |
        #  |             |           |
        #  S-r  R*(C+1)  |   R*C     |
        #  |             |           |
        #  v             |           |
        #  ---------------------------
        #

        R, r = divmod(height, sideLength)
        C, c = divmod(width, sideLength)
        assert (R <= C)
        area_counts = [(r * c, (R + 1) * (C + 1)), (r * (sideLength - c), (R + 1) * C),
                       ((sideLength - r) * c, R * (C + 1)), ((sideLength - r) * (sideLength - c), R * C)]
        # print(R,r,C,c,sideLength,area_counts)
        result = 0
        for area, count in area_counts:
            area = min(maxOnes, area)
            result += count * area
            maxOnes -= area
            if not maxOnes:
                break
        return result


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(width=3, height=3, sideLength=2, maxOnes=1), 4],
    [dict(width=3, height=3, sideLength=2, maxOnes=2), 6],
    [dict(width=11, height=7, sideLength=3, maxOnes=2), 24],
])
def test_solutions(kw, expected):
    assert Solution().maximumNumberOfOnes(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

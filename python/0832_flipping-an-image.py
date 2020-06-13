#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给定一个二进制矩阵 A，我们想先水平翻转图像，然后反转图像并返回结果。 
# 
#  水平翻转图片就是将图片的每一行都进行翻转，即逆序。例如，水平翻转 [1, 1, 0] 的结果是 [0, 1, 1]。 
# 
#  反转图片的意思是图片中的 0 全部被 1 替换， 1 全部被 0 替换。例如，反转 [0, 1, 1] 的结果是 [1, 0, 0]。 
# 
#  示例 1: 
# 
#  
# 输入: [[1,1,0],[1,0,1],[0,0,0]]
# 输出: [[1,0,0],[0,1,0],[1,1,1]]
# 解释: 首先翻转每一行: [[0,1,1],[1,0,1],[0,0,0]]；
#      然后反转图片: [[1,0,0],[0,1,0],[1,1,1]]
#  
# 
#  示例 2: 
# 
#  
# 输入: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
# 输出: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# 解释: 首先翻转每一行: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]]；
#      然后反转图片: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
#  
# 
#  说明: 
# 
#  
#  1 <= A.length = A[0].length <= 20 
#  0 <= A[i][j] <= 1 
#  
#  Related Topics 数组

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        ans = []
        for row in A:
            ans.append([bit ^ 1 for bit in reversed(row)])
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ([[1, 1, 0], [1, 0, 1], [0, 0, 0]], [[1, 0, 0], [0, 1, 0], [1, 1, 1]]),
    ([[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]], [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]]),
])
def test_solutions(args, expected):
    assert Solution().flipAndInvertImage(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

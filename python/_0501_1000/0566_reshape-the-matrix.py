#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 在MATLAB中，有一个非常有用的函数 reshape，它可以将一个矩阵重塑为另一个大小不同的新矩阵，但保留其原始数据。 
# 
#  给出一个由二维数组表示的矩阵，以及两个正整数r和c，分别表示想要的重构的矩阵的行数和列数。 
# 
#  重构后的矩阵需要将原始矩阵的所有元素以相同的行遍历顺序填充。 
# 
#  如果具有给定参数的reshape操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。 
# 
#  示例 1: 
# 
#  
# 输入: 
# nums = 
# [[1,2],
#  [3,4]]
# r = 1, c = 4
# 输出: 
# [[1,2,3,4]]
# 解释:
# 行遍历nums的结果是 [1,2,3,4]。新的矩阵是 1 * 4 矩阵, 用之前的元素值一行一行填充新矩阵。
#  
# 
#  示例 2: 
# 
#  
# 输入: 
# nums = 
# [[1,2],
#  [3,4]]
# r = 2, c = 4
# 输出: 
# [[1,2],
#  [3,4]]
# 解释:
# 没有办法将 2 * 2 矩阵转化为 2 * 4 矩阵。 所以输出原矩阵。
#  
# 
#  注意： 
# 
#  
#  给定矩阵的宽和高范围在 [1, 100]。 
#  给定的 r 和 c 都是正数。 
#  
#  Related Topics 数组

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)

class Solution(object):

    def matrixReshape(self, nums, r, c):
        if not nums or r * c != len(nums) * len(nums[0]):
            return nums

        result = [[0 for _ in range(c)] for _ in range(r)]
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                result[count // c][count % c] = nums[i][j]
                count += 1
        return result


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:

    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if not nums:
            return []
        m, n = len(nums), len(nums[0])

        if m * n != r * c or (m == r and n == c):
            return nums
        ans = []
        row = []
        idx = 0
        for i in range(m):
            for j in range(n):
                row.append(nums[i][j])
                idx += 1
                if idx == c:
                    ans.append(row)
                    row = []
                    idx = 0
        return ans


@pytest.mark.parametrize("kwargs,expected", [
    (dict(nums=[[1, 2], [3, 4]], r=1, c=4), [[1, 2, 3, 4]]),
    pytest.param(dict(nums=[[1, 2], [3, 4]], r=2, c=4), [[1, 2], [3, 4]]),
])
def test_solutions(kwargs, expected):
    assert Solution().matrixReshape(**kwargs) == expected
    assert Solution1().matrixReshape(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

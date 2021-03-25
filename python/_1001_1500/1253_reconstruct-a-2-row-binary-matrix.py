#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-05 15:08:46
# @Last Modified : 2020-07-05 15:08:46
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给你一个 2 行 n 列的二进制数组： 
# 
#  
#  矩阵是一个二进制矩阵，这意味着矩阵中的每个元素不是 0 就是 1。 
#  第 0 行的元素之和为 upper。 
#  第 1 行的元素之和为 lower。 
#  第 i 列（从 0 开始编号）的元素之和为 colsum[i]，colsum 是一个长度为 n 的整数数组。 
#  
# 
#  你需要利用 upper，lower 和 colsum 来重构这个矩阵，并以二维整数数组的形式返回它。 
# 
#  如果有多个不同的答案，那么任意一个都可以通过本题。 
# 
#  如果不存在符合要求的答案，就请返回一个空的二维数组。 
# 
#  
# 
#  示例 1： 
# 
#  输入：upper = 2, lower = 1, colsum = [1,1,1]
# 输出：[[1,1,0],[0,0,1]]
# 解释：[[1,0,1],[0,1,0]] 和 [[0,1,1],[1,0,0]] 也是正确答案。
#  
# 
#  示例 2： 
# 
#  输入：upper = 2, lower = 3, colsum = [2,2,1,1]
# 输出：[]
#  
# 
#  示例 3： 
# 
#  输入：upper = 5, lower = 5, colsum = [2,1,2,0,1,0,1,2,0,1]
# 输出：[[1,1,1,0,1,0,0,1,0,0],[1,0,1,0,0,0,1,1,0,1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= colsum.length <= 10^5 
#  0 <= upper, lower <= colsum.length 
#  0 <= colsum[i] <= 2 
#  
#  Related Topics 贪心算法 数学 
#  👍 11 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        C = len(colsum)
        upper_list = [0] * C
        lower_list = [0] * C
        for i, v in enumerate(colsum):
            if v == 1:
                if upper > lower:
                    upper_list[i] = 1
                    upper -= 1
                else:
                    lower_list[i] = 1
                    lower -= 1
            elif v == 2:
                upper_list[i] = lower_list[i] = 1
                upper -= 1
                lower -= 1
        return [upper_list, lower_list] if upper == lower == 0 else []


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kwargs,expected", [
    (dict(
        upper=2, lower=1, colsum=[1, 1, 1]
    ), ([[1, 1, 0], [0, 0, 1]], [[1, 0, 1], [0, 1, 0]], [[0, 1, 1], [1, 0, 0]])),
    pytest.param(dict(upper=2, lower=3, colsum=[2, 2, 1, 1]), []),
    pytest.param(dict(upper=5, lower=5, colsum=[2, 1, 2, 0, 1, 0, 1, 2, 0, 1]),
                 ([[1, 1, 1, 0, 1, 0, 0, 1, 0, 0], [1, 0, 1, 0, 0, 0, 1, 1, 0, 1]],)),
])
def test_solutions(kwargs, expected):
    res = Solution().reconstructMatrix(**kwargs)
    if not expected:
        assert res == []
        return
    assert sum(res[0]) == kwargs["upper"] and sum(res[1]) == kwargs["lower"]
    assert list(map(sum, zip(*res))) == kwargs["colsum"]


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])

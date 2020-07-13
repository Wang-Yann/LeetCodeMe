#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-13 11:38:24
# @Last Modified : 2020-07-13 11:38:24
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 在经典汉诺塔问题中，有 3 根柱子及 N 个不同大小的穿孔圆盘，盘子可以滑入任意一根柱子。一开始，所有盘子自上而下按升序依次套在第一根柱子上(即每一个盘子只
# 能放在更大的盘子上面)。移动圆盘时受到以下限制: 
# (1) 每次只能移动一个盘子; 
# (2) 盘子只能从柱子顶端滑出移到下一根柱子; 
# (3) 盘子只能叠在比它大的盘子上。 
# 
#  请编写程序，用栈将所有盘子从第一根柱子移到最后一根柱子。 
# 
#  你需要原地修改栈。 
# 
#  示例1: 
# 
#   输入：A = [2, 1, 0], B = [], C = []
#  输出：C = [2, 1, 0]
#  
# 
#  示例2: 
# 
#   输入：A = [1, 0], B = [], C = []
#  输出：C = [1, 0]
#  
# 
#  提示: 
# 
#  
#  A中盘子的数目不大于14个。 
#  
#  Related Topics 递归 
#  👍 29 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        """
        Do not return anything, modify C in-place instead.
        """

        def helper(n, x, y, z):
            """
            helper(n,x,y,z)代表将x柱上的n个盘，借助y柱移动到z柱上
            """
            if n == 1:
                z.append(x.pop())
                return
            else:
                helper(n - 1, x, z, y)
                helper(1, x, y, z)
                helper(n - 1, y, x, z)

        helper(len(A), A, B, C)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(A=[2, 1, 0], B=[], C=[]), [2, 1, 0]],
    [dict(A=[1, 0], B=[], C=[]), [1, 0]],
])
def test_solutions(kw, expected):
    Solution().hanota(**kw)
    assert kw["C"] == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

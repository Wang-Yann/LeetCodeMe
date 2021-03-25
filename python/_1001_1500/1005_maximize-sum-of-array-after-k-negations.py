#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给定一个整数数组 A，我们只能用以下方法修改该数组：我们选择某个索引 i 并将 A[i] 替换为 -A[i]，然后总共重复这个过程 K 次。（我们可以多次选
# 择同一个索引 i。） 
# 
#  以这种方式修改数组后，返回数组可能的最大和。 
# 
#  
# 
#  示例 1： 
# 
#  输入：A = [4,2,3], K = 1
# 输出：5
# 解释：选择索引 (1,) ，然后 A 变为 [4,-2,3]。
#  
# 
#  示例 2： 
# 
#  输入：A = [3,-1,0,2], K = 3
# 输出：6
# 解释：选择索引 (1, 2, 2) ，然后 A 变为 [3,1,0,2]。
#  
# 
#  示例 3： 
# 
#  输入：A = [2,-3,-1,5,-4], K = 2
# 输出：13
# 解释：选择索引 (1, 4) ，然后 A 变为 [2,3,-1,5,4]。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length <= 10000 
#  1 <= K <= 10000 
#  -100 <= A[i] <= 100 
#  
#  Related Topics 贪心算法

"""
import copy
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A.sort()
        remain = K
        for i in range(min(K, len(A))):
            if A[i] >= 0:
                break
            A[i] = -A[i]
            remain -= 1
        # print(A,remain)
        return sum(A) - (remain % 2) * min(A) * 2


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:

    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        """ 自己写的不优雅"""
        N = len(A)
        A.sort()
        i = 0
        while K > 0:
            if A[i] < 0:
                A[i] *= -1
                K -= 1
                if i < N - 1:
                    i += 1
            elif A[i] == 0:
                K = 0
            else:
                if K % 2 == 1:
                    min_i = min(list(range(i + 1)), key=A.__getitem__)
                    A[min_i] *= -1
                K = 0

        return sum(A)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(A=[4, -5, 4, -5, 9, 4, 5], K=1), 26),
    (dict(A=[4, 2, 3], K=1), 5),
    (dict(A=[-4, -2, -3], K=5), 9),
    (dict(A=[-4, -2, -3], K=6), 5),
    (dict(A=[-8, 3, -5, -3, -5, -2], K=6), 22),
    pytest.param(dict(A=[3, -1, 0, 2], K=3), 6),
    pytest.param(dict(A=[2, -3, -1, 5, -4], K=2), 13),
])
def test_solutions(kwargs, expected):
    kw1 = copy.deepcopy(kwargs)
    kw2 = copy.deepcopy(kwargs)
    assert Solution().largestSumAfterKNegations(**kw1) == expected
    # assert Solution1().largestSumAfterKNegations(**kw2) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

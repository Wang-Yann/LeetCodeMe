#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-13 14:02:56
# @Last Modified : 2020-07-13 14:02:56
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定两个排序后的数组 A 和 B，其中 A 的末端有足够的缓冲空间容纳 B。 编写一个方法，将 B 合并入 A 并排序。 
# 
#  初始化 A 和 B 的元素数量分别为 m 和 n。 
# 
#  示例: 
# 
#  输入:
# A = [1,2,3,0,0,0], m = 3
# B = [2,5,6],       n = 3
# 
# 输出: [1,2,2,3,5,6] 
# 
#  说明: 
# 
#  
#  A.length == n + m 
#  
#  Related Topics 数组 双指针 
#  👍 61 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        pa, pb = m - 1, n - 1
        tail = m + n - 1
        while pa >= 0 or pb >= 0:
            if pa == -1:
                A[tail] = B[pb]
                pb -= 1
            elif pb == -1:
                A[tail] = A[pa]
                pa -= 1
            elif A[pa] > B[pb]:
                A[tail] = A[pa]
                pa -= 1
            else:
                A[tail] = B[pb]
                pb -= 1
            tail -= 1


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(
        A=[1, 2, 3, 0, 0, 0], m=3,
        B=[2, 5, 6], n=3
    ), [1, 2, 2, 3, 5, 6]],
])
def test_solutions(kw, expected):
    Solution().merge(**kw)
    assert kw["A"] == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

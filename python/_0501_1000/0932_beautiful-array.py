#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 对于某些固定的 N，如果数组 A 是整数 1, 2, ..., N 组成的排列，使得： 
# 
#  对于每个 i < j，都不存在 k 满足 i < k < j 使得 A[k] * 2 = A[i] + A[j]。 
# 
#  那么数组 A 是漂亮数组。 
# 
#  
# 
#  给定 N，返回任意漂亮数组 A（保证存在一个）。 
# 
#  
# 
#  示例 1： 
# 
#  输入：4
# 输出：[2,1,4,3]
#  
# 
#  示例 2： 
# 
#  输入：5
# 输出：[3,1,2,5,4] 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= N <= 1000 
#  
# 
#  
#  Related Topics 分治算法

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        """奇数放左边，偶数放右边"""
        ans = [1]
        while len(ans) < N:
            ans = [i * 2 - 1 for i in ans] + [i * 2 for i in ans]
        return [i for i in ans if i <= N]


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    (4, ([2, 1, 4, 3], [1, 3, 2, 4])),
    (5, ([3, 1, 2, 5, 4], [1, 5, 3, 2, 4])),
])
def test_solutions(args, expected):
    assert Solution().beautifulArray(args) in expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

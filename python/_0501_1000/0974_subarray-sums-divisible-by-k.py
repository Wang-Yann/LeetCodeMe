#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个整数数组 A，返回其中元素之和可被 K 整除的（连续、非空）子数组的数目。 
# 
#  
# 
#  示例： 
# 
#  输入：A = [4,5,0,-2,-3,1], K = 5
# 输出：7
# 解释：
# 有 7 个子数组满足其元素之和可被 K = 5 整除：
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length <= 30000 
#  -10000 <= A[i] <= 10000 
#  2 <= K <= 10000 
#  
#  Related Topics 数组 哈希表

"""
import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
    通常，涉及连续子数组问题的时候，我们使用前缀和来解决。

    """

    def subarraysDivByK(self, A: List[int], K: int) -> int:
        res = 0
        prefix = 0
        lookup = collections.defaultdict(int)
        lookup[0] = 1
        for num in A:
            prefix = (prefix + num) % K
            res += lookup[prefix]
            lookup[prefix] += 1
        return res


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kwargs,expected", [
    (dict(
        A=[4, 5, 0, -2, -3, 1], K=5
    ), 7),
])
def test_solutions(kwargs, expected):
    assert Solution().subarraysDivByK(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

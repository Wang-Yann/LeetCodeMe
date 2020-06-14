#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给定一个整数数组 A，对于每个整数 A[i]，我们可以选择 x = -K 或是 x = K，并将 x 加到 A[i] 中。 
# 
#  在此过程之后，我们得到一些数组 B。 
# 
#  返回 B 的最大值和 B 的最小值之间可能存在的最小差值。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  输入：A = [1], K = 0
# 输出：0
# 解释：B = [1]
#  
# 
#  示例 2： 
# 
#  输入：A = [0,10], K = 2
# 输出：6
# 解释：B = [2,8]
#  
# 
#  示例 3： 
# 
#  输入：A = [1,3,6], K = 3
# 输出：3
# 解释：B = [4,6,3]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length <= 10000 
#  0 <= A[i] <= 10000 
#  0 <= K <= 10000 
#  
#  Related Topics 贪心算法 数学

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def smallestRangeII(self, A: List[int], K: int) -> int:
        """
        https://leetcode-cn.com/problems/smallest-range-ii/solution/tai-nan-liao-zhi-neng-hua-tu-ping-zhi-jue-by-user8/
        """
        A.sort()
        min_val, max_val = A[0], A[-1]
        ans = max_val - min_val
        for i in range(len(A) - 1):
            a, b = A[i], A[i + 1]
            ans = min(ans, max(max_val - K, a + K) - min(min_val + K, b - K))
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(
        A=[1], K=0
    ), 0),
    pytest.param(dict(A=[0, 10], K=2), 6),
    pytest.param(dict(A=[1, 3, 6], K=3), 3),
])
def test_solutions(kwargs, expected):
    assert Solution().smallestRangeII(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

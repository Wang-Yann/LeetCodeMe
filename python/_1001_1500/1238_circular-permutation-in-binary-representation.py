#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-05 12:10:10
# @Last Modified : 2020-07-05 12:10:10
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给你两个整数 n 和 start。你的任务是返回任意 (0,1,2,,...,2^n-1) 的排列 p，并且满足： 
# 
#  
#  p[0] = start 
#  p[i] 和 p[i+1] 的二进制表示形式只有一位不同 
#  p[0] 和 p[2^n -1] 的二进制表示形式也只有一位不同 
#  
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 2, start = 3
# 输出：[3,2,0,1]
# 解释：这个排列的二进制表示是 (11,10,00,01)
#      所有的相邻元素都有一位是不同的，另一个有效的排列是 [3,1,0,2]
#  
# 
#  示例 2： 
# 
#  输出：n = 3, start = 2
# 输出：[2,6,7,5,4,0,1,3]
# 解释：这个排列的二进制表示是 (010,110,111,101,100,000,001,011)
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 16 
#  0 <= start < 2^n 
#  
#  Related Topics 数学 
#  👍 23 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def circularPermutation(self, n: int, start: int) -> List[int]:
        """
        4-line Gray Code
        """
        return [start ^ i ^ (i >> 1) for i in range(1 << n)]


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(n=2, start=3), ([3, 2, 0, 1],)),
    pytest.param(dict(n=3, start=2), ([2, 3, 1, 0, 4, 5, 7, 6], [2, 6, 7, 5, 4, 0, 1, 3])),
])
def test_solutions(kwargs, expected):
    assert Solution().circularPermutation(**kwargs) in expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])

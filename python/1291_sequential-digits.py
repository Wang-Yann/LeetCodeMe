#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 我们定义「顺次数」为：每一位上的数字都比前一位上的数字大 1 的整数。 
# 
#  请你返回由 [low, high] 范围内所有顺次数组成的 有序 列表（从小到大排序）。 
# 
#  
# 
#  示例 1： 
# 
#  输出：low = 100, high = 300
# 输出：[123,234]
#  
# 
#  示例 2： 
# 
#  输出：low = 1000, high = 13000
# 输出：[1234,2345,3456,4567,5678,6789,12345]
#  
# 
#  
# 
#  提示： 
# 
#  
#  10 <= low <= high <= 10^9 
#  
#  Related Topics 回溯算法

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        for i in range(1, 10):
            num = i
            for j in range(i + 1, 10):
                num = num * 10 + j
                if low <= num <= high:
                    ans.append(num)
        return sorted(ans)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(low=100, high=300), [123, 234]],
    [dict(low=1000, high=13000), [1234, 2345, 3456, 4567, 5678, 6789, 12345]],
])
def test_solutions(kw, expected):
    assert Solution().sequentialDigits(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

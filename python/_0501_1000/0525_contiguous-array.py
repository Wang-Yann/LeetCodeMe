#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给定一个二进制数组, 找到含有相同数量的 0 和 1 的最长连续子数组（的长度）。 
# 
#  
# 
#  示例 1: 
# 
#  输入: [0,1]
# 输出: 2
# 说明: [0, 1] 是具有相同数量0和1的最长连续子数组。 
# 
#  示例 2: 
# 
#  输入: [0,1,0]
# 输出: 2
# 说明: [0, 1] (或 [1, 0]) 是具有相同数量0和1的最长连续子数组。 
# 
#  
# 
#  注意: 给定的二进制数组的长度不会超过50000。 
#  Related Topics 哈希表

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def findMaxLength(self, nums: List[int]) -> int:
        """
        我们使用一个变量 countcount ，用来保存遍历数组过程中到目前为止遇到的 0 和 1 的相对数量。 遇到 \text{1}1 的时候， countcount 变量加 1 ，遇到 0 的时候 countcount 变量减 1

        """
        ans, cnt = 0, 0
        lookup = {0:-1}
        for i, num in enumerate(nums):
            if num == 1:
                cnt += 1
            else:
                cnt -= 1
            if cnt in lookup:
                ans = max(ans, i - lookup[cnt])
            else:
                lookup[cnt] = i
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ([0, 1], 2),
    pytest.param([0, 1, 0], 2),
])
def test_solutions(args, expected):
    assert Solution().findMaxLength(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

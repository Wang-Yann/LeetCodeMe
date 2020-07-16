#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-16 09:36:12
# @Last Modified : 2020-07-16 09:36:12
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 桌上有 n 堆力扣币，每堆的数量保存在数组 coins 中。我们每次可以选择任意一堆，拿走其中的一枚或者两枚，求拿完所有力扣币的最少次数。 
# 
#  示例 1： 
# 
#  
#  输入：[4,2,1] 
# 
#  输出：4 
# 
#  解释：第一堆力扣币最少需要拿 2 次，第二堆最少需要拿 1 次，第三堆最少需要拿 1 次，总共 4 次即可拿完。 
#  
# 
#  示例 2： 
# 
#  
#  输入：[2,3,10] 
# 
#  输出：8 
#  
# 
#  限制： 
# 
#  
#  1 <= n <= 4 
#  1 <= coins[i] <= 10 
#  
#  👍 5 👎 0

"""

import math
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minCount(self, coins: List[int]) -> int:
        return sum(math.ceil(coin / 2) for coin in coins)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ([4, 2, 1], 4),
    ([2, 3, 10], 8),
])
def test_solutions(args, expected):
    assert Solution().minCount(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

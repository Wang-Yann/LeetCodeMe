#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给定一副牌，每张牌上都写着一个整数。 
# 
#  此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组： 
# 
#  
#  每组都有 X 张牌。 
#  组内所有的牌上都写着相同的整数。 
#  
# 
#  仅当你可选的 X >= 2 时返回 true。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[1,2,3,4,4,3,2,1]
# 输出：true
# 解释：可行的分组是 [1,1]，[2,2]，[3,3]，[4,4]
#  
# 
#  示例 2： 
# 
#  输入：[1,1,1,2,2,2,3,3]
# 输出：false
# 解释：没有满足要求的分组。
#  
# 
#  示例 3： 
# 
#  输入：[1]
# 输出：false
# 解释：没有满足要求的分组。
#  
# 
#  示例 4： 
# 
#  输入：[1,1]
# 输出：true
# 解释：可行的分组是 [1,1]
#  
# 
#  示例 5： 
# 
#  输入：[1,1,2,2,2,2]
# 输出：true
# 解释：可行的分组是 [1,1]，[2,2]，[2,2]
#  
# 
#  
# 提示： 
# 
#  
#  1 <= deck.length <= 10000 
#  0 <= deck[i] < 10000 
#  
# 
#  
#  Related Topics 数组 数学

"""

import collections
import functools
from typing import List

import pytest
import fractions


# leetcode submit region begin(Prohibit modification and deletion)


class Solution:

    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        counter = collections.Counter(deck)
        return functools.reduce(fractions.gcd, counter.values()) >= 2


# leetcode submit region end(Prohibit modification and deletion)
big_dict = {3:2880, 1:2130, 2:1377, 7:708, 5:633, 6:516, 0:423, 12:288, 8:201, 11:189, 10:138, 13:126, 9:108, 4:93, 15:48, 16:42, 17:39,
            14:27, 18:24}
big_input = [x for k, v in big_dict.items() for x in [k] * v]


@pytest.mark.parametrize("args,expected", [
    ([1, 2, 3, 4, 4, 3, 2, 1], True),
    ([1, 1], True),
    ([1, 1, 2, 2, 2, 2], True),
    pytest.param([1, 1, 1, 2, 2, 2, 3, 3], False),
    pytest.param([1], False),
    pytest.param([1, 1, 1, 1, 2, 2, 2, 2, 2, 2], True),
    pytest.param(big_input, True),
])
def test_solutions(args, expected):
    assert Solution().hasGroupsSizeX(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

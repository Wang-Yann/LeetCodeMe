#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 爱丽丝有一手（hand）由整数数组给定的牌。 
# 
#  现在她想把牌重新排列成组，使得每个组的大小都是 W，且由 W 张连续的牌组成。 
# 
#  如果她可以完成分组就返回 true，否则返回 false。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  输入：hand = [1,2,3,6,2,3,4,7,8], W = 3
# 输出：true
# 解释：爱丽丝的手牌可以被重新排列为 [1,2,3]，[2,3,4]，[6,7,8]。 
# 
#  示例 2： 
# 
#  输入：hand = [1,2,3,4,5], W = 4
# 输出：false
# 解释：爱丽丝的手牌无法被重新排列成几个大小为 4 的组。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= hand.length <= 10000 
#  0 <= hand[i] <= 10^9 
#  1 <= W <= hand.length 
#  
# 
#  
# 
#  注意：此题目与 1294 重复：https://leetcode-cn.com/problems/divide-array-in-sets-of-k-co
# nsecutive-numbers/ 
#  Related Topics Ordered Map

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        """
        GOOD
        """
        cards = collections.Counter(hand)
        for start in sorted(hand):
            if cards[start] > 0:
                for j in range(W - 1, -1, -1):
                    if start + j not in cards:
                        return False
                    cards[start + j] -= cards[start]
                    if cards[start + j] < 0:
                        return False
        return True


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(
        hand=[1, 2, 3, 6, 2, 3, 4, 7, 8], W=3
    ), True),
    pytest.param(dict(hand=[1, 2, 3, 4, 5], W=4), False),
])
def test_solutions(kwargs, expected):
    assert Solution().isNStraightHand(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

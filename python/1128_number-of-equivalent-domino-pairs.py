#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 18:00:00
# @Last Modified : 2020-07-02 18:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给你一个由一些多米诺骨牌组成的列表 dominoes。 
# 
#  如果其中某一张多米诺骨牌可以通过旋转 0 度或 180 度得到另一张多米诺骨牌，我们就认为这两张牌是等价的。 
# 
#  形式上，dominoes[i] = [a, b] 和 dominoes[j] = [c, d] 等价的前提是 a==c 且 b==d，或是 a==d 且 
# b==c。 
# 
#  在 0 <= i < j < dominoes.length 的前提下，找出满足 dominoes[i] 和 dominoes[j] 等价的骨牌对 (i,
#  j) 的数量。 
# 
#  
# 
#  示例： 
# 
#  输入：dominoes = [[1,2],[2,1],[3,4],[5,6]]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= dominoes.length <= 40000 
#  1 <= dominoes[i][j] <= 9 
#  
#  Related Topics 数组

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counter = collections.Counter([(min(x), max(x)) for x in dominoes])
        ans = 0
        for k, v in counter.items():
            ans += v * (v - 1) // 2
        return ans


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    (
            [[1, 2], [2, 1], [3, 4], [5, 6]]
            , 1),
])
def test_solutions(args, expected):
    assert Solution().numEquivDominoPairs(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

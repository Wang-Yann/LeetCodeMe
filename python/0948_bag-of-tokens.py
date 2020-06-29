#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 你的初始能量为 P，初始分数为 0，只有一包令牌。 
# 
#  令牌的值为 token[i]，每个令牌最多只能使用一次，可能的两种使用方法如下： 
# 
#  
#  如果你至少有 token[i] 点能量，可以将令牌置为正面朝上，失去 token[i] 点能量，并得到 1 分。 
#  如果我们至少有 1 分，可以将令牌置为反面朝上，获得 token[i] 点能量，并失去 1 分。 
#  
# 
#  在使用任意数量的令牌后，返回我们可以得到的最大分数。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  输入：tokens = [100], P = 50
# 输出：0
#  
# 
#  示例 2： 
# 
#  输入：tokens = [100,200], P = 150
# 输出：1
#  
# 
#  示例 3： 
# 
#  输入：tokens = [100,200,300,400], P = 200
# 输出：2
#  
# 
#  
# 
#  提示： 
# 
#  
#  tokens.length <= 1000 
#  0 <= tokens[i] < 10000 
#  0 <= P < 10000 
#  
#  Related Topics 贪心算法

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        """
        贪心
        在有能量时候，只能让令牌正面朝上，直到能量不够用了才能让令牌反面朝上
        """
        tokens.sort()
        res, points = 0, 0
        l, r = 0, len(tokens) - 1
        while l <= r:
            if P >= tokens[l]:
                P -= tokens[l]
                l += 1
                points += 1
                res = max(res, points)
            elif points > 0:
                points -= 1
                P += tokens[r]
                r -= 1
            else:
                break
        return res


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(tokens=[100], P=50), 0],
    [dict(tokens=[100, 200], P=150), 1],
    [dict(tokens=[100, 200, 300, 400], P=200), 2],
])
def test_solutions(kw, expected):
    assert Solution().bagOfTokensScore(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

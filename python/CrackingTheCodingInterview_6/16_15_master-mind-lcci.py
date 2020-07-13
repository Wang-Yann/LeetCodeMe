#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-13 17:29:01
# @Last Modified : 2020-07-13 17:29:01
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 珠玑妙算游戏（the game of master mind）的玩法如下。 
#  计算机有4个槽，每个槽放一个球，颜色可能是红色（R）、黄色（Y）、绿色（G）或蓝色（B）。例如，计算机可能有RGGB 4种（槽1为红色，槽2、3为绿色，槽
# 4为蓝色）。作为用户，你试图猜出颜色组合。打个比方，你可能会猜YRGB。要是猜对某个槽的颜色，则算一次“猜中”；要是只猜对颜色但槽位猜错了，则算一次“伪猜中”。
# 注意，“猜中”不能算入“伪猜中”。 
#  给定一种颜色组合solution和一个猜测guess，编写一个方法，返回猜中和伪猜中的次数answer，其中answer[0]为猜中的次数，answer[
# 1]为伪猜中的次数。 
#  示例： 
#  输入： solution="RGBY",guess="GGRR"
# 输出： [1,1]
# 解释： 猜中1次，伪猜中1次。
#  
#  提示： 
#  
#  len(solution) = len(guess) = 4 
#  solution和guess仅包含"R","G","B","Y"这4种字符 
#  
#  Related Topics 数组 
#  👍 12 👎 0

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def masterMind(self, solution: str, guess: str) -> List[int]:
        total = sum((collections.Counter(solution) & collections.Counter(guess)).values())
        right = sum(1 for (i, j) in zip(solution, guess) if i == j)
        return [right, total - right]


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(solution="RGBY", guess="GGRR"), [1, 1]],
])
def test_solutions(kw, expected):
    assert Solution().masterMind(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 19:09:37
# @Last Modified : 2020-05-05 19:09:37
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 森林中，每个兔子都有颜色。其中一些兔子（可能是全部）告诉你还有多少其他的兔子和自己有相同的颜色。我们将这些回答放在 answers 数组里。
#
#  返回森林中兔子的最少数量。
#
#
# 示例:
# 输入: answers = [1, 1, 2]
# 输出: 5
# 解释:
# 两只回答了 "1" 的兔子可能有相同的颜色，设为红色。
# 之后回答了 "2" 的兔子不会是红色，否则他们的回答会相互矛盾。
# 设回答了 "2" 的兔子为蓝色。
# 此外，森林中还应有另外 2 只蓝色兔子的回答没有包含在数组中。
# 因此森林中兔子的最少数量是 5: 3 只回答的和 2 只没有回答的。
#
# 输入: answers = [10, 10, 10]
# 输出: 11
#
# 输入: answers = []
# 输出: 0
#
#
#  说明:
#
#
#  answers 的长度最大为1000。
#  answers[i] 是在 [0, 999] 范围内的整数。
#
#  Related Topics 哈希表 数学
#  👍 33 👎 0

"""

import collections
from typing import List

import pytest


class Solution:

    def numRabbits(self, answers: List[int]) -> int:
        """
        HARD
        """
        counter = collections.Counter(answers)
        ret = 0
        for k, v in counter.items():
            ret+=v+((k+1-v)%(k+1))
        return ret


@pytest.mark.parametrize("args,expected", [
    ([1, 1, 2], 5),
    ([], 0),
    pytest.param([10, 10, 10], 11),
])
def test_solutions(args, expected):
    assert Solution().numRabbits(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

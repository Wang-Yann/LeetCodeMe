#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 19:51:49
# @Last Modified : 2020-05-05 19:51:49
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

from typing import List

import pytest


class Solution:

    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        """
        方法一：曼哈顿距离
        https://leetcode-cn.com/problems/escape-the-ghosts/solution/tao-tuo-zu-ai-zhe-by-leetcode/

        计算我们到目的地的曼哈顿距离是否小于所有阻碍者到达目的地的曼哈顿距离。

        """

        def taxi_dist(P, Q):
            return abs(P[0] - Q[0]) + abs(P[1] - Q[1])

        return all(taxi_dist([0, 0], target) < taxi_dist(ghost, target) for ghost in ghosts)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(ghosts=[[1, 0], [0, 3]], target=[0, 1]), True),
    (dict(ghosts=[[1, 0]], target=[2, 0]), False),
    (dict(ghosts=[[2, 0]], target=[1, 0]), False),
])
def test_solutions(kwargs, expected):
    assert Solution().escapeGhosts(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

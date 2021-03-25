#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-05-03 14:24:14
# @Last Modified : 2020-05-03 14:24:14
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# N 辆车沿着一条车道驶向位于 target 英里之外的共同目的地。
#
#  每辆车 i 以恒定的速度 speed[i] （英里/小时），从初始位置 position[i] （英里） 沿车道驶向目的地。
#
#  一辆车永远不会超过前面的另一辆车，但它可以追上去，并与前车以相同的速度紧接着行驶。
#
#  此时，我们会忽略这两辆车之间的距离，也就是说，它们被假定处于相同的位置。
#
#  车队 是一些由行驶在相同位置、具有相同速度的车组成的非空集合。注意，一辆车也可以是一个车队。
#
#  即便一辆车在目的地才赶上了一个车队，它们仍然会被视作是同一个车队。
#
#
#
#  会有多少车队到达目的地?
#
#
#
#  示例：
#
#  输入：target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
# 输出：3
# 解释：
# 从 10 和 8 开始的车会组成一个车队，它们在 12 处相遇。
# 从 0 处开始的车无法追上其它车，所以它自己就是一个车队。
# 从 5 和 3 开始的车会组成一个车队，它们在 6 处相遇。
# 请注意，在到达目的地之前没有其它车会遇到这些车队，所以答案是 3。
#
#
#
# 提示：
#
#
#  0 <= N <= 10 ^ 4
#  0 < target <= 10 ^ 6
#  0 < speed[i] <= 10 ^ 6
#  0 <= position[i] < target
#  所有车的初始位置各不相同。
#
#  Related Topics 排序
#  👍 65 👎 0

"""


from typing import List

import pytest


class Solution:

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        将车辆按照起始位置排序后，我们顺序扫描这些车辆。如果相邻的两辆车，前者比后者行驶到终点需要的时间短，那么后者永远追不上前者，
        即从后者开始的若干辆车辆会组成一个新的车队；
        如果前者不比后者行驶到终点需要的时间短，那么后者可以在终点前追上前者，并和前者形成车队。此时我们将后者到达终点的时间置为前者到达终点的时间。
        """
        cars = sorted(zip(position, speed))
        times = [float(target - p) / s for p, s in cars]
        ans, cur = 0, 0
        for t in reversed(times):
            if t > cur:
                ans += 1
                cur = t
        return ans


@pytest.mark.parametrize("kwargs,expected", [
    (dict(target=12, position=[10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3]), 3),
])
def test_solutions(kwargs, expected):
    assert Solution().carFleet(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

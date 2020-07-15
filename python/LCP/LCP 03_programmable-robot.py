#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-15 17:46:48
# @Last Modified : 2020-07-15 17:46:48
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 力扣团队买了一个可编程机器人，机器人初始位置在原点(0, 0)。小伙伴事先给机器人输入一串指令command，机器人就会无限循环这条指令的步骤进行移动。指令
# 有两种： 
# 
#  
#  U: 向y轴正方向移动一格 
#  R: 向x轴正方向移动一格。 
#  
# 
#  不幸的是，在 xy 平面上还有一些障碍物，他们的坐标用obstacles表示。机器人一旦碰到障碍物就会被损毁。 
# 
#  给定终点坐标(x, y)，返回机器人能否完好地到达终点。如果能，返回true；否则返回false。 
# 
#  
# 
#  示例 1： 
# 
#  输入：command = "URR", obstacles = [], x = 3, y = 2
# 输出：true
# 解释：U(0, 1) -> R(1, 1) -> R(2, 1) -> U(2, 2) -> R(3, 2)。 
# 
#  示例 2： 
# 
#  输入：command = "URR", obstacles = [[2, 2]], x = 3, y = 2
# 输出：false
# 解释：机器人在到达终点前会碰到(2, 2)的障碍物。 
# 
#  示例 3： 
# 
#  输入：command = "URR", obstacles = [[4, 2]], x = 3, y = 2
# 输出：true
# 解释：到达终点后，再碰到障碍物也不影响返回结果。 
# 
#  
# 
#  限制： 
# 
#  
#  2 <= command的长度 <= 1000 
#  command由U，R构成，且至少有一个U，至少有一个R 
#  0 <= x <= 1e9, 0 <= y <= 1e9 
#  0 <= obstacles的长度 <= 1000 
#  obstacles[i]不为原点或者终点 
#  
#  👍 69 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def robot(self, command: str, obstacles: List[List[int]], x: int, y: int) -> bool:
        xi = 0
        yi = 0
        ls = [[0, 0]]
        for m in command:
            if m == 'U':
                yi += 1
            elif m == 'R':
                xi += 1
            ls.append([xi, yi])
        nu = min(x // xi, y // yi)
        if [x, y] not in [[k[0] + xi * nu, k[1] + yi * nu] for k in ls]:
            return False
        for n in obstacles:
            if n[0] <= x and n[1] <= y:
                nu = min(n[0] // xi, n[1] // yi)
                if n in [[k[0] + xi * nu, k[1] + yi * nu] for k in ls]:
                    return False
        return True



# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(command="URR", obstacles=[], x=3, y=2), True],
    [dict(command="URR", obstacles=[[2, 2]], x=3, y=2), False],
    [dict(command="URR", obstacles=[[4, 2]], x=3, y=2), True],
    [dict(command="RUUR", obstacles=[[10, 5], [1, 6], [6, 10], [3, 0], [0, 3], [0, 10], [6, 2]], x=7856, y=9033), False],

])
def test_solutions(kw, expected):
    assert Solution().robot(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

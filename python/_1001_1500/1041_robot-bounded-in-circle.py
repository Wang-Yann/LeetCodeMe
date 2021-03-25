#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-29 18:00:00
# @Last Modified : 2020-06-29 18:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 在无限的平面上，机器人最初位于 (0, 0) 处，面朝北方。机器人可以接受下列三条指令之一： 
# 
#  
#  "G"：直走 1 个单位 
#  "L"：左转 90 度 
#  "R"：右转 90 度 
#  
# 
#  机器人按顺序执行指令 instructions，并一直重复它们。 
# 
#  只有在平面中存在环使得机器人永远无法离开时，返回 true。否则，返回 false。 
# 
#  
# 
#  示例 1： 
# 
#  输入："GGLLGG"
# 输出：true
# 解释：
# 机器人从 (0,0) 移动到 (0,2)，转 180 度，然后回到 (0,0)。
# 重复这些指令，机器人将保持在以原点为中心，2 为半径的环中进行移动。
#  
# 
#  示例 2： 
# 
#  输入："GG"
# 输出：false
# 解释：
# 机器人无限向北移动。
#  
# 
#  示例 3： 
# 
#  输入："GL"
# 输出：true
# 解释：
# 机器人按 (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ... 进行移动。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= instructions.length <= 100 
#  instructions[i] 在 {'G', 'L', 'R'} 中 
#  
#  Related Topics 数学

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def isRobotBounded(self, instructions: str) -> bool:
        """
        1.假设一轮后起点和终点重合，那么下一次的每一轮执行后，都必将回到起点，true
        2.假设一轮后起点和终点不重合，但方向终点和起点一致，那必将一条路走到黑了，false
        3.假设一轮后起点和终点不重合，但方向终点和起点不一致，也必将回到起点，因为不管角度偏移的如何，都会形成一个正多边形，角度偏移足够小，那就是个无线接近圆的正多边形，true

        """
        x, y, direction_id = 0, 0, 0
        directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        for char in instructions:
            if char == "L":
                direction_id = (direction_id + 1) % 4
            elif char == "R":
                direction_id = (direction_id - 1) % 4
            else:
                i, j = directions[direction_id]
                x += i
                y += j
        # print(seen,cur_x,cur_y)
        return (x == 0 and y == 0) or direction_id > 0


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ("GGLLGG", True),
    pytest.param("GG", False),
    pytest.param("GL", True),
    pytest.param("GLGLGGLGL", False),
])
def test_solutions(args, expected):
    assert Solution().isRobotBounded(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

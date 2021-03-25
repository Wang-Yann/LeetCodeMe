#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 机器人在一个无限大小的网格上行走，从点 (0, 0) 处开始出发，面向北方。该机器人可以接收以下三种类型的命令： 
# 
#  
#  -2：向左转 90 度 
#  -1：向右转 90 度 
#  1 <= x <= 9：向前移动 x 个单位长度 
#  
# 
#  在网格上有一些格子被视为障碍物。 
# 
#  第 i 个障碍物位于网格点 (obstacles[i][0], obstacles[i][1]) 
# 
#  机器人无法走到障碍物上，它将会停留在障碍物的前一个网格方块上，但仍然可以继续该路线的其余部分。 
# 
#  返回从原点到机器人所有经过的路径点（坐标为整数）的最大欧式距离的平方。 
# 
#  
# 
#  示例 1： 
# 
#  输入: commands = [4,-1,3], obstacles = []
# 输出: 25
# 解释: 机器人将会到达 (3, 4)
#  
# 
#  示例 2： 
# 
#  输入: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
# 输出: 65
# 解释: 机器人在左转走到 (1, 8) 之前将被困在 (1, 4) 处
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= commands.length <= 10000 
#  0 <= obstacles.length <= 10000 
#  -30000 <= obstacle[i][0] <= 30000 
#  -30000 <= obstacle[i][1] <= 30000 
#  答案保证小于 2 ^ 31 
#  
#  Related Topics 贪心算法

"""

import pytest
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools





# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        NORTH,WEST,SOUTH,EAST=range(4)
        directions ={NORTH:(0,1),WEST:(-1,0),SOUTH:(0,-1),EAST:(1,0)}
        obstacles_set={tuple(x) for x in obstacles}
        ans =0
        x,y=0,0
        d_index =NORTH
        for cmd in commands:
            if cmd==-2:
                d_index = (d_index+1)%4
            elif cmd==-1:
                d_index=(d_index+4-1)%4
            else:
                dx,dy = directions[d_index]
                for k in range(cmd):
                    if (x+dx,y+dy) not in obstacles_set:
                        x+=dx
                        y+=dy
                    ans =max(ans,x*x+y*y)

        return ans




        
# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(
        commands = [4,-1,3], obstacles = []
    ), 25),
    pytest.param(dict( commands = [4,-1,4,-2,4], obstacles = [[2,4]]  ), 65),
])
def test_solutions(kwargs, expected):
    assert Solution().robotSim(**kwargs) == expected






if __name__ == '__main__':
    pytest.main(["-q", "--color=yes","--capture=no", __file__])


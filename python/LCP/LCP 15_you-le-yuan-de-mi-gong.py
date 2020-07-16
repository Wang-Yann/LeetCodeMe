#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-16 21:17:58
# @Last Modified : 2020-07-16 21:17:58
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 小王来到了游乐园，她玩的第一个项目是模拟推销员。有一个二维平面地图，其中散布着 N 个推销点，编号 0 到 N-1，不存在三点共线的情况。每两点之间有一条直
# 线相连。游戏没有规定起点和终点，但限定了每次转角的方向。首先，小王需要先选择两个点分别作为起点和终点，然后从起点开始访问剩余 N-2 个点恰好一次并回到终点。访
# 问的顺序需要满足一串给定的长度为 N-2 由 L 和 R 组成的字符串 direction，表示从起点出发之后在每个顶点上转角的方向。根据这个提示，小王希望你能
# 够帮她找到一个可行的遍历顺序，输出顺序下标（若有多个方案，输出任意一种）。可以证明这样的遍历顺序一定是存在的。 
# 
#  
# 
#  （上图：A->B->C 右转； 下图：D->E->F 左转） 
# 
#  示例 1： 
# 
#  
#  输入：points = [[1,1],[1,4],[3,2],[2,1]], direction = "LL" 
# 
#  输入：[0,2,1,3] 
# 
#  解释：[0,2,1,3] 是符合"LL"的方案之一。在 [0,2,1,3] 方案中，0->2->1 是左转方向， 2->1->3 也是左转方向 
#  
# 
#  示例 2： 
# 
#  
#  输入：points = [[1,3],[2,4],[3,3],[2,1]], direction = "LR" 
# 
#  输入：[0,3,1,2] 
# 
#  解释：[0,3,1,2] 是符合"LR"的方案之一。在 [0,3,1,2] 方案中，0->3->1 是左转方向， 3->1->2 是右转方向 
#  
# 
#  限制： 
# 
#  
#  3 <= points.length <= 1000 且 points[i].length == 2 
#  1 <= points[i][0],points[i][1] <= 10000 
#  direction.length == points.length - 2 
#  direction 只包含 "L","R" 
#  
#  👍 5 👎 0


"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def sub(self, a, b):  # 求点 a 到点 b 的向量
        return [a[0] - b[0], a[1] - b[1]]

    def cross(self, a, b):  # 求向量 a 到向量 b 的向量叉积
        return a[0] * b[1] - a[1] * b[0]

    def visitOrder(self, points: List[List[int]], direction: str) -> List[int]:
        N = len(points)
        used = [False] * N  # 记录点的遍历情况， False未遍历 / True已遍历
        order = []  # 记录返回结果

        # 查找最左的点作为 起始点
        start = 0
        for i in range(0, N):
            if points[i][0] < points[start][0]:
                start = i
        used[start] = True
        order.append(start)

        for i in direction:
            nxt = -1
            if i == 'L':
                # 转向方向为 L，选择相对方向最右的点
                for j in range(0, N):
                    if not used[j]:
                        if nxt == -1 or self.cross(self.sub(points[nxt], points[start]), self.sub(points[j], points[start])) < 0:
                            nxt = j
            else:
                # 转向方向为 R，选择相对方向最左的点
                for j in range(0, N):
                    if not used[j]:
                        if nxt == -1 or self.cross(self.sub(points[nxt], points[start]), self.sub(points[j], points[start])) > 0:
                            nxt = j
            # 返回结果加入选择的点，更新下一次转向的起点
            used[nxt] = True
            order.append(nxt)
            start = nxt

        # 添加最后一个剩余点
        for i in range(0, N):
            if not used[i]:
                order.append(i)
        return order


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kwargs,expected", [
    [dict(points=[[1, 1], [1, 4], [3, 2], [2, 1]], direction="LL"),
     ([0, 2, 1, 3], [0, 3, 2, 1])],

    pytest.param(dict(points=[[1, 3], [2, 4], [3, 3], [2, 1]], direction="LR"), ([0, 2, 1, 3], [0, 3, 1, 2])),
])
def test_solutions(kwargs, expected):
    assert Solution().visitOrder(**kwargs) in expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])

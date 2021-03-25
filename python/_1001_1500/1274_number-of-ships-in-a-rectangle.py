#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-07 14:23:31
# @Last Modified : 2020-08-07 14:23:31
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# (此题是 交互式问题 ) 
# 
#  在用笛卡尔坐标系表示的二维海平面上，有一些船。每一艘船都在一个整数点上，且每一个整数点最多只有 1 艘船。 
# 
#  有一个函数 Sea.hasShips(topRight, bottomLeft) ，输入参数为右上角和左下角两个点的坐标，当且仅当这两个点所表示的矩形区域
# （包含边界）内至少有一艘船时，这个函数才返回 true ，否则返回 false 。 
# 
#  给你矩形的右上角 topRight 和左下角 bottomLeft 的坐标，请你返回此矩形内船只的数目。题目保证矩形内 至多只有 10 艘船。 
# 
#  调用函数 hasShips 超过400次 的提交将被判为 错误答案（Wrong Answer） 。同时，任何尝试绕过评测系统的行为都将被取消比赛资格。 
# 
#  
# 
#  示例： 
# 
#  
# 
#  输入：
# ships = [[1,1],[2,2],[3,3],[5,5]], topRight = [4,4], bottomLeft = [0,0]
# 输出：3
# 解释：在 [0,0] 到 [4,4] 的范围内总共有 3 艘船。
#  
# 
#  
# 
#  提示： 
# 
#  
#  ships 数组只用于评测系统内部初始化。你无法得知 ships 的信息，所以只能通过调用 hasShips 接口来求解。 
#  0 <= bottomLeft[0] <= topRight[0] <= 1000 
#  0 <= bottomLeft[1] <= topRight[1] <= 1000 
#  
#  Related Topics 分治算法 
#  👍 12 👎 0

"""

import pytest


class Point(object):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


cnt = 0
ships = []


class Sea(object):
    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
        global cnt, ships
        cnt += 1
        for p in ships:
            if bottomLeft.x <= p.x <= topRight.x and bottomLeft.y <= p.y <= topRight.y:
                return True
        return False


# leetcode submit region begin(Prohibit modification and deletion)
# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Sea(object):
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
# class Point(object):
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution(object):
    """AC """

    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:

        def helper(tr, bl):
            ans = 0
            if bl.x <= tr.x and bl.y <= tr.y and sea.hasShips(tr, bl):
                # 直接判断bl==tr陷入死循环　吸取教训 !!! 且判断
                if (tr.x, tr.y) == (bl.x, bl.y):
                    return 1
                mx, my = (tr.x + bl.x) // 2, (tr.y + bl.y) // 2
                ans += helper(Point(mx, my), bl)
                ans += helper(Point(mx, tr.y), Point(bl.x, my + 1))
                ans += helper(Point(tr.x, my), Point(mx + 1, bl.y))
                ans += helper(tr, Point(mx + 1, my + 1))
            return ans

        return helper(topRight, bottomLeft)


# leetcode submit region end(Prohibit modification and deletion)


class Solution1(object):
    def countShips(self, sea, topRight, bottomLeft):
        result = 0
        if topRight.x >= bottomLeft.x and \
                topRight.y >= bottomLeft.y and \
                sea.hasShips(topRight, bottomLeft):
            if (topRight.x, topRight.y) == (bottomLeft.x, bottomLeft.y):
                return 1
            mid_x, mid_y = (topRight.x + bottomLeft.x) // 2, (topRight.y + bottomLeft.y) // 2
            result += self.countShips(sea, topRight, Point(mid_x + 1, mid_y + 1))
            result += self.countShips(sea, Point(mid_x, topRight.y), Point(bottomLeft.x, mid_y + 1))
            result += self.countShips(sea, Point(topRight.x, mid_y), Point(mid_x + 1, bottomLeft.y))
            result += self.countShips(sea, Point(mid_x, mid_y), bottomLeft)
        return result


@pytest.mark.parametrize("kw,expected", [
    [dict(ships=[Point(1, 1), Point(2, 2), Point(3, 3), Point(5, 5)],
          topRight=Point(4, 4), bottomLeft=Point(0, 0)), 3],
    [dict(ships=[Point(1, 1), Point(2, 2), Point(3, 3)],
          topRight=Point(1000, 1000), bottomLeft=Point(0, 0)), 3],
])
def test_solutions(kw, expected):
    global ships
    ships = kw.pop("ships")
    kw['sea'] = Sea()
    res = Solution().countShips(**kw)
    assert res == expected
    assert cnt <= 400


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

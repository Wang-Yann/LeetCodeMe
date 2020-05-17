#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 有 N 个房间，开始时你位于 0 号房间。每个房间有不同的号码：0，1，2，...，N-1，并且房间里可能有一些钥匙能使你进入下一个房间。 
# 
#  在形式上，对于每个房间 i 都有一个钥匙列表 rooms[i]，每个钥匙 rooms[i][j] 由 [0,1，...，N-1] 中的一个整数表示，其中 
# N = rooms.length。 钥匙 rooms[i][j] = v 可以打开编号为 v 的房间。 
# 
#  最初，除 0 号房间外的其余所有房间都被锁住。 
# 
#  你可以自由地在房间之间来回走动。 
# 
#  如果能进入每个房间返回 true，否则返回 false。 
# 
#  
#  
# 
#  示例 1： 
# 
#  输入: [[1],[2],[3],[]]
# 输出: true
# 解释:  
# 我们从 0 号房间开始，拿到钥匙 1。
# 之后我们去 1 号房间，拿到钥匙 2。
# 然后我们去 2 号房间，拿到钥匙 3。
# 最后我们去了 3 号房间。
# 由于我们能够进入每个房间，我们返回 true。
#  
# 
#  示例 2： 
# 
#  输入：[[1,3],[3,0,1],[2],[0]]
# 输出：false
# 解释：我们不能进入 2 号房间。
#  
# 
#  提示： 
# 
#  
#  1 <= rooms.length <= 1000 
#  0 <= rooms[i].length <= 1000 
#  所有房间中的钥匙数量总计不超过 3000。 
#  
#  Related Topics 深度优先搜索 图

"""
import pytest
import math, fractions, operator
from typing import List
import collections, bisect, heapq
import functools, itertools





# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        length =len(rooms)
        if not length:return True
        graph = rooms
        seen = set()
        q=[0]
        while q:
            node =q.pop(0)
            seen.add(node)
            for neighbor in graph[node]:
                if neighbor not in seen:
                    q.append(neighbor)
                    seen.add(neighbor)
        return len(seen)==length

        
# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ( [[1],[2],[3],[]], True),
    pytest.param([[1,3],[3,0,1],[2],[0]], False),
])
def test_solutions(args, expected):
    assert Solution().canVisitAllRooms(args) == expected




if __name__ == '__main__':
    pytest.main(["-q", "--color=yes","--capture=no", __file__])
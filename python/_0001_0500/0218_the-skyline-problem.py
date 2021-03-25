#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 城市的天际线是从远处观看该城市中所有建筑物形成的轮廓的外部轮廓。现在，假设您获得了城市风光照片（图A）上显示的所有建筑物的位置和高度，请编写一个程序以输出由
# 这些建筑物形成的天际线（图B）。 
# 
#  
# 
#  每个建筑物的几何信息用三元组 [Li，Ri，Hi] 表示，其中 Li 和 Ri 分别是第 i 座建筑物左右边缘的 x 坐标，Hi 是其高度。可以保证 0 
# ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX 和 Ri - Li > 0。您可以假设所有建筑物都是在绝对平坦且高度为 0 的表面上的
# 完美矩形。 
# 
#  例如，图A中所有建筑物的尺寸记录为：[ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] 。 
# 
# 
#  输出是以 [ [x1,y1], [x2, y2], [x3, y3], ... ] 格式的“关键点”（图B中的红点）的列表，它们唯一地定义了天际线。关键点
# 是水平线段的左端点。请注意，最右侧建筑物的最后一个关键点仅用于标记天际线的终点，并始终为零高度。此外，任何两个相邻建筑物之间的地面都应被视为天际线轮廓的一部分。
#  
# 
#  例如，图B中的天际线应该表示为：[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ]。
#  
# 
#  说明: 
# 
#  
#  任何输入列表中的建筑物数量保证在 [0, 10000] 范围内。 
#  输入列表已经按左 x 坐标 Li 进行升序排列。 
#  输出列表必须按 x 位排序。 
#  输出天际线中不得有连续的相同高度的水平线。例如 [...[2 3], [4 5], [7 5], [11 5], [12 7]...] 是不正确的答案；三
# 条高度为 5 的线应该在最终输出中合并为一个：[...[2 3], [4 5], [12 7], ...] 
#  
#  Related Topics 堆 树状数组 线段树 分治算法 Line Sweep
https://leetcode-cn.com/problems/the-skyline-problem/solution/218tian-ji-xian-wen-ti-sao-miao-xian-fa-by-ivan_al/

"""
import bisect
import heapq
from typing import List

import pytest


class Solution0:

    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        """
        扫描线算法
        """
        if len(buildings) == 0:
            return []

        points = []
        for l, r, h in buildings:
            # 左端点通过负数高度来标识，同时适用于标准库中的小顶堆转换为大顶堆
            points.append((l, -h, r))
            points.append((r, h, 0))

        # 将扫描线中的关键点按照points的前两个元素x, y来排序
        points.sort()
        # 初始值，[0初始高度， float('inf')对应无穷右边界]
        height_heap = [[0, float('inf')]]
        res = [[0, 0]]

        for x, h, r in points:
            # 关键点：清除扫过的高楼
            while x >= height_heap[0][1]:
                heapq.heappop(height_heap)

            # 左端点入堆
            if h < 0:
                heapq.heappush(height_heap, [h, r])

            # 如果当前最大高度变化，说明是天际线中的关键点
            if res[-1][1] != -height_heap[0][0]:
                res.append([x, -height_heap[0][0]])

        return res[1:]


# leetcode submit region begin(Prohibit modification and deletion)


class Solution:

    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        """
        扫描线算法
        """
        heap_all = []
        res = []
        for l, r, h in buildings:
            # // critical point, left corner
            heap_all.append((l, -h))
            # // critical point, right corner
            heap_all.append((r, h))
        # // 保存当前位置所有高度。
        heights = [0]
        # // 保存上一个位置的横坐标以及高度
        last = [0, 0]
        heap_all.sort()
        for pos, h in heap_all:
            if h < 0:
                bisect.insort_left(heights,-h)
                # heapq.heappush(heights, -h) #// 左端点，高度入堆
            else:
                heights.remove(h) #// 右端点，移除高度
            # // 当前关键点，最大高度
            # max_h = heapq.nlargest(1, heights)[0]
            max_h = heights[-1]
            # // 当前最大高度如果不同于上一个高度，说明这是一个转折点
            if last[-1] != max_h:
                # // 更新 last，并加入结果集
                last = [pos, max_h]
                res.append(last)
        # print("res",res)
        return res


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]],
     [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]])
])
def test_solutions(args, expected):
    assert Solution().getSkyline(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

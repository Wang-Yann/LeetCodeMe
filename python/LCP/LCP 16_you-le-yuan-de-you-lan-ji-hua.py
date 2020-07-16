#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-16 22:02:11
# @Last Modified : 2020-07-16 22:02:11
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 又到了一年一度的春游时间，小吴计划去游乐场游玩 1 天，游乐场总共有 N 个游乐项目，编号从 0 到 N-1。小吴给每个游乐项目定义了一个非负整数值 val
# ue[i] 表示自己的喜爱值。两个游乐项目之间会有双向路径相连，整个游乐场总共有 M 条双向路径，保存在二维数组 edges中。 小吴计划选择一个游乐项目 A 
# 作为这一天游玩的重点项目。上午小吴准备游玩重点项目 A 以及与项目 A 相邻的两个项目 B、C （项目A、B与C要求是不同的项目，且项目B与项目C要求相邻），并
# 返回 A ，即存在一条 A-B-C-A 的路径。 下午，小吴决定再游玩重点项目 A以及与A相邻的两个项目 B'、C'，（项目A、B'与C'要求是不同的项目，且项
# 目B'与项目C'要求相邻），并返回 A ，即存在一条 A-B'-C'-A 的路径。下午游玩项目 B'、C' 可与上午游玩项目B、C存在重复项目。 小吴希望提前安
# 排好游玩路径，使得喜爱值之和最大。请你返回满足游玩路径选取条件的最大喜爱值之和，如果没有这样的路径，返回 0。 注意：一天中重复游玩同一个项目并不能重复增加喜爱
# 值了。例如：上下午游玩路径分别是 A-B-C-A与A-C-D-A 那么只能获得 value[A] + value[B] + value[C] + value[D
# ] 的总和。 
# 
#  示例 1： 
# 
#  
#  输入：edges = [[0,1],[1,2],[0,2]], value = [1,2,3] 
# 
#  输出：6 
# 
#  解释：喜爱值之和最高的方案之一是 0->1->2->0 与 0->2->1->0 。重复游玩同一点不重复计入喜爱值，返回1+2+3=6 
#  
# 
#  示例 2： 
# 
#  
#  输入：edges = [[0,2],[2,1]], value = [1,2,5] 
# 
#  输出：0 
# 
#  解释：无满足要求的游玩路径，返回 0 
#  
# 
#  示例 3： 
# 
#  
#  输入：edges = [[0,1],[0,2],[0,3],[0,4],[0,5],[1,3],[2,4],[2,5],[3,4],[3,5],[4,5]
# ], value = [7,8,6,8,9,7] 
# 
#  输出：39 
# 
#  解释：喜爱值之和最高的方案之一是 3->0->1->3 与 3->4->5->3 。喜爱值最高为 7+8+8+9+7=39 
#  
# 
#  限制： 
# 
#  
#  3 <= value.length <= 10000 
#  1 <= edges.length <= 10000 
#  0 <= edges[i][0],edges[i][1] < value.length 
#  0 <= value[i] <= 10000 
#  edges中没有重复的边 
#  edges[i][0] != edges[i][1] 
#  
#  👍 8 👎 0


"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def maxWeight(self, edges: List[List[int]], value: List[int]) -> int:

        def count_val(info1, info2):
            # 计算 两个三角的val总和， 过滤重复点
            all_points = set(info1[:3]) | set(info2[:3])
            return sum([weight[x] for x in all_points])

        def get_top3(triangle_list, triangle_info):
            # 更新 同一条边 的 top3 的三角形
            if not triangle_list:
                return [triangle_info]
            if triangle_list[-1][-1] >= triangle_info[-1]:
                triangle_list.append(triangle_info)
                return triangle_list
            for index in range(0, len(triangle_list)):
                if triangle_list[index][-1] < triangle_info[-1]:
                    triangle_list.insert(index, triangle_info)
                    break
            triangle_list = triangle_list[:3]
            return triangle_list

        weight = value
        N = len(weight)
        point_set = collections.defaultdict(set)  # 记录和 i相连且编号大于i的所有点
        for x, y in edges:
            if x > y:
                x, y = y, x
            point_set[x].add(y)

        max_triangle_point_dict = collections.defaultdict(list)  # 点i能构成的最大三角形
        triangle_point_dict = collections.defaultdict(list)  # 点i能构成的所有三角形
        triangle_edge_dict = collections.defaultdict(list)  # 边(i,j)能构成的 Top3 三角形

        # 查找三角形
        for i in range(N):
            for j in point_set[i]:
                all_points_list = list(point_set[i] & point_set[j])  # 能与 i,j 构成三角形的点
                for k in all_points_list:
                    # 由于 point_set 结构， 满足 i<j<k
                    sum_weight = weight[i] + weight[j] + weight[k]
                    triangle_info = [i, j, k, sum_weight]
                    # i,j,k 三个点 记录和更新三角形信息
                    for lm in [i, j, k]:
                        if not max_triangle_point_dict[lm] or max_triangle_point_dict[lm][-1] < sum_weight:
                            max_triangle_point_dict[lm] = triangle_info
                        triangle_point_dict[lm].append([i, j, k])
                    # 三个条边 记录和更新三角形信息
                    for edge in [(i, j), (i, k), (j, k)]:
                        triangle_edge_dict[edge] = get_top3(triangle_edge_dict[edge], triangle_info)

        res = 0
        for i in range(N):
            # 点无三角形的情况
            if not max_triangle_point_dict[i]:
                continue
            max_triange = max_triangle_point_dict[i]
            # 两个三角形完全重合的情况，即一个三角形
            res = max(res, max_triange[-1])

            # 最大三角形 max_triange 和所有包含 i 的三角形一一组合
            for info in triangle_point_dict[i]:
                res = max(res, count_val(max_triange, info))

            # 两个包含max_triangle边（i,x),(i,y) 的 Top3 三角形一一组合
            max_points = max_triange[:3]
            max_points.remove(i)
            edge1, edge2 = [(i, x) if i < x else (x, i) for x in max_points]
            for info1 in triangle_edge_dict[edge1]:
                for info2 in triangle_edge_dict[edge2]:
                    res = max(res, count_val(info1, info2))

        return res


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    [dict(edges=[[0, 1], [1, 2], [0, 2]], value=[1, 2, 3]), 6],

    pytest.param(dict(edges=[[0, 2], [2, 1]], value=[1, 2, 5]), 0),
    pytest.param(dict(edges=[[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [1, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5]],
                      value=[7, 8, 6, 8, 9, 7]), 39),
])
def test_solutions(kwargs, expected):
    assert Solution().maxWeight(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])

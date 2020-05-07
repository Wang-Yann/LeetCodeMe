#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给出方程式 A / B = k, 其中 A 和 B 均为代表字符串的变量， k 是一个浮点型数字。根据已知方程式求解问题，并返回计算结果。如果结果不存在，则
# 返回 -1.0。 
# 
#  示例 : 
# 给定 a / b = 2.0, b / c = 3.0 
# 问题: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
# 返回 [6.0, 0.5, -1.0, 1.0, -1.0 ] 
# 
#  输入为: vector<pair<string, string>> equations, vector<double>& values, vector<p
# air<string, string>> queries(方程式，方程式结果，问题方程式)， 其中 equations.size() == values.siz
# e()，即方程式的长度与方程式结果长度相等（程式与结果一一对应），并且结果值均为正数。以上为方程式的描述。 返回vector<double>类型。 
# 
#  基于上述例子，输入如下： 
# 
#  
# equations(方程式) = [ ["a", "b"], ["b", "c"] ],
# values(方程式结果) = [2.0, 3.0],
# queries(问题方程式) = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] 
# ]. 
#  
# 
#  输入总是有效的。你可以假设除法运算中不会出现除数为0的情况，且不存在任何矛盾的结果。 
#  Related Topics 并查集 图

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
    Graph
    先构造图，使用dict实现，其天然的hash可以在in判断时做到O(1)复杂度。
对每个equation如"a/b=v"构造a到b的带权v的有向边和b到a的带权1/v的有向边，
之后对每个query，只需要进行dfs并将路径上的边权重叠乘就是结果了，如果路径不可达则结果为-1

    """

    def calcEquation(self, equations: List[List[str]], values: List[float],
                     queries: List[List[str]]) -> List[float]:
        # 构造图
        graph = {}
        for (x, y), val in zip(equations, values):
            if x in graph:
                graph[x][y] = val
            else:
                graph[x] = {y: val}
            if y in graph:
                graph[y][x] = 1.0 / val
            else:
                graph[y] = {x: 1.0 / val}

        def dfs(s, t, visited):
            if s not in graph:
                return -1
            if t == s:
                return 1
            for node in graph[s].keys():
                if node == t:
                    return graph[s][node]
                elif node not in visited:
                    visited.add(node)
                    v = dfs(node, t, visited)
                    if v != -1:
                        return graph[s][node] * v
            return -1

        res = []
        for qs, qt in queries:
            res.append(dfs(qs, qt, set()))
        return res


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(equations=[["a", "b"], ["b", "c"]],
          values=[2.0, 3.0],
          queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]),
     [6.0, 0.5, -1.0, 1.0, -1.0]],
])
def test_solutions(kw, expected):
    assert Solution().calcEquation(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

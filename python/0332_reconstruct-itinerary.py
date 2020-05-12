#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个机票的字符串二维数组 [from, to]，子数组中的两个成员分别表示飞机出发和降落的机场地点，对该行程进行重新规划排序。所有这些机票都属于一个从J
# FK（肯尼迪国际机场）出发的先生，所以该行程必须从 JFK 出发。 
# 
#  说明: 
# 
#  
#  如果存在多种有效的行程，你可以按字符自然排序返回最小的行程组合。例如，行程 ["JFK", "LGA"] 与 ["JFK", "LGB"] 相比就更小，排
# 序更靠前 
#  所有的机场都用三个大写字母表示（机场代码）。 
#  假定所有机票至少存在一种合理的行程。 
#  
# 
#  示例 1: 
# 
#  输入: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# 输出: ["JFK", "MUC", "LHR", "SFO", "SJC"]
#  
# 
#  示例 2: 
# 
#  输入: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# 输出: ["JFK","ATL","JFK","SFO","ATL","SFO"]
# 解释: 另一种有效的行程是 ["JFK","SFO","ATL","JFK","ATL","SFO"]。但是它自然排序更大更靠后。 
#  Related Topics 深度优先搜索 图

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        欧拉通路
        TODO TODO
        """
        graph = collections.defaultdict(list)
        for f, t in tickets:
            graph[f].append([t, True])
        for k in graph.keys():
            graph[k].sort()
        ans = []

        def dfs(current, ticket_cnt):
            if ticket_cnt == 0:
                return True
            for i, (dest, valid) in enumerate(graph[current]):
                if valid:
                    graph[current][i][1] = False
                    ans.append(dest)
                    if dfs(dest, ticket_cnt - 1):
                        return ans
                    ans.pop()
                    graph[current][i][1] = True
            return False

        origin = "JFK"
        ans = [origin]
        dfs(origin, len(tickets))
        return ans

# leetcode submit region end(Prohibit modification and deletion)


class Solution1:
    """
    欧拉通路
    https://leetcode-cn.com/problems/reconstruct-itinerary/solution/332-zhong-xin-an-pai-xing-cheng-shen-sou-hui-su-by/
    首先先把图的邻接表存进字典，并且按字典序排序，然后从‘JFK’开始深搜，每前进一层就减去一条路径，直到某个起点不存在路径的时候就会跳出while循环进行回溯，相对先找不到路径的一定是放在相对后面，所以当前搜索的起点from会插在当前输出路径的第一个位置

    """

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        d = collections.defaultdict(list)  # 邻接表
        for f, t in tickets:
            d[f] += [t]  # 路径存进邻接表
        for f in d:
            d[f].sort()  # 邻接表排序
        ans = []

        def dfs(f):  # 深搜函数
            while d[f]:
                dfs(d[f].pop(0))  # 路径检索
            ans.insert(0, f)  # 放在最前

        dfs('JFK')
        return ans


@pytest.mark.parametrize("args,expected", [
    ([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]],
     ["JFK", "MUC", "LHR", "SFO", "SJC"]),
    ([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]],
     ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"])
])
def test_solutions(args, expected):
    assert Solution().findItinerary(args) == expected
    assert Solution1().findItinerary(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-07 23:19:13
# @Last Modified : 2020-07-07 23:19:13
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""

# 公司里有 n 名员工，每个员工的 ID 都是独一无二的，编号从 0 到 n - 1。公司的总负责人通过 headID 进行标识。 
# 
#  在 manager 数组中，每个员工都有一个直属负责人，其中 manager[i] 是第 i 名员工的直属负责人。对于总负责人，manager[headI
# D] = -1。题目保证从属关系可以用树结构显示。 
# 
#  公司总负责人想要向公司所有员工通告一条紧急消息。他将会首先通知他的直属下属们，然后由这些下属通知他们的下属，直到所有的员工都得知这条紧急消息。 
# 
#  第 i 名员工需要 informTime[i] 分钟来通知它的所有直属下属（也就是说在 informTime[i] 分钟后，他的所有直属下属都可以开始传播
# 这一消息）。 
# 
#  返回通知所有员工这一紧急消息所需要的 分钟数 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 1, headID = 0, manager = [-1], informTime = [0]
# 输出：0
# 解释：公司总负责人是该公司的唯一一名员工。
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
# 输出：1
# 解释：id = 2 的员工是公司的总负责人，也是其他所有员工的直属负责人，他需要 1 分钟来通知所有员工。
# 上图显示了公司员工的树结构。
#  
# 
#  示例 3： 
# 
#  
# 
#  输入：n = 7, headID = 6, manager = [1,2,3,4,5,6,-1], informTime = [0,6,5,4,3,2,1
# ]
# 输出：21
# 解释：总负责人 id = 6。他将在 1 分钟内通知 id = 5 的员工。
# id = 5 的员工将在 2 分钟内通知 id = 4 的员工。
# id = 4 的员工将在 3 分钟内通知 id = 3 的员工。
# id = 3 的员工将在 4 分钟内通知 id = 2 的员工。
# id = 2 的员工将在 5 分钟内通知 id = 1 的员工。
# id = 1 的员工将在 6 分钟内通知 id = 0 的员工。
# 所需时间 = 1 + 2 + 3 + 4 + 5 + 6 = 21 。
#  
# 
#  示例 4： 
# 
#  输入：n = 15, headID = 0, manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6], informTime
#  = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
# 输出：3
# 解释：第一分钟总负责人通知员工 1 和 2 。
# 第二分钟他们将会通知员工 3, 4, 5 和 6 。
# 第三分钟他们将会通知剩下的员工。
#  
# 
#  示例 5： 
# 
#  输入：n = 4, headID = 2, manager = [3,3,-1,2], informTime = [0,0,162,914]
# 输出：1076
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 10^5 
#  0 <= headID < n 
#  manager.length == n 
#  0 <= manager[i] < n 
#  manager[headID] == -1 
#  informTime.length == n 
#  0 <= informTime[i] <= 1000 
#  如果员工 i 没有下属，informTime[i] == 0 。 
#  题目 保证 所有员工都可以收到通知。 
#  
#  Related Topics 深度优先搜索 
#  👍 25 👎 0


"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        """
        有坑
        仔细想下为啥
        """
        graph = collections.defaultdict(list)
        for i, v in enumerate(manager):
            graph[v].append(i)
        dp = [0] * n
        dq = collections.deque([headID])
        seen = {headID}
        while dq:
            size = len(dq)
            for _ in range(size):
                node = dq.popleft()
                dp[node] += informTime[node]
                for son in graph[node]:
                    if son not in seen:
                        seen.add(son)
                        dq.append(son)
                        dp[son] += dp[node]
        # print(dp)
        return max(dp)


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        children = collections.defaultdict(list)
        for child, parent in enumerate(manager):
            if parent != -1:
                children[parent].append(child)

        result = 0
        stk = [(headID, 0)]
        while stk:
            node, curr = stk.pop()
            curr += informTime[node]
            result = max(result, curr)
            if node not in children:
                continue
            for c in children[node]:
                stk.append((c, curr))
        return result


@pytest.mark.parametrize("kwargs,expected", [
    (dict(n=1, headID=0, manager=[-1], informTime=[0]), 0),
    pytest.param(dict(n=6, headID=2, manager=[2, 2, -1, 2, 2, 2], informTime=[0, 0, 1, 0, 0, 0]), 1),
    pytest.param(dict(n=7, headID=6, manager=[1, 2, 3, 4, 5, 6, -1], informTime=[0, 6, 5, 4, 3, 2, 1]), 21),
    pytest.param(dict(n=15, headID=0, manager=[-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],
                      informTime=[1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]), 3),
    pytest.param(dict(n=4, headID=2, manager=[3, 3, -1, 2], informTime=[0, 0, 162, 914]), 1076),
    pytest.param(dict(n=11, headID=4, manager=[5, 9, 6, 10, -1, 8, 9, 1, 9, 3, 4],
                      informTime=[0, 213, 0, 253, 686, 170, 975, 0, 261, 309, 337]), 2560),
])
def test_solutions(kwargs, expected):
    assert Solution().numOfMinutes(**kwargs) == expected
    assert Solution1().numOfMinutes(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])

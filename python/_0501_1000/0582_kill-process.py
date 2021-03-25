#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-30 15:45:43
# @Last Modified : 2020-07-30 15:45:43
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给 n 个进程，每个进程都有一个独一无二的 PID （进程编号）和它的 PPID （父进程编号）。 
# 
#  每一个进程只有一个父进程，但是每个进程可能会有一个或者多个孩子进程。它们形成的关系就像一个树状结构。只有一个进程的 PPID 是 0 ，意味着这个进程没有
# 父进程。所有的 PID 都会是唯一的正整数。 
# 
#  我们用两个序列来表示这些进程，第一个序列包含所有进程的 PID ，第二个序列包含所有进程对应的 PPID。 
# 
#  现在给定这两个序列和一个 PID 表示你要杀死的进程，函数返回一个 PID 序列，表示因为杀这个进程而导致的所有被杀掉的进程的编号。 
# 
#  当一个进程被杀掉的时候，它所有的孩子进程和后代进程都要被杀掉。 
# 
#  你可以以任意顺序排列返回的 PID 序列。 
# 
#  示例 1: 
# 
#  输入: 
# pid =  [1, 3, 10, 5]
# ppid = [3, 0, 5, 3]
# kill = 5
# 输出: [5,10]
# 解释: 
#            3
#          /   \
#         1     5
#              /
#             10
# 杀掉进程 5 ，同时它的后代进程 10 也被杀掉。
#  
# 
#  
# 
#  注意: 
# 
#  
#  被杀掉的进程编号一定在 PID 序列中。 
#  n >= 1. 
#  
# 
#  
#  Related Topics 树 队列 
#  👍 30 👎 0

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        """AC"""
        ans = []
        G = collections.defaultdict(list)
        for p, pp in zip(pid, ppid):
            G[pp].append(p)
        dq = collections.deque([kill])
        while dq:
            node = dq.popleft()
            ans.append(node)
            for children in G[node]:
                dq.append(children)
        return ans


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(
        pid=[1, 3, 10, 5],
        ppid=[3, 0, 5, 3],
        kill=5
    ), [5, 10]],
])
def test_solutions(kw, expected):
    assert sorted(Solution().killProcess(**kw)) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

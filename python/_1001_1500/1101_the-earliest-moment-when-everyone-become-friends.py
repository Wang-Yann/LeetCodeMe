#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-04 16:27:31
# @Last Modified : 2020-08-04 16:27:31
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 在一个社交圈子当中，有 N 个人。每个人都有一个从 0 到 N-1 唯一的 id 编号。 
# 
#  我们有一份日志列表 logs，其中每条记录都包含一个非负整数的时间戳，以及分属两个人的不同 id，logs[i] = [timestamp, id_A, 
# id_B]。 
# 
#  每条日志标识出两个人成为好友的时间，友谊是相互的：如果 A 和 B 是好友，那么 B 和 A 也是好友。 
# 
#  如果 A 是 B 的好友，或者 A 是 B 的好友的好友，那么就可以认为 A 也与 B 熟识。 
# 
#  返回圈子里所有人之间都熟识的最早时间。如果找不到最早时间，就返回 -1 。 
# 
#  
# 
#  示例： 
# 
#  输入：logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190
# 224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], N = 6
# 输出：20190301
# 解释：
# 第一次结交发生在 timestamp = 20190101，0 和 1 成为好友，社交朋友圈如下 [0,1], [2], [3], [4], [5]。
# 第二次结交发生在 timestamp = 20190104，3 和 4 成为好友，社交朋友圈如下 [0,1], [2], [3,4], [5].
# 第三次结交发生在 timestamp = 20190107，2 和 3 成为好友，社交朋友圈如下 [0,1], [2,3,4], [5].
# 第四次结交发生在 timestamp = 20190211，1 和 5 成为好友，社交朋友圈如下 [0,1,5], [2,3,4].
# 第五次结交发生在 timestamp = 20190224，2 和 4 已经是好友了。
# 第六次结交发生在 timestamp = 20190301，0 和 3 成为好友，大家都互相熟识了。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= N <= 100 
#  1 <= logs.length <= 10^4 
#  0 <= logs[i][0] <= 10^9 
#  0 <= logs[i][1], logs[i][2] <= N - 1 
#  保证 logs[i][0] 中的所有时间戳都不同 
#  Logs 不一定按某一标准排序 
#  logs[i][1] != logs[i][2] 
#  
#  Related Topics 并查集 
#  👍 9 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class UnionFind(object):

    def __init__(self, n):
        self.set = list(range(n))
        self.size = n

    def find_set(self, x):
        if self.set[x] != x:
            self.set[x] = self.find_set(self.set[x])  # path compression.
        return self.set[x]

    def union_set(self, x, y):
        x_root, y_root = map(self.find_set, (x, y))
        if x_root == y_root:
            return False
        self.set[min(x_root, y_root)] = max(x_root, y_root)
        self.size -= 1
        return True


class Solution:
    def earliestAcq(self, logs: List[List[int]], N: int) -> int:
        logs.sort()
        uf = UnionFind(N)
        for ts, a, b in logs:
            uf.union_set(a, b)
            if uf.size == 1:
                return ts
        return -1


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(
        logs=[[20190101, 0, 1], [20190104, 3, 4], [20190107, 2, 3], [20190211, 1, 5], [20190224, 2, 4],
              [20190301, 0, 3], [20190312, 1, 2], [20190322, 4, 5]], N=6
    ), 20190301],
    [dict(
        logs=[[3, 0, 3], [4, 1, 2], [0, 2, 0], [2, 0, 2], [8, 0, 3], [1, 0, 1], [5, 1, 2], [7, 3, 1], [6, 1, 0],
              [9, 3, 0]], N=4
    ), 3],
])
def test_solutions(kw, expected):
    assert Solution().earliestAcq(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 写一个 RecentCounter 类来计算最近的请求。 
# 
#  它只有一个方法：ping(int t)，其中 t 代表以毫秒为单位的某个时间。 
# 
#  返回从 3000 毫秒前到现在的 ping 数。 
# 
#  任何处于 [t - 3000, t] 时间范围之内的 ping 都将会被计算在内，包括当前（指 t 时刻）的 ping。 
# 
#  保证每次对 ping 的调用都使用比之前更大的 t 值。 
# 
#  
# 
#  示例： 
# 
#  输入：inputs = ["RecentCounter","ping","ping","ping","ping"], inputs = [[],[1],[
# 100],[3001],[3002]]
# 输出：[null,1,2,3,3] 
# 
#  
# 
#  提示： 
# 
#  
#  每个测试用例最多调用 10000 次 ping。 
#  每个测试用例会使用严格递增的 t 值来调用 ping。 
#  每次调用 ping 都有 1 <= t <= 10^9。 
#  
# 
#  
#  Related Topics 队列

"""

import collections

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class RecentCounter:

    def __init__(self):
        self.q = collections.deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
# leetcode submit region end(Prohibit modification and deletion)

def test_solution():
    obj = RecentCounter()
    assert obj.ping(1) == 1
    assert obj.ping(100) == 2
    assert obj.ping(3001) == 3
    assert obj.ping(3002) == 3


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都
# 是O(1)。 
# 
#  若队列为空，pop_front 和 max_value 需要返回 -1 
# 
#  示例 1： 
# 
#  输入: 
# ["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
# [[],[1],[2],[],[],[]]
# 输出: [null,null,null,2,1,2]
#  
# 
#  示例 2： 
# 
#  输入: 
# ["MaxQueue","pop_front","max_value"]
# [[],[],[]]
# 输出: [null,-1,-1]
#  
# 
#  
# 
#  限制： 
# 
#  
#  1 <= push_back,pop_front,max_value的总操作数 <= 10000 
#  1 <= value <= 10^5 
#  
#  Related Topics 栈 Sliding Window

"""
import collections
import pytest


# leetcode submit region begin(Prohibit modification and deletion)
import queue

class MaxQueue:

    def __init__(self):
        self.dq = collections.deque()
        self.q = queue.Queue()

    def max_value(self) -> int:
        return self.dq[0] if self.dq else -1

    def push_back(self, value: int) -> None:
        while self.dq and self.dq[-1] < value:
            self.dq.pop()
        self.dq.append(value)
        self.q.put(value)

    def pop_front(self) -> int:
        if not self.dq:
            return -1
        ans = self.q.get()
        if ans == self.dq[0]:
            self.dq.popleft()
        return ans


# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
# leetcode submit region end(Prohibit modification and deletion)

def test_solutions():
    q = MaxQueue()
    q.push_back(1)
    assert q.max_value() == 1
    q.push_back(2)
    assert q.max_value() == 2
    assert q.pop_front() == 1
    assert q.max_value() == 2
    assert q.pop_front() == 2
    assert q.max_value() == -1


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

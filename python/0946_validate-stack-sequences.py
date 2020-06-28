#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给定 pushed 和 popped 两个序列，每个序列中的 值都不重复，只有当它们可能是在最初空栈上进行的推入 push 和弹出 pop 操作序列的结果时
# ，返回 true；否则，返回 false 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
# 输出：true
# 解释：我们可以按以下顺序执行：
# push(1), push(2), push(3), push(4), pop() -> 4,
# push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
#  
# 
#  示例 2： 
# 
#  输入：pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
# 输出：false
# 解释：1 不能在 2 之前弹出。
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= pushed.length == popped.length <= 1000 
#  0 <= pushed[i], popped[i] < 1000 
#  pushed 是 popped 的排列。 
#  
#  Related Topics 栈

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        for v in pushed:
            stack.append(v)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return i == len(popped)


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kwargs,expected", [
    (dict(pushed=[1, 2, 3, 4, 5], popped=[4, 5, 3, 2, 1]), True),
    pytest.param(dict(pushed=[1, 2, 3, 4, 5], popped=[4, 3, 5, 1, 2]), False),
])
def test_solutions(kwargs, expected):
    assert Solution().validateStackSequences(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

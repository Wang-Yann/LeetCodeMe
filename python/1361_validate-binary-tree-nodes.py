#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 二叉树上有 n 个节点，按从 0 到 n - 1 编号，其中节点 i 的两个子节点分别是 leftChild[i] 和 rightChild[i]。 
# 
#  只有 所有 节点能够形成且 只 形成 一颗 有效的二叉树时，返回 true；否则返回 false。 
# 
#  如果节点 i 没有左子节点，那么 leftChild[i] 就等于 -1。右子节点也符合该规则。 
# 
#  注意：节点没有值，本问题中仅仅使用节点编号。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
# 输出：false
#  
# 
#  示例 3： 
# 
#  
# 
#  输入：n = 2, leftChild = [1,0], rightChild = [-1,-1]
# 输出：false
#  
# 
#  示例 4： 
# 
#  
# 
#  输入：n = 6, leftChild = [1,-1,-1,4,-1,-1], rightChild = [2,-1,-1,5,-1,-1]
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 10^4 
#  leftChild.length == rightChild.length == n 
#  -1 <= leftChild[i], rightChild[i] <= n - 1 
#  
#  Related Topics 图

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        """要找到根节点　注意"""
        roots = set(range(n)) - set(leftChild) - set(rightChild)
        if len(roots) != 1:
            return False
        source = roots.pop()
        seen = set()
        dq = collections.deque([source])
        while dq:
            node = dq.popleft()
            if node in seen:
                return False
            seen.add(node)
            if leftChild[node] != -1:
                dq.append(leftChild[node])
            if rightChild[node] != -1:
                dq.append(rightChild[node])
        return len(seen) == n


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(n=4, leftChild=[1, -1, 3, -1], rightChild=[2, -1, -1, -1]), True],
    [dict(n=4, leftChild=[1, -1, 3, -1], rightChild=[2, 3, -1, -1]), False],
    [dict(n=2, leftChild=[1, 0], rightChild=[-1, -1]), False],
    [dict(n=6, leftChild=[1, -1, -1, 4, -1, -1], rightChild=[2, -1, -1, 5, -1, -1]), False],
    [dict(n=5, leftChild=[1, -1, 3, 4, -1], rightChild=[-1, 2, -1, -1, -1]), True],
    [dict(n=10, leftChild=[1, 6, 3, 5, -1, 7, -1, -1, -1, -1], rightChild=[2, -1, -1, 4, -1, 9, -1, 8, -1, -1]), True],
    [dict(n=2, leftChild=[-1, 0], rightChild=[-1, -1]), True],
])
def test_solutions(kw, expected):
    assert Solution().validateBinaryTreeNodes(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

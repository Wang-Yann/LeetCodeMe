#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-12 21:45:50
# @Last Modified : 2020-07-12 21:45:50
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 从左向右遍历一个数组，通过不断将其中的元素插入树中可以逐步地生成一棵二叉搜索树。给定一个由不同节点组成的二叉树，输出所有可能生成此树的数组。 
# 
#  示例: 
# 给定如下二叉树 
# 
#          2
#        / \
#       1   3
#  
# 
#  返回: 
# 
#  [
#    [2,1,3],
#    [2,3,1]
# ]
#  
#  Related Topics 树 动态规划 
#  👍 25 👎 0


"""

from typing import List

import pytest

from common_utils import TreeNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def BSTSequences(self, root: TreeNode) -> List[List[int]]:
        """
        使用一个queue存储下个所有可能的节点
        然后选择其中一个作为path的下一个元素
        递归直到queue元素为空
        将对应的path加入结果中
        由于二叉搜索树没有重复元素, 而且每次递归的使用元素的顺序都不一样, 所以自动做到了去重

        """
        if not root:
            return [[]]
        res = []
        def dfs(cur, q, path):
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
            if not q:
                res.append(path)
                return
            for i, nex in enumerate(q):
                newq = q[:i] + q[i + 1:]
                dfs(nex, newq, path + [nex.val])
        dfs(root, [], [root.val])
        return res


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    [dict(        root=TreeNode(2,TreeNode(1),TreeNode(3))                        ),
      [
        [2,1,3],
        [2,3,1]
     ]
     ],

])
def test_solutions(kwargs, expected):
    assert Solution().BSTSequences(**kwargs) == expected






if __name__ == '__main__':
    pytest.main(["-q", "--color=yes","--capture=tee-sys", __file__])


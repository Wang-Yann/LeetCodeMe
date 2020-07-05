#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-05 16:02:45
# @Last Modified : 2020-07-05 16:02:45
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给出一个满足下述规则的二叉树： 
# 
#  
#  root.val == 0 
#  如果 treeNode.val == x 且 treeNode.left != null，那么 treeNode.left.val == 2 * x + 
# 1 
#  如果 treeNode.val == x 且 treeNode.right != null，那么 treeNode.right.val == 2 * x 
# + 2 
#  
# 
#  现在这个二叉树受到「污染」，所有的 treeNode.val 都变成了 -1。 
# 
#  请你先还原二叉树，然后实现 FindElements 类： 
# 
#  
#  FindElements(TreeNode* root) 用受污染的二叉树初始化对象，你需要先把它还原。 
#  bool find(int target) 判断目标值 target 是否存在于还原后的二叉树中并返回结果。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：
# ["FindElements","find","find"]
# [[[-1,null,-1]],[1],[2]]
# 输出：
# [null,false,true]
# 解释：
# FindElements findElements = new FindElements([-1,null,-1]); 
# findElements.find(1); // return False 
# findElements.find(2); // return True 
# 
#  示例 2： 
# 
#  
# 
#  输入：
# ["FindElements","find","find","find"]
# [[[-1,-1,-1,-1,-1]],[1],[3],[5]]
# 输出：
# [null,true,true,false]
# 解释：
# FindElements findElements = new FindElements([-1,-1,-1,-1,-1]);
# findElements.find(1); // return True
# findElements.find(3); // return True
# findElements.find(5); // return False 
# 
#  示例 3： 
# 
#  
# 
#  输入：
# ["FindElements","find","find","find","find"]
# [[[-1,null,-1,-1,null,-1]],[2],[3],[4],[5]]
# 输出：
# [null,true,false,false,true]
# 解释：
# FindElements findElements = new FindElements([-1,null,-1,-1,null,-1]);
# findElements.find(2); // return True
# findElements.find(3); // return False
# findElements.find(4); // return False
# findElements.find(5); // return True
#  
# 
#  
# 
#  提示： 
# 
#  
#  TreeNode.val == -1 
#  二叉树的高度不超过 20 
#  节点的总数在 [1, 10^4] 之间 
#  调用 find() 的总次数在 [1, 10^4] 之间 
#  0 <= target <= 10^6 
#  
#  Related Topics 树 哈希表 
#  👍 12 👎 0

"""

import pytest

from common_utils import TreeNode


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class FindElements:

    def __init__(self, root: TreeNode):
        self.lookup = set()

        def dfs(node, v):
            if not node:
                return
            node.val = v
            self.lookup.add(v)
            dfs(node.left, 2 * v + 1)
            dfs(node.right, 2 * v + 2)

        dfs(root, 0)

    def find(self, target: int) -> bool:
        return target in self.lookup


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
# leetcode submit region end(Prohibit modification and deletion)

def test_solution1():
    root = TreeNode(-1, right=TreeNode(-1))
    findElements = FindElements(root)
    assert not findElements.find(1)
    assert findElements.find(2)


def test_solution2():
    root = TreeNode(-1, left=TreeNode(-1, TreeNode(-1), TreeNode(-1)), right=TreeNode(-1))
    findElements = FindElements(root)
    assert findElements.find(1)
    assert findElements.find(3)
    assert not findElements.find(5);


def test_solution3():
    root = TreeNode(-1, right=TreeNode(-1, left=TreeNode(-1, left=TreeNode(-1))))
    findElements = FindElements(root)
    assert findElements.find(2)
    assert not findElements.find(3)
    assert not findElements.find(4);
    assert findElements.find(5)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])

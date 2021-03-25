#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 我们从二叉树的根节点 root 开始进行深度优先搜索。 
# 
#  在遍历中的每个节点处，我们输出 D 条短划线（其中 D 是该节点的深度），然后输出该节点的值。（如果节点的深度为 D，则其直接子节点的深度为 D + 1。
# 根节点的深度为 0）。 
# 
#  如果节点只有一个子节点，那么保证该子节点为左子节点。 
# 
#  给出遍历输出 S，还原树并返回其根节点 root。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入："1-2--3--4-5--6--7"
# 输出：[1,2,5,3,4,6,7]
#  
# 
#  示例 2： 
# 
#  
# 
#  输入："1-2--3---4-5--6---7"
# 输出：[1,2,5,3,null,6,null,4,null,7]
#  
# 
#  示例 3： 
# 
#  
# 
#  输入："1-401--349---90--88"
# 输出：[1,401,null,349,88,90]
#  
# 
#  
# 
#  提示： 
# 
#  
#  原始树中的节点数介于 1 和 1000 之间。 
#  每个节点的值介于 1 和 10 ^ 9 之间。 
#  
#  Related Topics 树 深度优先搜索

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


class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        """ 
        如果 T 是 S 的左子节点，那么 T 的深度恰好比 S 的深度大 11；在其它的情况下，T 是栈中某个节点（不包括 S）的右子节点，
        那么我们将栈顶的节点不断地出栈，直到 T 的深度恰好比栈顶节点的深度大 11，此时我们就找到了 T 的双亲节点
        """
        N = len(S)
        path, i = [], 0
        while i < N:
            level = 0
            while i < N and S[i] == "-":
                level += 1
                i += 1
            value = 0
            while i < N and S[i].isdigit():
                value = value * 10 + (ord(S[i]) - ord("0"))
                i += 1
            node = TreeNode(value)
            if level == len(path):
                if path:
                    path[-1].left = node
            else:
                path = path[:level]
                path[-1].right = node
            path.append(node)
            # print(path)
        return path[0]


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        ans = {-1: TreeNode(0)}  # 字典初始化

        def addTree(v, p):  # 添加树函数
            ans[p] = TreeNode(int(v))
            if not ans[p - 1].left:  # 左子树不存在就加在左边
                ans[p - 1].left = ans[p]
            else:  # 反之加在右边
                ans[p - 1].right = ans[p]

        val, dep = '', 0  # 值和对应深度初始化
        for c in S:
            if c != '-':
                val += c  # 累加字符来获得数字
            elif val:  # 如果是‘-’且存在val
                addTree(val, dep)  # 就把累加好的数字和对应深度添加进树
                val, dep = '', 1  # 值和对应深度重新初始化
            else:
                dep += 1  # 连续的‘-’只加深度不加值
        addTree(val, dep)  # 末尾剩余的数字也要加进树
        return ans[0]


@pytest.mark.parametrize("args,expected", [
    ("1-2--3--4-5--6--7", TreeNode(1,
                                   left=TreeNode(2, TreeNode(3), TreeNode(4)),
                                   right=TreeNode(5, TreeNode(6), TreeNode(7)))
     ),
    ("1-2--3---4-5--6---7", TreeNode(1,
                                     left=TreeNode(2, left=TreeNode(3, left=TreeNode(4))),
                                     right=TreeNode(5, left=TreeNode(6, left=TreeNode(7))))
     ),
    ("1-401--349---90--88", TreeNode(1, left=(
            TreeNode(401,
                     left=TreeNode(349,
                                   left=TreeNode(90)),
                     right=TreeNode(88)
                     )))
     ),
])
def test_solutions(args, expected):
    assert repr(Solution().recoverFromPreorder(args)) == repr(expected)
    assert repr(Solution1().recoverFromPreorder(args)) == repr(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

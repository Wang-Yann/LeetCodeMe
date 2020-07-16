#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-16 10:38:23
# @Last Modified : 2020-07-16 10:38:23
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 任务调度优化是计算机性能优化的关键任务之一。在任务众多时，不同的调度策略可能会得到不同的总体执行时间，因此寻求一个最优的调度方案是非常有必要的。 
# 
#  通常任务之间是存在依赖关系的，即对于某个任务，你需要先完成他的前导任务（如果非空），才能开始执行该任务。我们保证任务的依赖关系是一棵二叉树，其中 root
#  为根任务，root.left 和 root.right 为他的两个前导任务（可能为空），root.val 为其自身的执行时间。 
# 
#  在一个 CPU 核执行某个任务时，我们可以在任何时刻暂停当前任务的执行，并保留当前执行进度。在下次继续执行该任务时，会从之前停留的进度开始继续执行。暂停的
# 时间可以不是整数。 
# 
#  现在，系统有两个 CPU 核，即我们可以同时执行两个任务，但是同一个任务不能同时在两个核上执行。给定这颗任务树，请求出所有任务执行完毕的最小时间。 
# 
#  示例 1： 
# 
#  
#  
# 
#  输入：root = [47, 74, 31] 
# 
#  输出：121 
# 
#  解释：根节点的左右节点可以并行执行31分钟，剩下的43+47分钟只能串行执行，因此总体执行时间是121分钟。 
#  
# 
#  示例 2： 
# 
#  
#  
# 
#  输入：root = [15, 21, null, 24, null, 27, 26] 
# 
#  输出：87 
#  
# 
#  示例 3： 
# 
#  
#  
# 
#  输入：root = [1,3,2,null,null,4,4] 
# 
#  输出：7.5 
#  
# 
#  限制： 
# 
#  
#  1 <= 节点数量 <= 1000 
#  1 <= 单节点执行时间 <= 1000 
#  
#  👍 22 👎 0

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
    def minimalExecTime(self, root: TreeNode) -> float:
        """

        链接：https://leetcode-cn.com/problems/er-cha-shu-ren-wu-diao-du/solution/pythonshu-xing-dptu-jie-guan-jian-guo-cheng-by-dij/
        """

        def dfs(rt):
            """
            返回结果：
            (该结点及子树的最短运行时间, 该结点及子树的最大运行时间)
            """

            if not rt:
                return 0, 0
            l = dfs(rt.left)
            r = dfs(rt.right)
            return max(l[0], r[0], (l[1] + r[1]) / 2) + rt.val, l[1] + r[1] + rt.val

        return dfs(root)[0]


# leetcode submit region end(Prohibit modification and deletion)


class Solution1(object):
    def minimalExecTime(self, root):
        

        def dfs(root):
            if root is None:
                return 0., 0.
            tc = root.val

            # 先递归左右子树
            a, b = dfs(root.left)
            c, d = dfs(root.right)

            tc = tc + a + c
            # 只考虑 a >= c 的情况，不满足就交换
            if a < c:
                a, c = c, a
                b, d = d, b

            if a - 2 * b <= c:
                pc = (a + c) / 2
            else:
                pc = c + b

            return tc, pc

        tc, pc = dfs(root)
        return tc - pc


@pytest.mark.parametrize("args,expected", [
    (TreeNode(47, TreeNode(74), TreeNode(31)), 121),
    (TreeNode(15, left=TreeNode(21, left=TreeNode(24, TreeNode(27), TreeNode(26)))), 87),
    (TreeNode(1, left=TreeNode(3), right=TreeNode(2, TreeNode(4), TreeNode(4))), 7.5),
    (TreeNode(47, TreeNode(74), TreeNode(31)), 121),
])
def test_solutions(args, expected):
    res = Solution().minimalExecTime(args)
    res1 = Solution().minimalExecTime(args)
    assert res == pytest.approx(expected, 1e-5)
    assert res1 == pytest.approx(expected, 1e-5)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-08 18:16:05
# @Last Modified : 2020-08-08 18:16:05
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""

Given a root of an N-ary tree, you need to compute the length of the diameter of the tree.

The diameter of an N-ary tree is the length of the longest path between any two nodes in the tree. This path may or may not pass through the root.

(Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value.)

 

Example 1:



Input: root = [1,null,3,2,4,null,5,6]
Output: 3
Explanation: Diameter is shown in red color.
Example 2:



Input: root = [1,null,2,null,3,4,null,5,null,6]
Output: 4
Example 3:



Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: 7
 

Constraints:

The depth of the n-ary tree is less than or equal to 1000.
The total number of nodes is between [0, 10^4].
通过次数42提交次数55

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/diameter-of-n-ary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

#  👍 0 👎 0
	 

"""

import pytest

from common_utils import TreeNodeWithChildren as Node

# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""


class Solution:

    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """

        def dfs(node):
            max_dia = max_depth = 0
            for child in node.children:
                child_max_dia, child_max_depth = dfs(child)
                max_dia = max(max_dia, child_max_dia, max_depth + child_max_depth + 1)
                max_depth = max(max_depth, child_max_depth + 1)
            return max_dia, max_depth

        return dfs(root)[0]


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kwargs,expected", [
    [dict(
        root=Node(1, children=[Node(3, children=[Node(5), Node(6)]), Node(2), Node(4)])
    ), 3],

])
def test_solutions(kwargs, expected):
    assert Solution().diameter(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])

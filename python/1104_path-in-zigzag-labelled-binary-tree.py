#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 在一棵无限的二叉树上，每个节点都有两个子节点，树中的节点 逐行 依次按 “之” 字形进行标记。 
# 
#  如下图所示，在奇数行（即，第一行、第三行、第五行……）中，按从左到右的顺序进行标记； 
# 
#  而偶数行（即，第二行、第四行、第六行……）中，按从右到左的顺序进行标记。 
# 
#  
# 
#  给你树上某一个节点的标号 label，请你返回从根节点到该标号为 label 节点的路径，该路径是由途经的节点标号所组成的。 
# 
#  
# 
#  示例 1： 
# 
#  输入：label = 14
# 输出：[1,3,4,14]
#  
# 
#  示例 2： 
# 
#  输入：label = 26
# 输出：[1,2,6,10,26]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= label <= 10^6 
#  
#  Related Topics 树 数学

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        """
        数学
        https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/discuss/324011/Python-O(logn)-time-and-space-with-readable-code-and-step-by-step-explanation
        """
        res = []  # O(log n) space
        node_count = 1
        level = 1
        # Determine level of the label
        while label >= node_count * 2:  # O(log n) time
            node_count *= 2
            level += 1
        # Iterate from the target label to the root
        while label != 0:  # O(log n) time
            res.append(label)
            level_max = 2 ** level - 1
            level_min = 2 ** (level - 1)
            label = int((level_max + level_min - label) / 2)
            level -= 1
        return res[::-1]  # O(n) time


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    (14, [1, 3, 4, 14]),
    (26, [1, 2, 6, 10, 26]),
])
def test_solutions(args, expected):
    assert Solution().pathInZigZagTree(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

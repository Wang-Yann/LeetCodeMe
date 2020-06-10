#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一个字母只会出现在其中的一个片段。返回一个表示每个字符串片段的长度的列表。 
# 
#  
# 
#  示例 1： 
# 
#  输入：S = "ababcbacadefegdehijhklij"
# 输出：[9,7,8]
# 解释：
# 划分结果为 "ababcbaca", "defegde", "hijhklij"。
# 每个字母最多出现在一个片段中。
# 像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。
#  
# 
#  
# 
#  提示： 
# 
#  
#  S的长度在[1, 500]之间。 
#  S只包含小写字母 'a' 到 'z' 。 
#  
#  Related Topics 贪心算法 双指针

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        """ 
        贪心
        对于遇到的每一个字母，去找这个字母最后一次出现的位置，用来更新当前的最小区间。
        贪心算法巧妙
        """
        lookup = {c: i for i, c in enumerate(S)}
        first = last = 0
        res = []
        for i, c in enumerate(S):
            last = max(last, lookup[c])
            if i == last:
                res.append(i - first + 1)
                first = i + 1
        return res


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ("ababcbacadefegdehijhklij", [9, 7, 8])
])
def test_solutions(args, expected):
    assert Solution().partitionLabels(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

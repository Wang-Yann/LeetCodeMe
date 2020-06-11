#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 字符串S和 T 只包含小写字符。在S中，所有字符只会出现一次。 
# 
#  S 已经根据某种规则进行了排序。我们要根据S中的字符顺序对T进行排序。更具体地说，如果S中x在y之前出现，那么返回的字符串中x也应出现在y之前。 
# 
#  返回任意一种符合条件的字符串T。 
# 
#  
# 示例:
# 输入:
# S = "cba"
# T = "abcd"
# 输出: "cbad"
# 解释: 
# S中出现了字符 "a", "b", "c", 所以 "a", "b", "c" 的顺序应该是 "c", "b", "a". 
# 由于 "d" 没有在S中出现, 它可以放在T的任意位置. "dcba", "cdba", "cbda" 都是合法的输出。
#  
# 
#  注意: 
# 
#  
#  S的最大长度为26，其中没有重复的字符。 
#  T的最大长度为200。 
#  S和T只包含小写字符。 
#  
#  Related Topics 字符串

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def customSortString(self, S: str, T: str) -> str:
        lookup = {char:i for i, char in enumerate(S)}
        l = sorted(T, key=lambda x: lookup.get(x,0))
        return "".join(l)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    (dict(S="cba", T="abcd"), ["cbad","dcba", "cdba", "cbda" ]),
])
def test_solutions(kwargs, expected):
    assert Solution().customSortString(**kwargs) in expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-11 23:22:56
# @Last Modified : 2020-07-11 23:22:56
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 实现一个算法，确定一个字符串 s 的所有字符是否全都不同。 
# 
#  示例 1： 
# 
#  输入: s = "leetcode"
# 输出: false 
#  
# 
#  示例 2： 
# 
#  输入: s = "abc"
# 输出: true
#  
# 
#  限制： 
#  
#  0 <= len(s) <= 100 
#  如果你不使用额外的数据结构，会很加分。 
#  
#  Related Topics 数组 
#  👍 41 👎 0


"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def isUnique(self, astr: str) -> bool:
        mark = 0
        for char in astr:
            move_bit = ord(char) - ord('a')
            if mark & (1 << move_bit):
                return False
            else:
                mark |= (1 << move_bit)
        return True


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:

    def isUnique(self, astr: str) -> bool:
        return len(set(astr)) == len(astr)


@pytest.mark.parametrize("kwargs,expected", [
    [dict(astr="leetcode"), False],

    pytest.param(dict(astr="abc"), True),
])
def test_solutions(kwargs, expected):
    assert Solution().isUnique(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])

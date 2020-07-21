#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-21 18:36:57
# @Last Modified : 2020-07-21 18:36:57
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 中心对称数是指一个数字在旋转了 180 度之后看起来依旧相同的数字（或者上下颠倒地看）。 
# 
#  请写一个函数来判断该数字是否是中心对称数，其输入将会以一个字符串的形式来表达数字。 
# 
#  
# 
#  示例 1: 
# 
#  输入: num = "69"
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入: num = "88"
# 输出: true 
# 
#  示例 3: 
# 
#  输入: num = "962"
# 输出: false 
# 
#  示例 4： 
# 
#  输入：num = "1"
# 输出：true
#  
#  Related Topics 哈希表 数学 
#  👍 14 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        """没意思"""
        lookup = {
            "6": "9",
            "9": "6",
            "1": "1",
            "8": "8",
            "0": "0"
        }
        l, r = 0, len(num) - 1
        while l <= r:
            if lookup.get(num[l]) == num[r]:
                l += 1
                r -= 1
            else:
                return False
        return True


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(num="69"), True],
    [dict(num="88"), True],
    [dict(num="962"), False],
    [dict(num="1"), True],
    [dict(num="101"), True],
    [dict(num="2"), False],
])
def test_solutions(kw, expected):
    assert Solution().isStrobogrammatic(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

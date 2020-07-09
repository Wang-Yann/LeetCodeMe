#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-09 23:47:55
# @Last Modified : 2020-07-09 23:47:55
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""

# 给你一个字符串 s ，字符串的「能量」定义为：只包含一种字符的最长非空子字符串的长度。 
# 
#  请你返回字符串的能量。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "leetcode"
# 输出：2
# 解释：子字符串 "ee" 长度为 2 ，只包含字符 'e' 。
#  
# 
#  示例 2： 
# 
#  输入：s = "abbcccddddeeeeedcba"
# 输出：5
# 解释：子字符串 "eeeee" 长度为 5 ，只包含字符 'e' 。
#  
# 
#  示例 3： 
# 
#  输入：s = "triplepillooooow"
# 输出：5
#  
# 
#  示例 4： 
# 
#  输入：s = "hooraaaaaaaaaaay"
# 输出：11
#  
# 
#  示例 5： 
# 
#  输入：s = "tourist"
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 500 
#  s 只包含小写英文字母。 
#  
#  Related Topics 字符串 
#  👍 2 👎 0


"""

import itertools

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def maxPower(self, s: str) -> int:
        ans = 0
        for char, grp in itertools.groupby(s):
            ans = max(len(tuple(grp)), ans)
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    [dict(s="leetcode"), 2],

    pytest.param(dict(s="abbcccddddeeeeedcba"), 5),
    pytest.param(dict(s="triplepillooooow"), 5),
    pytest.param(dict(s="hooraaaaaaaaaaay"), 11),
    pytest.param(dict(s="tourist"), 1),
])
def test_solutions(kwargs, expected):
    assert Solution().maxPower(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])

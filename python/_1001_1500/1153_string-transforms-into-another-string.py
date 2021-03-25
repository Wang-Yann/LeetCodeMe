#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-05 10:32:44
# @Last Modified : 2020-08-05 10:32:44
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给出两个长度相同的字符串，分别是 str1 和 str2。请你帮忙判断字符串 str1 能不能在 零次 或 多次 转化后变成字符串 str2。 
# 
#  每一次转化时，将会一次性将 str1 中出现的 所有 相同字母变成其他 任何 小写英文字母（见示例）。 
# 
#  只有在字符串 str1 能够通过上述方式顺利转化为字符串 str2 时才能返回 True，否则返回 False。 
# 
#  
# 
#  示例 1： 
# 
#  输入：str1 = "aabcc", str2 = "ccdee"
# 输出：true
# 解释：将 'c' 变成 'e'，然后把 'b' 变成 'd'，接着再把 'a' 变成 'c'。注意，转化的顺序也很重要。
#  
# 
#  示例 2： 
# 
#  输入：str1 = "leetcode", str2 = "codeleet"
# 输出：false
# 解释：我们没有办法能够把 str1 转化为 str2。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= str1.length == str2.length <= 10^4 
#  str1 和 str2 中都只会出现 小写英文字母 
#  
#  Related Topics 图 
#  👍 24 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        """
        GOOD
        因为一共只有 26 个字符，如果 str2 中存在 26 个不同的字符，那么将无法进行转换。
        我们可以通过哈希表的方式，保存 str2 中出现的每一个字符。如果小于 26，那么就可以转换
        """
        if str1 == str2:
            return True
        lookup = {}
        for a, b in zip(str1, str2):
            if lookup.setdefault(a, b) != b:
                return False

        return len(set(str2)) < 26


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(str1="aabcc", str2="ccdee"), True],
    [dict(str1="leetcode", str2="codeleet"), False],
    [dict(str1="abcdefghijklmnopqrstuvwxyz", str2="bcdefghijklmnopqrstuvwxyza"), False],
    [dict(str1="ab", str2="ba"), True],
])
def test_solutions(kw, expected):
    assert Solution().canConvert(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

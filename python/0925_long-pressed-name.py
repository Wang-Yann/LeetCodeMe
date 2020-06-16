#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 你的朋友正在使用键盘输入他的名字 name。偶尔，在键入字符 c 时，按键可能会被长按，而字符可能被输入 1 次或多次。 
# 
#  你将会检查键盘输入的字符 typed。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回 True。 
# 
#  
# 
#  示例 1： 
# 
#  输入：name = "alex", typed = "aaleex"
# 输出：true
# 解释：'alex' 中的 'a' 和 'e' 被长按。
#  
# 
#  示例 2： 
# 
#  输入：name = "saeed", typed = "ssaaedd"
# 输出：false
# 解释：'e' 一定需要被键入两次，但在 typed 的输出中不是这样。
#  
# 
#  示例 3： 
# 
#  输入：name = "leelee", typed = "lleeelee"
# 输出：true
#  
# 
#  示例 4： 
# 
#  输入：name = "laiden", typed = "laiden"
# 输出：true
# 解释：长按名字中的字符并不是必要的。
#  
# 
#  
# 
#  提示： 
# 
#  
#  name.length <= 1000 
#  typed.length <= 1000 
#  name 和 typed 的字符都是小写字母。 
#  
# 
#  
# 
#  
#  Related Topics 双指针 字符串

"""
import itertools

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        for j in range(len(typed)):
            if i < len(name) and name[i] == typed[j]:
                i += 1
            elif j == 0 or typed[j] != typed[j - 1]:
                return False
        return i == len(name)


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        l1 = l2 = 0
        len_name, len_typed = len(name), len(typed)
        while l1 < len_name and l2 < len_typed:
            l1_char, l2_char = name[l1], typed[l2]
            if l1_char != l2_char:
                return False
            while l1 < len_name and l2 < len_typed and name[l1] == typed[l2] == l1_char:
                l1 += 1
                l2 += 1
            while l2 < len_typed and typed[l2] == l1_char:
                l2 += 1
            # print(l1,l2,name[l1],typed[l2])
        while l2 < len_typed and typed[l2] == name[l1 - 1]:
            l2 += 1

        return l1 == len_name and l2 == len_typed


class Solution2:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        g1 = [(k, len(list(grp))) for k, grp in itertools.groupby(name)]
        g2 = [(k, len(list(grp))) for k, grp in itertools.groupby(typed)]
        if len(g1) != len(g2):
            return False

        return all(k1 == k2 and v1 <= v2 for (k1, v1), (k2, v2) in zip(g1, g2))


@pytest.mark.parametrize("kw,expected", [
    [dict(name="alex", typed="aaleex"), True],
    [dict(name="saeed", typed="ssaaedd"), False],
    [dict(name="leelee", typed="lleeelee"), True],
    [dict(name="laiden", typed="laiden"), True],
])
def test_solutions(kw, expected):
    assert Solution().isLongPressedName(**kw) == expected
    assert Solution1().isLongPressedName(**kw) == expected
    assert Solution2().isLongPressedName(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

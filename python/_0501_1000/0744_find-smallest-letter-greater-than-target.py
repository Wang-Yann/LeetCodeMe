#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-05-02 14:50:37
# @Last Modified : 2020-05-02 14:50:37
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给你一个排序后的字符列表 letters ，列表中只包含小写英文字母。另给出一个目标字母 target，请你寻找在这一有序列表里比目标字母大的最小字母。
#
#  在比较时，字母是依序循环出现的。举个例子：
#
#
#  如果目标字母 target = 'z' 并且字符列表为 letters = ['a', 'b']，则答案返回 'a'
#
#
#
#
#  示例：
#
#  输入:
# letters = ["c", "f", "j"]
# target = "a"
# 输出: "c"
#
# 输入:
# letters = ["c", "f", "j"]
# target = "c"
# 输出: "f"
#
# 输入:
# letters = ["c", "f", "j"]
# target = "d"
# 输出: "f"
#
# 输入:
# letters = ["c", "f", "j"]
# target = "g"
# 输出: "j"
#
# 输入:
# letters = ["c", "f", "j"]
# target = "j"
# 输出: "c"
#
# 输入:
# letters = ["c", "f", "j"]
# target = "k"
# 输出: "c"
#
#
#
#
#  提示：
#
#
#  letters长度范围在[2, 10000]区间内。
#  letters 仅由小写字母组成，最少包含两个不同的字母。
#  目标字母target 是一个小写字母。
#
#  Related Topics 二分查找
#  👍 80 👎 0

"""
import bisect
from typing import List

import pytest


class Solution:

    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        length = len(letters)
        l,r =0,length-1
        while l<=r:
            mid = (l+r)>>1
            if letters[mid]>target:
                r=mid-1
            else:
                l=mid+1
        # print(l,letters)
        return letters[l%length]



class Solution1:

    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        idx = bisect.bisect_right(letters,target)
        return letters[0] if idx==len(letters) else letters[idx]


@pytest.mark.parametrize("letters", [
    (["c", "f", "j"])
])
@pytest.mark.parametrize("target,expected", [
    ("a", "c"),
    ("c", "f"),
    ("d", "f"),
    ("g", "j"),
    ("j", "c"),
    ("k", "c")
])
def test_solutions(letters, target, expected):
    assert Solution().nextGreatestLetter(letters, target, ) == expected
    assert Solution1().nextGreatestLetter(letters, target, ) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 在一个由小写字母构成的字符串 S 中，包含由一些连续的相同字符所构成的分组。 
# 
#  例如，在字符串 S = "abbxxxxzyy" 中，就含有 "a", "bb", "xxxx", "z" 和 "yy" 这样的一些分组。 
# 
#  我们称所有包含大于或等于三个连续字符的分组为较大分组。找到每一个较大分组的起始和终止位置。 
# 
#  最终结果按照字典顺序输出。 
# 
#  示例 1: 
# 
#  
# 输入: "abbxxxxzzy"
# 输出: [[3,6]]
# 解释: "xxxx" 是一个起始于 3 且终止于 6 的较大分组。
#  
# 
#  示例 2: 
# 
#  
# 输入: "abc"
# 输出: []
# 解释: "a","b" 和 "c" 均不是符合要求的较大分组。
#  
# 
#  示例 3: 
# 
#  
# 输入: "abcdddeeeeaabbbcd"
# 输出: [[3,5],[6,9],[12,14]] 
# 
#  说明: 1 <= S.length <= 1000 
#  Related Topics 数组

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def largeGroupPositions(self, S: str) -> List[List[int]]:
        ans = []
        i = 0
        for j in range(len(S)):
            if j == len(S) - 1 or S[j] != S[j + 1]:
                if j - i + 1 >= 3:
                    ans.append([i, j])
                i = j + 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:

    def largeGroupPositions(self, S: str) -> List[List[int]]:
        if len(S) < 3:
            return []
        ans = []
        S += "$"
        start, cur_char, cnt = 0, S[0], 0
        for idx, char in enumerate(S):
            if char == cur_char:
                cnt += 1
            else:
                if cnt >= 3:
                    ans.append([start, idx - 1])
                start = idx
                cur_char = char
                cnt = 1
        return ans


@pytest.mark.parametrize("args,expected", [
    ("aaa", [[0, 2]]),
    ("abbxxxxzzy", [[3, 6]]),
    ("abcdddeeeeaabbbcd", [[3, 5], [6, 9], [12, 14]]),
    pytest.param("abc", []),
])
def test_solutions(args, expected):
    assert Solution().largeGroupPositions(args) == expected
    assert Solution1().largeGroupPositions(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-26 22:19:58
# @Last Modified : 2020-04-26 22:19:58
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。
#
#  注意：如果对空文本输入退格字符，文本继续为空。
#
#
#
#  示例 1：
#
#  输入：S = "ab#c", T = "ad#c"
# 输出：true
# 解释：S 和 T 都会变成 “ac”。
#
#
#  示例 2：
#
#  输入：S = "ab##", T = "c#d#"
# 输出：true
# 解释：S 和 T 都会变成 “”。
#
#
#  示例 3：
#
#  输入：S = "a##c", T = "#a#c"
# 输出：true
# 解释：S 和 T 都会变成 “c”。
#
#
#  示例 4：
#
#  输入：S = "a#c", T = "b"
# 输出：false
# 解释：S 会变成 “c”，但 T 仍然是 “b”。
#
#
#
#  提示：
#
#
#  1 <= S.length <= 200
#  1 <= T.length <= 200
#  S 和 T 只含有小写字母以及字符 '#'。
#
#
#
#
#  进阶：
#
#
#  你可以用 O(N) 的时间复杂度和 O(1) 的空间复杂度解决该问题吗？
#
#
#
#  Related Topics 栈 双指针
#  👍 135 👎 0

"""

import itertools

import pytest


class Solution0:

    def backspaceCompare(self, S: str, T: str) -> bool:
        def helper(s):
            stack = []
            for char in s:
                if char != "#":
                    stack.append(char)
                else:
                    if stack:
                        stack.pop()
            return stack

        s_lst = helper(S)
        t_lst = helper(T)
        # print(s_lst,t_lst)
        return s_lst == t_lst


class Solution:

    def backspaceCompare(self, S: str, T: str) -> bool:
        def helper_generator(s):
            skip = 0
            length = len(s)
            for i in range(length - 1, -1, -1):
                if s[i] == "#":
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield s[i]

        for x, y in itertools.zip_longest(helper_generator(S), helper_generator(T)):
            if x != y:
                return False
        return True


@pytest.mark.parametrize("kw,expected", [
    [dict(S="ab#c", T="ad#c"), True],
    [dict(S="ab##", T="c#d#"), True],
    [dict(S="a##c", T="#a#c"), True],
    [dict(S="aba#cbbb", T="abbb"), False],
])
def test_solutions(kw, expected):
    assert Solution().backspaceCompare(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

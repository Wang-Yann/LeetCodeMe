#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。 
# 
#  有效的 IP 地址正好由四个整数（每个整数位于 0 到 255 之间组成），整数之间用 '.' 分隔。 
# 
#  
# 
#  示例: 
# 
#  输入: "25525511135"
# 输出: ["255.255.11.135", "255.255.111.35"] 
#  Related Topics 字符串 回溯算法

"""
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []

        def dfs(rest_str, path, dots):
            if dots == 4:
                if rest_str == "":
                    # remove first '.'
                    ans.append(path[1:])
                return
            for i in range(1, 4):
                if i <= len(rest_str):
                    if int(rest_str[:i]) <= 255:
                        dfs(rest_str[i:], path + "." + rest_str[:i], dots + 1)
                        # make sure that res just can be '0.0.0.0' and remove like '00'
                    if rest_str[0] == "0":
                        break

        dfs(s, "", 0)
        return ans


# leetcode submit region end(Prohibit modification and deletion)
class Solution0:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        n = len(s)

        def backtrack(i, tmp, flag):
            if i == n and flag == 0:
                res.append(tmp[:-1])
                return
            if flag < 0:
                return
            for j in range(i, i + 3):
                if j < n:
                    if i == j and s[j] == "0":
                        backtrack(j + 1, tmp + s[j] + ".", flag - 1)
                        break
                    if 0 < int(s[i:j + 1]) <= 255:
                        backtrack(j + 1, tmp + s[i:j + 1] + ".", flag - 1)

        backtrack(0, "", 4)
        return res



class Solution1:

    def restoreIpAddresses(self, s: str) -> List[str]:
        """
        """

        def valid(segment):
            """
            Check if the current segment is valid :
            1. less or equal to 255
            2. the first character could be '0'
               only if the segment is equal to '0'
            """
            return int(segment) <= 255 if segment[0] != '0' else len(segment) == 1

        def update_output(curr_pos):
            """
            Append the current list of segments
            to the list of solutions
            """
            segment = s[curr_pos + 1:n]
            if valid(segment):
                segments.append(segment)
                output.append('.'.join(segments))
                segments.pop()

        def backtrack(prev_pos=-1, dots=3):
            """
            prev_pos : the position of the previously placed dot
            dots : number of dots to place
            """
            # The current dot curr_pos could be placed
            # in a range from prev_pos + 1 to prev_pos + 4.
            # The dot couldn't be placed
            # after the last character in the string.
            for curr_pos in range(prev_pos + 1, min(n - 1, prev_pos + 4)):
                segment = s[prev_pos + 1:curr_pos + 1]
                if valid(segment):
                    # print(segments)
                    segments.append(segment)  # place dot
                    if dots - 1 == 0:  # if all 3 dots are placed
                        update_output(curr_pos)  # add the solution to output
                    else:
                        backtrack(curr_pos, dots - 1)  # continue to place dots
                    segments.pop()  # remove the last placed dot

        n = len(s)
        output, segments = [], []
        backtrack(-1, 3)
        return output


@pytest.mark.parametrize("args,expected", [
    ("25525511135", ["255.255.11.135", "255.255.111.35"]),
])
def test_solutions(args, expected):
    assert sorted(Solution().restoreIpAddresses(args)) == sorted(expected)
    assert sorted(Solution0().restoreIpAddresses(args)) == sorted(expected)
    assert sorted(Solution1().restoreIpAddresses(args)) == sorted(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

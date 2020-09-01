#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 18:21:10
# @Last Modified : 2020-05-05 18:21:10
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 有一个需要密码才能打开的保险箱。密码是 n 位数, 密码的每一位是 k 位序列 0, 1, ..., k-1 中的一个 。
#
#  你可以随意输入密码，保险箱会自动记住最后 n 位输入，如果匹配，则能够打开保险箱。
#
#  举个例子，假设密码是 "345"，你可以输入 "012345" 来打开它，只是你输入了 6 个字符.
#
#  请返回一个能打开保险箱的最短字符串。
#
#
#
#  示例1:
#
#  输入: n = 1, k = 2
# 输出: "01"
# 说明: "10"也可以打开保险箱。
#
#
#
#
#  示例2:
#
#  输入: n = 2, k = 2
# 输出: "00110"
# 说明: "01100", "10011", "11001" 也能打开保险箱。
#
#
#
#
#  提示：
#
#
#  n 的范围是 [1, 4]。
#  k 的范围是 [1, 10]。
#  k^n 最大可能为 4096。
#
#
#
#  Related Topics 深度优先搜索 数学
#  👍 34 👎 0

"""

import pytest


class Solution:

    def crackSafe(self, n: int, k: int) -> str:
        """题意?
        Hierholzer 算法可以在一个欧拉图中找出欧拉回路。
        我们从任意节点 u 开始，任意地经过未经过的边，直到我们“无路可走”。
        可以发现，我们最终一定会停在节点 u，这是因为所有节点的入度和出度都相等
            https://leetcode-cn.com/problems/cracking-the-safe/solution/po-jie-bao-xian-xiang-by-leetcode/
        """
        seen = set()
        self.ans = "0" * (n - 1)

        def dfs(node):
            # print(node )
            for digit in map(str, range(k)):
                neighbor = node + digit
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor[1:])
                    self.ans += digit

        dfs("0" * (n - 1))
        return self.ans


@pytest.mark.parametrize("kwargs,expected", [
    (dict(n=1, k=2), ["01", "10"]),
    pytest.param(dict(n=2, k=2), ["01100", "10011", "11001", "00110"]),
])
def test_solutions(kwargs, expected):
    assert Solution().crackSafe(**kwargs) in expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

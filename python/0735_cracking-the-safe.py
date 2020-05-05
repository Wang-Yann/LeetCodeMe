#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 18:21:10
# @Last Modified : 2020-05-05 18:21:10
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import pytest


class Solution:

    def crackSafe(self, n: int, k: int) -> str:
        """题意?
        Hierholzer 算法可以在一个欧拉图中找出欧拉回路。
        我们从任意节点 u 开始，任意地经过未经过的边，直到我们“无路可走”。可以发现，我们最终一定会停在节点 u，这是因为所有节点的入度和出度都相等

        """
        seen = set()
        ans = []

        def dfs(node):
            # print(node )
            for x in map(str, range(k)):
                neighbor = node + x
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor[1:])
                    ans.append(x)

        dfs("0" * (n - 1))
        # print(ans)
        return "".join(ans) + "0" * (n - 1)


@pytest.mark.parametrize("kwargs,expected", [
    # (dict(n=1, k=2), ["01", "10"]),
    pytest.param(dict(n=2, k=2), ["01100", "10011", "11001", "00110"]),
])
def test_solutions(kwargs, expected):
    assert Solution().crackSafe(**kwargs) in  expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

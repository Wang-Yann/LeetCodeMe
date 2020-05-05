#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 17:48:24
# @Last Modified : 2020-05-05 17:48:24
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

import itertools

import pytest


class Solution0:

    def flipLights(self, n: int, m: int) -> int:
        sample = min(n,3)
        last=[tuple(True for _ in range(sample))]
        for _ in range(m):
            new_status=set()
            for one_list in last:
                new_status.add(tuple(not x for x in one_list))
                new_status.add(tuple(not x  if i%2 else x for i,x in enumerate( one_list) ))
                new_status.add(tuple(not x  if not i%2 else x for i,x in enumerate( one_list) ))
                new_status.add(tuple(not x if i%3 else x for i,x in enumerate(one_list) ))
            last=list(new_status)
        return len(last)



class Solution:

    def flipLights(self, n: int, m: int) -> int:
        """
        Good
        现有一个房间，墙上挂有 n 只已经打开的灯泡和 4 个按钮。在进行了 m 次未知操作后，你需要返回这 n 只灯泡可能有多少种不同的状态

        #前三个?
        前6个灯唯一地决定了其余的灯。这是因为每一个修改 第 xx 的灯光的操作都会修改第 (x+6)(x+6) 的灯光。
        另外：进行 A 操作后接 B 操作 和 B 操作后接 A 操作是一样的，所以我们可以假设我们按顺序进行所有操作。
        最后，连续两次执行相同的操作与不执行任何操作相同。所以我们只需要考虑每个操作是 0 次还是 1 次
        """
        seen = set()
        for cand in itertools.product((0, 1), repeat=4):
            # print(cand)
            if sum(cand) % 2 == m % 2 and sum(cand) <= m:
                A = []
                for i in range(min(n, 3)):
                    light = 1
                    light ^= cand[0]
                    light ^= cand[1] and i % 2
                    light ^= cand[2] and i % 2 == 0
                    light ^= cand[3] and i % 3 == 0
                    A.append(light)
                seen.add(tuple(A))
        print(seen)
        return len(seen)


@pytest.mark.parametrize("kw,expected", [
    (dict(n=1, m=1), 2),
    (dict(n=2, m=1), 3),
    (dict(n=3, m=1), 4)
])
def test_solutions(kw, expected):
    assert Solution().flipLights(**kw) == expected
    assert Solution0().flipLights(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-18 09:58:32
# @Last Modified : 2020-06-18 09:58:32
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0


"""
杭州人称那些傻乎乎粘嗒嗒的人为62（音：laoer）。
杭州交通管理局经常会扩充一些的士车牌照，新近出来一个好消息，以后上牌照，不再含有不吉利的数字了，这样一来，就可以消除个别的士司机和乘客的心理障碍，更安全地服务大众。
不吉利的数字为所有含有4或62的号码。例如：
62315 73418 88914
都属于不吉利号码。但是，61152虽然含有6和2，但不是62连号，所以不属于不吉利数字之列。
你的任务是，对于每次给出的一个牌照区间号，推断出交管局今次又要实际上给多少辆新的士车上牌照了。
问题：输入的都是整数对n、m（0<n≤m<1000000），如果遇到都是0的整数对，则输入结束。

"""

# https://blog.csdn.net/wust_zzwh/article/details/52100392
import pytest


class No62(object):

    def no62num(self, le, ri):

        def solve(x):
            pos = 0
            while x:
                a[pos] = x % 10
                pos += 1
                x //= 10
            return dfs(pos - 1, -1, 0, True)

        def dfs(pos, pre, sta, limit):
            if pos == -1:
                return 1
            sta = int(sta)
            # print(pos, int(sta))
            if not limit and dp[pos][sta] != -1:
                return dp[pos][sta]
            up = a[pos] if limit else 9
            tmp = 0
            for i in range(up + 1):
                if pre == 6 and i == 2:
                    continue
                if i == 4:
                    continue
                tmp += dfs(pos - 1, i, i == 6, limit and i == a[pos])
            if not limit:
                dp[pos][sta] = tmp
            return tmp

        a = [0] * 20
        dp = [[-1] * 20 for _ in range(2)]
        ans = solve(ri) - solve(le - 1)
        return ans


def test_no62():
    assert No62().no62num(1, 100) == 80


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

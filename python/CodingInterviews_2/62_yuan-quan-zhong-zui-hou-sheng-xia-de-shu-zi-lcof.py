#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 0,1,,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。 
# 
#  例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。 
# 
#  
# 
#  示例 1： 
# 
#  输入: n = 5, m = 3
# 输出: 3
#  
# 
#  示例 2： 
# 
#  输入: n = 10, m = 17
# 输出: 2
#  
# 
#  
# 
#  限制： 
# 
#  
#  1 <= n <= 10^5 
#  1 <= m <= 10^6 
#  
# 

"""
import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def lastRemaining(self, n: int, m: int) -> int:
        """
        最终剩下一个人时的安全位置肯定为0，反推安全位置在人数为n时的编号
        人数为1： 0
        人数为2： (0+m) % 2
        人数为3： ((0+m) % 2 + m) % 3
        人数为4： (((0+m) % 2 + m) % 3 + m) % 4
        ........
        迭代推理到n就可以得出答案

链接：https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/solution/c-dao-tui-fa-mian-shi-ti-62-yuan-quan-zhong-zui-ho/

        """
        if n < 1 or m < 1:
            return -1
        last = 0
        for i in range(2, n + 1):
            last = (last + m) % i
        return last


# leetcode submit region end(Prohibit modification and deletion)


class Solution0:

    def lastRemaining(self, n: int, m: int) -> int:
        i, a = 0, list(range(n))
        while len(a) > 1:
            i = (i + m - 1) % len(a)
            a.pop(i)
        return a[0]


class SolutionTTL:
    """TTL"""

    def lastRemaining(self, n: int, m: int) -> int:
        rest = list(range(n))
        idx = 1
        while len(rest) > 1:
            if idx % m == 0:
                rest.pop(0)
            else:
                rest.append(rest.pop(0))
            idx += 1
        return rest[0]


@pytest.mark.parametrize("kwargs,expected", [
    (dict(n=5, m=3), 3),
    pytest.param(dict(n=10, m=17), 2),
    pytest.param(dict(n=70866, m=116922), 64165),  # TTL
])
def test_solutions(kwargs, expected):
    assert Solution().lastRemaining(**kwargs) == expected
    assert Solution0().lastRemaining(**kwargs) == expected
    # assert Solution1().lastRemaining(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

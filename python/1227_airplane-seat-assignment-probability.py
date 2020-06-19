#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-19 08:00:00
# @Last Modified : 2020-06-19 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 有 n 位乘客即将登机，飞机正好有 n 个座位。第一位乘客的票丢了，他随便选了一个座位坐下。 
# 
#  剩下的乘客将会： 
# 
#  
#  
#  如果他们自己的座位还空着，就坐到自己的座位上， 
#  
#  当他们自己的座位被占用时，随机选择其他座位 
#  
# 
#  第 n 位乘客坐在自己的座位上的概率是多少？ 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 1
# 输出：1.00000
# 解释：第一个人只会坐在自己的位置上。 
# 
#  示例 2： 
# 
#  
# 输入: n = 2
# 输出: 0.50000
# 解释：在第一个人选好座位坐下后，第二个人坐在自己的座位上的概率是 0.5。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 10^5 
#  
#  Related Topics 脑筋急转弯 数学 动态规划

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        # p(k) = 1 * (prob that 1th passenger takes his own seat) +
        #        0 * (prob that 1th passenger takes kth one's seat) +
        #        1 * (prob that 1th passenger takes the others' seat) *
        #            (prob that the first k-1 passengers get a seat
        #             which is not kth one's seat)
        #      = 1/k + p(k-1)*(k-2)/k
        #
        # p(1) = 1
        # p(2) = 1/2 + p(1) * (2-2)/2 = 1/2
        # p(3) = 1/3 + p(2) * (3-2)/3 = 1/3 + 1/2 * (3-2)/3 = 1/2
        # ...
        # p(n) = 1/n + 1/2 * (n-2)/n = (2+n-2)/(2n) = 1/2
        return 1.0 if n == 1 else 0.5


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    (1, 1.0),
    (2, 0.5),
])
def test_solutions(args, expected):
    res = Solution().nthPersonGetsNthSeat(args)
    assert res == pytest.approx(expected, 1e-5)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

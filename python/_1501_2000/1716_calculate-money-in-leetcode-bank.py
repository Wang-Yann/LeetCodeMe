#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2021-02-26 21:17:32
# @Last Modified : 2021-02-26 21:17:32
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# Hercy 想要为购买第一辆车存钱。他 每天 都往力扣银行里存钱。 
# 
#  最开始，他在周一的时候存入 1 块钱。从周二到周日，他每天都比前一天多存入 1 块钱。在接下来每一个周一，他都会比 前一个周一 多存入 1 块钱。 
# 
#  给你 n ，请你返回在第 n 天结束的时候他在力扣银行总共存了多少块钱。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 4
# 输出：10
# 解释：第 4 天后，总额为 1 + 2 + 3 + 4 = 10 。
#  
# 
#  示例 2： 
# 
#  输入：n = 10
# 输出：37
# 解释：第 10 天后，总额为 (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37 。注意到第二个星期一，Hercy
#  存入 2 块钱。
#  
# 
#  示例 3： 
# 
#  输入：n = 20
# 输出：96
# 解释：第 20 天后，总额为 (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 
# + 4 + 5 + 6 + 7 + 8) = 96 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 1000 
#  
#  Related Topics 贪心算法 数学 
#  👍 5 👎 0
  

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def totalMoney(self, n: int) -> int:
        monday = 0
        res = cur = 0
        for i in range(1, n + 1):
            if i % 7 == 1:
                monday += 1
                cur = monday
            res += cur
            cur += 1
        return res


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(n=4), 10],
    [dict(n=10), 37],
    [dict(n=20), 96],

])
@pytest.mark.parametrize("SolutionCLS", [Solution, ])
def test_solutions(kw, expected, SolutionCLS):
    res = SolutionCLS().totalMoney(**kw)
    assert res == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])

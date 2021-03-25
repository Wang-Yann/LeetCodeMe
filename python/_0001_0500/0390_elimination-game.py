#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个从1 到 n 排序的整数列表。 
# 首先，从左到右，从第一个数字开始，每隔一个数字进行删除，直到列表的末尾。 
# 第二步，在剩下的数字中，从右到左，从倒数第一个数字开始，每隔一个数字进行删除，直到列表开头。 
# 我们不断重复这两步，从左到右和从右到左交替进行，直到只剩下一个数字。 
# 返回长度为 n 的列表中，最后剩下的数字。 
# 
#  示例： 
# 
#  
# 输入:
# n = 9,
# 1 2 3 4 5 6 7 8 9
# 2 4 6 8
# 2 6
# 6
# 
# 输出:
# 6 
# 

"""
import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def lastRemaining(self, n: int) -> int:
        """约瑟夫环
        https://leetcode-cn.com/problems/elimination-game/solution/mei-ri-suan-fa-day-85-tu-jie-suan-fa-yi-xing-dai-m/
        假设我们用 f(2k)f(2k) 表示初始时 n=2kn=2k 个数字最后剩下的编号
        f(2k)=2(k+1−f(k))
        """
        if n == 1:
            return 1
        return 2 * (1 + n // 2 - self.lastRemaining(n // 2))


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:

    def lastRemaining(self, n: int) -> int:
        start, step, direction = 1, 2, 1
        while n > 1:
            start += direction * (step * (n // 2) - step // 2)
            n //= 2
            step *= 2
            direction *= -1
        return start


@pytest.mark.parametrize("args,expected", [
    (9, 6),
    (100000000, 32896342),
])
def test_solutions(args, expected):
    assert Solution().lastRemaining(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

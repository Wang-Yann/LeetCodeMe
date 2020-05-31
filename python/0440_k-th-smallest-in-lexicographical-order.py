#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给定整数 n 和 k，找到 1 到 n 中字典序第 k 小的数字。 
# 
#  注意：1 ≤ k ≤ n ≤ 109。 
# 
#  示例 : 
# 
#  
# 输入:
# n: 13   k: 2
# 
# 输出:
# 10
# 
# 解释:
# 字典序的排列是 [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]，所以第二小的数字是 10。
#  
# 

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def findKthNumber(self, n: int, k: int) -> int:
        """
            https://leetcode-cn.com/problems/k-th-smallest-in-lexicographical-order/solution/shi-cha-shu-by-powcai/
        十叉树
        """
        res = 1
        k -= 1
        while k > 0:
            cnt = 0
            interval = [res, res + 1]  # 计算result开头至result+1开头间的字符串数量
            while interval[0] <= n:
                cnt += (min(n + 1, interval[1]) - interval[0])  # 每次加上当前的字符串数量
                interval = [10 * interval[0], 10 * interval[1]]  # 每次均扩大10倍
            if k >= cnt:  # 如果不在当前层，减去count
                res += 1
                k -= cnt
            else:
                res *= 10  # 说明在当前层,result*10缩小搜索范围继续查找
                k -= 1
        return res


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    """
    GOOD GOOD TODO

    """

    def findKthNumber(self, n: int, k: int) -> int:

        def cal_steps(n1, n2):
            step = 0
            while n1 <= n:
                step += min(n2, n + 1) - n1
                n1 *= 10
                n2 *= 10
            return step

        cur = 1
        k -= 1

        while k > 0:
            steps = cal_steps(cur, cur + 1)
            if steps <= k:
                k -= steps
                cur += 1
            else:
                k -= 1
                cur *= 10

        return cur


@pytest.mark.parametrize("kwargs,expected", [
    ({"n":13, "k":2}, 10),
])
def test_solutions(kwargs, expected):
    assert Solution().findKthNumber(**kwargs) == expected
    assert Solution1().findKthNumber(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# N 对情侣坐在连续排列的 2N 个座位上，想要牵到对方的手。 计算最少交换座位的次数，以便每对情侣可以并肩坐在一起。 一次交换可选择任意两人，让他们站起来交
# 换座位。 
# 
#  人和座位用 0 到 2N-1 的整数表示，情侣们按顺序编号，第一对是 (0, 1)，第二对是 (2, 3)，以此类推，最后一对是 (2N-2, 2N-1)
# 。 
# 
#  这些情侣的初始座位 row[i] 是由最初始坐在第 i 个座位上的人决定的。 
# 
#  示例 1: 
# 
#  
# 输入: row = [0, 2, 1, 3]
# 输出: 1
# 解释: 我们只需要交换row[1]和row[2]的位置即可。
#  
# 
#  示例 2: 
# 
#  
# 输入: row = [3, 2, 0, 1]
# 输出: 0
# 解释: 无需交换座位，所有的情侣都已经可以手牵手了。
#  
# 
#  说明: 
# 
#  
#  len(row) 是偶数且数值在 [4, 60]范围内。 
#  可以保证row 是序列 0...len(row)-1 的一个全排列。 
#  
#  Related Topics 贪心算法 并查集 图

"""
import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def minSwapsCouples(self, row: List[int]) -> int:
        """
        循环搜索  连通分量
        https://leetcode-cn.com/problems/couples-holding-hands/solution/qing-lu-qian-shou-by-leetcode/
        """
        length = len(row) // 2
        couples = [[] for _ in range(length)]
        for idx, x in enumerate(row):
            couples[x // 2].append(idx // 2)
        graph = collections.defaultdict(list)
        for x, y in couples:
            graph[x].append(y)
            graph[y].append(x)
        ans = length
        for start in range(length):
            if not graph[start]:
                continue
            ans -= 1
            x, y = start, graph[start].pop()
            while y != start:
                graph[y].remove(x)
                x, y = y, graph[y].pop()
        return ans


# leetcode submit region end(Prohibit modification and deletion)
class Solution1(object):
    """
    贪心

    根据我们的假设，可以制定按顺序让每张沙发上情侣开心的策略。对于每张沙发，找到沙发上第一个人的情侣，如果不在同一个沙发上，就把沙发上的第二人换成第一个人的情侣。


如果一个人的编号为 x，那么他的情侣的编号为 x ^ 1， ^ 在这里是异或操作。对于每张沙发上的第一个人 x = row[i]，找到他们的同伴所在的位置 row[j]，将 row[j] 和 row[i + 1] 互相交换。



    """

    def minSwapsCouples(self, row):
        ans = 0
        for i in range(0, len(row), 2):
            x = row[i]
            if row[i + 1] == x ^ 1:
                continue
            ans += 1
            for j in range(i + 1, len(row)):
                if row[j] == x ^ 1:
                    row[i + 1], row[j] = row[j], row[i + 1]
                    break
        return ans


@pytest.mark.parametrize("args,expected", [
    ([0, 2, 1, 3], 1),
    pytest.param([3, 2, 0, 1], 0),
])
def test_solutions(args, expected):
    assert Solution().minSwapsCouples(args) == expected
    assert Solution1().minSwapsCouples(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

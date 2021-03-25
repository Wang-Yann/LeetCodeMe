#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 这里有 n 个航班，它们分别从 1 到 n 进行编号。 
# 
#  我们这儿有一份航班预订表，表中第 i 条预订记录 bookings[i] = [i, j, k] 意味着我们在从 i 到 j 的每个航班上预订了 k 个座
# 位。 
# 
#  请你返回一个长度为 n 的数组 answer，按航班编号顺序返回每个航班上预订的座位数。 
# 
#  
# 
#  示例： 
# 
#  输入：bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
# 输出：[10,55,45,25,25]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= bookings.length <= 20000 
#  1 <= bookings[i][0] <= bookings[i][1] <= n <= 20000 
#  1 <= bookings[i][2] <= 10000 
#  
#  Related Topics 数组 数学

"""
from typing import List

import pytest

from sample_datas import BIG_CASE, BIG_RES


# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        """
        前缀和
        GOOD　掌握好
        将对一个区间的操作转化为左、右两个端点上的操作
        """
        res = [0] * n
        for l, r, seat in bookings:
            res[l - 1] += seat
            if r < n:
                res[r] -= seat
        # print(res)
        for i in range(1, n):
            res[i] += res[i - 1]
        return res


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(bookings=[[1, 2, 10], [2, 3, 20], [2, 5, 25]], n=5), [10, 55, 45, 25, 25]],
    [dict(bookings=BIG_CASE.BIG_1109, n=20000), BIG_RES.BIG_1109],
    [dict(bookings=BIG_CASE.BIG_1109_2, n=20000), BIG_RES.BIG_1109_2],
])
def test_solutions(kw, expected):
    assert Solution().corpFlightBookings(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

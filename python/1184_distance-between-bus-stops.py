#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-02 08:00:00
# @Last Modified : 2020-07-02 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 环形公交路线上有 n 个站，按次序从 0 到 n - 1 进行编号。我们已知每一对相邻公交站之间的距离，distance[i] 表示编号为 i 的车站和编号
# 为 (i + 1) % n 的车站之间的距离。 
# 
#  环线上的公交车都可以按顺时针和逆时针的方向行驶。 
# 
#  返回乘客从出发点 start 到目的地 destination 之间的最短距离。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：distance = [1,2,3,4], start = 0, destination = 1
# 输出：1
# 解释：公交站 0 和 1 之间的距离是 1 或 9，最小值是 1。 
# 
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：distance = [1,2,3,4], start = 0, destination = 2
# 输出：3
# 解释：公交站 0 和 2 之间的距离是 3 或 7，最小值是 3。
#  
# 
#  
# 
#  示例 3： 
# 
#  
# 
#  输入：distance = [1,2,3,4], start = 0, destination = 3
# 输出：4
# 解释：公交站 0 和 3 之间的距离是 6 或 4，最小值是 4。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 10^4 
#  distance.length == n 
#  0 <= start, destination < n 
#  0 <= distance[i] <= 10^4 
#  
#  Related Topics 数组

"""
import itertools
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        if start > destination:
            start, destination = destination, start
        s_to_d = sum(itertools.islice(distance, start, destination))
        d_to_s = sum(itertools.islice(distance, 0, start)) + sum(itertools.islice(distance, destination, len(distance)))
        return min(s_to_d, d_to_s)


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        N = len(distance)
        if start == destination:
            return 0
        start, destination = min(start, destination), max(start, destination)
        ans1 = ans2 = 0
        for i in range(start, destination):
            ans1 += distance[i]
        for i in range(destination, start + N):
            ans2 += distance[i % N]
        # print(ans1,ans2)
        return min(ans2, ans1)


@pytest.mark.parametrize("kw,expected", [
    [dict(distance=[1, 2, 3, 4], start=0, destination=1), 1],
    [dict(distance=[1, 2, 3, 4], start=0, destination=2), 3],
    [dict(distance=[1, 2, 3, 4], start=0, destination=3), 4],
])
def test_solutions(kw, expected):
    assert Solution().distanceBetweenBusStops(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

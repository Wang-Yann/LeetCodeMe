#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。 
# 
#  你需要按照以下要求，帮助老师给这些孩子分发糖果： 
# 
#  
#  每个孩子至少分配到 1 个糖果。 
#  相邻的孩子中，评分高的孩子必须获得更多的糖果。 
#  
# 
#  那么这样下来，老师至少需要准备多少颗糖果呢？ 
# 
#  示例 1: 
# 
#  输入: [1,0,2]
# 输出: 5
# 解释: 你可以分别给这三个孩子分发 2、1、2 颗糖果。
#  
# 
#  示例 2: 
# 
#  输入: [1,2,2]
# 输出: 4
# 解释: 你可以分别给这三个孩子分发 1、2、1 颗糖果。
#      第三个孩子只得到 1 颗糖果，这已满足上述两个条件。 
#  Related Topics 贪心算法

"""
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    """
    首先从左到右遍历, 如果发现一个小孩左边的小孩比自己的 rating 低, 那么把这个小孩的糖果数设为他左边的小孩 + 1
    这时我们分配的糖果已经满足了: 评分更高的小孩比他左边的小孩获得更多的糖果. 然后我们再从右往左遍历一次就可以了.
    但是这时还应该注意一点: 当一个小孩右边的小孩比自己的 rating 低时, 这个小孩的糖果可能已经比他右边的小孩多了, 而且可能多不止一个, 这时应该保留他的糖果数目不变.
    """

    def candy(self, ratings: List[int]) -> int:
        length = len(ratings)
        candy_nums = [1] * length
        for i in range(1, length):
            if ratings[i] > ratings[i - 1]:
                candy_nums[i] = candy_nums[i - 1] + 1
        for i in range(length - 2, -1, -1):
            if ratings[i + 1] < ratings[i] and candy_nums[i + 1] >= candy_nums[i]:
                candy_nums[i] = candy_nums[i + 1] + 1
        return sum(candy_nums)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ([1, 0, 2], 5),
    pytest.param([1, 2, 2], 4),
])
def test_solutions(args, expected):
    assert Solution().candy(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

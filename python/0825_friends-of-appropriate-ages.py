#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 人们会互相发送好友请求，现在给定一个包含有他们年龄的数组，ages[i] 表示第 i 个人的年龄。 
# 
#  当满足以下条件时，A 不能给 B（A、B不为同一人）发送好友请求： 
# 
#  
#  age[B] <= 0.5 * age[A] + 7 
#  age[B] > age[A] 
#  age[B] > 100 && age[A] < 100 
#  
# 
#  否则，A 可以给 B 发送好友请求。 
# 
#  注意如果 A 向 B 发出了请求，不等于 B 也一定会向 A 发出请求。而且，人们不会给自己发送好友请求。 
# 
#  求总共会发出多少份好友请求? 
# 
#  
# 
#  示例 1: 
# 
#  输入: [16,16]
# 输出: 2
# 解释: 二人可以互发好友申请。
#  
# 
#  示例 2: 
# 
#  输入: [16,17,18]
# 输出: 2
# 解释: 好友请求可产生于 17 -> 16, 18 -> 17. 
# 
#  示例 3: 
# 
#  输入: [20,30,100,110,120]
# 输出: 3
# 解释: 好友请求可产生于 110 -> 100, 120 -> 110, 120 -> 100.
#  
# 
#  
# 
#  说明: 
# 
#  
#  1 <= ages.length <= 20000. 
#  1 <= ages[i] <= 120. 
#  
#  Related Topics 数组

"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def numFriendRequests(self, ages: List[int]) -> int:
        def request(a, b):
            return 0.5 * a + 7 < b <= a

        counter = collections.Counter(ages)

        return sum(
            int(request(a, b)) * counter[a] * (counter[b] - int(a == b))
            for a in counter for b in counter
        )


# leetcode submit region end(Prohibit modification and deletion)

class Solution1(object):

    def numFriendRequests(self, ages):
        """
        当 ageA == ageB 的时候我们就数多了：我们只有 countA * (countA - 1) 对好友请求
        """
        count = [0] * 121
        for age in ages:
            count[age] += 1

        ans = 0
        for ageA, countA in enumerate(count):
            for ageB, countB in enumerate(count):
                if ageA * 0.5 + 7 >= ageB:
                    continue
                if ageA < ageB:
                    continue
                if ageA < 100 < ageB:
                    continue
                ans += countA * countB
                if ageA == ageB:
                    ans -= countA

        return ans


@pytest.mark.parametrize("args,expected", [
    ([16, 16], 2),
    ([16, 17, 18], 2),
    ([20, 30, 100, 110, 120], 3),
])
def test_solutions(args, expected):
    assert Solution().numFriendRequests(args) == expected
    assert Solution1().numFriendRequests(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

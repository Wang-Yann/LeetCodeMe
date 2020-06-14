#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 第 i 个人的体重为 people[i]，每艘船可以承载的最大重量为 limit。 
# 
#  每艘船最多可同时载两人，但条件是这些人的重量之和最多为 limit。 
# 
#  返回载到每一个人所需的最小船数。(保证每个人都能被船载)。 
# 
#  
# 
#  示例 1： 
# 
#  输入：people = [1,2], limit = 3
# 输出：1
# 解释：1 艘船载 (1, 2)
#  
# 
#  示例 2： 
# 
#  输入：people = [3,2,2,1], limit = 3
# 输出：3
# 解释：3 艘船分别载 (1, 2), (2) 和 (3)
#  
# 
#  示例 3： 
# 
#  输入：people = [3,5,3,4], limit = 5
# 输出：4
# 解释：4 艘船分别载 (3), (3), (4), (5) 
# 
#  提示： 
# 
#  
#  1 <= people.length <= 50000 
#  1 <= people[i] <= limit <= 30000 
#  
#  Related Topics 贪心算法 双指针

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        ans = 0
        l, r = 0, len(people) - 1
        while l <= r:
            if  people[r] + people[l] <= limit:
                ans += 1
                l += 1
                r -= 1
            elif people[r] <= limit:
                r -= 1
                ans += 1
            else:
                return -1
        return ans


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kwargs,expected", [
    (dict(people=[1, 2], limit=3), 1),
    (dict(people=[1, 2,2], limit=3), 2),
    pytest.param(dict(people=[3, 2, 2, 1], limit=3), 3),
    pytest.param(dict(people=[3, 5, 3, 4], limit=5), 4),
])
def test_solutions(kwargs, expected):
    assert Solution().numRescueBoats(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

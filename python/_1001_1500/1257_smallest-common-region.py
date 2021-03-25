#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-07 10:06:23
# @Last Modified : 2020-08-07 10:06:23
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一些区域列表 regions ，每个列表的第一个区域都包含这个列表内所有其他区域。 
# 
#  很自然地，如果区域 X 包含区域 Y ，那么区域 X 比区域 Y 大。 
# 
#  给定两个区域 region1 和 region2 ，找到同时包含这两个区域的 最小 区域。 
# 
#  如果区域列表中 r1 包含 r2 和 r3 ，那么数据保证 r2 不会包含 r3 。 
# 
#  数据同样保证最小公共区域一定存在。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：
# regions = [["Earth","North America","South America"],
# ["North America","United States","Canada"],
# ["United States","New York","Boston"],
# ["Canada","Ontario","Quebec"],
# ["South America","Brazil"]],
# region1 = "Quebec",
# region2 = "New York"
# 输出："North America"
#  
# 
#  
# 
#  提示： 
# 
#  
#  2 <= regions.length <= 10^4 
#  region1 != region2 
#  所有字符串只包含英文字母和空格，且最多只有 20 个字母。 
#  
#  Related Topics 树 
#  👍 12 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        """AC"""
        lookup = {}
        for region in regions:
            p = region[0]
            for son in region[1:]:
                lookup[son] = p
        path1 = {region1}
        while region1 in lookup:
            region1 = lookup[region1]
            path1.add(region1)
        while region2:
            if region2 in path1:
                return region2
            region2 = lookup.get(region2)


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kw,expected", [
    [dict(
        regions=[["Earth", "North America", "South America"],
                 ["North America", "United States", "Canada"],
                 ["United States", "New York", "Boston"],
                 ["Canada", "Ontario", "Quebec"],
                 ["South America", "Brazil"]],
        region1="Quebec",
        region2="New York"

    ), "North America"],
])
def test_solutions(kw, expected):
    assert Solution().findSmallestRegion(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

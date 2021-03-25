#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示，其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。 编写一个算法来
# 重建这个队列。 
# 
#  注意： 
# 总人数少于1100人。 
# 
#  示例 
# 
#  
# 输入:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
# 
# 输出:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
#  
#  Related Topics 贪心算法

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """
        ...TODO
        """
        res = []
        people.sort(key=lambda h_cnt: (-h_cnt[0], h_cnt[1]))
        # print(people)
        for p in people:
            res.insert(p[1], p)
        return res


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]],
     [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]])
])
def test_solutions(args, expected):
    assert Solution().reconstructQueue(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

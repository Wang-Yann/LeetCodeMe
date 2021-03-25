#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-04 14:10:12
# @Last Modified : 2020-08-04 14:10:12
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给你一个不同学生的分数列表，请按 学生的 id 顺序 返回每个学生 最高的五科 成绩的 平均分。 
# 
#  对于每条 items[i] 记录， items[i][0] 为学生的 id，items[i][1] 为学生的分数。平均分请采用整数除法计算。 
# 
#  
# 
#  示例： 
# 
#  输入：[[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[
# 2,76]]
# 输出：[[1,87],[2,88]]
# 解释：
# id = 1 的学生平均分为 87。
# id = 2 的学生平均分为 88.6。但由于整数除法的缘故，平均分会被转换为 88。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= items.length <= 1000 
#  items[i].length == 2 
#  学生的 ID 在 1 到 1000 之间 
#  学生的分数在 1 到 100 之间 
#  每个学生至少有五个分数 
#  
#  Related Topics 排序 数组 哈希表 
#  👍 9 👎 0

"""

import itertools
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        ans = []
        for idx, scores in itertools.groupby(sorted(items, key=lambda x: (x[0], -x[1])),
                                             key=lambda x: x[0]):
            scores_all = list(x[1] for x in scores)
            avg = sum(scores_all[:5]) // 5
            ans.append([idx, avg])
        return ans


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    ([[1, 91], [1, 92], [2, 93], [2, 97], [1, 60], [2, 77], [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]],
     [[1, 87], [2, 88]]
     )
])
def test_solutions(args, expected):
    assert Solution().highFive(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

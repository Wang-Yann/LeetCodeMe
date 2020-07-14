#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-14 23:09:04
# @Last Modified : 2020-07-14 23:09:04
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 假设你有两个数组，一个长一个短，短的元素均不相同。找到长数组中包含短数组所有的元素的最短子数组，其出现顺序无关紧要。 
# 
#  返回最短子数组的左端点和右端点，如有多个满足条件的子数组，返回左端点最小的一个。若不存在，返回空数组。 
# 
#  示例 1: 
# 
#  输入:
# big = [7,5,9,0,2,1,3,5,7,9,1,1,5,8,8,9,7]
# small = [1,5,9]
# 输出: [7,10] 
# 
#  示例 2: 
# 
#  输入:
# big = [1,2,3]
# small = [4]
# 输出: [] 
# 
#  提示： 
# 
#  
#  big.length <= 100000 
#  1 <= small.length <= 100000 
#  
#  Related Topics Sliding Window 
#  👍 8 👎 0


"""

import collections
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def shortestSeq(self, big: List[int], small: List[int]) -> List[int]:
        counter = collections.Counter(small)
        l = 0
        window_cnt = 0
        ans = []
        for r, num in enumerate(big):
            if num not in counter:  # counter 继续
                continue
            counter[num] -= 1  # counter
            if counter[num] == 0:
                window_cnt += 1  # 统计n
            while big[l] not in counter or counter[big[l]] < 0:  # 移动左指针：big[l]counter，或者big[l]出现不止一次
                if counter[big[l]] < 0:
                    counter[big[l]] += 1  # 如果出现不止一次， 左指针右移，并加一
                l += 1
            if window_cnt == len(counter):  # 如果符合题目条件：
                if not ans or (ans[1] - ans[0]) > r - l:  # 找最小串
                    ans = [l, r]
        return ans


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    [dict(big=[7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7], small=[1, 5, 9]), [7, 10]],
    [dict(big=[1, 2, 3], small=[4]), []],

])
def test_solutions(kwargs, expected):
    assert Solution().shortestSeq(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])

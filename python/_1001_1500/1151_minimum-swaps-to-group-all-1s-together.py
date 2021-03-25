#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-04 18:23:00
# @Last Modified : 2020-08-04 18:23:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给出一个二进制数组 data，你需要通过交换位置，将数组中 任何位置 上的 1 组合到一起，并返回所有可能中所需 最少的交换次数。 
# 
#  
# 
#  示例 1： 
# 
#  输入：[1,0,1,0,1]
# 输出：1
# 解释： 
# 有三种可能的方法可以把所有的 1 组合在一起：
# [1,1,1,0,0]，交换 1 次；
# [0,1,1,1,0]，交换 2 次；
# [0,0,1,1,1]，交换 1 次。
# 所以最少的交换次数为 1。
#  
# 
#  示例 2： 
# 
#  输入：[0,0,0,1,0]
# 输出：0
# 解释： 
# 由于数组中只有一个 1，所以不需要交换。
#  
# 
#  示例 3： 
# 
#  输入：[1,0,1,0,1,0,0,1,1,0,1]
# 输出：3
# 解释：
# 交换 3 次，一种可行的只用 3 次交换的解决方案是 [0,0,0,0,0,1,1,1,1,1,1]。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= data.length <= 10^5 
#  0 <= data[i] <= 1 
#  
#  Related Topics 数组 Sliding Window 
#  👍 13 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minSwaps(self, data: List[int]) -> int:
        """
        TODO
        计算原数组 data 中 1 的个数 totalOne。
            维护一个长度为 totalOne 的窗口，计算窗口中 1 的个数。先遍历求出第一个窗口 1 的个数，并保存好这个数字，记为 countOne。
            向右移动窗口，继续计算 1 的个数。假设当前下标为 i，那么需要加上当前的数字，再减去移出窗口的数字，
            移出窗口的下标为 i - totalOne。所以新的窗口 1 的个数为 countOne += data[i] - data[i-totalOne]。
            求 countOne 的最大值，和 totalOne 相减就是我们要求的结果

        """
        total_one = sum(data)
        one, count, l = 0, 0, 0
        for r in range(len(data)):
            count += data[r]
            if r - l + 1 > total_one:
                count -= data[l]
                l += 1
            one = max(one, count)
        return total_one - one


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:
    def minSwaps(self, data: List[int]) -> int:
        # Find the longest continuous string which gap smaller than zero_cnt
        zero_cnt, one_cnt, sum_one = 0, 0, sum(data)
        j, res = 0, 0
        for i in range(len(data)):
            if data[i] == 0:
                zero_cnt += 1
            else:
                one_cnt += 1
            while zero_cnt > sum_one - one_cnt:
                if data[j] == 0:
                    zero_cnt -= 1
                else:
                    one_cnt -= 1
                j += 1
            res = max(res, one_cnt)
        return sum_one - res


@pytest.mark.parametrize("args,expected", [
    ([1, 0, 1, 0, 1], 1),
    ([0, 0, 0, 1, 0], 0),
])
def test_solutions(args, expected):
    assert Solution().minSwaps(args) == expected
    assert Solution1().minSwaps(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-09 16:29:16
# @Last Modified : 2020-08-09 16:29:16
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
We have an integer array nums, where all the integers in nums are 0 or 1. You will not be given direct access to the array, instead, you will have
an API ArrayReader which have the following functions:

int query(int a, int b, int c, int d): where 0 <= a < b < c < d < ArrayReader.length(). The function returns the distribution of the value of the 4
elements and returns:
4 : if the values of the 4 elements are the same (0 or 1).
2 : if three elements have a value equal to 0 and one element has value equal to 1 or vice versa.
0 : if two element have a value equal to 0 and two elements have a value equal to 1.
int length(): Returns the size of the array.
You are allowed to call query() 2 * n times at most where n is equal to ArrayReader.length().

Return any index of the most frequent value in nums, in case of tie, return -1.

Follow up: What is the minimum number of calls needed to find the majority element?

 

Example 1:

Input: nums = [0,0,1,0,1,1,1,1]
Output: 5
Explanation: The following calls to the API
reader.length() // returns 8 because there are 8 elements in the hidden array.
reader.query(0,1,2,3) // returns 2 this is a query that compares the elements nums[0], nums[1], nums[2], nums[3]
// Three elements have a value equal to 0 and one element has value equal to 1 or viceversa.
reader.query(4,5,6,7) // returns 4 because nums[4], nums[5], nums[6], nums[7] have the same value.
we can infer that the most frequent value is found in the last 4 elements.
Index 2, 4, 6, 7 is also a correct answer.
Example 2:

Input: nums = [0,0,1,1,0]
Output: 0
Example 3:

Input: nums = [1,0,1,0,1,0,1,0]
Output: -1
 

Constraints:

5 <= nums.length <= 10^5
0 <= nums[i] <= 1
通过次数15提交次数38


 👍 1 👎 0
	 

"""

import collections

import pytest


class ArrayReader(object):

    def __init__(self, arr):
        self.arr = arr
        self.cnt = 0

    # Compares 4 different elements in the array
    #	 # return 4 if the values of the 4 elements are the same (0 or 1).
    #	 # return 2 if three elements have a value equal to 0 and one element has value equal to 1 or vice versa.
    #	 # return 0 : if two element have a value equal to 0 and two elements have a value equal to 1.
    def query(self, a: int, b: int, c: int, d: int) -> int:
        self.cnt += 1
        counter = collections.Counter([self.arr[a], self.arr[b], self.arr[c], self.arr[d]])
        if len(counter) == 1:
            return 4
        if len(counter) == 2 and 3 in counter.values():
            return 2
        else:
            return 0

    def length(self) -> int:
        return len(self.arr)


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:

    def guessMajority(self, reader: 'ArrayReader') -> int:
        """
        如果我们希望得到位置 p 和 q 的数是否相等，我们只要查询 p, x, y, z 和 q, x, y, z，这两次查询结果相等当且仅当位置 p 和 q 的数相等
        """
        N = reader.length()
        v = [0] * N
        v[0] = 1
        q0123 = reader.query(0, 1, 2, 3)
        q0124 = reader.query(0, 1, 2, 4)
        q0134 = reader.query(0, 1, 3, 4)
        q0234 = reader.query(0, 2, 3, 4)
        q1234 = reader.query(1, 2, 3, 4)
        v[1] = (q0234 == q1234)
        v[2] = (q0134 == q1234)
        v[3] = (q0124 == q1234)
        v[4] = (q0123 == q1234)
        prev = q1234
        for i in range(5, N):
            curr = reader.query(i - 3, i - 2, i - 1, i)
            v[i] = v[i - 4] if prev == curr else 1 - v[i - 4]
            prev = curr
        sum_val = sum(v)
        if sum_val * 2 < N:
            return v.index(0)
        elif sum_val * 2 > N:
            return v.index(1)
        else:
            return -1


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    [dict(nums=[0, 0, 1, 0, 1, 1, 1, 1]), 5],

    pytest.param(dict(nums=[0, 0, 1, 1, 0]), 0),
    pytest.param(dict(nums=[1, 0, 1, 0, 1, 0, 1, 0]), -1),
])
def test_solutions(kwargs, expected):
    nums = kwargs.pop("nums")
    reader = ArrayReader(nums)
    N = len(nums)
    ret = Solution().guessMajority(reader)
    assert ret == expected == -1 or nums[ret] == nums[expected]
    assert reader.cnt <= 2 * N


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])

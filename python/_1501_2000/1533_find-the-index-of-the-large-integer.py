#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-08-09 14:15:03
# @Last Modified : 2020-08-09 14:15:03
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
We have an integer array arr, where all the integers in arr are equal except for one integer which is larger than the rest of the integers. You
will not be given direct access to the array, instead, you will have an API ArrayReader which have the following functions:

int compareSub(int l, int r, int x, int y): where 0 <= l, r, x, y < ArrayReader.length(), l <= r and x <= y. The function compares the sum of
sub-array arr[l..r] with the sum of the sub-array arr[x..y] and returns:
1 if arr[l]+arr[l+1]+...+arr[r] > arr[x]+arr[x+1]+...+arr[y].
0 if arr[l]+arr[l+1]+...+arr[r] == arr[x]+arr[x+1]+...+arr[y].
-1 if arr[l]+arr[l+1]+...+arr[r] < arr[x]+arr[x+1]+...+arr[y].
int length(): Returns the size of the array.
You are allowed to call compareSub() 20 times at most. You can assume both functions work in O(1) time.

Return the index of the array arr which has the largest integer.

Follow-up:

What if there are two numbers in arr that are bigger than all other numbers?
What if there is one number that is bigger than other numbers and one number that is smaller than other numbers?
 

Example 1:

Input: arr = [7,7,7,7,10,7,7,7]
Output: 4
Explanation: The following calls to the API
reader.compareSub(0, 0, 1, 1) // returns 0 this is a query comparing the sub-array (0, 0) with the sub array (1, 1), (i.e. compares arr[0] with
arr[1]).
Thus we know that arr[0] and arr[1] doesn't contain the largest element.
reader.compareSub(2, 2, 3, 3) // returns 0, we can exclude arr[2] and arr[3].
reader.compareSub(4, 4, 5, 5) // returns 1, thus for sure arr[4] is the largest element in the array.
Notice that we made only 3 calls, so the answer is valid.
Example 2:

Input: nums = [6,6,12]
Output: 2
 

Constraints:

2 <= arr.length <= 5 * 10^5
1 <= arr[i] <= 100
All elements of arr are equal except for one element which is larger than all other elements.
通过次数23提交次数26

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-the-index-of-the-large-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

#  Related Topics 二分查找
#  👍 1 👎 0
	 

"""

import pytest


class ArrayReader(object):

    def __init__(self, arr):
        self.arr = arr
        self.cnt = 0

    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
        """
        # return 1 if sum(arr[l..r]) > sum(arr[x..y])
        # return 0 if sum(arr[l..r]) == sum(arr[x..y])
        # return -1 if sum(arr[l..r]) < sum(arr[x..y])
        """
        a, b = sum(self.arr[l:r + 1]), sum(self.arr[x:y + 1])
        self.cnt += 1
        if a > b:
            return 1
        elif a < b:
            return -1
        else:
            return 0

    def length(self) -> int:
        return len(self.arr)


# leetcode submit region begin(Prohibit modification and deletion)
# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#


class Solution:

    def getIndex(self, reader: 'ArrayReader') -> int:
        l, r = 0, reader.length() - 1
        while l <= r:

            mid = (l + r) // 2
            if (r - l) % 2 == 1:
                m_l, m_r = mid, mid + 1
            else:
                m_l, m_r = mid, mid

            # print(l, l1, r0, r, mid)
            flag = reader.compareSub(l, m_l, m_r, r)
            if flag == 1:
                r = m_l
            elif flag == -1:
                l = m_r
            else:
                return mid


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("kwargs,expected", [
    [dict(arr=[7, 7, 7, 7, 10, 7, 7, 7]), 4],

    pytest.param(dict(arr=[6, 6, 12]), 2),
])
def test_solutions(kwargs, expected):
    reader = ArrayReader(kwargs["arr"])
    assert Solution().getIndex(reader) == expected
    assert reader.cnt <= 20


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])

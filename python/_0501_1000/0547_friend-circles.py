#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C 
# 的朋友。所谓的朋友圈，是指所有朋友的集合。 
# 
#  给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。你
# 必须输出所有学生中的已知的朋友圈总数。 
# 
#  示例 1: 
# 
#  
# 输入: 
# [[1,1,0],
#  [1,1,0],
#  [0,0,1]]
# 输出: 2 
# 说明：已知学生0和学生1互为朋友，他们在一个朋友圈。
# 第2个学生自己在一个朋友圈。所以返回2。
#  
# 
#  示例 2: 
# 
#  
# 输入: 
# [[1,1,0],
#  [1,1,1],
#  [0,1,1]]
# 输出: 1
# 说明：已知学生0和学生1互为朋友，学生1和学生2互为朋友，所以学生0和学生2也是朋友，所以他们三个在一个朋友圈，返回1。
#  
# 
#  注意： 
# 
#  
#  N 在[1,200]的范围内。 
#  对于所有学生，有M[i][i] = 1。 
#  如果有M[i][j] = 1，则有M[j][i] = 1。 
#  
#  Related Topics 深度优先搜索 并查集

"""
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class UnionFind(object):
    def __init__(self,n):
        self.set=list(range(n))
        self.count=n
    def find_set(self,x):
        if self.set[x]!=x:
            self.set[x]=self.find_set(self.set[x])
        return self.set[x]
    def union_set(self,x,y):
        x_root,y_root = map(self.find_set,(x,y))
        if x_root==y_root:
            return False
        self.set[min(x_root,y_root)]=max(x_root,y_root)
        self.count-=1
        return True
        

class Solution:

    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M:
            return 0
        m= len(M)
        uf=UnionFind(m)
        for i in range(m):
            for j in range(m):
                if M[i][j]==1 and i!=j:
                    uf.union_set(i,j)
        return uf.count
                    


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("args,expected", [
    ([[1, 1, 0],
      [1, 1, 0],
      [0, 0, 1]]
     , 2),
    pytest.param(
        [[1, 1, 0],
         [1, 1, 1],
         [0, 1, 1]],
        1),
])
def test_solutions(args, expected):
    assert Solution().findCircleNum(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-06-18 09:58:32
# @Last Modified : 2020-06-18 09:58:32
# @Mail          : rock@get.com.mm
# @Version       : alpha-1.0
"""
模板
memset(dp,0,sizeof(dp));
//初始dp数组
for(int len=2;len<=n;len++){
    //枚举区间长度
    for(int i=1;i<n;++i){//枚举区间的起点
        int j=i+len-1;//根据起点和长度得出终点
        if(j>n) break;//符合条件的终点
        for(int k=i;k<=j;++k)//枚举最优分割点
            dp[i][j]=min(dp[i][j],dp[i][k]+dp[k+1][j]+w[i][j]);//状态转移方程
        }
}

作者：52hz-r
链接：https://leetcode-cn.com/problems/minimum-score-triangulation-of-polygon/solution/qu-jian-dpwen-ti-fu-mo-ban-by-52hz-r/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
import pytest

if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])

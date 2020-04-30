//
/* Created by rock on 4/27/20.
*/
#pragma once
#ifndef LEETCODE_FUNCTIONS_H
#define LEETCODE_FUNCTIONS_H

#include "common.h"
//0002
int* twoSum(int* nums, int numsSize, int target, int* returnSize);
//0026
int nthUglyNumber(int n);

//0028
int strStr(char * haystack, char * needle);

//0646
int findLongestChain(int **pairs, int pairsSize, int *pairsColSize);

struct ListNode {
    int val;
    struct ListNode *next;
};


#define max(a,b) \
   ({ __typeof__ (a) _a = (a); \
       __typeof__ (b) _b = (b); \
     _a > _b ? _a : _b; });


#define min(a,b) \
   ({ __typeof__ (a) _a = (a); \
       __typeof__ (b) _b = (b); \
     _a < _b ? _a : _b; })




#endif //LEETCODE_FUNCTIONS_H

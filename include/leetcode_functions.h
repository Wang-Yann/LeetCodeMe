//
/* Created by rock on 4/27/20.
*/
#pragma once
#ifndef LEETCODE_FUNCTIONS_H
#define LEETCODE_FUNCTIONS_H

#include "common.h"

#define max(a,b) \
   ({ __typeof__ (a) _a = (a); \
       __typeof__ (b) _b = (b); \
     _a > _b ? _a : _b; });


#define min(a,b) \
   ({ __typeof__ (a) _a = (a); \
       __typeof__ (b) _b = (b); \
     _a < _b ? _a : _b; })

#define MIN(a,b,c) ((a)<(b)?( (a)<(c)?(a):(c) ):( (b)<(c)?(b):(c) ))



//0002
int* twoSum(int* nums, int numsSize, int target, int* returnSize);

//0007
int reverse(int x);

//0020
bool isValid(char * s);

//0026
int nthUglyNumber(int n);

//0028
int strStr(char * haystack, char * needle);

//0050
double myPow(double x, int n);
//0065
bool isNumber(char * s);

//0069
int mySqrt(int x);


//0098
bool isValidBST(struct TreeNode * root);

//0221
int maximalSquare(char **matrix, int matrixSize, int *matrixColSize);
//00236
struct TreeNode* lowestCommonAncestor(struct TreeNode* root, struct TreeNode* p, struct TreeNode* q);

//0646
int findLongestChain(int **pairs, int pairsSize, int *pairsColSize);




#endif //LEETCODE_FUNCTIONS_H

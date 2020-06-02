//
/* Created by rock on 4/27/20.
*/
#pragma once
#ifndef LEETCODE_FUNCTIONS_H
#define LEETCODE_FUNCTIONS_H

#include "common.h"


//0002
int *twoSum(int *nums, int numsSize, int target, int *returnSize);

//0004
double findMedianSortedArrays(int *nums1, int nums1Size, int *nums2, int nums2Size);

//0005
char *longestPalindrome(char *s);

//0007
int reverse(int x);

//0020
bool isValid(char *s);

//0025
struct ListNode *reverseKGroup(struct ListNode *head, int k);

//0026
int nthUglyNumber(int n);

//0028
int strStr(char *haystack, char *needle);

//0050
double myPow(double x, int n);

//0065
bool isNumber(char *s);

//0069
int mySqrt(int x);

//0076
char *minWindow(char *s, char *t);

//0084
int largestRectangleArea(int* heights, int heightsSize);
//0098
bool isValidBST(struct TreeNode *root);
//0101
bool isSymmetric(struct TreeNode* root);
//0102
int **levelOrder(struct TreeNode *root, int *returnSize, int **returnColumnSizes);

//0105
struct TreeNode *buildTree(int *preorder, int preorderSize, int *inorder, int inorderSize);

//0136
int singleNumber(int *nums, int numsSize);

//0152
int maxProduct(int *nums, int numsSize);
//0198
int rob(int* nums, int numsSize);

//0210
int *findOrder(int numCourses, int **prerequisites, int prerequisitesSize, int *prerequisitesColSize, int *returnSize);

//0221
int maximalSquare(char **matrix, int matrixSize, int *matrixColSize);

//00236
struct TreeNode *lowestCommonAncestor(struct TreeNode *root, struct TreeNode *p, struct TreeNode *q);

//0287
int findDuplicate(int *nums, int numsSize);
//0394
char * decodeString(char * s);
//0560
int subarraySum(int *nums, int numsSize, int k);

//0646
int findLongestChain(int **pairs, int pairsSize, int *pairsColSize);

//0680
bool validPalindrome(char *s);
//0974
int subarraysDivByK(int* A, int ASize, int K);
//1371
int findTheLongestSubstring(char *s);
//1431
bool* kidsWithCandies(int* candies, int candiesSize, int extraCandies, int* returnSize);


//ms064
int sumNums(int n);
#endif //LEETCODE_FUNCTIONS_H

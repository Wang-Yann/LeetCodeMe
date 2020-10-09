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

//0009
bool isPalindrome(int x);
//0010
bool isMatch(char * s, char * p);

//0014
char * longestCommonPrefix(char ** strs, int strsSize);
//0015
int **threeSum(int *nums, int numsSize, int *returnSize, int **returnColumnSizes);


//0016
int threeSumClosest(int* nums, int numsSize, int target);

//0020
bool isValid(char *s);

//0025
struct ListNode *reverseKGroup(struct ListNode *head, int k);

//0026
int nthUglyNumber(int n);

//0028
int strStr(char *haystack, char *needle);

//0041
int firstMissingPositive(int* nums, int numsSize);


//0050
double myPow(double x, int n);

//0065
bool isNumber(char *s);
//0067
char *addBinary(char *a, char *b);

//0069
int mySqrt(int x);

//0070
int climbStairs(int n);

//0076
char *minWindow(char *s, char *t);

//0084
int largestRectangleArea(int *heights, int heightsSize);

//0098
bool isValidBST(struct TreeNode *root);

//0101
bool isSymmetric(struct TreeNode *root);

//0102
int **levelOrder(struct TreeNode *root, int *returnSize, int **returnColumnSizes);

//0105
struct TreeNode *buildTree(int *preorder, int preorderSize, int *inorder, int inorderSize);

//0124

int maxPathSum(struct TreeNode* root);


//0125
bool isPalindrome1(char * s);

//0126
char ***findLadders(char *beginWord, char *endWord, char **wordList, int wordListSize,
                    int *returnSize, int **returnColumnSizes);

//0128
int longestConsecutive(int *nums, int numsSize);

//0136
int singleNumber(int *nums, int numsSize);

//0139
bool wordBreak(char * s, char ** wordDict, int wordDictSize);

//0152
int maxProduct(int *nums, int numsSize);

//0198
int rob(int *nums, int numsSize);

//0209
int minSubArrayLen(int s, int* nums, int numsSize);

//0210
int *findOrder(int numCourses, int **prerequisites, int prerequisitesSize, int *prerequisitesColSize, int *returnSize);

//0221
int maximalSquare(char **matrix, int matrixSize, int *matrixColSize);

//0236
struct TreeNode *lowestCommonAncestor(struct TreeNode *root, struct TreeNode *p, struct TreeNode *q);

//0238
int *productExceptSelf(int *nums, int numsSize, int *returnSize);

//0287
int findDuplicate(int *nums, int numsSize);

//0394
char *decodeString(char *s);

//0560
int subarraySum(int *nums, int numsSize, int k);

//0646
int findLongestChain(int **pairs, int pairsSize, int *pairsColSize);

//0680
bool validPalindrome(char *s);

//0739
int *dailyTemperatures(int *T, int TSize, int *returnSize);

//0837
double new21Game(int N, int K, int W);

//0974
int subarraysDivByK(int *A, int ASize, int K);

//0990
bool equationsPossible(char **equations, int equationsSize);

//1014
int maxScoreSightseeingPair(int* A, int ASize);
//1028
struct TreeNode* recoverFromPreorder(char * S);

//1300
int findBestValue(int* arr, int arrSize, int target);

//1371
int findTheLongestSubstring(char *s);

//1431
bool *kidsWithCandies(int *candies, int candiesSize, int extraCandies, int *returnSize);

//ms029
int *spiralOrder(int **matrix, int matrixSize, int *matrixColSize, int *returnSize);

//0046
int translateNum(int num);

//ms064
int sumNums(int n);

#endif //LEETCODE_FUNCTIONS_H

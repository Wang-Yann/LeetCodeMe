//
/* Created by rock on 5/24/20.
*/
#include "leetcode_functions.h"
//#define max(a,b) (((a) > (b)) ? (a) : (b))
//#define min(a,b) (((a) < (b)) ? (a) : (b))
//https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/4-xun-zhao-liang-ge-you-xu-shu-zu-de-zhong-wei-shu/
double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size){

    int n = nums1Size;
    int m = nums2Size;
    if (n > m) {
        return findMedianSortedArrays(nums2, nums2Size, nums1, nums1Size);
    }
    int LMax1, LMax2, RMin1, RMin2, c1, c2, lo = 0, hi = 2 * n;
    while (lo <= hi) {
        c1 = (lo + hi) >> 1;
        c2 = m + n - c1;

        LMax1 = (c1 == 0) ? INT_MIN : nums1[(c1 - 1) / 2];
        RMin1 = (c1 == 2 * n) ? INT_MAX : nums1[c1 / 2];
        LMax2 = (c2 == 0) ? INT_MIN : nums2[(c2 - 1) / 2];
        RMin2 = (c2 == 2 * m) ? INT_MAX : nums2[c2 / 2];

        if (LMax1 > RMin2) {
            hi = c1 - 1;
        } else if (LMax2 > RMin1) {
            lo = c1 + 1;
        } else {
            break;
        }

    }
    return (max(LMax1,LMax2) +  min(RMin1,RMin2))*0.5;


}
//
/* Created by rock on 4/28/20.
*/

#include "leetcode_functions.h"
#include "units_all.h"


START_TEST(t_findMedianSortedArrays)
{
    int res = myPow(2.0,10);
    int nums1[] = {1, 3};
    int nums2[] = {2};

    int nums3[] = {1, 2};
    int nums4[] = {3, 4};
    double res1 = findMedianSortedArrays(nums1, sizeof(nums1) / sizeof(int), nums2, sizeof(nums2) / sizeof(int));
    double res2 = findMedianSortedArrays(nums3, sizeof(nums3) / sizeof(int), nums4, sizeof(nums4) / sizeof(int));
    ck_assert_double_eq_tol(res1, 121.00,ELLIPSIS);
    ck_assert_double_eq_tol(res2,2.5,ELLIPSIS);
}
END_TEST

Suite *make_a_suite() {
    Suite *s = suite_create("t_findMedianSortedArrays");       // 建立Suite
    TCase *tc_add = tcase_create("t_findMedianSortedArrays");  // 建立测试用例集
    tcase_add_test(tc_add, t_findMedianSortedArrays);     // 测试用例加到测试集中
    suite_add_tcase(s, tc_add);           // 将测试用例加到Suite中
    return s;
}



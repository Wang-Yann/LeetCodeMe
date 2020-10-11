//
/* Created by rock on 4/27/20.
*/

#include "leetcode_functions.h"
#include "units_all.h"


START_TEST(t_0152) {
    int nums[] = {2, 3, -2, 4};
    int nums1[] = {-2, 0, -1};
    int nums2[] = {-4, -3};
    int result = maxProduct(nums, sizeof(nums) / sizeof(int));
    int result1 = maxProduct(nums1, sizeof(nums1) / sizeof(int));
    int result2 = maxProduct(nums2, sizeof(nums1) / sizeof(int));

    ck_assert_uint_eq(6, result);
    ck_assert_uint_eq(0, result1);
    ck_assert_uint_eq(12, result2);
}

END_TEST

Suite *make_a_suite() {
    Suite *s = suite_create("t_0152");       // 建立Suite
    TCase *tc_add = tcase_create("t_0152");  // 建立测试用例集
    suite_add_tcase(s, tc_add);           // 将测试用例加到Suite中
    tcase_add_test(tc_add, t_0152);     // 测试用例加到测试集中
    return s;
}

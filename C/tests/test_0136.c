//
/* Created by rock on 4/27/20.
*/

#include "leetcode_functions.h"
#include "units_all.h"


START_TEST(t_0136) {
    int nums[] = {2, 2, 1};
    int nums1[] = {4, 1, 2, 1, 2};
    int result = singleNumber(nums, sizeof(nums) / sizeof(int));
    int result1 = singleNumber(nums1, sizeof(nums1) / sizeof(int));

    ck_assert_uint_eq(1, result);
    ck_assert_uint_eq(4, result1);
}

END_TEST

Suite *make_a_suite() {
    Suite *s = suite_create("t_0136");       // 建立Suite
    TCase *tc_add = tcase_create("t_0136");  // 建立测试用例集
    suite_add_tcase(s, tc_add);           // 将测试用例加到Suite中
    tcase_add_test(tc_add, t_0136);     // 测试用例加到测试集中
    return s;
}

//
/* Created by rock on 4/27/20.
*/

#include "leetcode_functions.h"
#include "units_all.h"


START_TEST(t_0198) {
    int nums[] = {1, 2, 3, 1};
    int nums1[] = {2, 7, 9, 3, 1};
    int result = rob(nums, sizeof(nums) / sizeof(int));
    int result1 = rob(nums1, sizeof(nums1) / sizeof(int));

    ck_assert_uint_eq(result, 4);
    ck_assert_uint_eq(result1, 12);
}

END_TEST

Suite *make_a_suite() {
    Suite *s = suite_create("t_0198");       // 建立Suite
    TCase *tc_add = tcase_create("t_0198");  // 建立测试用例集
    suite_add_tcase(s, tc_add);           // 将测试用例加到Suite中
    tcase_add_test(tc_add, t_0198);     // 测试用例加到测试集中
    return s;
}


//
/* Created by rock on 4/27/20.
*/

#include "leetcode_functions.h"
#include "units_all.h"


START_TEST(t_0128) {
    int nums[] = {100, 4, 200, 1, 3, 2};
    int result = longestConsecutive(nums, sizeof(nums) / sizeof(int));

    ck_assert_uint_eq(4, result);
}

END_TEST

Suite *make_a_suite() {
    Suite *s = suite_create("t_0128");       // 建立Suite
    TCase *tc_add = tcase_create("t_0128");  // 建立测试用例集
    suite_add_tcase(s, tc_add);           // 将测试用例加到Suite中
    tcase_add_test(tc_add, t_0128);     // 测试用例加到测试集中
    return s;
}

//
/* Created by rock on 4/27/20.
*/

#include "leetcode_functions.h"
#include "units_all.h"


START_TEST(t_0209) {
    int nums[] = {2, 3, 1, 2, 4, 3};
    int s = 7;
    int result = minSubArrayLen(s, nums, sizeof(nums) / sizeof(int));
    ck_assert_uint_eq(result, 2);
}

END_TEST

Suite *make_a_suite() {
    Suite *s = suite_create("t_0209");       // 建立Suite
    TCase *tc_add = tcase_create("t_0209");  // 建立测试用例集
    suite_add_tcase(s, tc_add);           // 将测试用例加到Suite中
    tcase_add_test(tc_add, t_0209);     // 测试用例加到测试集中
    return s;
}


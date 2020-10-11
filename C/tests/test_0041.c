//
/* Created by rock on 4/28/20.
*/

#include "leetcode_functions.h"
#include "units_all.h"


START_TEST(t_firstMissingPositive)
    {
        int nums[] = {3, 4, -1, 1, -4};
        int res = firstMissingPositive(nums, sizeof(nums) / sizeof(int));
        ck_assert_uint_eq(res, 2);
    }
END_TEST

Suite *make_a_suite() {
    Suite *s = suite_create("t_firstMissingPositive");       // 建立Suite
    TCase *tc_add = tcase_create("t_firstMissingPositive");  // 建立测试用例集
    suite_add_tcase(s, tc_add);           // 将测试用例加到Suite中
    tcase_add_test(tc_add, t_firstMissingPositive);     // 测试用例加到测试集中
    return s;
}

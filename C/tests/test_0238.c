//
/* Created by rock on 4/27/20.
*/

#include "leetcode_functions.h"
#include "units_all.h"


START_TEST(t_0238) {
    int nums[] = {1, 2, 3, 4};
    int expected[] = {24, 12, 8, 6};
    int returnSize;
    int *result = productExceptSelf(nums, sizeof(nums) / sizeof(int), &returnSize);
    for (int i = 0; i < returnSize; ++i) {
        ck_assert_uint_eq(result[i], expected[i]);
    }
}

END_TEST

Suite *make_a_suite() {
    Suite *s = suite_create("t_0238");       // 建立Suite
    TCase *tc_add = tcase_create("t_0238");  // 建立测试用例集
    suite_add_tcase(s, tc_add);           // 将测试用例加到Suite中
    tcase_add_test(tc_add, t_0238);     // 测试用例加到测试集中
    return s;
}

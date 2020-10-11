//
/* Created by rock on 4/27/20.
*/

#include "leetcode_functions.h"
#include "units_all.h"


START_TEST(t_0739)
    {
        int nums[] = {73, 74, 75, 71, 69, 72, 76, 73};
        int expected[] = {1, 1, 4, 2, 1, 1, 0, 0};
        int returnSize;
        int* result = dailyTemperatures(nums, sizeof(nums) / sizeof(int),&returnSize);
        ck_assert_uint_eq(returnSize,sizeof(nums)/ sizeof(int));
        for (int i = 0; i < returnSize; ++i) {
            ck_assert_uint_eq(result[i], expected[i]);
        }
    }
END_TEST

Suite *make_a_suite() {
    Suite *s = suite_create("t_0739");       // 建立Suite
    TCase *tc_add = tcase_create("t_0739");  // 建立测试用例集
    suite_add_tcase(s, tc_add);           // 将测试用例加到Suite中
    tcase_add_test(tc_add, t_0739);     // 测试用例加到测试集中
    return s;
}


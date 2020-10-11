//
/* Created by rock on 4/27/20.
*/

#include "leetcode_functions.h"
#include <check.h>


START_TEST(test_myadd)
{
    int nums[4] = {2, 7, 11, 15};
    int target = 9;
    int numsSize = 4;
    int ret = 2;
    int *result = twoSum(nums, numsSize, target, &ret);
    fail_unless(*result == 15, "error, 102 + 103 != 105");
}

END_TEST

Suite *make_a_suite(void) {
    Suite *s;
    s = suite_create("TEST_MYADD");       // 建立Suite
    TCase *tc_core = tcase_create("t_myadd");  // 建立测试用例集
    tcase_add_test(tc_core, test_myadd);     // 测试用例加到测试集中
    suite_add_tcase(s, tc_core);           // 将测试用例加到Suite中
    return s;
}

//
/* Created by rock on 4/27/20.
*/

#include "leetcode_functions.h"
#include "units_all.h"


START_TEST(test_myadd)
    {
        int nums[4] = {2, 7, 11, 15};
        int target = 9;
        int numsSize = 4;
        int ret = 2;
        int *result = twoSum(nums, numsSize, target, &ret);
                fail_unless(*result == 5, "error, 102 + 103 != 105"); // "error, 2 + 3 != 5"是出错提示信息
    }
END_TEST
//
Suite *make_a_suite(void) {
    Suite *s = suite_create("myadd");       // 建立Suite
    TCase *tc_add = tcase_create("myadd");  // 建立测试用例集
    suite_add_tcase(s, tc_add);           // 将测试用例加到Suite中
    tcase_add_test(tc_add, test_myadd);     // 测试用例加到测试集中
    return s;
}
//
//int main(void) {
//    int n;
//    SRunner *sr;
//    sr = srunner_create(make_add_suite()); // 将Suite加入到SRunner
//    srunner_run_all(sr, CK_NORMAL);
//    n = srunner_ntests_failed(sr);         // 运行所有测试用例
//    srunner_free(sr);
//    return (n == 0) ? EXIT_SUCCESS : EXIT_FAILURE;
//}

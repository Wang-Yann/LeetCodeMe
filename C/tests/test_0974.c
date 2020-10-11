//
/* Created by rock on 4/27/20.
*/

#include "leetcode_functions.h"
#include "units_all.h"


START_TEST(t_0974)
    {
        int nums[] = {4,5,0,-2,-3,1};
        int result = subarraysDivByK(nums, sizeof(nums) / sizeof(int),5);

        ck_assert_uint_eq( result,7);
    }
END_TEST

Suite *make_a_suite() {
    Suite *s = suite_create("t_0974");       // 建立Suite
    TCase *tc_add = tcase_create("t_0974");  // 建立测试用例集
    suite_add_tcase(s, tc_add);           // 将测试用例加到Suite中
    tcase_add_test(tc_add, t_0974);     // 测试用例加到测试集中
    return s;
}

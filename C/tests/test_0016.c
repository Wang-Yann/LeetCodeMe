//
/* Created by rock on 4/28/20.
*/

#include "leetcode_functions.h"
#include "units_all.h"


START_TEST(tt_hreeSumClosest)
    {
        int nums[] = {-1,2,1,-4};
        int numSize = 4;
        int target = 1;
        int res = threeSumClosest(nums, numSize, target);

        ck_assert_uint_eq(res, 2);
    }
END_TEST

Suite *make_a_suite() {
    Suite *s = suite_create("tt_hreeSumClosest");       // 建立Suite
    TCase *tc_add = tcase_create("tt_hreeSumClosest");  // 建立测试用例集
    suite_add_tcase(s, tc_add);           // 将测试用例加到Suite中
    tcase_add_test(tc_add, tt_hreeSumClosest);     // 测试用例加到测试集中
    return s;
}

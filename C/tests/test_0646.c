//
/* Created by rock on 4/28/20.
*/


#include "leetcode_functions.h"
#include "units_all.h"


START_TEST(t_0646)
    {
        int pairs[3][2] = {{1, 2},
                           {2, 3},
                           {3, 4}};
        int *ptr[3];
        for (int i = 0; i < 3; i++) {
            ptr[i] = pairs[i];
        }
        int pairSize = 3;
        int pairsColSize = 2;
        int res = findLongestChain(ptr, pairSize, &pairsColSize);
        printf("Res:%d", res);
        ck_assert_uint_eq(res, 2);
    }
END_TEST

Suite *make_a_suite() {
    Suite *s = suite_create("t_0646");       // 建立Suite
    TCase *tc_add = tcase_create("t_0646");  // 建立测试用例集
    suite_add_tcase(s, tc_add);           // 将测试用例加到Suite中
    tcase_add_test(tc_add, t_0646);     // 测试用例加到测试集中
    return s;
}

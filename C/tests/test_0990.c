//
/* Created by rock on 4/27/20.
*/

#include "leetcode_functions.h"
#include "units_all.h"


START_TEST(t_1014)
    {
        char *equations[] = {"a==b", "b!=a"};
//    printf("Size:%d", sizeof(equations) / sizeof(char *));
    bool result = equationsPossible(equations, sizeof(equations) / sizeof(char *));
    ck_assert(!result);
    char *equations1[] = {"b==a", "a==b"};
    bool result1 = equationsPossible(equations1, sizeof(equations1) / sizeof(char *));
    ck_assert(result1);
    char *equations2[] = {"a==b", "b==c", "a==c"};
    bool result2 = equationsPossible(equations2, sizeof(equations2) / sizeof(char *));
    ck_assert(result2);
    char *equations3[] = {"a==b", "b!=c", "c==a"};
    bool result3 = equationsPossible(equations3, sizeof(equations3) / sizeof(char *));
    ck_assert(!result3);
    char *equations4[] = {"c==c", "b==d", "x!=z"};
    bool result4 = equationsPossible(equations4, sizeof(equations4) / sizeof(char *));
    ck_assert(result4);
    }
END_TEST

Suite *make_a_suite() {
    Suite *s = suite_create("t_1014");       // 建立Suite
    TCase *tc_add = tcase_create("t_1014");  // 建立测试用例集
    suite_add_tcase(s, tc_add);           // 将测试用例加到Suite中
    tcase_add_test(tc_add, t_1014);     // 测试用例加到测试集中
    return s;
}

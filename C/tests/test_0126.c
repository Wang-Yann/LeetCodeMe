//
/* Created by rock on 4/28/20.
*/

#include "leetcode_functions.h"
#include "units_all.h"


START_TEST(t_0126) {
    char *beginWord = (char *) "hit";
    char *endWord = (char *) "cog";
    char *wordList[] = {
            "hot", "dot", "dog", "lot", "log", "cog"
    };
    char *expectedList1[] = {"hit", "hot", "dot", "dog", "cog"};
    char *expectedList2[] = {"hit", "hot", "lot", "log", "cog"};
    char **expected[] = {expectedList1, expectedList2};
//    for (int i = 0; i < 2; ++i) {
//        for (int j = 0; j < 5; ++j) {
//            printf("Res:%s\n", expected[i][j]);
//        }
//    }
    int wordListSize = 6;
    int returnSize;
    int **returnColumnSizes = (int **) malloc(sizeof(int *) * 2);

    char ***result = findLadders(beginWord, endWord, wordList, wordListSize, &returnSize, returnColumnSizes);
    ck_assert(returnSize != 0);
//    ck_assert(&returnColumnSizes != NULL);
    ck_assert_uint_eq(returnSize, 2);
    ck_assert_uint_eq(**(returnColumnSizes), 5);
    for (int i = 0; i < returnSize; ++i) {
        for (int j = 0; j < **(returnColumnSizes); j++) {
            ck_assert(result[i][j]== expected[i][j]);
//            printf("Res:%s\n", result[i][j]);
        }
    }
}

END_TEST

Suite *make_a_suite() {
    Suite *s = suite_create("t_0126");       // 建立Suite
    TCase *tc_add = tcase_create("t_0126");  // 建立测试用例集
    suite_add_tcase(s, tc_add);           // 将测试用例加到Suite中
    tcase_add_test(tc_add, t_0126);     // 测试用例加到测试集中
    return s;
}


//
/* Created by rock on 4/28/20.
*/

#include "gtest/gtest.h"

extern "C"
{
#include "leetcode_functions.h"

}



TEST(findLadders, test1) {
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
    ASSERT_TRUE(returnSize != 0);
//    ASSERT_TRUE(&returnColumnSizes != NULL);
    ASSERT_EQ(returnSize, 2);
    ASSERT_EQ(**(returnColumnSizes), 5);
    for (int i = 0; i < returnSize; ++i) {
        for (int j = 0; j < **(returnColumnSizes); j++) {
            ASSERT_EQ(result[i][j], expected[i][j]);
//            printf("Res:%s\n", result[i][j]);
        }
    }

}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}

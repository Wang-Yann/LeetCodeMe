//
/* Created by rock on 4/28/20.
*/

#include "gtest/gtest.h"

extern "C"
{
#include "leetcode_functions.h"

}


TEST(findOrder, test1) {
    int row1[] = {1, 0};
    int *prerequisites[] = {row1};
    int prerequisitesSize = 1;
    int prerequisitesColSize[] = {2};
    int numCourses = 2;
    int returnSize = 2;
    int *res = findOrder(numCourses, prerequisites, prerequisitesSize, prerequisitesColSize, &returnSize);
//    printf("Res:%d", res[0]);
    int expected[] = {0, 1};
    ASSERT_EQ(sizeof(expected), sizeof(res));
    for (int i = 0; i < returnSize; ++i) {
        ASSERT_EQ(res[i], expected[i]);
    }
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}

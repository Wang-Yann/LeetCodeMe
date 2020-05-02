//
/* Created by rock on 4/28/20.
*/

#include "gtest/gtest.h"
extern "C"
{
#include "leetcode_functions.h"

}


TEST(findLongestChainTest, test1) {
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
    ASSERT_EQ(res, 2);
}

//int main(int argc, char **argv) {
//    ::testing::InitGoogleTest(&argc, argv);
//    return RUN_ALL_TESTS();
//}

//
/* Created by rock on 4/27/20.
*/
#include "gtest/gtest.h"

extern "C"
{
#include "leetcode_functions.h"

}


TEST(maxScoreSightseeingPair, test1) {
    int A[] = {8,1,5,2,6};
    int result = maxScoreSightseeingPair(A, sizeof(A) / sizeof(int));

    ASSERT_EQ( result,11);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}

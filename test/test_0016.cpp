//
/* Created by rock on 4/28/20.
*/

#include "gtest/gtest.h"

extern "C"
{
#include "leetcode_functions.h"

}


TEST(threeSumClosest, test1) {
    int nums[] = {-1,2,1,-4};
    int numSize = 4;
    int target = 1;
    int res = threeSumClosest(nums, numSize, target);

    ASSERT_EQ(res, 2);

}


int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
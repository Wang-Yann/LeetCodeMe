//
/* Created by rock on 4/28/20.
*/

#include "gtest/gtest.h"

extern "C"
{
#include "leetcode_functions.h"

}


TEST(findMedianSortedArrays, test1) {
    int res = myPow(2.0,10);
    int nums1[] = {1, 3};
    int nums2[] = {2};

    int nums3[] = {1, 2};
    int nums4[] = {3, 4};
    double res1 = findMedianSortedArrays(nums1, sizeof(nums1) / sizeof(int), nums2, sizeof(nums2) / sizeof(int));
    double res2 = findMedianSortedArrays(nums3, sizeof(nums3) / sizeof(int), nums4, sizeof(nums4) / sizeof(int));
    ASSERT_DOUBLE_EQ(res1, 2.00);
    ASSERT_DOUBLE_EQ(res2,2.5);
}



int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}

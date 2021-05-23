package com.rock.ltc;

import com.rock.ltc.utils.TreeNode;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

import java.util.Arrays;
import java.util.stream.Stream;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;

/**
 * @Author: Rock
 * @Date: 2021-05-17 22:22
 * @Description:
 */
public class SolutionFrom1000Test {
    
    private static final Solution1035 solution1035 = new Solution1035();
    private static final Solution1707 solution1707 = new Solution1707();
    
    static Stream<Arguments> testSolution1035() {
        return Stream.of(
                Arguments.of(new int[]{1, 4, 2}, new int[]{1, 2, 4}, 2),
                Arguments.of(new int[]{2, 5, 1, 2, 5}, new int[]{10, 5, 2, 1, 5, 2}, 3),
                Arguments.of(new int[]{1, 3, 7, 1, 7, 5}, new int[]{1, 9, 2, 5, 1}, 2)
        );
    }
    
    @ParameterizedTest
    @MethodSource
    void testSolution1035(int[] nums1, int[] nums2, int res) {
        assertEquals(solution1035.maxUncrossedLines(nums1, nums2), res);
        
    }
    
    
    static Stream<Arguments> testSolution1707() {
        return Stream.of(
                Arguments.of(new int[]{0, 1, 2, 3, 4},
                        new int[][]{new int[]{3, 1}, new int[]{1, 3}, new int[]{5, 6}},
                        new int[]{3, 3, 7}),
                
                Arguments.of(new int[]{5, 2, 4, 6, 6, 3},
                        new int[][]{new int[]{12, 4}, new int[]{8, 1}, new int[]{6, 3}},
                        new int[]{15, -1, 5})
        );
    }
    
    @ParameterizedTest
    @MethodSource
    void testSolution1707(int[] nums, int[][] queries, int[] res) {
        assertArrayEquals(solution1707.maximizeXor(nums, queries), res);
    }
    
    
}

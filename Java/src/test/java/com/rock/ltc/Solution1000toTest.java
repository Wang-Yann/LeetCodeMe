package com.rock.ltc;

import com.rock.ltc.utils.TreeNode;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.Arguments;
import org.junit.jupiter.params.provider.MethodSource;

import java.util.stream.Stream;

import static org.junit.jupiter.api.Assertions.assertEquals;

/**
 * @Author: Rock
 * @Date: 2021-05-17 22:22
 * @Description:
 */
public class Solution1000toTest {
    static Stream<Arguments> testSolution() {
        return Stream.of(
                Arguments.of(new int[]{0, 1, 3, 5, 6, 8, 12, 17}, true),
                Arguments.of(new int[]{0, 1, 2, 3, 4, 8, 9, 11}, false)
        );
    }
    
    @ParameterizedTest
    @MethodSource
    void testSolution(int[] stones, Boolean res) {
    }
    
    
}

package org.minions.common.utils;

import org.minions.common.constant.Constant;

import javax.validation.constraints.NotNull;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class StringUtil {
    public static boolean isEmpty(String value) {
        if (value == null || value.length() == 0) {
            return false;
        }
        return true;
    }

    public static boolean equals(String value, String anotherValue) {
        if (value == null || anotherValue == null) {
            return false;
        }
        return value.equals(anotherValue);
    }

    public static String concat(String... values) {
        if (null == values) {
            return Constant.BLACK;
        }

        return String.join(Constant.BLACK, values);
    }

    public static boolean fuzzyMatch(@NotNull String separate, @NotNull String matchValue, @NotNull String anotherValue) {
        List<String> matchValues = Arrays.stream(matchValue.split(separate)).collect(Collectors.toList());
        List<String> anotherValues = Arrays.stream(anotherValue.split(separate)).collect(Collectors.toList());
        matchValues.retainAll(anotherValues);
        return matchValues.size() > 0 ? true : false;
    }
}

package org.minions.common.utils

import org.minions.common.constant.Constant
import java.util.*
import java.util.stream.Collectors


class StringUtil {
    companion object {

        fun isEmpty(value: String?): Boolean {
            return value == null || value.isEmpty()
        }

        fun equals(value: String?, anotherValue: String?): Boolean {
            return if (value == null || anotherValue == null) {
                false
            } else value == anotherValue
        }

        fun concat(vararg values: String?): String? {
            return java.lang.String.join(Constant.BLACK, *values)
        }

        fun fuzzyMatch(separate: String, matchValue: String, anotherValue: String): Boolean {
            val matchValues = Arrays.stream(matchValue.split(separate).toTypedArray()).collect(Collectors.toSet())
            val anotherValues = Arrays.stream(anotherValue.split(separate).toTypedArray()).collect(Collectors.toSet())
            matchValues.retainAll(anotherValues)
            return matchValues.size > 0
        }
    }

}
package org.minions.common.utils

import org.junit.jupiter.api.Assertions.*
import org.spekframework.spek2.Spek
import org.spekframework.spek2.style.gherkin.Feature

class UtilFeature : Spek({

    Feature("test string utils") {
        Scenario("test is empty") {
            var value: String = ""
            When("empty") {
                value = ""
            }

            Then("result is true") {
                assertEquals(true, StringUtil.isEmpty(value), "value: ${value} empty is ture")
            }

            When("not empty") {
                value = "aa"
            }

            Then("result is false") {
                assertEquals(false, StringUtil.isEmpty(value), "value: ${value} empty is false")
            }
        }

        Scenario("test equals") {
            var string1 = ""
            var string2 = ""
            When("equal") {
            }
            Then("result is true") {
                assertEquals(true, StringUtil.equals(string1, string2))
            }

            When("not equal") {
                string2 = "aa"
            }
            Then("resule is false") {
                assertEquals(false, StringUtil.equals(string1, string2))
            }
        }
    }
})
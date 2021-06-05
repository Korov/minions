package org.minions.common.utils

import spock.lang.Specification

/**
 * @author zhu.lei* @date 2021-03-13 03:33
 */
/*class CollectionsUtilTest extends Specification {

    def setup() {
        println("setup")
    }

    def "test isEmpty"() {
        given:
        def list;
        when:
        list = new ArrayList()
        then:
        CollectionsUtil.isEmpty(list)

        when:
        list.add("aaa")
        then:
        !CollectionsUtil.isEmpty(notEmptyList)
    }

    def "test isEmpty1"() {
        expect:
        CollectionsUtil.isEmpty(list) == isTrue

        where:
        list      | isTrue
        null      | true
        []        | true
        [1, 2, 3] | false
    }

    def "maximum of two numbers"() {
        expect:
        Math.max(a as int, b as int) == c

        where:
        a << [3, 5, 9]
        b << [7, 4, 9]
        c << [7, 5, 9]
    }

    def "maximum of two numbers1"() {
        def value = 1

        when:
        value == 1

        then:
        println("first")

        then:
        println("second")
    }

    def cleanup() {
        println 'clean up'
    }
}*/


abstract class BaseSpec extends Specification {
    private static final long serialVersionUID = 123456L
    def x = { println 'base field initializer' }()

    def setupSpec() { println 'base setupSpec()' }

    def cleanupSpec() { println 'base cleanupSpec()' }

    def setup() { println 'base setup()' }

    def cleanup() { println 'base cleanup()' }

    def baseSpecMethod() {
        setup:
        println 'base spec method'
    }
}

class DerivedSpec extends BaseSpec {
    private static final long serialVersionUID = 1234567L
    def y = { println 'derived field initializer' }()

    def setupSpec() { println 'derived setupSpec()' }

    def cleanupSpec() { println 'derived cleanupSpec()' }

    def setup() { println 'derived setup()' }

    def cleanup() { println 'derived cleanup()' }

    def derivedSpecMethod() {
        setup:
        println 'derived spec method'
    }
}

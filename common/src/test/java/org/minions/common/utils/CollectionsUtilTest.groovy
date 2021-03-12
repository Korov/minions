package org.minions.common.utils

import spock.lang.Specification

/**
 * @author zhu.lei* @date 2021-03-13 03:33
 */
class CollectionsUtilTest extends Specification {
    def "test isEmpty"() {
        given:
        def emptyList = new ArrayList();
        def notEmptyList = new ArrayList();
        when:
        notEmptyList.add("aaa")
        then:
        CollectionsUtil.isEmpty(emptyList)
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
}

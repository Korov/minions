package org.minions.demo.mapper

import groovy.util.logging.Slf4j
import org.minions.common.model.demo.Demo
import org.minions.demo.DemoApplicationTest
import org.springframework.beans.factory.annotation.Autowired

/**
 * @author zhu.lei
 * @date 2021-09-06 12:44
 */
@Slf4j
class DemoMapperTest extends DemoApplicationTest {

    @Autowired
    DemoMapper demoMapper

    def "test select"() {
        def result = new Demo()
        result.id = 1
        result.name = "minions"

        when:
        def id = 1

        then:
        Demo demo = demoMapper.selectById(id)
        log.info("query result:{}", demo.toString())

        expect:
        result == demo
    }
}

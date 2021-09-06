package org.minions.demo

import groovy.util.logging.Slf4j
import org.junit.jupiter.api.Test
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc
import org.springframework.boot.test.context.SpringBootTest
import org.springframework.test.web.servlet.MockMvc
import spock.lang.Specification

/**
 * ./gradlew :demo:test --tests "org.minions.demo.DemoApplicationTest.contextLoader"
 * @author zhu.lei* @date 2021-03-13 03:00
 */
@Slf4j
@AutoConfigureMockMvc
@SpringBootTest
class DemoApplicationTest extends Specification {
    @Autowired
    protected MockMvc mockMvc;

    def "application start success"() {
        expect: "the MockMvc is created"
        mockMvc
        log.info("start success")
    }
}

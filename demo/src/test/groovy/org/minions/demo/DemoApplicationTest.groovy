package org.minions.demo

import org.junit.jupiter.api.Test
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc
import org.springframework.boot.test.context.SpringBootTest
import org.springframework.test.web.servlet.MockMvc
import spock.lang.Specification

/**
 * @author zhu.lei* @date 2021-03-13 03:00
 */
@AutoConfigureMockMvc
@SpringBootTest
class DemoApplicationTest extends Specification {
    @Autowired
    protected MockMvc mockMvc;

    @Test
    def "application start success"() {
        expect: "the MockMvc is created"
        mockMvc
    }
}

package org.minions.demo.controller

import com.fasterxml.jackson.databind.JsonNode
import org.junit.jupiter.api.Assertions
import org.minions.common.utils.JsonUtil
import org.minions.demo.DemoApplicationTest
import org.springframework.test.web.servlet.request.MockMvcRequestBuilders
import org.springframework.test.web.servlet.result.MockMvcResultHandlers
import org.springframework.test.web.servlet.result.MockMvcResultMatchers

/**
 * @author zhu.lei* @date 2021-03-13 03:22
 */
class DemoControllerTest extends DemoApplicationTest {

    def "test getDemo"() {
        expect: "Status is 200 and the response is 'Hello world!'"
        String response = mockMvc.perform(MockMvcRequestBuilders.get("/demo/get/1"))
                .andExpect(MockMvcResultMatchers.status().isOk())
                .andDo(MockMvcResultHandlers.print())
                .andReturn().getResponse().getContentAsString()
        JsonNode resultVo = JsonUtil.jsonToNode(response)

        Assertions.assertEquals(1, resultVo.get("code").asInt())
    }
}

package org.minions.kafka.controller;

import com.fasterxml.jackson.databind.JsonNode;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import org.minions.common.utils.JsonUtil;
import org.minions.kafka.KafkaConsumersTest;
import org.springframework.test.web.servlet.request.MockMvcRequestBuilders;
import org.springframework.test.web.servlet.result.MockMvcResultHandlers;
import org.springframework.test.web.servlet.result.MockMvcResultMatchers;

/**
 * @author korov
 */
public class HeroControllerTest extends KafkaConsumersTest {

    @Test
    void getHeros() throws Exception {
        String response = mockMvc.perform(MockMvcRequestBuilders.get("/kafka/hero"))
                .andExpect(MockMvcResultMatchers.status().isOk())
                .andDo(MockMvcResultHandlers.print())
                .andReturn().getResponse().getContentAsString();
        JsonNode resultVo = JsonUtil.jsonToNode(response);
        Assertions.assertEquals(1, resultVo.get("code").asInt());
    }
}
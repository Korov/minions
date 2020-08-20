package org.minions.demo.controller;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import org.minions.demo.TestAnnotation;
import org.springframework.test.web.servlet.request.MockMvcRequestBuilders;
import org.springframework.test.web.servlet.result.MockMvcResultHandlers;
import org.springframework.test.web.servlet.result.MockMvcResultMatchers;


class DemoControllerTest extends TestAnnotation {
    @Test
    void getDemo() throws Exception {
        String response = mockMvc.perform(MockMvcRequestBuilders.get("/demo/get/1"))
                .andExpect(MockMvcResultMatchers.status().isOk())
                .andDo(MockMvcResultHandlers.print())
                .andReturn().getResponse().getContentAsString();
        JSONObject resultVo = JSON.parseObject(response);
        Assertions.assertEquals(1, resultVo.get("code"));
    }
}
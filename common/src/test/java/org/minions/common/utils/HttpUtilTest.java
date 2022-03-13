package org.minions.common.utils;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.JsonNode;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

/**
 * Http测试
 *
 * @author korov
 * @date 2020/10/3
 */
class HttpUtilTest {

    @Disabled
    @Test
    void httpPostConnect() throws JsonProcessingException {
        JsonNode result = HttpUtil.postSpider("172.16.193.141", 6800, "test", "hero");
        System.out.println(JsonUtil.objectToJson(result, JsonUtil.SNAKE_CASE_MAPPER));
    }
}
package org.minions.common.utils;

import com.alibaba.fastjson.JSONObject;
import org.junit.jupiter.api.Test;

/**
 * Http测试
 *
 * @author korov
 * @date 2020/10/3
 */
class HttpUtilTest {

    @Test
    void httpPostConnect() {
        JSONObject result = HttpUtil.postSpider("172.16.193.141", 6800, "test", "hero");
        System.out.println(result.toJSONString());
    }
}
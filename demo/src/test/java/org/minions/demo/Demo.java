package org.minions.demo;

import com.alibaba.fastjson.JSONValidator;
import org.junit.jupiter.api.Test;

/**
 * @author korov
 * @date 2020/11/1
 */
public class Demo {
    /**
     * fastjsonVersion = "1.2.73"
     * https://github.com/alibaba/fastjson/issues/3510
     */
    @Test
    public void test() {
        String content = "{\"a\":\"b\" \"c\":\"d\"}";
        JSONValidator jsonValidator = JSONValidator.from(content);
        boolean isValid = jsonValidator.validate();
        System.out.println(isValid); // isValid = false
    }
}

package org.minions.demo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.web.servlet.MockMvc;

/**
 * TODO
 *
 * @author korov
 * @date 2020/8/19
 */
@AutoConfigureMockMvc
@SpringBootTest
public class TestAnnotation {
    @Autowired
    protected MockMvc mockMvc;
}

package org.minions.kafka;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.web.servlet.MockMvc;

/**
 * @author korov
 */
@SpringBootTest
@AutoConfigureMockMvc
public class KafkaConsumersTest {
    @Autowired
    protected MockMvc mockMvc;
    @Test
    public void loadContext() {
        System.out.println("Applications start success!");
    }
}
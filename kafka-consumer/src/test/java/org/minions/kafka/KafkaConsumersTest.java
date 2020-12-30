package org.minions.kafka;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.kafka.test.context.EmbeddedKafka;
import org.springframework.test.web.servlet.MockMvc;

/**
 * @author korov
 */
@SpringBootTest
@AutoConfigureMockMvc
@EmbeddedKafka(partitions = 10, brokerProperties = {"listeners=PLAINTEXT://localhost:9093", "port=9092"})
public class KafkaConsumersTest {
    protected MockMvc mockMvc;

    @Autowired
    public void setMockMvc(MockMvc mockMvc) {
        this.mockMvc = mockMvc;
    }

    @Test
    public void loadContext() {
        System.out.println("Applications start success!");
    }
}
package org.minions.demo;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.web.servlet.MockMvc;

@AutoConfigureMockMvc
@SpringBootTest
public class DemoApplicationTest {
    @Autowired
    protected MockMvc mockMvc;

    @Test
    public void loadContext() {
        System.out.println("Application start success!");
    }
}
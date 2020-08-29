package org.minions.kafka;

import lombok.extern.slf4j.Slf4j;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import springfox.documentation.swagger2.annotations.EnableSwagger2;

/**
 * TODO
 *
 * @author korov
 * @date 2020/8/29
 */
@EnableSwagger2
@SpringBootApplication
@Slf4j
public class KafkaConsumers {
    public static void main(String[] args) {
        SpringApplication.run(KafkaConsumers.class, args);
    }
}
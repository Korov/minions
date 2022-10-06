package org.minions.kafka;

import org.minions.kafka.mapper.MarkMapper;
import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.scheduling.annotation.EnableScheduling;

/**
 * @author korov
 */
@EnableScheduling
@SpringBootApplication
@MapperScan(basePackageClasses = {MarkMapper.class})
public class KafkaConsumers {
    public static void main(String[] args) {
        SpringApplication.run(KafkaConsumers.class, args);
    }
}
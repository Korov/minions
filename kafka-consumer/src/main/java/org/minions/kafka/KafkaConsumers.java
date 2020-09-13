package org.minions.kafka;

import org.minions.kafka.mapper.MarkMapper;
import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import springfox.documentation.swagger2.annotations.EnableSwagger2;

/**
 * @author korov
 * @date 2020/8/29
 */
@EnableSwagger2
@SpringBootApplication
@MapperScan(basePackageClasses = {MarkMapper.class})
public class KafkaConsumers {
    public static void main(String[] args) {
        SpringApplication.run(KafkaConsumers.class, args);
    }
}
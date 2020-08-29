package org.minions.kafka.consumer;

import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Component;

import java.util.Optional;

/**
 * @author korov
 */
@Component
public class HeroConsumer {
    private static final Logger logger = LoggerFactory.getLogger(HeroConsumer.class);

    /**
     * 会根据id生成一个消费者信息存储在kafka端
     */
    @KafkaListener(id = "minions01", topics = "heros", containerFactory = "kafkaListenerContainerFactory")
    public static void listen(ConsumerRecord<?, ?> record) {
        Optional<?> kafkaMessage = Optional.ofNullable(record.value());
        if (kafkaMessage.isPresent()) {
            Object message = kafkaMessage.get();
            logger.info("listen consumer the message. record: {}, message: {}!", record, message);
        }
    }
}

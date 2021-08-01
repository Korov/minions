package org.minions.kafka.kafkatest;

import lombok.extern.slf4j.Slf4j;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;
import org.minions.kafka.KafkaConsumersTest;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.kafka.support.SendResult;
import org.springframework.util.concurrent.ListenableFuture;
import org.springframework.util.concurrent.ListenableFutureCallback;

/**
 * @author zhu.lei
 */
@Slf4j
public class EmbeddedKafkaTest extends KafkaConsumersTest {
    private KafkaTemplate<String, String> kafkaTemplate;

    @Autowired
    public void setKafkaTemplate(KafkaTemplate<String, String> kafkaTemplate) {
        this.kafkaTemplate = kafkaTemplate;
    }

    @Disabled
    @Test
    public void sendMsg() {
        ListenableFuture<SendResult<String, String>> future = kafkaTemplate
                .send("hero", "test", "time: " + System.currentTimeMillis());
        future.addCallback(new ListenableFutureCallback<>() {

            @Override
            public void onFailure(Throwable throwable) {
                log.error("onFailure", throwable);
            }

            @Override
            public void onSuccess(SendResult<String, String> stringStringSendResult) {
                log.info("onSuccess {}", stringStringSendResult);
            }
        });
    }
}

package org.minions.kafka.consumer;

import com.alibaba.fastjson.JSONObject;
import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.minions.common.dto.kafka.HeroInfoDTO;
import org.minions.common.model.kafka.HeroInfoModel;
import org.minions.kafka.mapper.HeroInfoMapper;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Component;

import java.util.Optional;

/**
 * @author korov
 */
@Component
public class HeroConsumer {
    private static final Logger logger = LoggerFactory.getLogger(HeroConsumer.class);

    @Autowired
    private HeroInfoMapper heroInfoMapper;

    /**
     * 会根据id生成一个消费者信息存储在kafka端
     */
    @KafkaListener(id = "minions01", topics = "hero", containerFactory = "kafkaListenerContainerFactory")
    public void listen(ConsumerRecord<?, ?> record) {
        Optional<?> kafkaMessage = Optional.ofNullable(record.value());
        if (kafkaMessage.isPresent()) {
            String message = kafkaMessage.get().toString();
            HeroInfoDTO infoDTO = JSONObject.parseObject(message, HeroInfoDTO.class);
            HeroInfoModel infoModel = infoDTO.getInfo();
            heroInfoMapper.insert(infoModel);
            logger.info("listen consumer the message. record: {}, message: {}!", record, message);
        }

    }
}

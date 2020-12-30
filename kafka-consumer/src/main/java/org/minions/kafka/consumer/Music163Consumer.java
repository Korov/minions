package org.minions.kafka.consumer;

import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.minions.common.model.kafka.MusicRaw;
import org.minions.kafka.mapper.MusicRawMapper;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Component;

import java.util.Optional;

/**
 * TODO
 *
 * @author korov
 */
@Component
public class Music163Consumer {
    private static final Logger logger = LoggerFactory.getLogger(HeroConsumer.class);

    private MusicRawMapper musicRawMapper;

    @Autowired
    public void setMusicRawMapper(MusicRawMapper musicRawMapper) {
        this.musicRawMapper = musicRawMapper;
    }

    @KafkaListener(id = "minions_music_01", topics = "music_163", containerFactory = "kafkaListenerContainerFactory")
    public void listen(ConsumerRecord<String, String> record) {
        Optional<String> kafkaMessage = Optional.ofNullable(record.value());
        String key = record.key();
        if (kafkaMessage.isPresent()) {
            String message = kafkaMessage.get();
            MusicRaw musicRaw = new MusicRaw();
            musicRaw.setSongId(key);
            musicRaw.setComments(message);
            musicRawMapper.insert(musicRaw);
            logger.info("listen consumer the message. key: {}, message: {}!", record.key(), message);
        }

    }

}

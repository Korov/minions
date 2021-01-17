package org.minions.kafka.consumer;

import org.apache.kafka.clients.consumer.ConsumerRecord;
import org.minions.common.model.mongo.MusicComment;
import org.minions.kafka.dao.MusicCommentDao;
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

    private MusicCommentDao musicCommentDao;

    @Autowired
    public void setMusicCommentDao(MusicCommentDao musicCommentDao) {
        this.musicCommentDao = musicCommentDao;
    }

    @KafkaListener(id = "minions_music01", topics = "music_163", containerFactory = "kafkaListenerContainerFactory")
    public void listen(ConsumerRecord<String, String> record) {
        Optional<String> kafkaMessage = Optional.ofNullable(record.value());
        String key = record.key();
        if (kafkaMessage.isPresent()) {
            String message = kafkaMessage.get();
            MusicComment musicComment = new MusicComment();
            musicComment.setSongId(key);
            musicComment.setComment(message);
            musicCommentDao.saveDemo(musicComment);
            logger.info("listen consumer the message. key: {}, message: {}!", record.key(), message);
        }

    }

}

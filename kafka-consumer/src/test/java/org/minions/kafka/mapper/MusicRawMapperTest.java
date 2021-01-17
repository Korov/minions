package org.minions.kafka.mapper;

import org.junit.jupiter.api.Test;
import org.minions.common.model.kafka.MusicRaw;
import org.minions.kafka.KafkaConsumersTest;
import org.springframework.beans.factory.annotation.Autowired;

class MusicRawMapperTest extends KafkaConsumersTest {

    @Autowired
    private MusicRawMapper musicRawMapper;



    @Test
    void insert() {
        MusicRaw musicRaw = new MusicRaw();
        musicRaw.setSongId("111111");
        musicRaw.setComments("test");
        musicRawMapper.insert(musicRaw);
    }
}
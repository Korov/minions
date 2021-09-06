package org.minions.kafka.mapper;

import org.junit.jupiter.api.Test;
import org.minions.common.model.kafka.HeroInfos;
import org.minions.kafka.KafkaConsumersTest;
import org.springframework.beans.factory.annotation.Autowired;

/**
 * @author korov
 */
public class HeroInfoMapperTest extends KafkaConsumersTest {

    @Autowired
    private HeroInfosMapper mapper;

    @Test
    void selectByPrimaryKey() {
        HeroInfos heroInfoModel = mapper.selectById(1);
        System.out.println(heroInfoModel.getHeroName());
    }
}
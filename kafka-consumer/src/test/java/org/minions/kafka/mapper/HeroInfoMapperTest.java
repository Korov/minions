package org.minions.kafka.mapper;

import org.junit.jupiter.api.Test;
import org.minions.common.model.kafka.HeroInfoModel;
import org.minions.kafka.KafkaConsumersTest;
import org.springframework.beans.factory.annotation.Autowired;

/**
 * @author korov
 * @date 2020/9/13
 */
public class HeroInfoMapperTest extends KafkaConsumersTest {

    @Autowired
    private HeroInfoMapper mapper;

    @Test
    void selectByPrimaryKey() {
        HeroInfoModel heroInfoModel = mapper.selectByPrimaryKey(1);
        System.out.println(heroInfoModel.getHeroName());
    }
}
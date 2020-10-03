package org.minions.kafka.schedule;

import org.junit.jupiter.api.Test;
import org.minions.kafka.KafkaConsumersTest;
import org.springframework.beans.factory.annotation.Autowired;

/**
 * TODO
 *
 * @author korov
 * @date 2020/10/3
 */
class HeroScheduleTest extends KafkaConsumersTest {
    @Autowired
    private HeroSchedule heroSchedule;

    @Test
    void spiderHero() {
        heroSchedule.spiderHero();
    }
}
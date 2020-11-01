package org.minions.kafka.schedule;

import org.springframework.context.annotation.Profile;
import org.springframework.scheduling.annotation.Scheduled;
import org.springframework.stereotype.Component;

/**
 * @author korov
 * @date 2020/10/3
 */
@Component
@Profile({"dev", "test"})
public class HeroSchedule {
    @Scheduled(cron = "0 0/2 8-20 * * ?")
    public void spiderHero() {
        //HttpUtil.postSpider(host, port, "test", "hero");
    }
}

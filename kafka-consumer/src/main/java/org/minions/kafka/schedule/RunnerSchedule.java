package org.minions.kafka.schedule;

import com.alibaba.fastjson.JSONObject;
import lombok.extern.slf4j.Slf4j;
import org.minions.common.utils.HttpUtil;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.ApplicationArguments;
import org.springframework.boot.ApplicationRunner;
import org.springframework.stereotype.Component;

/**
 * 项目启动之后执行的方法
 *
 * @author korov
 * @date 2020/10/3
 */
@Slf4j
@Component
public class RunnerSchedule implements ApplicationRunner {
    @Value("${minions.spider.host}")
    private String host;
    @Value("${minions.spider.port}")
    private int port;
    @Value("${minions.spider.project}")
    private String project;

    @Override
    public void run(ApplicationArguments args) throws Exception {
        JSONObject result = HttpUtil.postSpider(host, port, project, "hero");
        log.info(result.toJSONString());
    }
}

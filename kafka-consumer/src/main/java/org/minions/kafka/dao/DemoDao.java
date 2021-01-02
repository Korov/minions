package org.minions.kafka.dao;

import org.minions.common.model.mongo.DemoEntity;

/**
 * TODO
 *
 * @author korov
 * @date 2021/1/3
 */
public interface DemoDao {
    void saveDemo(DemoEntity demoEntity);

    void removeDemo(Long id);

    void updateDemo(DemoEntity demoEntity);

    DemoEntity findDemoById(Long id);
}

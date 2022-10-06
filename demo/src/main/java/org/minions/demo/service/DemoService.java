package org.minions.demo.service;

import org.minions.common.model.demo.Demo;

public interface DemoService {
    Demo queryDemoById(Integer id);

    void testTransaction(String name) throws Exception;
}

package org.minions.demo.service.impl;

import org.minions.common.model.demo.Demo;
import org.minions.demo.mapper.DemoMapper;
import org.minions.demo.service.DemoService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class DemoServiceImpl implements DemoService {
    private DemoMapper demoMapper;

    @Autowired
    public void setDemoMapper(DemoMapper demoMapper) {
        this.demoMapper = demoMapper;
    }

    @Override
    public Demo queryDemoById(Integer id) {
        return demoMapper.selectByPrimaryKey(id);
    }
}

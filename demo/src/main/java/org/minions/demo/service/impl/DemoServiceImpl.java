package org.minions.demo.service.impl;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import org.minions.common.model.demo.Demo;
import org.minions.demo.mapper.DemoMapper;
import org.minions.demo.service.DemoService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
public class DemoServiceImpl implements DemoService {
    private static final Logger log = LoggerFactory.getLogger(DemoService.class);

    private DemoMapper demoMapper;

    @Autowired
    public void setDemoMapper(DemoMapper demoMapper) {
        this.demoMapper = demoMapper;
    }

    @Override
    public Demo queryDemoById(Integer id) {
        return demoMapper.selectById(id);
    }

    @Transactional(rollbackFor = Exception.class)
    @Override
    public void testTransaction(String name) throws Exception {
        QueryWrapper<Demo> queryWrapper = new QueryWrapper<>();
        queryWrapper.eq(Demo.NAME, name);
        Demo dbDemo = demoMapper.selectOne(queryWrapper);
        if (dbDemo == null) {
            Demo demo = new Demo();
            demo.setName(name);
            int insertCount = demoMapper.insert(demo);
            log.info("insert count:{}, demo:{}", insertCount, demo);
        } else {
            log.info("demo name:{} exists", name);
        }

        dbDemo = demoMapper.selectOne(queryWrapper);
        log.info("db demo:{}", dbDemo);
        int deleteCount = demoMapper.delete(queryWrapper);
        log.info("delete count:{}", deleteCount);
        dbDemo = demoMapper.selectOne(queryWrapper);
        if (dbDemo == null) {
            log.info("demo name:{} has been deleted", name);
            // throw new Exception("error");
        } else {
            log.info("delete db demo:{} failed", dbDemo);
        }
    }
}

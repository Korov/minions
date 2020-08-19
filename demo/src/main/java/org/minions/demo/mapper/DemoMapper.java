package org.minions.demo.mapper;

import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.minions.common.model.demo.Demo;

import java.util.List;

@Mapper
public interface DemoMapper {
    int deleteByPrimaryKey(Integer id);

    int insert(Demo record);

    int insertSelective(Demo record);

    Demo selectByPrimaryKey(Integer id);

    int updateByPrimaryKeySelective(Demo record);

    int updateByPrimaryKey(Demo record);

    int updateBatch(List<Demo> list);

    int updateBatchSelective(List<Demo> list);

    int batchInsert(@Param("list") List<Demo> list);
}
// package org.minions.kafka.dao;
//
// import com.alibaba.fastjson.JSONObject;
// import org.junit.jupiter.api.Test;
// import org.minions.common.model.mongo.DemoEntity;
// import org.minions.kafka.KafkaConsumersTest;
// import org.springframework.beans.factory.annotation.Autowired;
//
// /**
//  * TODO
//  *
//  * @author korov
//  * @date 2021/1/3
//  */
// class DemoDaoTest extends KafkaConsumersTest {
//
//     private DemoDao demoDao;
//
//     @Autowired
//     public void setDemoDao(DemoDao demoDao) {
//         this.demoDao = demoDao;
//     }
//
//     @Test
//     void saveDemo() {
//         DemoEntity demoEntity = new DemoEntity();
//         demoEntity.setId(1L);
//         demoEntity.setTitle("Spring Boot 中使用 MongoDB");
//         demoEntity.setDescription("描述1");
//         demoEntity.setBy("korov");
//         demoEntity.setUrl("lllll");
//
//         demoDao.saveDemo(demoEntity);
//
//         demoEntity = new DemoEntity();
//         demoEntity.setId(2L);
//         demoEntity.setTitle("Spring Boot 中使用 MongoDB");
//         demoEntity.setDescription("描述2");
//         demoEntity.setBy("korov");
//         demoEntity.setUrl("lllll");
//
//         demoDao.saveDemo(demoEntity);
//     }
//
//     @Test
//     void removeDemo() {
//         demoDao.removeDemo(2L);
//     }
//
//     @Test
//     void updateDemo() {
//         DemoEntity demoEntity = new DemoEntity();
//         demoEntity.setId(1L);
//         demoEntity.setTitle("Spring Boot 中使用 MongoDB 更新数据");
//         demoEntity.setDescription("生生世世");
//         demoEntity.setBy("korov");
//         demoEntity.setUrl("事实上");
//
//         demoDao.updateDemo(demoEntity);
//     }
//
//     @Test
//     void findDemoById() {
//         DemoEntity demoEntity = demoDao.findDemoById(1L);
//
//         System.out.println(JSONObject.toJSONString(demoEntity));
//     }
// }
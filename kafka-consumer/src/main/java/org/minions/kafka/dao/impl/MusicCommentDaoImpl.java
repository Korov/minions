package org.minions.kafka.dao.impl;

import org.minions.common.model.mongo.MusicComment;
import org.minions.kafka.dao.MusicCommentDao;
import org.springframework.data.mongodb.core.MongoTemplate;
import org.springframework.stereotype.Component;

import javax.annotation.Resource;

/**
 * TODO
 *
 * @author korov
 * @date 2021/1/3
 */
@Component
public class MusicCommentDaoImpl implements MusicCommentDao {
    private MongoTemplate mongoTemplate;

    @Resource
    public void setMongoTemplate(MongoTemplate mongoTemplate) {
        this.mongoTemplate = mongoTemplate;
    }

    @Override
    public void saveDemo(MusicComment musicComment) {
        mongoTemplate.save(musicComment);
    }
}

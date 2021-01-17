package org.minions.common.model.mongo;

import lombok.Data;
import org.bson.types.ObjectId;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Data
@Document(value = "music_comment")
public class MusicComment {
    @Id
    private ObjectId id;
    private String songId;
    private String comment;
}

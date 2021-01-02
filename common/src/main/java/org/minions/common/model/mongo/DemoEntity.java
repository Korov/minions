package org.minions.common.model.mongo;

import lombok.Data;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

/**
 * TODO
 *
 * @author korov
 * @date 2021/1/3
 */
@Data
@Document(value = "demo_collection")
public class DemoEntity {
    @Id
    private Long id;
    private String title;
    private String description;
    private String by;
    private String url;
}

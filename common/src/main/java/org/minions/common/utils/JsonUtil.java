package org.minions.common.utils;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.DeserializationFeature;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.PropertyNamingStrategy;
import lombok.extern.slf4j.Slf4j;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Objects;

@Slf4j
public class JsonUtil {
    /**
     * 默认的mapper，只配置了如果json中的属性在类中不存在则忽略
     */
    public static final ObjectMapper DEFAULT_MAPPER = new ObjectMapper();
    public static final ObjectMapper SNAKE_CASE_MAPPER = new ObjectMapper();

    static {
        DEFAULT_MAPPER.configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false);
    }

    static {
        SNAKE_CASE_MAPPER.setPropertyNamingStrategy(PropertyNamingStrategy.SNAKE_CASE);
        SNAKE_CASE_MAPPER.configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false);
    }

    /**
     * Object转json string
     *
     * @param object
     * @return
     * @throws JsonProcessingException
     */
    public static String objectToJson(Object object, ObjectMapper mapper) throws JsonProcessingException {
        Objects.requireNonNull(object);
        Objects.requireNonNull(mapper);
        return mapper.writeValueAsString(object);
    }

    public static <T> T jsonToObject(String json, Class<T> valueType) {
        try {
            return jsonToObject(json, valueType, DEFAULT_MAPPER);
        } catch (JsonProcessingException e) {
            log.error("parse json {} to object [{}] failed, {}", json, valueType.getName(), e.getMessage());
        }
        return null;
    }

    public static <T> T jsonToObject(String json, Class<T> valueType, ObjectMapper mapper) throws JsonProcessingException {
        Objects.requireNonNull(json);
        Objects.requireNonNull(valueType);
        Objects.requireNonNull(mapper);
        try {
            return mapper.readValue(json, valueType);
        } catch (Exception e) {
            log.error("parse json {} to object [{}] failed, {}", json, valueType.getName(), e.getMessage());
        }
        return null;
    }

    /**
     * 将json String转换为JsonNode
     *
     * @param json
     * @return JsonNode if succ, otherwise null
     */
    public static JsonNode jsonToNode(String json) {
        try {
            return jsonToNode(json, DEFAULT_MAPPER);
        } catch (JsonProcessingException e) {
            log.error("parse json {} to json node failed, {}", json, e.getMessage());
        }
        return null;
    }

    public static JsonNode jsonToNode(String json, ObjectMapper mapper) throws JsonProcessingException {
        Objects.requireNonNull(json);
        Objects.requireNonNull(mapper);
        try {
            return mapper.readTree(json);
        } catch (JsonProcessingException e) {
            log.error("parse json {} to json node failed, {}", json, e.getMessage());
        }
        return null;
    }

    public static <T> JsonNode objectToNode(T object, ObjectMapper mapper) throws JsonProcessingException {
        Objects.requireNonNull(object);
        Objects.requireNonNull(mapper);
        return mapper.valueToTree(object);
    }

    public static List jsonToList(String json) throws JsonProcessingException {
        return jsonToObject(json, List.class, DEFAULT_MAPPER);
    }

    public static <T> List<T> jsonToList(String json, Class<T> valueType, ObjectMapper mapper) throws JsonProcessingException {
        JsonNode array = JsonUtil.jsonToNode(json, mapper);
        List<T> result = new ArrayList<>(array.size());
        for (JsonNode node : array) {
            T temp = mapper.treeToValue(node, valueType);
            result.add(temp);
        }
        return result;
    }
}

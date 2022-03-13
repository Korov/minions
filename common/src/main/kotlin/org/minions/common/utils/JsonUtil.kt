package org.minions.common.utils

import com.fasterxml.jackson.core.JsonProcessingException
import com.fasterxml.jackson.databind.DeserializationFeature
import com.fasterxml.jackson.databind.JsonNode
import com.fasterxml.jackson.databind.ObjectMapper
import com.fasterxml.jackson.databind.PropertyNamingStrategy
import org.slf4j.Logger
import org.slf4j.LoggerFactory
import java.util.*

/**
 * @author zhu.lei
 * @date 2022-03-13 15:36
 */
class JsonUtil {
    companion object {
        val log: Logger = LoggerFactory.getLogger(JsonUtil::class.java)

        /**
         * 默认的mapper，只配置了如果json中的属性在类中不存在则忽略
         */
        val DEFAULT_MAPPER = ObjectMapper().configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false)
        val SNAKE_CASE_MAPPER = ObjectMapper().setPropertyNamingStrategy(PropertyNamingStrategy.SNAKE_CASE)
            .configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false)

        /**
         * Object转json string
         *
         * @param object
         * @return
         * @throws JsonProcessingException
         */
        @Throws(JsonProcessingException::class)
        fun objectToJson(`object`: Any, mapper: ObjectMapper): String? {
            Objects.requireNonNull(`object`)
            Objects.requireNonNull(mapper)
            return mapper.writeValueAsString(`object`)
        }

        fun <T> jsonToObject(json: String?, valueType: Class<T>): T? {
            try {
                return jsonToObject(json, valueType, DEFAULT_MAPPER)
            } catch (e: JsonProcessingException) {
                log.error("parse json {} to object [{}] failed, {}", json, valueType.name, e.message)
            }
            return null
        }

        @Throws(JsonProcessingException::class)
        fun <T> jsonToObject(json: String?, valueType: Class<T>, mapper: ObjectMapper): T? {
            Objects.requireNonNull(json)
            Objects.requireNonNull(valueType)
            Objects.requireNonNull(mapper)
            try {
                return mapper.readValue(json, valueType)
            } catch (e: Exception) {
                log.error("parse json {} to object [{}] failed, {}", json, valueType.name, e.message)
            }
            return null
        }

        /**
         * 将json String转换为JsonNode
         *
         * @param json
         * @return JsonNode if succ, otherwise null
         */
        fun jsonToNode(json: String?): JsonNode? {
            try {
                return jsonToNode(json, DEFAULT_MAPPER)
            } catch (e: JsonProcessingException) {
                log.error("parse json {} to json node failed, {}", json, e.message)
            }
            return null
        }

        @Throws(JsonProcessingException::class)
        fun jsonToNode(json: String?, mapper: ObjectMapper): JsonNode? {
            Objects.requireNonNull(json)
            Objects.requireNonNull(mapper)
            try {
                return mapper.readTree(json)
            } catch (e: JsonProcessingException) {
                log.error("parse json {} to json node failed, {}", json, e.message)
            }
            return null
        }

        @Throws(JsonProcessingException::class)
        fun <T> objectToNode(`object`: T, mapper: ObjectMapper): JsonNode? {
            Objects.requireNonNull(`object`)
            Objects.requireNonNull(mapper)
            return mapper.valueToTree(`object`)
        }

        @Throws(JsonProcessingException::class)
        fun jsonToList(json: String?): List<*>? {
            return jsonToObject(json, List::class.java, DEFAULT_MAPPER)
        }

        @JvmStatic
        fun objectToJson(node: JsonNode, mapper: ObjectMapper): String? {
            return mapper.writeValueAsString(node)
        }
    }
}
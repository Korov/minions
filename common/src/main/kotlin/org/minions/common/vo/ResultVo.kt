package org.minions.common.vo


import com.fasterxml.jackson.databind.JsonNode
import io.swagger.annotations.ApiModel
import io.swagger.annotations.ApiModelProperty
import org.minions.common.constant.Constant
import org.minions.common.utils.JsonUtil
import org.minions.common.utils.StringUtil.Companion.isEmpty

@ApiModel(value = "返回数据的格式")
class ResultVo<T>(
    code: Int = Constant.OPERATION_SUCCESS,
    description: String = Constant.DESCRIPTION_SUCCESS,
    data: T = null!!
) {

    @ApiModelProperty(value = "1表示执行成功，0表示执行失败")
    var code: Int

    @ApiModelProperty(value = "description")
    var description: String

    @ApiModelProperty(value = "execute result")
    var data: T

    init {
        this.code = code
        this.description = description
        this.data = data
    }

    fun <T> getResultVo(vo: String, clazz: Class<T>): ResultVo<T> {
        if (isEmpty(vo)) {
            return ResultVo()
        }
        val jsonNode = JsonUtil.jsonToNode(vo, JsonUtil.SNAKE_CASE_MAPPER)
        val code = jsonNode.get("code").numberValue().toInt()
        val description = jsonNode.get("description").textValue()
        val data = JsonUtil.jsonToObject(jsonNode.get("data").textValue(), clazz, JsonUtil.SNAKE_CASE_MAPPER)
        return ResultVo(code, description, data)
    }
}
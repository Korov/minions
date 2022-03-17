package org.minions.common.vo


import io.swagger.annotations.ApiModel
import io.swagger.annotations.ApiModelProperty
import org.minions.common.constant.Constant
import org.minions.common.utils.JsonUtil
import org.minions.common.utils.StringUtil.Companion.isEmpty

@ApiModel(value = "返回数据的格式")
class ResultVo<T>(
    code: Int = Constant.OPERATION_SUCCESS,
    description: String = Constant.DESCRIPTION_SUCCESS,
    data: T? = null
) {

    @ApiModelProperty(value = "1表示执行成功，0表示执行失败")
    var code: Int

    @ApiModelProperty(value = "description")
    var description: String

    @ApiModelProperty(value = "execute result")
    var data: T?

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
        if (jsonNode == null) {
            return ResultVo(Constant.OPERATION_FAIL, "")
        } else {
            val codeNode = jsonNode.get("code")
            var code = Constant.OPERATION_FAIL
            if (codeNode == null || !codeNode.isNumber) {
                code = codeNode.numberValue().toInt()
            }
            val descriptionNode = jsonNode.get("description")
            var description = Constant.DESCRIPTION_FAIL
            if (descriptionNode == null || !descriptionNode.isTextual) {
                description = descriptionNode.textValue()
            }
            val dataNode = jsonNode.get("data")

            val data = JsonUtil.jsonToObject(dataNode.textValue(), clazz, JsonUtil.SNAKE_CASE_MAPPER)
            return ResultVo(code, description, data)
        }
    }
}
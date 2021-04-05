package org.minions.common.model.demo

import io.swagger.annotations.ApiModelProperty
import org.minions.common.constant.Constant

class Demo {
    @ApiModelProperty(value = "0")
    val id: Int = 0

    @ApiModelProperty(value = Constant.BLACK)
    val name: String = Constant.BLACK
}
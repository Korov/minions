package org.minions.common.model.demo

import io.swagger.annotations.ApiModelProperty
import lombok.Data
import lombok.EqualsAndHashCode
import org.minions.common.constant.Constant

class Demo {
    @ApiModelProperty(value = "0")
    var id: Int = 0

    @ApiModelProperty(value = Constant.BLACK)
    var name: String = Constant.BLACK

    override fun equals(other: Any?): Boolean {
        if (this === other) return true
        if (javaClass != other?.javaClass) return false

        other as Demo

        if (id != other.id) return false
        if (name != other.name) return false

        return true
    }

    override fun hashCode(): Int {
        var result = id
        result = 31 * result + name.hashCode()
        return result
    }

    override fun toString(): String {
        return "Demo(id=$id, name='$name')"
    }

}
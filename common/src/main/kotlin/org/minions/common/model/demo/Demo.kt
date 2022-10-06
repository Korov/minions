package org.minions.common.model.demo

import io.swagger.v3.oas.annotations.media.Schema
import org.minions.common.constant.Constant

class Demo {
    @Schema(example = "0")
    var id: Long = 0

    @Schema(example = Constant.BLACK)
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
        var result = id.hashCode()
        result = 31 * result + name.hashCode()
        return result
    }

    override fun toString(): String {
        return "Demo(id=$id, name='$name')"
    }
}
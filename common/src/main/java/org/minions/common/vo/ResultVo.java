package org.minions.common.vo;

import com.alibaba.fastjson.JSONObject;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;
import lombok.ToString;
import org.minions.common.utils.StringUtil;

/**
 * @author korov
 */
@Data
@ToString
@ApiModel(value = "返回数据的格式")
public class ResultVo<T> {

    @ApiModelProperty(value = "1表示执行成功，0表示执行失败")
    private Integer code;
    @ApiModelProperty(value = "description")
    private String description;
    @ApiModelProperty(value = "execute result")
    private T data;

    public ResultVo() {
    }

    public ResultVo(Integer code, String description, T data) {
        set(code, description, data);
    }

    public void set(Integer code, String description, T data) {
        setCode(code);
        setDescription(description);
        setData(data);
    }

    public static <T> ResultVo<T> getResultVo(String vo, Class<T> clazz) {
        if (StringUtil.isEmpty(vo)) {
            return new ResultVo<>();
        }
        JSONObject jsonObject = JSONObject.parseObject(vo);
        Integer code = jsonObject.getInteger("code");
        String description = jsonObject.getString("description");
        T data = JSONObject.parseObject(jsonObject.getString("data"), clazz);
        return new ResultVo<>(code, description, data);
    }
}

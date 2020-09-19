package org.minions.common.vo;

import com.alibaba.fastjson.JSON;
import lombok.Data;
import lombok.ToString;
import org.minions.common.constant.Constant;
import org.minions.common.utils.StringUtil;

/**
 * @author korov
 */
@Data
@ToString
public class ResultVo<T> {

    private Integer code;
    private String description;
    private T data;

    public ResultVo() {
        super();
    }

    public ResultVo(Integer code, String description, T data) {
        set(code, description, data);
    }

    public void set(Integer code, String description, T data) {
        setCode(code);
        setDescription(description);
        setData(data);
    }

    public static ResultVo getFail() {
        return new ResultVo(Constant.OPERATION_FAIL, Constant.DESCRIPTION_FAIL, null);
    }

    public static ResultVo getSuccess() {
        return new ResultVo(Constant.OPERATION_SUCCESS, Constant.DESCRIPTION_SUCCESS, null);
    }

    public static <T> ResultVo<T> getResultVo(String vo) {
        if (StringUtil.isEmpty(vo)) {
            return getFail();
        }
        ResultVo<T> tableData = JSON.parseObject(vo, ResultVo.class);
        if (tableData != null) {
            return tableData;
        }
        return getFail();
    }
}

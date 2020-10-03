package org.minions.common.vo;

import org.minions.common.constant.Constant;

public class ResultVoBuilder {
    private static final ResultVo<String> FAIL_VO = new ResultVo<>(Constant.OPERATION_FAIL, Constant.DESCRIPTION_FAIL, Constant.BLACK);
    private static final ResultVo<String> SUCCESS_VO = new ResultVo<>(Constant.OPERATION_SUCCESS, Constant.DESCRIPTION_SUCCESS, Constant.BLACK);

    public static ResultVo<String> buildFailVo() {
        return FAIL_VO;
    }

    public static ResultVo<String> buildSuccessVo() {
        return SUCCESS_VO;
    }
}

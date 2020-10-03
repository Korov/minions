package org.minions.demo.controller;

import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import org.minions.common.constant.Constant;
import org.minions.common.vo.ResultVo;
import org.minions.demo.service.DemoService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

@Api(tags = "测试用接口", value = "目前只有id为1的用户")
@RestController
public class DemoController {
    @Autowired
    private DemoService demoService;

    @ApiOperation(value = "获取用户名", notes = "目前只有id为1的用户")
    @GetMapping(value = "/demo/get/{id}")
    public ResultVo<String> getDemo(@PathVariable(value = "id") Integer id) {
        return new ResultVo<String>(Constant.OPERATION_SUCCESS, Constant.DESCRIPTION_SUCCESS, "Hello " + demoService.queryDemoById(id).getName());
    }
}

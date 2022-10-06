package org.minions.demo.controller;

import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.minions.common.constant.Constant;
import org.minions.common.model.demo.Demo;
import org.minions.common.vo.ResultVo;
import org.minions.demo.service.DemoService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

@Tag(name = "测试用接口", description = "目前只有id为1的用户")
@RestController
public class DemoController {
    private DemoService demoService;

    @Autowired
    public void setDemoService(DemoService demoService) {
        this.demoService = demoService;
    }

    @Operation(summary = "获取用户名", description = "目前只有id为1的用户")
    @GetMapping(value = "/demo/get/{id}")
    public ResultVo<Demo> getDemo(@PathVariable(value = "id") Integer id) {
        Demo demo = demoService.queryDemoById(id);
        return new ResultVo<>(Constant.OPERATION_SUCCESS, Constant.DESCRIPTION_SUCCESS, demo);
    }
}

package org.minions.demo.controller;

import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import org.minions.common.model.demo.Demo;
import org.minions.common.vo.ResultVo;
import org.minions.demo.service.DemoService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

@Api(tags = "测试用接口", value = "目前只有id为1的用户")
@RestController
public class DemoController {
    private DemoService demoService;

    @Autowired
    public void setDemoService(DemoService demoService) {
        this.demoService = demoService;
    }

    @ApiOperation(value = "获取用户名", notes = "目前只有id为1的用户")
    @GetMapping(value = "/demo/get/{id}")
    public ResultVo<Demo> getDemo(@PathVariable(value = "id") Integer id) {
        Demo demo = demoService.queryDemoById(id);
        return new ResultVo<>(ResultVo.CODE_SUCCESS, ResultVo.DES_SUCCESS, demo);
    }
}

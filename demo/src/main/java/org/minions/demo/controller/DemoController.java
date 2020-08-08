package org.minions.demo.controller;

import org.minions.common.constant.Constant;
import org.minions.common.vo.ResultVo;
import org.minions.demo.service.DemoService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class DemoController {
    @Autowired
    private DemoService demoService;

    @GetMapping(value = "/demo/get/{id}")
    public ResultVo getDemo(@PathVariable(value = "id") Integer id) {
        return new ResultVo(Constant.OPERATION_SUCCESS, Constant.DESCRIPTION_SUCCESS, "Hello " + demoService.queryDemoById(id).getName());
    }
}

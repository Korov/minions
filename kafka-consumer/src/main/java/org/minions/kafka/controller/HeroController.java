package org.minions.kafka.controller;

import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import org.minions.common.dto.kafka.HeroInfoDTO;
import org.minions.common.vo.ResultVo;
import org.minions.kafka.service.HeroService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

/**
 * @author korov
 */
@Api(tags = "英雄信息",value = "HeroController")
@RestController
public class HeroController {
    @Autowired
    private HeroService heroService;

    @ApiOperation(value = "获取所有英雄信息", notes = "不需要参数", httpMethod = "GET")
    @GetMapping("/kafka/hero")
    public ResultVo getHeros() {
        List<HeroInfoDTO> dtos = heroService.getHeros();
        ResultVo resultVo = ResultVo.getSuccess();
        resultVo.setData(dtos);
        return resultVo;
    }
}

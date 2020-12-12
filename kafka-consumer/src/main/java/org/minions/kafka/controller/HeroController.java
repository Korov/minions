package org.minions.kafka.controller;

import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import org.minions.common.constant.Constant;
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
    private HeroService heroService;

    @Autowired
    public void setHeroService(HeroService heroService) {
        this.heroService = heroService;
    }

    @ApiOperation(value = "获取所有英雄信息", notes = "不需要参数", httpMethod = "GET")
    @GetMapping("/kafka/hero")
    public ResultVo<List<HeroInfoDTO>> getHeros() {
        List<HeroInfoDTO> hero = heroService.getHero();
        return new ResultVo<>(Constant.OPERATION_SUCCESS, Constant.DESCRIPTION_SUCCESS, hero);
    }
}

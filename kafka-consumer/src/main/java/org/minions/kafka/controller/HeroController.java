package org.minions.kafka.controller;

import org.minions.common.dto.kafka.HeroInfoDTO;
import org.minions.common.vo.ResultVo;
import org.minions.kafka.service.HeroService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

/**
 * @author korov
 * @date 2020/9/13
 */
@RestController
public class HeroController {
    @Autowired
    private HeroService heroService;

    @GetMapping("/kafka/hero")
    public ResultVo getHeros() {
        List<HeroInfoDTO> dtos = heroService.getHeros();
        ResultVo resultVo = ResultVo.getSuccess();
        resultVo.setData(dtos);
        return resultVo;
    }
}

package org.minions.kafka.service;

import org.minions.common.dto.kafka.HeroInfoDTO;

import java.util.List;

/**
 * @author korov
 * @date 2020/9/13
 */
public interface HeroService {
    List<HeroInfoDTO> getHeros();
}

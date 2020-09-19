package org.minions.kafka.service;

import org.minions.common.dto.kafka.HeroInfoDTO;

import java.util.List;

/**
 * @author korov
 */
public interface HeroService {
    List<HeroInfoDTO> getHeros();
}

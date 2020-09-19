package org.minions.kafka.service.impl;

import org.minions.common.constant.Constant;
import org.minions.common.dto.kafka.HeroInfoDTO;
import org.minions.common.model.kafka.HeroInfoModel;
import org.minions.kafka.mapper.HeroInfoMapper;
import org.minions.kafka.service.HeroService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

/**
 * @author korov
 */
@Service
public class HeroServiceImpl implements HeroService {
    @Autowired
    private HeroInfoMapper heroInfoMapper;

    @Override
    public List<HeroInfoDTO> getHeros() {
        List<HeroInfoModel> models = heroInfoMapper.selectAll();
        List<HeroInfoDTO> dtos = new ArrayList<>(Constant.COLLECTION_INIT_SIZE);
        models.forEach(heroInfoModel -> {
            HeroInfoDTO dto = new HeroInfoDTO(heroInfoModel);
            dtos.add(dto);
        });
        return dtos;
    }
}
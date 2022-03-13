package org.minions.common.model.kafka;

import com.baomidou.mybatisplus.annotation.TableId;
import lombok.Data;
import org.springframework.data.annotation.Id;

import java.math.BigDecimal;
import java.io.Serializable;

/**
 * <p>
 * 英雄武器
 * </p>
 *
 * @author korov
 * @since 2021-09-07
 */
@Data
public class HeroWeapon implements Serializable {

    private static final long serialVersionUID = 1L;

    /**
     * 武器id
     */
    @TableId
    private Integer weaponId;

    /**
     * 武器名称
     */
    private String weaponName;

    /**
     * 价格
     */
    private BigDecimal weaponPrice;

    /**
     * 类型
     */
    private String weaponType;

    public static final String WEAPON_ID = "weapon_id";

    public static final String WEAPON_NAME = "weapon_name";

    public static final String WEAPON_PRICE = "weapon_price";

    public static final String WEAPON_TYPE = "weapon_type";
}

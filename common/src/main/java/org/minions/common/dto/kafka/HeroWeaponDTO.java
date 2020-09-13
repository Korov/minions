package org.minions.common.dto.kafka;

import io.swagger.annotations.ApiModel;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.ToString;

import java.math.BigDecimal;

/**
 * Database Table Remarks:
 *   英雄武器
 *
 * This class was generated by MyBatis Generator.
 * This class corresponds to the database table hero_weapon
 */
@Data
@ToString
@AllArgsConstructor
@NoArgsConstructor
@ApiModel(value="org-minions-common-moedel-kafka-HeroWeaponModel")
public class HeroWeaponDTO {
    /**
     * Database Column Remarks:
     *   武器id
     *
     * This field was generated by MyBatis Generator.
     * This field corresponds to the database column hero_weapon.weapon_id
     *
     * @mbg.generated Sun Sep 13 17:22:56 CST 2020
     */
    private Integer weaponId;

    /**
     * Database Column Remarks:
     *   武器名称
     *
     * This field was generated by MyBatis Generator.
     * This field corresponds to the database column hero_weapon.weapon_name
     *
     * @mbg.generated Sun Sep 13 17:22:56 CST 2020
     */
    private String weaponName;

    /**
     * Database Column Remarks:
     *   价格
     *
     * This field was generated by MyBatis Generator.
     * This field corresponds to the database column hero_weapon.weapon_price
     *
     * @mbg.generated Sun Sep 13 17:22:56 CST 2020
     */
    private BigDecimal weaponPrice;

    /**
     * Database Column Remarks:
     *   类型
     *
     * This field was generated by MyBatis Generator.
     * This field corresponds to the database column hero_weapon.weapon_type
     *
     * @mbg.generated Sun Sep 13 17:22:56 CST 2020
     */
    private String weaponType;
}
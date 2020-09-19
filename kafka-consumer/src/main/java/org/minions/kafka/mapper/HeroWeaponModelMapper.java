package org.minions.kafka.mapper;

import org.minions.common.model.kafka.HeroWeaponModel;

public interface HeroWeaponModelMapper {
    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table hero_weapon
     *
     * @mbg.generated Sun Sep 13 19:51:28 CST 2020
     */
    int deleteByPrimaryKey(Integer weaponId);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table hero_weapon
     *
     * @mbg.generated Sun Sep 13 19:51:28 CST 2020
     */
    int insert(HeroWeaponModel record);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table hero_weapon
     *
     * @mbg.generated Sun Sep 13 19:51:28 CST 2020
     */
    int insertSelective(HeroWeaponModel record);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table hero_weapon
     *
     * @mbg.generated Sun Sep 13 19:51:28 CST 2020
     */
    HeroWeaponModel selectByPrimaryKey(Integer weaponId);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table hero_weapon
     *
     * @mbg.generated Sun Sep 13 19:51:28 CST 2020
     */
    int updateByPrimaryKeySelective(HeroWeaponModel record);

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table hero_weapon
     *
     * @mbg.generated Sun Sep 13 19:51:28 CST 2020
     */
    int updateByPrimaryKey(HeroWeaponModel record);
}
package org.minions.common.model.kafka;

import java.math.BigDecimal;

/**
 * Database Table Remarks:
 *   英雄武器
 *
 * This class was generated by MyBatis Generator.
 * This class corresponds to the database table hero_weapon
 */
public class HeroWeaponModel {
    /**
     * Database Column Remarks:
     *   武器id
     *
     * This field was generated by MyBatis Generator.
     * This field corresponds to the database column hero_weapon.weapon_id
     *
     * @mbg.generated Thu Dec 31 00:27:50 CST 2020
     */
    private Integer weaponId;

    /**
     * Database Column Remarks:
     *   武器名称
     *
     * This field was generated by MyBatis Generator.
     * This field corresponds to the database column hero_weapon.weapon_name
     *
     * @mbg.generated Thu Dec 31 00:27:50 CST 2020
     */
    private String weaponName;

    /**
     * Database Column Remarks:
     *   价格
     *
     * This field was generated by MyBatis Generator.
     * This field corresponds to the database column hero_weapon.weapon_price
     *
     * @mbg.generated Thu Dec 31 00:27:50 CST 2020
     */
    private BigDecimal weaponPrice;

    /**
     * Database Column Remarks:
     *   类型
     *
     * This field was generated by MyBatis Generator.
     * This field corresponds to the database column hero_weapon.weapon_type
     *
     * @mbg.generated Thu Dec 31 00:27:50 CST 2020
     */
    private String weaponType;

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table hero_weapon
     *
     * @mbg.generated Thu Dec 31 00:27:50 CST 2020
     */
    public HeroWeaponModel(Integer weaponId, String weaponName, BigDecimal weaponPrice, String weaponType) {
        this.weaponId = weaponId;
        this.weaponName = weaponName;
        this.weaponPrice = weaponPrice;
        this.weaponType = weaponType;
    }

    /**
     * This method was generated by MyBatis Generator.
     * This method corresponds to the database table hero_weapon
     *
     * @mbg.generated Thu Dec 31 00:27:50 CST 2020
     */
    public HeroWeaponModel() {
        super();
    }

    /**
     * This method was generated by MyBatis Generator.
     * This method returns the value of the database column hero_weapon.weapon_id
     *
     * @return the value of hero_weapon.weapon_id
     *
     * @mbg.generated Thu Dec 31 00:27:50 CST 2020
     */
    public Integer getWeaponId() {
        return weaponId;
    }

    /**
     * This method was generated by MyBatis Generator.
     * This method sets the value of the database column hero_weapon.weapon_id
     *
     * @param weaponId the value for hero_weapon.weapon_id
     *
     * @mbg.generated Thu Dec 31 00:27:50 CST 2020
     */
    public void setWeaponId(Integer weaponId) {
        this.weaponId = weaponId;
    }

    /**
     * This method was generated by MyBatis Generator.
     * This method returns the value of the database column hero_weapon.weapon_name
     *
     * @return the value of hero_weapon.weapon_name
     *
     * @mbg.generated Thu Dec 31 00:27:50 CST 2020
     */
    public String getWeaponName() {
        return weaponName;
    }

    /**
     * This method was generated by MyBatis Generator.
     * This method sets the value of the database column hero_weapon.weapon_name
     *
     * @param weaponName the value for hero_weapon.weapon_name
     *
     * @mbg.generated Thu Dec 31 00:27:50 CST 2020
     */
    public void setWeaponName(String weaponName) {
        this.weaponName = weaponName == null ? null : weaponName.trim();
    }

    /**
     * This method was generated by MyBatis Generator.
     * This method returns the value of the database column hero_weapon.weapon_price
     *
     * @return the value of hero_weapon.weapon_price
     *
     * @mbg.generated Thu Dec 31 00:27:50 CST 2020
     */
    public BigDecimal getWeaponPrice() {
        return weaponPrice;
    }

    /**
     * This method was generated by MyBatis Generator.
     * This method sets the value of the database column hero_weapon.weapon_price
     *
     * @param weaponPrice the value for hero_weapon.weapon_price
     *
     * @mbg.generated Thu Dec 31 00:27:50 CST 2020
     */
    public void setWeaponPrice(BigDecimal weaponPrice) {
        this.weaponPrice = weaponPrice;
    }

    /**
     * This method was generated by MyBatis Generator.
     * This method returns the value of the database column hero_weapon.weapon_type
     *
     * @return the value of hero_weapon.weapon_type
     *
     * @mbg.generated Thu Dec 31 00:27:50 CST 2020
     */
    public String getWeaponType() {
        return weaponType;
    }

    /**
     * This method was generated by MyBatis Generator.
     * This method sets the value of the database column hero_weapon.weapon_type
     *
     * @param weaponType the value for hero_weapon.weapon_type
     *
     * @mbg.generated Thu Dec 31 00:27:50 CST 2020
     */
    public void setWeaponType(String weaponType) {
        this.weaponType = weaponType == null ? null : weaponType.trim();
    }
}
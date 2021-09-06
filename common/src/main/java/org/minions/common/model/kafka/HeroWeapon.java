package org.minions.common.model.kafka;

import com.baomidou.mybatisplus.annotation.TableId;
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


    public Integer getWeaponId() {
        return weaponId;
    }

    public void setWeaponId(Integer weaponId) {
        this.weaponId = weaponId;
    }

    public String getWeaponName() {
        return weaponName;
    }

    public void setWeaponName(String weaponName) {
        this.weaponName = weaponName;
    }

    public BigDecimal getWeaponPrice() {
        return weaponPrice;
    }

    public void setWeaponPrice(BigDecimal weaponPrice) {
        this.weaponPrice = weaponPrice;
    }

    public String getWeaponType() {
        return weaponType;
    }

    public void setWeaponType(String weaponType) {
        this.weaponType = weaponType;
    }

    @Override
    public String toString() {
        return "HeroWeapon{" +
        "weaponId=" + weaponId +
        ", weaponName=" + weaponName +
        ", weaponPrice=" + weaponPrice +
        ", weaponType=" + weaponType +
        "}";
    }
}

package org.minions.common.model.kafka;

import com.baomidou.mybatisplus.annotation.TableId;

import java.io.Serializable;
import java.math.BigDecimal;

/**
 * <p>
 * 英雄信息
 * </p>
 *
 * @author korov
 * @since 2021-09-07
 */

public class HeroInfos implements Serializable {

    private static final long serialVersionUID = 1L;

    /**
     * 英雄id
     */
    @TableId
    private Integer heroId;

    /**
     * 英雄名称
     */
    private String heroName;

    /**
     * 英雄昵称
     */
    private String heroNickname;

    /**
     * 图片
     */
    private String heroImg;

    /**
     * 类型
     */
    private String heroType;

    /**
     * 故事
     */
    private String heroStory;

    /**
     * 难度
     */
    private String heroLevels;

    /**
     * 金币价格
     */
    private BigDecimal heroGoldPrice;

    /**
     * 点券价格
     */
    private BigDecimal heroTicketPrice;

    /**
     * 钻石价格
     */
    private BigDecimal heroDiamondPrice;

    /**
     * 推荐生存技能
     */
    private String recommendSummonerSkill;

    /**
     * 推荐铭文
     */
    private String recInscriptions;

    /**
     * 皮肤图片
     */
    private String skinImgs;

    /**
     * 大图
     */
    private String bigImg;

    /**
     * 历史介绍
     */
    private String historyIntro;

    /**
     * 技能提示
     */
    private String skillTips;

    /**
     * 推荐技能升级
     */
    private String recommendSummonerSkillTips;

    /**
     * 英雄提示
     */
    private String heroTips;

    /**
     * 生存提示
     */
    private String meleeTips;

    /**
     * 技能
     */
    private String skillList;

    /**
     * 装备介绍
     */
    private String equipChoice;

    /**
     * 关联英雄
     */
    private String partnerHero;

    /**
     * 克制英雄
     */
    private String beRestrainedHero;


    public Integer getHeroId() {
        return heroId;
    }

    public void setHeroId(Integer heroId) {
        this.heroId = heroId;
    }

    public String getHeroName() {
        return heroName;
    }

    public void setHeroName(String heroName) {
        this.heroName = heroName;
    }

    public String getHeroNickname() {
        return heroNickname;
    }

    public void setHeroNickname(String heroNickname) {
        this.heroNickname = heroNickname;
    }

    public String getHeroImg() {
        return heroImg;
    }

    public void setHeroImg(String heroImg) {
        this.heroImg = heroImg;
    }

    public String getHeroType() {
        return heroType;
    }

    public void setHeroType(String heroType) {
        this.heroType = heroType;
    }

    public String getHeroStory() {
        return heroStory;
    }

    public void setHeroStory(String heroStory) {
        this.heroStory = heroStory;
    }

    public String getHeroLevels() {
        return heroLevels;
    }

    public void setHeroLevels(String heroLevels) {
        this.heroLevels = heroLevels;
    }

    public BigDecimal getHeroGoldPrice() {
        return heroGoldPrice;
    }

    public void setHeroGoldPrice(BigDecimal heroGoldPrice) {
        this.heroGoldPrice = heroGoldPrice;
    }

    public BigDecimal getHeroTicketPrice() {
        return heroTicketPrice;
    }

    public void setHeroTicketPrice(BigDecimal heroTicketPrice) {
        this.heroTicketPrice = heroTicketPrice;
    }

    public BigDecimal getHeroDiamondPrice() {
        return heroDiamondPrice;
    }

    public void setHeroDiamondPrice(BigDecimal heroDiamondPrice) {
        this.heroDiamondPrice = heroDiamondPrice;
    }

    public String getRecommendSummonerSkill() {
        return recommendSummonerSkill;
    }

    public void setRecommendSummonerSkill(String recommendSummonerSkill) {
        this.recommendSummonerSkill = recommendSummonerSkill;
    }

    public String getRecInscriptions() {
        return recInscriptions;
    }

    public void setRecInscriptions(String recInscriptions) {
        this.recInscriptions = recInscriptions;
    }

    public String getSkinImgs() {
        return skinImgs;
    }

    public void setSkinImgs(String skinImgs) {
        this.skinImgs = skinImgs;
    }

    public String getBigImg() {
        return bigImg;
    }

    public void setBigImg(String bigImg) {
        this.bigImg = bigImg;
    }

    public String getHistoryIntro() {
        return historyIntro;
    }

    public void setHistoryIntro(String historyIntro) {
        this.historyIntro = historyIntro;
    }

    public String getSkillTips() {
        return skillTips;
    }

    public void setSkillTips(String skillTips) {
        this.skillTips = skillTips;
    }

    public String getRecommendSummonerSkillTips() {
        return recommendSummonerSkillTips;
    }

    public void setRecommendSummonerSkillTips(String recommendSummonerSkillTips) {
        this.recommendSummonerSkillTips = recommendSummonerSkillTips;
    }

    public String getHeroTips() {
        return heroTips;
    }

    public void setHeroTips(String heroTips) {
        this.heroTips = heroTips;
    }

    public String getMeleeTips() {
        return meleeTips;
    }

    public void setMeleeTips(String meleeTips) {
        this.meleeTips = meleeTips;
    }

    public String getSkillList() {
        return skillList;
    }

    public void setSkillList(String skillList) {
        this.skillList = skillList;
    }

    public String getEquipChoice() {
        return equipChoice;
    }

    public void setEquipChoice(String equipChoice) {
        this.equipChoice = equipChoice;
    }

    public String getPartnerHero() {
        return partnerHero;
    }

    public void setPartnerHero(String partnerHero) {
        this.partnerHero = partnerHero;
    }

    public String getBeRestrainedHero() {
        return beRestrainedHero;
    }

    public void setBeRestrainedHero(String beRestrainedHero) {
        this.beRestrainedHero = beRestrainedHero;
    }

    @Override
    public String toString() {
        return "HeroInfos{" +
                "heroId=" + heroId +
                ", heroName=" + heroName +
                ", heroNickname=" + heroNickname +
                ", heroImg=" + heroImg +
                ", heroType=" + heroType +
                ", heroStory=" + heroStory +
                ", heroLevels=" + heroLevels +
                ", heroGoldPrice=" + heroGoldPrice +
                ", heroTicketPrice=" + heroTicketPrice +
                ", heroDiamondPrice=" + heroDiamondPrice +
                ", recommendSummonerSkill=" + recommendSummonerSkill +
                ", recInscriptions=" + recInscriptions +
                ", skinImgs=" + skinImgs +
                ", bigImg=" + bigImg +
                ", historyIntro=" + historyIntro +
                ", skillTips=" + skillTips +
                ", recommendSummonerSkillTips=" + recommendSummonerSkillTips +
                ", heroTips=" + heroTips +
                ", meleeTips=" + meleeTips +
                ", skillList=" + skillList +
                ", equipChoice=" + equipChoice +
                ", partnerHero=" + partnerHero +
                ", beRestrainedHero=" + beRestrainedHero +
                "}";
    }
}

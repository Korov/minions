package org.minions.common.model.kafka;

import com.baomidou.mybatisplus.annotation.TableId;
import lombok.Data;

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
@Data
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

    public static final String HERO_ID = "hero_id";

    public static final String HERO_NAME = "hero_name";

    public static final String HERO_NICKNAME = "hero_nickname";

    public static final String HERO_IMG = "hero_img";

    public static final String HERO_TYPE = "hero_type";

    public static final String HERO_STORY = "hero_story";

    public static final String HERO_LEVELS = "hero_levels";

    public static final String HERO_GOLD_PRICE = "hero_gold_price";

    public static final String HERO_TICKET_PRICE = "hero_ticket_price";

    public static final String HERO_DIAMOND_PRICE = "hero_diamond_price";

    public static final String RECOMMEND_SUMMONER_SKILL = "recommend_summoner_skill";

    public static final String REC_INSCRIPTIONS = "rec_inscriptions";

    public static final String SKIN_IMGS = "skin_imgs";

    public static final String BIG_IMG = "big_img";

    public static final String HISTORY_INTRO = "history_intro";

    public static final String SKILL_TIPS = "skill_tips";

    public static final String RECOMMEND_SUMMONER_SKILL_TIPS = "recommend_summoner_skill_tips";

    public static final String HERO_TIPS = "hero_tips";

    public static final String MELEE_TIPS = "melee_tips";

    public static final String SKILL_LIST = "skill_list";

    public static final String EQUIP_CHOICE = "equip_choice";

    public static final String PARTNER_HERO = "partner_hero";

    public static final String BE_RESTRAINED_HERO = "be_restrained_hero";
}

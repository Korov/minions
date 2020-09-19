package org.minions.common.dto.kafka;

import com.alibaba.fastjson.JSONObject;
import com.alibaba.fastjson.annotation.JSONField;
import com.fasterxml.jackson.annotation.JsonProperty;
import io.swagger.annotations.ApiModel;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.ToString;
import org.minions.common.model.kafka.HeroInfoModel;

import java.math.BigDecimal;
import java.util.List;

/**
 * Database Table Remarks:
 * 英雄信息
 * <p>
 * This class was generated by MyBatis Generator.
 * This class corresponds to the database table hero_infos
 */
@Data
@ToString
@AllArgsConstructor
@NoArgsConstructor
@ApiModel(value = "org-minions-common-moedel-kafka-HeroInfoModel")
public class HeroInfoDTO {

    /**
     * name : 西施
     * title : 幻纱之灵
     * half_img : http://pic.wankacn.com/2019-09-26_5d8c2403ae49c.jpeg
     * type : ["2"]
     * background_story : 无主之地并非无忧童年的乐土，西施因此学会了许多生存的小手段。譬如寻宝、倒卖，以及在黑市中讨价还价。尽管拥有鉴别珍宝的能力，但她从未了解什么是真正的“宝贵之物”。在一次倒卖时，她意外闯祸，并在被追捕的雨夜中误入一座破败的古祠堂，机缘巧合地获得了一条富有魔道力量的纱织，躲过了危机。为了避祸，她隐姓埋名来到稷下，并在庄周老师门下一边学习如何运用力量，一边收集宝贝，希望有朝一日要用这些宝贝换回自己的自由。直到与星之队遇到“珠玑”之难关，她才在队友的选择中获得了对珍宝的认识。
     * levels : {"survival":"1","attack":"1","skill":"6","difficulty":"6"}
     * diamond_price : 0
     * gold_price : 13888
     * ticket_price : 388
     * text_price :
     * recommend_summoner_skill : [{"name":"闪现","icon":"http://pictest.wankacn.com/2017-04-27_5901deac66009.jpeg","description":"120秒CD：向指定方向位移一段距离"},{"name":"疾跑","icon":"http://pictest.wankacn.com/2017-04-27_5901deab66bb8.jpeg","description":"100秒CD：增加30%移动速度持续10秒"}]
     * rec_inscriptions : [{"title":"four","list":[{"name":"阳炎","level":"4","icon":"http://pictest.wankacn.com/2017-04-27_5901c32aec40d.png","attrs":"法术攻击+2.5|法术穿透+1.4"},{"name":"侵蚀","level":"4","icon":"http://pictest.wankacn.com/2017-04-27_5901c3367da4c.png","attrs":"法术攻击+0.9|法术穿透+3.8"},{"name":"刹那","level":"4","icon":"http://pictest.wankacn.com/2017-04-27_5901c330001ad.png","attrs":"最大生命+13.5|移动速度+0.7%"}]},{"title":"five","list":[{"name":"梦魇","level":"5","icon":"http://pictest.wankacn.com/2017-04-27_5901c32c9839e.png","attrs":"法术攻击+4.2|法术穿透+2.4"},{"name":"调和","level":"5","icon":"http://pictest.wankacn.com/2017-04-27_5901c3327da76.png","attrs":"最大生命+45|每5秒回血+5.2|移动速度+0.4%"},{"name":"心眼","level":"5","icon":"http://pictest.wankacn.com/2017-04-27_5901c33820f7d.png","attrs":"攻击速度+0.6%|法术穿透+6.4"}]}]
     * skin_imgs : [{"skin_name":"浣纱之灵","big_img":"http://pic.wankacn.com/2019-09-26_5d8c2403ae49c.jpeg"},{"skin_name":"归虚梦演","big_img":"http://pic.wankacn.com/2019-09-26_5d8c241a5ea61.jpeg"}]
     * hero_id : 141
     * big_img : http://pic.wankacn.com/2019-10-16_5da697e4d20e3.png
     * history_intro : 暂无
     * skill_tips : 连招：213121
     * recommend_summoner_skill_tips : 提高位移，配合大招
     * hero_tips : 1、注意与敌人距离的把控；2、一二技能配合打出高额伤害；3、走位躲技能，西施最怕控；
     * melee_tips : 善用一技能强制位移，先手使用，抓人有奇效！
     * skill_list : [{"name":"少女的把戏","icon":"http://pic.wankacn.com/2019-09-26_5d8c24d958c9b.png","description":"西施的技能伤害会随着自身与敌人间的距离增加而增加，距离每增加100，伤害增加5%，最多提升40%。","intro":"被动","tags":"","cd":"","mana_cost":"","attrs":[]},{"name":"纱缚之印","icon":"http://pic.wankacn.com/2019-09-26_5d8c25143d452.png","description":"西施将法器扔向指定位置，对区域内的敌人造成120/144/168/192/216/240（+18%法术加成）点法术伤害并朝法器的位置拉扯一段距离，同时纱会缠绕在一名敌人英雄身上，之后5秒内西施再次点击1技能，纱会牵引敌人朝一个方向移动一段距离。如果敌人距离西施过远，则不会收到影响。一技能可以对非英雄单位造成双倍伤害。","intro":"主升","tags":"法术","cd":"9","mana_cost":"40","attrs":[]},{"name":"幻纱之灵","icon":"http://pic.wankacn.com/2019-09-26_5d8c253087b9c.png","description":"西施扔出一颗能量球，遇到野怪停下，其存在期间每0.5秒会朝四周发射一次能量攻击附近的敌人，造成200/240/280/320/360/400（+36%法术加成）点法术伤害，首次命中减少敌人30%的移动速度，持续1.5秒，若多次命中同个目标则伤害衰减为25%。2秒后能量球会爆炸造成150/180/210/240/270/300（+27%法术加成）点法术伤害，内圈的敌人受到双倍的伤害。","intro":"副升","tags":"法术","cd":"7","mana_cost":"40","attrs":[]},{"name":"心无旁骛","icon":"http://pic.wankacn.com/2019-09-26_5d8c255d465c1.png","description":"西施将法器的力量灌注到自己体内,获得持续8秒的强化状态并刷新幻纱之灵的冷却时间。强化期间纱缚之印命中后可以连续控制敌人移动两次；同时幻纱之灵的冷却时间减半。大招开启时西施获得持续0.5秒50%的加速效果。","intro":"有大点大","tags":"法术/控制","cd":"45","mana_cost":"90","attrs":[]}]
     * equip_choice : [{"title":"纯伤害","description":"常规出门装，稍微补充冷却后，全力累积法术攻击，用火力压制敌人，纯伤害向出装，配合大招刷新和2技能双倍伤害的爆发，足以对敌人造成致命威胁。","list":[{"equip_id":"76","icon":"http://pictest.wankacn.com/2017-04-28_59031676397b3.jpeg"},{"equip_id":"43","icon":"http://pictest.wankacn.com/2017-04-28_5903166b83498.jpeg"},{"equip_id":"45","icon":"http://pictest.wankacn.com/2017-04-28_5903166bda9f0.jpeg"},{"equip_id":"41","icon":"http://pictest.wankacn.com/2017-04-28_5903166b10ebe.jpeg"},{"equip_id":"40","icon":"http://pictest.wankacn.com/2017-04-28_5903166adc5c9.jpeg"},{"equip_id":"49","icon":"http://pictest.wankacn.com/2017-04-28_5903166c96be0.jpeg"}]},{"title":"辅助型","description":"常规出门装，利用疾步之靴快速支援，半肉出装能让西施靠近敌人更加稳定的打出控制，走辅助型法师路线，自身拥有一定坦度，并且可以配合队友给予足够的控制支撑。","list":[{"equip_id":"79","icon":"http://pictest.wankacn.com/2017-04-28_5903167739ff8.jpeg"},{"equip_id":"45","icon":"http://pictest.wankacn.com/2017-04-28_5903166bda9f0.jpeg"},{"equip_id":"69","icon":"http://pictest.wankacn.com/2017-04-28_590316729a783.jpeg"},{"equip_id":"41","icon":"http://pictest.wankacn.com/2017-04-28_5903166b10ebe.jpeg"},{"equip_id":"44","icon":"http://pictest.wankacn.com/2017-04-28_5903166bb25f7.jpeg"},{"equip_id":"42","icon":"http://pictest.wankacn.com/2017-04-28_5903166b5c100.jpeg"}]}]
     * partner_hero : [{"hero_id":"66","name":"黄忠","icon":"http://pictest.wankacn.com/2017-04-26_59005f2485019.png"},{"hero_id":"4","name":"墨子","icon":"http://pic.wankacn.com/2017-06-06_593628155b319.jpeg"}]
     * restrained_hero : [{"hero_id":"50","name":"牛魔","icon":"http://pictest.wankacn.com/2017-04-26_59005f12a0818.png"},{"hero_id":"11","name":"高渐离","icon":"http://pictest.wankacn.com/2017-04-26_59005ed5ca4df.png"}]
     * be_restrained_hero : [{"hero_id":"12","name":"阿轲","icon":"http://pictest.wankacn.com/2017-04-26_59005ed7228c5.png"}]
     */

    @JSONField(name = "name")
    @JsonProperty("name")
    private String name;
    @JSONField(name = "title")
    @JsonProperty("title")
    private String title;
    @JSONField(name = "half_img")
    @JsonProperty("half_img")
    private String halfImg;
    @JSONField(name = "background_story")
    @JsonProperty("background_story")
    private String backgroundStory;
    @JSONField(name = "levels")
    @JsonProperty("levels")
    private LevelsDTO levels;
    @JSONField(name = "diamond_price")
    @JsonProperty("diamond_price")
    private String diamondPrice;
    @JSONField(name = "gold_price")
    @JsonProperty("gold_price")
    private String goldPrice;
    @JSONField(name = "ticket_price")
    @JsonProperty("ticket_price")
    private String ticketPrice;
    @JSONField(name = "text_price")
    @JsonProperty("text_price")
    private String textPrice;
    @JSONField(name = "hero_id")
    @JsonProperty("hero_id")
    private String heroId;
    @JSONField(name = "big_img")
    @JsonProperty("big_img")
    private String bigImg;
    @JSONField(name = "history_intro")
    @JsonProperty("history_intro")
    private String historyIntro;
    @JSONField(name = "skill_tips")
    @JsonProperty("skill_tips")
    private String skillTips;
    @JSONField(name = "recommend_summoner_skill_tips")
    @JsonProperty("recommend_summoner_skill_tips")
    private String recommendSummonerSkillTips;
    @JSONField(name = "hero_tips")
    @JsonProperty("hero_tips")
    private String heroTips;
    @JSONField(name = "melee_tips")
    @JsonProperty("melee_tips")
    private String meleeTips;
    @JSONField(name = "type")
    @JsonProperty("type")
    private List<String> type;
    @JSONField(name = "recommend_summoner_skill")
    @JsonProperty("recommend_summoner_skill")
    private List<RecommendSummonerSkillDTO> recommendSummonerSkill;
    @JSONField(name = "rec_inscriptions")
    @JsonProperty("rec_inscriptions")
    private List<RecInscriptionsDTO> recInscriptions;
    @JSONField(name = "skin_imgs")
    @JsonProperty("skin_imgs")
    private List<SkinImgsDTO> skinImgs;
    @JSONField(name = "skill_list")
    @JsonProperty("skill_list")
    private List<SkillListDTO> skillList;
    @JSONField(name = "equip_choice")
    @JsonProperty("equip_choice")
    private List<EquipChoiceDTO> equipChoice;
    @JSONField(name = "partner_hero")
    @JsonProperty("partner_hero")
    private List<PartnerHeroDTO> partnerHero;
    @JSONField(name = "restrained_hero")
    @JsonProperty("restrained_hero")
    private List<RestrainedHeroDTO> restrainedHero;
    @JSONField(name = "be_restrained_hero")
    @JsonProperty("be_restrained_hero")
    private List<BeRestrainedHeroDTO> beRestrainedHero;

    public HeroInfoDTO(HeroInfoModel model) {
        heroId = model.getHeroId().toString();
        beRestrainedHero = JSONObject.parseArray(model.getBeRestrainedHero(), BeRestrainedHeroDTO.class);
        bigImg = model.getBigImg();
        equipChoice = JSONObject.parseArray(model.getEquipChoice(), EquipChoiceDTO.class);
        diamondPrice = model.getHeroDiamondPrice().toString();
        diamondPrice = diamondPrice.substring(0, diamondPrice.indexOf("."));
        goldPrice = model.getHeroGoldPrice().toString();
        goldPrice = goldPrice.substring(0, goldPrice.indexOf("."));
        levels = JSONObject.parseObject(model.getHeroLevels(), LevelsDTO.class);
        name = model.getHeroName();
        backgroundStory = model.getHeroStory();
        ticketPrice = model.getHeroTicketPrice().toString();
        ticketPrice = ticketPrice.substring(0, ticketPrice.indexOf("."));
        heroTips = model.getHeroTips();
        type = JSONObject.parseArray(model.getHeroType(), String.class);
        historyIntro = model.getHistoryIntro();
        meleeTips = model.getMeleeTips();
        partnerHero = JSONObject.parseArray(model.getPartnerHero(), PartnerHeroDTO.class);
        recInscriptions = JSONObject.parseArray(model.getRecInscriptions(), RecInscriptionsDTO.class);
        recommendSummonerSkill = JSONObject.parseArray(model.getRecommendSummonerSkill(), RecommendSummonerSkillDTO.class);
        recommendSummonerSkillTips = model.getRecommendSummonerSkillTips();
        skillList = JSONObject.parseArray(model.getSkillList(), SkillListDTO.class);
        skillTips = model.getSkillTips();
        skinImgs = JSONObject.parseArray(model.getSkinImgs(), SkinImgsDTO.class);
        title = "";
        halfImg = "";
        textPrice = "";
        restrainedHero = JSONObject.parseArray(model.getBeRestrainedHero(), RestrainedHeroDTO.class);
    }

    public HeroInfoModel getInfo() {
        HeroInfoModel model = new HeroInfoModel();
        model.setBeRestrainedHero(JSONObject.toJSONString(beRestrainedHero));
        model.setBigImg(bigImg);
        model.setEquipChoice(JSONObject.toJSONString(equipChoice));
        model.setHeroDiamondPrice(BigDecimal.valueOf(Long.parseLong(diamondPrice)));
        model.setHeroGoldPrice(BigDecimal.valueOf(Long.parseLong(goldPrice)));
        model.setHeroLevels(JSONObject.toJSONString(levels));
        model.setHeroName(name);
        model.setHeroNickname(name);
        model.setHeroStory(backgroundStory);
        model.setHeroTicketPrice(BigDecimal.valueOf(Long.parseLong(ticketPrice)));
        model.setHeroTips(heroTips);
        model.setHeroType(JSONObject.toJSONString(type));
        model.setHistoryIntro(historyIntro);
        model.setMeleeTips(meleeTips);
        model.setPartnerHero(JSONObject.toJSONString(partnerHero));
        model.setRecInscriptions(JSONObject.toJSONString(recInscriptions));
        model.setRecommendSummonerSkill(JSONObject.toJSONString(recommendSummonerSkill));
        model.setRecommendSummonerSkillTips(recommendSummonerSkillTips);
        model.setSkillList(JSONObject.toJSONString(skillList));
        model.setSkillTips(skillTips);
        model.setSkinImgs(JSONObject.toJSONString(skinImgs));
        return model;
    }

    @NoArgsConstructor
    @Data
    public static class LevelsDTO {
        /**
         * survival : 1
         * attack : 1
         * skill : 6
         * difficulty : 6
         */

        @JSONField(name = "survival")
        @JsonProperty("survival")
        private String survival;
        @JSONField(name = "attack")
        @JsonProperty("attack")
        private String attack;
        @JSONField(name = "skill")
        @JsonProperty("skill")
        private String skill;
        @JSONField(name = "difficulty")
        @JsonProperty("difficulty")
        private String difficulty;
    }

    @NoArgsConstructor
    @Data
    public static class RecommendSummonerSkillDTO {
        /**
         * name : 闪现
         * icon : http://pictest.wankacn.com/2017-04-27_5901deac66009.jpeg
         * description : 120秒CD：向指定方向位移一段距离
         */

        @JSONField(name = "name")
        @JsonProperty("name")
        private String name;
        @JSONField(name = "icon")
        @JsonProperty("icon")
        private String icon;
        @JSONField(name = "description")
        @JsonProperty("description")
        private String description;
    }

    @NoArgsConstructor
    @Data
    public static class RecInscriptionsDTO {
        /**
         * title : four
         * list : [{"name":"阳炎","level":"4","icon":"http://pictest.wankacn.com/2017-04-27_5901c32aec40d.png","attrs":"法术攻击+2.5|法术穿透+1.4"},{"name":"侵蚀","level":"4","icon":"http://pictest.wankacn.com/2017-04-27_5901c3367da4c.png","attrs":"法术攻击+0.9|法术穿透+3.8"},{"name":"刹那","level":"4","icon":"http://pictest.wankacn.com/2017-04-27_5901c330001ad.png","attrs":"最大生命+13.5|移动速度+0.7%"}]
         */

        @JSONField(name = "title")
        @JsonProperty("title")
        private String title;
        @JSONField(name = "list")
        @JsonProperty("list")
        private List<ListDTO> list;

        @NoArgsConstructor
        @Data
        public static class ListDTO {
            /**
             * name : 阳炎
             * level : 4
             * icon : http://pictest.wankacn.com/2017-04-27_5901c32aec40d.png
             * attrs : 法术攻击+2.5|法术穿透+1.4
             */

            @JSONField(name = "name")
            @JsonProperty("name")
            private String name;
            @JSONField(name = "level")
            @JsonProperty("level")
            private String level;
            @JSONField(name = "icon")
            @JsonProperty("icon")
            private String icon;
            @JSONField(name = "attrs")
            @JsonProperty("attrs")
            private String attrs;
        }
    }

    @NoArgsConstructor
    @Data
    public static class SkinImgsDTO {
        /**
         * skin_name : 浣纱之灵
         * big_img : http://pic.wankacn.com/2019-09-26_5d8c2403ae49c.jpeg
         */

        @JSONField(name = "skin_name")
        @JsonProperty("skin_name")
        private String skinName;
        @JSONField(name = "big_img")
        @JsonProperty("big_img")
        private String bigImg;
    }

    @NoArgsConstructor
    @Data
    public static class SkillListDTO {
        /**
         * name : 少女的把戏
         * icon : http://pic.wankacn.com/2019-09-26_5d8c24d958c9b.png
         * description : 西施的技能伤害会随着自身与敌人间的距离增加而增加，距离每增加100，伤害增加5%，最多提升40%。
         * intro : 被动
         * tags :
         * cd :
         * mana_cost :
         * attrs : []
         */

        @JSONField(name = "name")
        @JsonProperty("name")
        private String name;
        @JSONField(name = "icon")
        @JsonProperty("icon")
        private String icon;
        @JSONField(name = "description")
        @JsonProperty("description")
        private String description;
        @JSONField(name = "intro")
        @JsonProperty("intro")
        private String intro;
        @JSONField(name = "tags")
        @JsonProperty("tags")
        private String tags;
        @JSONField(name = "cd")
        @JsonProperty("cd")
        private String cd;
        @JSONField(name = "mana_cost")
        @JsonProperty("mana_cost")
        private String manaCost;
        @JSONField(name = "attrs")
        @JsonProperty("attrs")
        private List<?> attrs;
    }

    @NoArgsConstructor
    @Data
    public static class EquipChoiceDTO {
        /**
         * title : 纯伤害
         * description : 常规出门装，稍微补充冷却后，全力累积法术攻击，用火力压制敌人，纯伤害向出装，配合大招刷新和2技能双倍伤害的爆发，足以对敌人造成致命威胁。
         * list : [{"equip_id":"76","icon":"http://pictest.wankacn.com/2017-04-28_59031676397b3.jpeg"},{"equip_id":"43","icon":"http://pictest.wankacn.com/2017-04-28_5903166b83498.jpeg"},{"equip_id":"45","icon":"http://pictest.wankacn.com/2017-04-28_5903166bda9f0.jpeg"},{"equip_id":"41","icon":"http://pictest.wankacn.com/2017-04-28_5903166b10ebe.jpeg"},{"equip_id":"40","icon":"http://pictest.wankacn.com/2017-04-28_5903166adc5c9.jpeg"},{"equip_id":"49","icon":"http://pictest.wankacn.com/2017-04-28_5903166c96be0.jpeg"}]
         */

        @JSONField(name = "title")
        @JsonProperty("title")
        private String title;
        @JSONField(name = "description")
        @JsonProperty("description")
        private String description;
        @JSONField(name = "list")
        @JsonProperty("list")
        private List<ListDTO> list;

        @NoArgsConstructor
        @Data
        public static class ListDTO {
            /**
             * equip_id : 76
             * icon : http://pictest.wankacn.com/2017-04-28_59031676397b3.jpeg
             */

            @JSONField(name = "equip_id")
            @JsonProperty("equip_id")
            private String equipId;
            @JSONField(name = "icon")
            @JsonProperty("icon")
            private String icon;
        }
    }

    @NoArgsConstructor
    @Data
    public static class PartnerHeroDTO {
        /**
         * hero_id : 66
         * name : 黄忠
         * icon : http://pictest.wankacn.com/2017-04-26_59005f2485019.png
         */

        @JSONField(name = "hero_id")
        @JsonProperty("hero_id")
        private String heroId;
        @JSONField(name = "name")
        @JsonProperty("name")
        private String name;
        @JSONField(name = "icon")
        @JsonProperty("icon")
        private String icon;
    }

    @NoArgsConstructor
    @Data
    public static class RestrainedHeroDTO {
        /**
         * hero_id : 50
         * name : 牛魔
         * icon : http://pictest.wankacn.com/2017-04-26_59005f12a0818.png
         */

        @JSONField(name = "hero_id")
        @JsonProperty("hero_id")
        private String heroId;
        @JSONField(name = "name")
        @JsonProperty("name")
        private String name;
        @JSONField(name = "icon")
        @JsonProperty("icon")
        private String icon;
    }

    @NoArgsConstructor
    @Data
    public static class BeRestrainedHeroDTO {
        /**
         * hero_id : 12
         * name : 阿轲
         * icon : http://pictest.wankacn.com/2017-04-26_59005ed7228c5.png
         */

        @JSONField(name = "hero_id")
        @JsonProperty("hero_id")
        private String heroId;
        @JSONField(name = "name")
        @JsonProperty("name")
        private String name;
        @JSONField(name = "icon")
        @JsonProperty("icon")
        private String icon;
    }
}
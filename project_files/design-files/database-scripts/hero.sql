/*==============================================================*/
/* DBMS name:      PostgreSQL 9.x                               */
/* Created on:     2020/8/30 14:12:21                           */
/*==============================================================*/


drop index hero_infos_PK;

drop table hero_infos;

drop index hero_weapon_PK;

drop table hero_weapon;

/*==============================================================*/
/* Table: hero_infos                                            */
/*==============================================================*/
create table hero_infos (
   hero_id              NUMERIC(8)           not null,
   hero_name            VARCHAR(128)         not null,
   hero_nickname        VARCHAR(256)         null,
   hero_img             TEXT                 null,
   hero_type            VARCHAR(256)         null,
   hero_story           TEXT                 null,
   hero_levels          TEXT                 null,
   hero_gold_price      NUMERIC(8,2)         null,
   hero_ticket_price    NUMERIC(8,2)         null,
   hero_diamond_price   NUMERIC(8,2)         null,
   recommend_summoner_skill TEXT                 null,
   rec_inscriptions     TEXT                 null,
   skin_imgs            TEXT                 null,
   big_img              TEXT                 null,
   history_intro        TEXT                 null,
   skill_tips           TEXT                 null,
   recommend_summoner_skill_tips TEXT                 null,
   hero_tips            TEXT                 null,
   melee_tips           TEXT                 null,
   skill_list           TEXT                 null,
   equip_choice         TEXT                 null,
   partner_hero         TEXT                 null,
   be_restrained_hero   TEXT                 null,
   constraint PK_HERO_INFOS primary key (hero_id)
);

comment on table hero_infos is
'英雄信息';

comment on column hero_infos.hero_id is
'英雄id';

comment on column hero_infos.hero_name is
'英雄名称';

comment on column hero_infos.hero_nickname is
'英雄昵称';

comment on column hero_infos.hero_img is
'图片';

comment on column hero_infos.hero_type is
'类型';

comment on column hero_infos.hero_story is
'故事';

comment on column hero_infos.hero_levels is
'难度';

comment on column hero_infos.hero_gold_price is
'金币价格';

comment on column hero_infos.hero_ticket_price is
'点券价格';

comment on column hero_infos.hero_diamond_price is
'钻石价格';

comment on column hero_infos.recommend_summoner_skill is
'推荐生存技能';

comment on column hero_infos.rec_inscriptions is
'推荐铭文';

comment on column hero_infos.skin_imgs is
'皮肤图片';

comment on column hero_infos.big_img is
'大图';

comment on column hero_infos.history_intro is
'历史介绍';

comment on column hero_infos.skill_tips is
'技能提示';

comment on column hero_infos.recommend_summoner_skill_tips is
'推荐技能升级';

comment on column hero_infos.hero_tips is
'英雄提示';

comment on column hero_infos.melee_tips is
'生存提示';

comment on column hero_infos.skill_list is
'技能';

comment on column hero_infos.equip_choice is
'装备介绍';

comment on column hero_infos.partner_hero is
'关联英雄';

comment on column hero_infos.be_restrained_hero is
'克制英雄';

/*==============================================================*/
/* Index: hero_infos_PK                                         */
/*==============================================================*/
create unique index hero_infos_PK on hero_infos (
hero_id
);

/*==============================================================*/
/* Table: hero_weapon                                           */
/*==============================================================*/
create table hero_weapon (
   weapon_id            NUMERIC(8)           not null,
   weapon_name          VARCHAR(256)         not null,
   weapon_price         NUMERIC(8,2)         not null,
   weapon_type          VARCHAR(128)         null,
   constraint PK_HERO_WEAPON primary key (weapon_id)
);

comment on table hero_weapon is
'英雄武器';

comment on column hero_weapon.weapon_id is
'武器id';

comment on column hero_weapon.weapon_name is
'武器名称';

comment on column hero_weapon.weapon_price is
'价格';

comment on column hero_weapon.weapon_type is
'类型';

/*==============================================================*/
/* Index: hero_weapon_PK                                        */
/*==============================================================*/
create unique index hero_weapon_PK on hero_weapon (
weapon_id
);


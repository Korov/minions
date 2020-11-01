/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2020/11/1 18:52:11                           */
/*==============================================================*/


drop table if exists hero_infos;

drop table if exists hero_weapon;

/*==============================================================*/
/* Table: hero_infos                                            */
/*==============================================================*/
create table hero_infos
(
   hero_id              numeric(8,0) not null comment '英雄id',
   hero_name            varchar(128) not null comment '英雄名称',
   hero_nickname        varchar(256) comment '英雄昵称',
   hero_img             text comment '图片',
   hero_type            varchar(256) comment '类型',
   hero_story           text comment '故事',
   hero_levels          text comment '难度',
   hero_gold_price      numeric(8,2) comment '金币价格',
   hero_ticket_price    numeric(8,2) comment '点券价格',
   hero_diamond_price   numeric(8,2) comment '钻石价格',
   recommend_summoner_skill text comment '推荐生存技能',
   rec_inscriptions     text comment '推荐铭文',
   skin_imgs            text comment '皮肤图片',
   big_img              text comment '大图',
   history_intro        text comment '历史介绍',
   skill_tips           text comment '技能提示',
   recommend_summoner_skill_tips text comment '推荐技能升级',
   hero_tips            text comment '英雄提示',
   melee_tips           text comment '生存提示',
   skill_list           text comment '技能',
   equip_choice         text comment '装备介绍',
   partner_hero         text comment '关联英雄',
   be_restrained_hero   text comment '克制英雄',
   primary key (hero_id)
);

alter table hero_infos comment '英雄信息';

/*==============================================================*/
/* Table: hero_weapon                                           */
/*==============================================================*/
create table hero_weapon
(
   weapon_id            numeric(8,0) not null comment '武器id',
   weapon_name          varchar(256) not null comment '武器名称',
   weapon_price         numeric(8,2) not null comment '价格',
   weapon_type          varchar(128) comment '类型',
   primary key (weapon_id)
);

alter table hero_weapon comment '英雄武器';


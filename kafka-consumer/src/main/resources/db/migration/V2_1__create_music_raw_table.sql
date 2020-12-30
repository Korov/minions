drop table if exists music_raw;
create table music_raw
(
    song_id  TEXT not null,
    comments TEXT   null
);

comment on table music_raw is
    '网易云评论原始数据';

comment on column music_raw.song_id is
    '歌曲id';

comment on column music_raw.comments is
    '歌曲评论原始数据';

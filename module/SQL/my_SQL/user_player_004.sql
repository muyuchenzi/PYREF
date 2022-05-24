-- 变更表结构
alter table public.users
    add fullname varchar(255);
alter table public.users
    drop fullname;

alter table public.users
    rename player to nba_player;

alter table users
    alter nba_player type varchar(100);

create index nba_player_index on users (nba_player);
drop index nba_player_index;
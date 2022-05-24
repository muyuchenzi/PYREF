create table public.users
(
    id     serial primary key,
    player varchar(255) not null,
    score  real,
    team   varchar(255)
);
create table public.twitter
(
    id      serial primary key,
    user_id integer,
    content varchar(255) not null

);


-- 插入数据
insert into users(player, score, team)
values ('库里', 28.3, '勇士'),
       ('哈登', 30.2, '火箭'),
       ('阿杜', 25.6, '勇士'),
       ('阿詹', 27.8, '骑士'),
       ('阿龟', 31.3, '雷霆'),
       ('白边', 19.8, '热火');
insert into twitter(user_id, content)
values (1, '今天又是大胜，克莱打的真好'),
       (2, '今晚我得了60分'),
       (3, '获胜咱不怕，缺谁谁尴尬'),
       (4, '明年可能转会到西部'),
       (5, '我都双20了，球队依然不胜利'),
       (1, '明年听说有条大鱼要来，谁？');

-- 操作
select *
from users;
select *
from twitter;

select users.player, twitter.content
from users,
     twitter
where users.id = twitter.id;

select u.player, t.content
from users as u,
     twitter as t
where u.id = t.user_id;

select u.player, t.content
from users as u,
     twitter as t
where u.id = t.user_id
  and u.id = 1









-- 创建表格
create table public.users
(
    id     serial primary key,
    player varchar(255) not null,
    score  real,
    team   varchar(255)
);

-- 插入数据
insert into users(player, score, team)
values ('库里', 28.3, '勇士'),
       ('哈登', 30.2, '火箭'),
       ('阿杜', 25.6, '勇士'),
       ('阿詹', 27.8, '骑士'),
       ('阿龟', 31.3, '雷霆'),
       ('白边', 19.8, '热火');

-- 基本查询
select player, score, team
from public.users
limit 4;

-- 基本的查询
select *
from users
where score > 20;

select *
from users
where score > 20
  and score < 30;

select *
from users
where team = '勇士';

select *
from users
where team != '勇士';

select *
from users
where player like '阿%';








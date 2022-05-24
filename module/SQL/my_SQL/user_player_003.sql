-- 方便的函数
-- length concat alias substring random

select player, length(player)
from users;

select player, concat(player, '-', team) as 球队
from users;

select substring(team, 1, 1) as 球队首字
from users;

select concat('我', substr(team, 1, 1)) as 球队首字
from users;

select random();

select *
from users
order by random()
limit 1;
-- 更新删除数据

update users
set score=29.1
where player = '阿詹';

update users
set score = score + 1
where team = '勇士';

update users
set score =score + 10
where team in ('勇士', '骑士');

delete
from users
where score > 35;
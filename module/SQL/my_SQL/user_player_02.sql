-- order by
-- limit
-- offset


select *
from users
order by score desc;--asc

select *
from users
order by team;

select *
from users
order by team desc, score desc;

select *
from users
order by score desc
limit 3;

select *
from users
order by score desc
limit 3 offset 1;

-- 统计抽出数据
select distinct team, id
from users
;
--
select sum(score), min(score), max(score)
from users;

-- 子查询
select *
from users
where score = (select min(score) from users);

select *
from users
where score = (select max(score) from users);

-- 分组
select team, max(score)
from users
group by team;

select team, max(score)
from users
group by team
having max(score) > 25
order by max(score);


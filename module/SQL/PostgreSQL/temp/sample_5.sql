-- 检索"0001"课程分数小于60，按分数降序排列的学生信息

--
-- select *
-- from student
-- where 学号 in (
--     select 学号
--     from score
--     where 课程号 = '0001'
--       and 成绩 <= 90
--     order by 成绩
-- );

-- select b.*, a.成绩
-- from score as a
--          left join student as b
--                    on a.学号 = b.学号
-- where a.课程号 = '0001'
--   and a.成绩 <= 90
-- order by a.成绩;

-- 查询不同老师所教不同课程平均分从高到低显示
-- select c.教师号, round(cast(avg(c.成绩) as decimal), 2)
-- from (
--          select a.*, b.教师号
--          from score as a
--                   left join course as b
--                             on a.课程号 = b.课程号
--      ) as c
--          inner join teacher as t
--                     on c.教师号 = t.教师号
-- group by c.教师号
-- order by avg(c.成绩) desc
select r.课程号, avg(r.成绩) as 平均成绩
from (
         select c.教师姓名, a.*
         from score as a
                  left join course as b
                            on a.课程号 = b.教师号
                  left join teacher as c
                            on b.教师号 = c.教师号) as r
group by r.课程号
order by 平均成绩 desc
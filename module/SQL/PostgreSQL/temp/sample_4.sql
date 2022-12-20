-- -- 查询所有学生的学号、姓名、选课数、总成绩
--
-- select a.学号, a.姓名, 选课数, 总成绩
-- from student as a
--          left join
--      (
--          select b.学号, count(b.课程号) as 选课数, sum(b.成绩) as 总成绩
--          from score as b
--          group by b.学号
--      ) as b
--      on a.学号 = b.学号
-- order by a.学号 asc;

-- NOTE查询平均成绩大于85的所有学生的学号、姓名和平均成绩
-- select a.学号, a.姓名, b.平均成绩
-- from student as a
--          join
--      (
--          select 学号, round(cast(avg(成绩) as numeric), 2) as 平均成绩
--          from score
--          group by 学号
--          having avg(成绩) > 85
--      ) as b
--      on a.学号 = b.学号

-- 查询学生的选课情况：学号，姓名，课程号，课程名称

select a.学号, 姓名, b.课程号, c.课程名称
from student a
         right join score b on a.学号 = b.学号
         inner join course c on b.课程号 = c.课程号;
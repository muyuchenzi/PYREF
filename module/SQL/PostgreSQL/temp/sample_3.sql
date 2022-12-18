-- 汇总分析

-- 查询学生的总成绩并进行排名
-- select 学号, sum(成绩)
-- from score
-- group by 学号
-- order by sum(成绩);

-- 查询平均成绩大于80分的学生的学号和平均成绩

--
-- select 学号, round(cast(avg(成绩) as decimal), 2) as 平均成绩
-- from score
-- group by 学号
-- having avg(成绩) > 80

-- 查询课程平均成绩小于80分学生的学号、姓名
--
-- select student.学号, student.姓名
-- from student
-- where 学号 in (
--     select score.学号
--     from score
--     group by score.学号
--     having avg(score.成绩) < 80
-- );
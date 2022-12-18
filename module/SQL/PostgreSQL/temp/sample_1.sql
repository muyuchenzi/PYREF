-- select *
-- from temp.public.student
-- where 姓名 like '猴%'

-- #查询课程号位0002的总成绩

-- select sum(成绩)
-- from temp.public.score
-- where 课程号 = '0002'

-- 查询选了课程的学生人数
-- select count(distinct 学号)
-- from score;

-- -- 查询各科成绩最高和最低的分
-- select 课程号, max(成绩) as 最高分, min(成绩) as 最低分
-- from score
-- group by 课程号
-- order by 课程号

-- 查询每门课程被选修的学生数
-- select 课程号, count(学号) as 选修学生数
-- from score
-- group by 课程号

-- 查询男生、女生人数

-- select 性别, count(性别) 人数
-- from student
-- group by 性别
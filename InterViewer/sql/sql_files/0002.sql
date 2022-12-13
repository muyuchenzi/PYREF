-- select 课程号, round(cast(avg("成绩") as decimal), 2) as 平均成绩, count(学号)
-- from test.public.score
-- group by 课程号
-- having avg(成绩) > 60
-- order by 课程号
--NOTE 查询至少选修两门课程的学生学号

-- select count("学号"), round(cast(avg(成绩) as decimal), 2)
-- from test.public.score
-- group by 课程号
-- having count(学号) > 2;

--note查询同名同姓学生名单并统计同名人数

-- select 姓名, count(姓名) as 人数
-- from public.student
-- group by 姓名
-- having count(姓名) > 1;
-- note查询大于的课程并按课程号从大到小排列

-- select distinct 课程号
-- from test.public.score
-- where 成绩 > 80
-- order by 课程号 desc;

--note 查询每门课程的平均成绩，结果按平均成绩升序排序，平均成绩相同时，按课程号降序排列
select 课程号, round(cast(avg(成绩) as numeric), 3)
from test.public.score
group by 课程号
order by avg(成绩) asc, 课程号 desc;
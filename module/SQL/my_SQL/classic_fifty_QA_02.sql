-- NOTE 1、查询姓“猴”的学生名单
-- select *
-- from student
-- where 姓名 like '猴%';
-- select *
-- from student
-- where 姓名 like '%猴';
-- select *
-- from student
-- where 姓名 like '%猴%';
-- select *
-- from teacher
-- where teacher.教师姓名 like '孟%';

-- NOTE 2、
-- 面试题：查询课程编号为“0002”的总成绩
-- 查询选了课程的学生人数
-- select sum(成绩)
-- from score
-- where 课程号 = '0002';
--
-- select count(distinct 学号) as 学生人数
-- from score;

-- 3、分组 NOTE
-- 查询各科成绩最高和最低分
-- 查询每门课程被选修的学生数
-- 查询男生、女生人数

-- select 课程号, max(成绩) as 最高分, max(成绩) as 最低分
-- from score
-- group by score.课程号
-- order by 课程号 asc;
--
-- select 课程号, count(distinct 学号) as 学生数
-- from score
-- group by score.课程号
-- order by 学生数 desc;
--
-- select count(性别) as 数量, 性别
-- from student
-- group by 性别;

-- NOTE 4、分组结果的条件
-- 查询平均成绩大于75分学生的学号和平均成绩
select 学号, avg(成绩)
from score
group by 学号
having avg(成绩) > 75;
-- 查询大于选修两门课程的学生学号
select count(学号) as 学生数, 学号
from score
group by 学号
having count(学号) > 2;
-- 查询同名同姓学生名单并统计同名人数
select 姓名, count("姓名") as 同名人数
from student
group by 姓名
having count('姓名') > 1;
-- 查询大于85的课程并按课程号从大到小排列
select avg(成绩), 课程号
from score
group by 课程号
having avg(成绩) > 85
order by avg(成绩) desc;
-- 查询每门课程的平均成绩，结果按平均成绩升序排序，平均成绩相同时，按课程号降序排列
select 课程号, avg(成绩) as 平均分
from score
group by 课程号
order by avg(成绩) asc, 课程号 desc;

-- 检索课程编号为“0002”且分数小于80的学生学号，结果按按分数降序排列
select 学号, 成绩
from score
where 课程号 = '0002'
  and 成绩 > 70
order by 成绩 desc;
-- 查询两门以上不到90课程的同学的学号及其平均成绩,这个需求其实有点乱。。。
select 学号, avg(成绩)
from score
group by 学号
having avg(成绩) <= 80;


-- 汇总分析
-- 查询学生的总成绩并进行排名
select 学号, sum(成绩)
from score
group by 学号
order by sum(成绩) desc;

-- 查询平均成绩大于80分的学生的学号和平均成绩

select 学号, avg(成绩) as 平均分
from score
group by 学号
having avg(成绩) > 80;

-- 查询所有课程成绩小于80分学生的学号、姓名

select 学号, 姓名
from student
where 学号 in (
    select 学号
    from score
    where 成绩 < 80
);
-- 查询没有学全所有课的学生的学号、姓名
select student.学号, 姓名
from student
where student.学号 in (select score.学号
                     from score
                     group by score.学号
                     having count('课程号') < 3);
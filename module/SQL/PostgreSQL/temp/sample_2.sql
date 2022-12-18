-- select avg(成绩), 学号
-- from score
-- group by 学号
-- having avg(成绩) > 75;


-- select 学号, count(课程号) as 选修课程数
-- from score
-- group by 学号
-- having count(课程号) > 2

-- 查询同名同姓学生名单并统计同名人数
--
-- select 姓名, count(姓名) as 同名人数
-- from student
-- group by 姓名
-- having count(姓名) > 1

-- 查询平均成绩小于八十五分的课程并按课程号从大到小排列
-- select 课程号, avg(成绩) as 平均成绩
-- from score
-- group by 课程号
-- having avg(成绩) < 85
-- order by 课程号 desc

-- 查询每门课程的平均成绩，结果按平均成绩升序排序，平均成绩相同时，按课程号降序排列

-- select avg(成绩), 课程号
-- from temp.public.score
-- group by 课程号
-- order by avg(成绩) asc, 课程号 desc;

-- 检索课程编号为“0003”且分数小于90的学生学号，结果按按分数降序排列
-- select 学号, 成绩
-- from score
-- where 课程号 = '0003'
--   and 成绩 < 90
-- order by 成绩 desc
--
-- 统计每门课程的学生选修人数(超过2人的课程才统计)
--
-- --              要求输出课程号和选修人数，查询结果按人数降序排序，若人数相同，按课程号升序排序
--
-- select 课程号, count(学号) as 选修人数
-- from score
-- group by 课程号
-- having count(学号) > 2
-- order by 选修人数 desc, 课程号 asc

-- 查询两门以上不到90课程的同学的学号及其平均成绩

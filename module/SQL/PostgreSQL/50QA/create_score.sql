-- 创建 score 表

create table test.public.score
(
    学号  varchar not null,
    课程号 varchar not null,
    成绩  float4  not null
);
-- 创建course 表
create table test.public.course
(
    课程号  varchar not null,
    课程名称 varchar not null,
    教师号  varchar not null

);
create table test.public.teacher
(
    教师号  varchar not null,
    教师名称 varchar
)
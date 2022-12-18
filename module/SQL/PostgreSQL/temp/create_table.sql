-- create table student
-- (
--     学号   varchar not null,
--     姓名   varchar not null,
--     出生日期 date    not null,
--     性别   varchar
-- );

create table score
(
    学号  varchar not null,
    课程号 varchar not null,
    成绩  double precision
);
create table course
(
    课程号  varchar not null,
    课程名称 varchar,
    教师号  varchar
);

create table teacher
(
    教师号  varchar not null,
    教师姓名 varchar
)
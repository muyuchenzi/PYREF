-- 数据准备
-- NOTE 1、创建表
create table student
(
    学号   numeric primary key,
    姓名   varchar not null,
    出生年月 date,
    性别   varchar
);
create table score
(
    学号  varchar,
    课程号 varchar,
    成绩  float,
    primary key (学号, 课程号)
);
create table course
(
    课程号  varchar not null,
    课程名称 varchar not null,
    教师号  varchar not null
);
create table teacher
(
    教师号  varchar not null,
    教师姓名 varchar
);
-- NOTE 2、向学生表里添加数据
insert into student("学号", "姓名", "出生年月", "性别")
values ('0001', '猴子', '1989-01-01', '男'),
       ('0002', '猴子', '1990-12-21', '女'),
       ('0003', '马云', '1991-12-21', '男'),
       ('0004', '王思聪', '1990-05-20', '男');
insert into score("学号", "课程号", "成绩")
VALUES ('0001', '0001', 80),
       ('0001', '0002', 90),
       ('0001', '0003', 99),
       ('0002', '0002', 60),
       ('0002', '0003', 80),
       ('0003', '0001', 80),
       ('0003', '0002', 80),
       ('0003', '0003', 80);
insert into course("课程号", "课程名称", "教师号")
VALUES ('0001', '语文', '0002'),
       ('0002', '数学', '0001'),
       ('0003', '英语', '0003');
insert into teacher("教师号", "教师姓名")
VALUES ('0001', '孟扎扎'),
       ('0002', '马化腾'),
       ('0003', null),
       ('0004', '');



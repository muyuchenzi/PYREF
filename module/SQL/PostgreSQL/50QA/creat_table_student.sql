-- 创建表
create table student
(
    学号   varchar not null,
    姓名   varchar not null,
    出生日期 date,
    性别   varchar
);

-- drop table test.public.student


-- insert
insert into student(学号, 姓名, 出生日期, 性别)
values ('0001', '猴子', '1989-01-01', '男');

insert into student(学号, 姓名, 出生日期, 性别)
values ('0002', '猴子', '1990-12-21', '女');

insert into student(学号, 姓名, 出生日期, 性别)
values ('0003', '马云', '1991-12-21', '男');

insert into student(学号, 姓名, 出生日期, 性别)
values ('0004', '王思聪', '1990-05-20', '男');
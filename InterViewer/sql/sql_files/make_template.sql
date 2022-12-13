-- insert into student(学号,姓名,出生日期,性别)
-- values('0001' , '猴子' , '1989-01-01' , '男');
--
-- insert into student(学号,姓名,出生日期,性别)
-- values('0002' , '猴子' , '1990-12-21' , '女');
--
-- insert into student(学号,姓名,出生日期,性别)
-- values('0003' , '马云' , '1991-12-21' , '男');
--
-- insert into student(学号,姓名,出生日期,性别)
-- values('0004' , '王思聪' , '1990-05-20' , '男');

-- create table score
-- (
--     学号  varchar not null,
--     课程号 varchar not null,
--     成绩  float4
-- );
-- insert into score(学号, 课程号, 成绩)
-- values ('0001', '0001', 80);
--
-- insert into score(学号, 课程号, 成绩)
-- values ('0001', '0002', 90);
--
-- insert into score(学号, 课程号, 成绩)
-- values ('0001', '0003', 99);
--
-- insert into score(学号, 课程号, 成绩)
-- values ('0002', '0002', 60);
--
-- insert into score(学号, 课程号, 成绩)
-- values ('0002', '0003', 80);
--
-- insert into score(学号, 课程号, 成绩)
-- values ('0003', '0001', 80);
--
-- insert into score(学号, 课程号, 成绩)
-- values ('0003', '0002', 80);
--
-- insert into score(学号, 课程号, 成绩)
-- values ('0003', '0003', 80);
-- insert into course(课程号, 课程名称, 教师号)
-- values ('0001', '语文', '0002');
--
-- insert into course(课程号, 课程名称, 教师号)
-- values ('0002', '数学', '0001');
--
-- insert into course(课程号, 课程名称, 教师号)
-- values ('0003', '英语', '0003');

insert into teacher(教师号, 教师姓名)
values ('0001', '孟扎扎');

insert into teacher(教师号, 教师姓名)
values ('0002', '马化腾');

-- 这里的教师姓名是空值（null）
insert into teacher(教师号, 教师姓名)
values ('0003', null);

-- 这里的教师姓名是空字符串（''）
insert into teacher(教师号, 教师姓名)
values ('0004', '');
-- 创建表格
create table post_test
(
    id          integer primary key,
    title       varchar not null,
    content     text,
    is_draft    boolean   default true,
    is_del      boolean   default false,
    create_date timestamp default 'now'
);
-- 插入数据
insert into public.post_test (id, title, content)
values (1, 'list_001', 'a test text');

create table public.users
(
    id     serial primary key,
    player varchar(255) not null,
    score  real,
    team   varchar(255)
)

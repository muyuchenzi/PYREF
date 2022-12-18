select *
from student
where date_part('year', 出生日期) = 1991
;
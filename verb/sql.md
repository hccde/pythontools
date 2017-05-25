create databases verb;
use verb;

create table user(
name char(120),
last_login date,
password char(120),
uid char(120)
);

create table word
(
word_key int(12),
en char(120),
ch text(360)
);
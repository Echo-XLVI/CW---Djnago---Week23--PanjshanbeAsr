Create Database formdb;

Create Table users
(user_id serial primary key,
 firstname varchar(20) not null,
 lastname varchar(30) not null,
 company varchar(20) not null,
 email varchar(50) not null,
 phone varchar(13) not null,
 address varchar(50) not null,
 about text);
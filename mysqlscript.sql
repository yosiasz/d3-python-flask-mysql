DROP database IF EXISTS scheduler;

create database scheduler;

DROP TABLE IF EXISTS scheduler.sales;

CREATE  TABLE scheduler.sales (

  year INT NOT NULL ,
  age INT NOT NULL ,
  sex int NOT NULL,
  people int NOT NULL 

 );

INSERT INTO scheduler.sales(year,age, sex, people)
select 1850,0,1,1483789 union
select 1850,0,2,1450376 union
select 1850,5,1,1411067 union
select 1850,5,2,1359668 union
select 1850,10,1,1260099 ;
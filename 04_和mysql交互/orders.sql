-- 创建订单表

create table if not exists orders(
	id int unsigned primary key not null auto_increment,
	order_date_time datetime,
	customer_id int unsigned 
);

-- 创建订单详情表
create table if not exists order_detail(
	id int unsigned primary key not null auto_increment,
	order_id int unsigned not null,
	goods_id int unsigned not null,
	quantity int unsigned not null
);

-- 创建用户表
create table if not exists customer(
	id int unsigned primary key not null auto_increment,
	name varchar(40) not null,
	tel_num int unsigned not null,
	passwd varchar(20) not null,
	address varchar(200) not null
);

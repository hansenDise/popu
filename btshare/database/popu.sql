/*drop database popu;*/
create database popu;

use popu;

/* 资源类型.  如 电影，电视剧，游戏等 */
create table if not exists ResourceType(
typeid					INT AUTO_INCREMENT,
descript			VARCHAR(20),
PRIMARY KEY(typeid)
);

/* 资源. 资源描述 */
create table if not exists Resource(
resourceid 			INT AUTO_INCREMENT ,
typeid				INT,
title				VARCHAR(100) NOT NULL,
cn_title			VARCHAR(150),
release_year		INT,
languages    		VARCHAR(20),
runtime 			INT,
plot				TEXT,
poster_url  		VARCHAR(200),
hitcount			INT,
downloadcount		INT,

PRIMARY KEY(resourceid),
FOREIGN KEY(typeid) REFERENCES ResourceType(typeid)
);

/* 资源截屏图片的位置， 如电影，电视剧，游戏的截屏 */
create table if not exists Screenshot(
id					INT AUTO_INCREMENT,
resourceid			INT,
screenshot_url 		VARCHAR(200),

PRIMARY KEY(id),
FOREIGN KEY(resourceid) REFERENCES Resource(resourceid)
);

/* 预告片 */
create table if not exists Trailer(
id 					INT AUTO_INCREMENT,
resourceid			INT,
trailer_url			VARCHAR(200),

PRIMARY KEY(id),
FOREIGN KEY(resourceid) REFERENCES Resource(resourceid)
);

/* 用户表 */
create table if not exists Users(
userid				INT AUTO_INCREMENT,
name				VARCHAR(50) NOT NULL,
passwd				VARCHAR(100) NOT NULL,
email				VARCHAR(100),
cellphone			VARCHAR(15),

PRIMARY KEY(userid)
);

/* 评论 */
create table if not exists Comments(
commentid 			INT AUTO_INCREMENT,
resourceid			INT,
comments			VARCHAR(500),
userid				INT,

PRIMARY KEY(commentid),
FOREIGN KEY(resourceid) REFERENCES Resource(resourceid),
FOREIGN KEY(userid)	REFERENCES Users(userid) 
);

/* 职业类型，如导演，演员等 */
create table if not exists Proftype(
protypeid			INT AUTO_INCREMENT,
descript	VARCHAR(50),

PRIMARY KEY(protypeid)
);

/* 人物， 如导演，演员等 */
create table if not exists Peoples(
peopleid			INT AUTO_INCREMENT,
protypeid			INT,
first_name_en		VARCHAR(50),
middle_name_en		VARCHAR(50),
last_name_en		VARCHAR(50),
first_name_zh		VARCHAR(50),
middle_name_zh		VARCHAR(50),
last_name_zh		VARCHAR(50),
born_date			DATE,
summary				TEXT,

PRIMARY KEY(peopleid),
FOREIGN KEY(protypeid) REFERENCES Proftype(protypeid)
);

/* 类别, 如 动作，冒险，科幻等 */
create table if not exists Genres(
genresid 			INT AUTO_INCREMENT,
descript_en			VARCHAR(30),
descript_zh			VARCHAR(50),

PRIMARY KEY(genresid)
);

/* 种子 */
create table if not exists Torrents(
torrentid				INT AUTO_INCREMENT,
resourceid				INT,
downloadurl				VARCHAR(200),
magneturl				VARCHAR(400),
addedtime				datetime,
userid					int,
filesize				float,

PRIMARY KEY(torrentid),
FOREIGN KEY(resourceid) REFERENCES Resource(resourceid),
FOREIGN KEY(userid) REFERENCES Users(userid)
);

create table if not exists Resource_Torrents(
res_tor_id			INT AUTO_INCREMENT,
resourceid			INT,
torrentid			INT,

PRIMARY KEY(res_tor_id),
FOREIGN KEY(resourceid) REFERENCES Resource(resourceid),
FOREIGN KEY(torrentid) REFERENCES Torrents(torrentid)
);

create table if not exists Resource_Peoples(
res_peo_id				INT AUTO_INCREMENT,
resourceid				INT,
peopleid				INT,

PRIMARY KEY(res_peo_id),
FOREIGN KEY(resourceid) REFERENCES Resource(resourceid),
FOREIGN KEY(peopleid) REFERENCES Peoples(peopleid)
);

create table if not exists Resource_Genres(
res_gen_id			INT AUTO_INCREMENT,
resourceid			INT,
genresid			INT,

PRIMARY KEY(res_gen_id),
FOREIGN KEY(resourceid) REFERENCES Resource(resourceid),
FOREIGN KEY(genresid) REFERENCES Genres(genresid)
);

create table if not exists Resource_Comments(
res_com_id			INT AUTO_INCREMENT,
resourceid			INT,
commentid			INT,

PRIMARY KEY(res_com_id),
FOREIGN KEY(resourceid) REFERENCES Resource(resourceid) ,
FOREIGN KEY(commentid)  REFERENCES Comments(commentid)
);


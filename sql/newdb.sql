/*
SQLyog Community Edition- MySQL GUI v7.02 
MySQL - 5.1.59-community : Database - gene
*********************************************************************
*/


/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE IF NOT EXISTS/*!32312*/ `gene` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `gene`;

/*Table structure for table `ghis` */

DROP TABLE IF EXISTS `ghis`;

CREATE TABLE `ghis` (
  `sid` int(22) NOT NULL AUTO_INCREMENT,
  `uid` varchar(222) DEFAULT NULL,
  `gid` varchar(22) DEFAULT NULL,
  `gtype` varchar(22) DEFAULT NULL,
  PRIMARY KEY (`sid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `ghis` */

insert  into `ghis`(`sid`,`uid`,`gid`,`gtype`) values (1,'kahi','2629','extrinsic'),(2,'kahi','5580','intrinsic');

/*Table structure for table `reg` */

DROP TABLE IF EXISTS `reg`;

CREATE TABLE `reg` (
  `username` varchar(22) NOT NULL,
  `password` varchar(22) DEFAULT NULL,
  `mail` varchar(222) DEFAULT NULL,
  `mobile` varchar(222) DEFAULT NULL,
  `gender` varchar(22) DEFAULT NULL,
  `addr` varchar(222) DEFAULT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `reg` */

insert  into `reg`(`username`,`password`,`mail`,`mobile`,`gender`,`addr`) values ('kahi','123','kahilanmuthu5@gmail.com','1231231233','male','nellai\r\n');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;

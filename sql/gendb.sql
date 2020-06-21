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

/*Table structure for table `reg` */

DROP TABLE IF EXISTS `reg`;

CREATE TABLE `reg` (
  `name` varchar(25) DEFAULT NULL,
  `gender` varchar(269) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `phone` decimal(10,0) DEFAULT NULL,
  `email` varchar(26) DEFAULT NULL,
  `city` varchar(268) DEFAULT NULL,
  `uname` varchar(250) DEFAULT NULL,
  `psw` varchar(269) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `reg` */

insert  into `reg`(`name`,`gender`,`dob`,`phone`,`email`,`city`,`uname`,`psw`) values ('suresh','male','2016-10-17','7708252747','suresh.jayaram07@gmail.com','chennai','suresh','111'),('ramesh','male','2015-12-30','9830564635','suresh.jayaram07@gmail.com','chennai','ramesh','123');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;

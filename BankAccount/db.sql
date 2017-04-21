-- MySQL dump 10.13  Distrib 5.7.12, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: python_bank_project
-- ------------------------------------------------------
-- Server version	5.7.17-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `account`
--

DROP TABLE IF EXISTS `account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account` (
  `account_no` int(11) NOT NULL,
  `account_type` varchar(45) DEFAULT NULL,
  `balance` float DEFAULT NULL,
  `opening_date` date DEFAULT NULL,
  `closed_date` date DEFAULT NULL,
  `no_of_withdrawal` int(11) DEFAULT NULL,
  `status` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`account_no`),
  KEY `cust_id_fk_idx` (`account_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account`
--

LOCK TABLES `account` WRITE;
/*!40000 ALTER TABLE `account` DISABLE KEYS */;
INSERT INTO `account` VALUES (1,'Saving',15000,'2017-04-21',NULL,10,'A'),(2,'Saving',26900,'2017-04-21',NULL,10,'A'),(3,'Saving',57000,'2017-04-22',NULL,10,'A');
/*!40000 ALTER TABLE `account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `address`
--

DROP TABLE IF EXISTS `address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `address` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `address_line_1` varchar(50) DEFAULT NULL,
  `address_line_2` varchar(50) DEFAULT NULL,
  `city` varchar(45) DEFAULT NULL,
  `state` varchar(45) DEFAULT NULL,
  `pincode` varchar(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `address`
--

LOCK TABLES `address` WRITE;
/*!40000 ALTER TABLE `address` DISABLE KEYS */;
INSERT INTO `address` VALUES (2,'C-67','Govindpuram','Ghaziabad','UP','201010'),(3,'Inderlok Colony','Chor Gali','Hapur','UP','200101'),(4,'D-44','Shashtri Nagar','Ghaziabad','UP','201010');
/*!40000 ALTER TABLE `address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin` (
  `user_id` varchar(50) NOT NULL,
  `password` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='	';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES ('admin1','abcd'),('admin2','cdef'),('admin3','efgh');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customer` (
  `cust_id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(45) DEFAULT NULL,
  `first_name` varchar(45) DEFAULT NULL,
  `last_name` varchar(45) DEFAULT NULL,
  `address_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`cust_id`),
  KEY `address_id_fk_idx` (`address_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,'nadeem','Mohd','Nadeem',2),(2,'harshi','Harshi','Garg',3),(3,'nupur','Nupur','Garg',4);
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transaction`
--

DROP TABLE IF EXISTS `transaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `transaction` (
  `transaction_id` int(11) NOT NULL AUTO_INCREMENT,
  `cust_id` int(11) DEFAULT NULL,
  `transaction_type` varchar(100) DEFAULT NULL,
  `initial_balance` float DEFAULT NULL,
  `withdrawals` float DEFAULT NULL,
  `deposits` float DEFAULT NULL,
  `balance` float DEFAULT NULL,
  `time_of_transaction` datetime DEFAULT NULL,
  `from_account` int(11) DEFAULT NULL,
  `to_account` int(11) DEFAULT NULL,
  PRIMARY KEY (`transaction_id`),
  KEY `cust_id_fk_idx` (`cust_id`),
  KEY `transaction_type_fk_idx` (`transaction_type`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transaction`
--

LOCK TABLES `transaction` WRITE;
/*!40000 ALTER TABLE `transaction` DISABLE KEYS */;
INSERT INTO `transaction` VALUES (8,2,'Transfer-D',26000,NULL,900,26900,'2017-04-22 00:10:47',1,NULL),(9,1,'Transfer-W',14900,900,NULL,14000,'2017-04-22 00:10:48',NULL,2),(10,3,'Deposit',50000,NULL,10000,60000,'2017-04-22 00:57:22',NULL,NULL),(11,3,'Withdrawal',60000,2000,NULL,58000,'2017-04-22 00:57:30',NULL,NULL),(12,1,'Transfer-D',14000,NULL,1000,15000,'2017-04-22 00:57:46',3,NULL),(13,3,'Transfer-W',58000,1000,NULL,57000,'2017-04-22 00:57:46',NULL,1);
/*!40000 ALTER TABLE `transaction` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-04-22  1:25:49

-- MySQL dump 10.13  Distrib 5.7.21, for Linux (x86_64)
--
-- Host: localhost    Database: cse311db
-- ------------------------------------------------------
-- Server version	5.7.21-0ubuntu0.17.10.1

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
-- Table structure for table `flights`
--

DROP TABLE IF EXISTS `flights`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `flights` (
  `id` char(6) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `time` varchar(10) DEFAULT NULL,
  `from` varchar(15) DEFAULT NULL,
  `to` varchar(15) DEFAULT NULL,
  `seats` int(3) DEFAULT '320',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flights`
--

LOCK TABLES `flights` WRITE;
/*!40000 ALTER TABLE `flights` DISABLE KEYS */;
INSERT INTO `flights` VALUES ('BAY001','Baywatch','Twilight','White Harbor','Gulltown',320),('BAY002','Baywatch','Dawn','White Harbor','Gulltown',320),('BAY003','Baywatch','Dawn','White Harbor','King\'s Landing',320),('BAY004','Baywatch','Night','White Harbor','Lannisport',320),('BAY005','Baywatch','Night','White Harbor','King\'s Landing',320),('BAY006','Baywatch','Noon','White Harbor','Oldtown',320),('CFL001','Capital Flights','Noon','King\'s Landing','Gulltown',320),('CFL002','Capital Flights','Noon','King\'s Landing','Lannisport',320),('CFL003','Capital Flights','Dawn','King\'s Landing','Oldtown',320),('CFL004','Capital Flights','Night','King\'s Landing','White Harbor',320),('LPR001','Lion\'s Pride','Dawn','Lannisport','King\'s Landing',320),('LPR002','Lion\'s Pride','Dusk','Lannisport','King\'s Landing',320),('LPR003','Lion\'s Pride','Dusk','Lannisport','Gulltown',320),('LPR004','Lion\'s Pride','Night','Lannisport','White Harbor',320),('LPR005','Lion\'s Pride','Noon','Lannisport','Oldtown',320),('OLD001','Old Air','Dawn','Oldtown','King\'s Landing',320),('OLD002','Old Air','Noon','Oldtown','Lannisport',320),('OLD003','Old Air','Night','Oldtown','Lannisport',320),('OLD004','Old Air','Dawn','Oldtown','White Harbor',320),('OLD005','Old Air','Dusk','Oldtown','White Harbor',320),('SGA001','Seagull Airlines','Dawn','Gulltown','King\'s Landing',320),('SGA002','Seagull Airlines','Noon','Gulltown','King\'s Landing',320),('SGA003','Seagull Airlines','Dusk','Gulltown','King\'s Landing',320),('SGA004','Seagull Airlines','Dawn','Gulltown','Lannisport',320),('SGA005','Seagull Airlines','Dusk','Gulltown','Lannisport',320),('SGA006','Seagull Airlines','Twilight','Gulltown','White Harbor',320),('SGA007','Seagull Airlines','Night','Gulltown','White Harbor',320);
/*!40000 ALTER TABLE `flights` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `passengers`
--

DROP TABLE IF EXISTS `passengers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `passengers` (
  `passportnumber` int(10) NOT NULL,
  `ticket_id` int(3) DEFAULT NULL,
  `firstname` varchar(20) DEFAULT NULL,
  `lastname` varchar(20) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `passwordhash` char(65) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `passengers`
--

LOCK TABLES `passengers` WRITE;
/*!40000 ALTER TABLE `passengers` DISABLE KEYS */;
/*!40000 ALTER TABLE `passengers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pricing`
--

DROP TABLE IF EXISTS `pricing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pricing` (
  `class` varchar(10) DEFAULT NULL,
  `time` varchar(10) DEFAULT NULL,
  `price` int(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pricing`
--

LOCK TABLES `pricing` WRITE;
/*!40000 ALTER TABLE `pricing` DISABLE KEYS */;
INSERT INTO `pricing` VALUES ('First','Dawn',1024),('First','Noon',512),('First','Twilight',512),('First','Dusk',256),('First','Night',1024),('Business','Dawn',1000),('Business','Noon',500),('Business','Twilight',500),('Business','Dusk',230),('Business','Night',1000),('Economy','Dawn',500),('Economy','Noon',250),('Economy','Twilight',250),('Economy','Dusk',130),('Economy','Night',600);
/*!40000 ALTER TABLE `pricing` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tickets`
--

DROP TABLE IF EXISTS `tickets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tickets` (
  `id` int(3) NOT NULL AUTO_INCREMENT,
  `flight_id` char(6) NOT NULL,
  `passenger_id` int(10) NOT NULL,
  `seat` int(3) DEFAULT NULL,
  `class` varchar(10) DEFAULT NULL,
  `price` int(4) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tickets`
--

LOCK TABLES `tickets` WRITE;
/*!40000 ALTER TABLE `tickets` DISABLE KEYS */;
INSERT INTO `tickets` VALUES (1,'BAY003',0,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `tickets` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-04-08 10:12:39

-- phpMyAdmin SQL Dump
-- version 4.0.5
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Jun 25, 2014 at 02:55 PM
-- Server version: 5.0.96-community-log
-- PHP Version: 5.3.17

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `leonorag_apm`
--

-- --------------------------------------------------------

--
-- Table structure for table `reading`
--

CREATE TABLE IF NOT EXISTS `reading` (
  `id` int(10) NOT NULL auto_increment,
  `model` varchar(255) default NULL,
  `serial` varchar(255) default NULL,
  `target_ip` varchar(255) default NULL,
  `total_count` varchar(255) default NULL,
  `colour_count` varchar(255) default NULL,
  `loc` varchar(255) default NULL,
  `collector_date` varchar(255) default NULL,
  `site_ip` varchar(255) default NULL,
  `sys_date` timestamp NOT NULL default CURRENT_TIMESTAMP,
  `bl` varchar(255) default NULL,
  `blt` varchar(255) default NULL,
  `cl` varchar(255) default NULL,
  `clt` varchar(255) default NULL,
  `ml` varchar(255) default NULL,
  `mlt` varchar(255) default NULL,
  `yl` varchar(255) default NULL,
  `ylt` varchar(255) default NULL,
  `trans` varchar(255) default NULL,
  `transt` varchar(255) default NULL,
  `docfeeder` varchar(255) default NULL,
  `docfeeedert` varchar(255) default NULL,
  `fuser` varchar(255) default NULL,
  `fusert` varchar(255) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=105 ;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;


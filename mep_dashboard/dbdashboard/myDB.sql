-- phpMyAdmin SQL Dump
-- version 4.7.9
-- https://www.phpmyadmin.net/
--
-- Host: mysql
-- Generation Time: Apr 05, 2018 at 12:47 PM
-- Server version: 8.0.3-rc-log
-- PHP Version: 7.2.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `myDB`
--

-- --------------------------------------------------------

--
-- Table structure for table `Departments`
--

CREATE TABLE `Departments` (
  `id` int(11) NOT NULL,
  `name` varchar(75) NOT NULL,
  `acronym` varchar(8) NOT NULL,
  `head_id` int(11) NOT NULL,
  `is_active` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Teams`
--

CREATE TABLE `Teams` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `dpt_id` int(11) NOT NULL,
  `lead_id` int(11) NOT NULL,
  `head_id` int(11) NOT NULL,
  `section_name` varchar(8) NOT NULL,
  `is_active` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `Users`
--

CREATE TABLE `Users` (
  `id` int(11) NOT NULL,
  `username` varchar(8) NOT NULL,
  `team_id` int(11) NOT NULL,
  `first_name` varchar(15) NOT NULL,
  `last_name` varchar(15) NOT NULL,
  `date_in` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `last_connection` datetime DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `Users`
--

INSERT INTO `Users` (`id`, `username`, `team_id`, `first_name`, `last_name`, `date_in`, `last_connection`, `is_active`) VALUES
(2, 'lcorrevo', 1, 'loic', 'correvon', '2018-04-05 00:00:00', '2018-04-05 00:00:00', 1),
(10, 'brocha', 1, '', '', '2018-04-05 12:01:51', '2018-04-05 12:01:51', 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Users`
--
ALTER TABLE `Users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Users`
--
ALTER TABLE `Users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

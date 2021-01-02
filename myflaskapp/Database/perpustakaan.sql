-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 02, 2021 at 01:18 AM
-- Server version: 10.4.8-MariaDB
-- PHP Version: 7.3.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `perpustakaan`
--

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

CREATE TABLE `books` (
  `id` int(11) NOT NULL,
  `judul` varchar(100) NOT NULL,
  `pengarang` varchar(50) NOT NULL,
  `penerbit` varchar(50) NOT NULL,
  `tahun` year(4) NOT NULL,
  `rak` int(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `books`
--

INSERT INTO `books` (`id`, `judul`, `pengarang`, `penerbit`, `tahun`, `rak`) VALUES
(2, 'Dilan 1998', 'Joko Widodo', 'PT. Gramedia', 2018, 1),
(4, 'Komik One Piece', 'Eichiiro Oda', 'Shueisha', 1998, 5),
(5, 'Harry Potter', 'J.K. Rowling', 'Warner Bross', 2005, 1),
(7, 'Cerita Rakyat', 'David', 'PT. Gadgetin', 2016, 2),
(8, 'Secangkir Kopi', 'Uut Dwisetya', 'Jawa Pos', 2017, 1),
(9, '7 Keajaiban Rezeki', 'Ippho Santosa', 'Gramedia', 2010, 3),
(10, 'hewan', 'robert', 'jasa', 2018, 2),
(13, 'Belajar Pemrograman', 'Aga', 'univ', 2020, 4);

-- --------------------------------------------------------

--
-- Table structure for table `borrow`
--

CREATE TABLE `borrow` (
  `id` int(11) NOT NULL,
  `id_buku` int(11) NOT NULL,
  `id_students` int(11) NOT NULL,
  `id_staff` int(11) NOT NULL,
  `tanggal_pinjam` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Triggers `borrow`
--
DELIMITER $$
CREATE TRIGGER `inserttoriwayat` AFTER INSERT ON `borrow` FOR EACH ROW INSERT INTO riwayatpeminjaman SET id_buku=NEW.id_buku, id_student=NEW.id_students, id_staff=NEW.id_staff, tanggal_pinjam=NEW.tanggal_pinjam
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `riwayatpeminjaman`
--

CREATE TABLE `riwayatpeminjaman` (
  `id` int(11) NOT NULL,
  `id_buku` int(11) NOT NULL,
  `id_student` int(11) NOT NULL,
  `id_staff` int(11) NOT NULL,
  `tanggal_pinjam` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `riwayatpeminjaman`
--

INSERT INTO `riwayatpeminjaman` (`id`, `id_buku`, `id_student`, `id_staff`, `tanggal_pinjam`) VALUES
(1, 2, 2, 1, '2020-12-26'),
(2, 4, 1, 1, '2020-12-27'),
(3, 2, 2, 1, '2020-12-27'),
(4, 5, 1, 1, '2020-12-27'),
(5, 9, 1, 1, '2020-12-27'),
(6, 10, 2, 1, '2020-12-27'),
(7, 4, 2, 1, '2020-12-27'),
(8, 10, 1, 1, '2020-12-27'),
(9, 9, 1, 1, '2020-12-27'),
(10, 9, 1, 1, '2020-12-27'),
(11, 4, 2, 1, '2020-12-27'),
(12, 10, 2, 1, '2020-12-27'),
(13, 4, 1, 1, '2020-12-27'),
(14, 9, 2, 1, '2020-12-27'),
(15, 4, 1, 1, '2020-12-27'),
(16, 10, 1, 1, '2020-12-27'),
(17, 13, 1, 1, '2020-12-30');

-- --------------------------------------------------------

--
-- Table structure for table `staff`
--

CREATE TABLE `staff` (
  `id` int(11) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `nip` varchar(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `contact` varchar(20) NOT NULL,
  `alamat` varchar(100) NOT NULL,
  `pass` varchar(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `staff`
--

INSERT INTO `staff` (`id`, `nama`, `nip`, `email`, `contact`, `alamat`, `pass`) VALUES
(1, 'Hendra', '232456', 'hendra@gmail.com', '081523499778', 'Jl. Jawa 7 - Jember', 'abc12345');

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `id` int(11) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `nim` varchar(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `contact` varchar(20) NOT NULL,
  `alamat` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`id`, `nama`, `nim`, `email`, `contact`, `alamat`) VALUES
(1, 'Afif Nurrudin', '192410102039', 'afif.nrd@gmail.com', '087755657123', 'Jl. Kalimantan 10 - Jember'),
(2, 'Ade Londok', '172410101009', 'ade.londok@gmail.com', '083847317655', 'Jl. Sukorambi No. 7');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `borrow`
--
ALTER TABLE `borrow`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_buku` (`id_buku`),
  ADD KEY `id_students` (`id_students`),
  ADD KEY `id_staff` (`id_staff`);

--
-- Indexes for table `riwayatpeminjaman`
--
ALTER TABLE `riwayatpeminjaman`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `staff`
--
ALTER TABLE `staff`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `books`
--
ALTER TABLE `books`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `borrow`
--
ALTER TABLE `borrow`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;

--
-- AUTO_INCREMENT for table `riwayatpeminjaman`
--
ALTER TABLE `riwayatpeminjaman`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `staff`
--
ALTER TABLE `staff`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `students`
--
ALTER TABLE `students`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `borrow`
--
ALTER TABLE `borrow`
  ADD CONSTRAINT `borrow_ibfk_1` FOREIGN KEY (`id_buku`) REFERENCES `books` (`id`),
  ADD CONSTRAINT `borrow_ibfk_2` FOREIGN KEY (`id_students`) REFERENCES `students` (`id`),
  ADD CONSTRAINT `borrow_ibfk_3` FOREIGN KEY (`id_staff`) REFERENCES `staff` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

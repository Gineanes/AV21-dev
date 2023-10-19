-- phpMyAdmin SQL Dump
-- version 4.5.4.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: 19-Out-2023 às 13:11
-- Versão do servidor: 5.7.11
-- PHP Version: 5.6.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bd_financeira`
--
CREATE DATABASE IF NOT EXISTS `bd_financeira` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `bd_financeira`;

-- --------------------------------------------------------

--
-- Estrutura da tabela `tb_dado`
--

CREATE TABLE `tb_dado` (
  `codigo` int(11) NOT NULL,
  `TipoMovimentaçãoFinanceira` varchar(255) NOT NULL,
  `descricao` varchar(255) NOT NULL,
  `valor` varchar(9) NOT NULL,
  `categoria` varchar(255) NOT NULL,
  `dataMovimentacao` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Extraindo dados da tabela `tb_dado`
--

INSERT INTO `tb_dado` (`codigo`, `TipoMovimentaçãoFinanceira`, `descricao`, `valor`, `categoria`, `dataMovimentacao`) VALUES
(2, 'Entrada', 'Nota paga', '200', 'Receita', '2023-10-17'),
(4, 'Selecione', '', '', '', '2000-01-01'),
(5, 'Saída', 'recebere', '1.5', 'Despesa', '2000-01-01');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tb_dado`
--
ALTER TABLE `tb_dado`
  ADD PRIMARY KEY (`codigo`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tb_dado`
--
ALTER TABLE `tb_dado`
  MODIFY `codigo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3308
-- Généré le :  Dim 27 oct. 2019 à 20:42
-- Version du serveur :  5.7.26
-- Version de PHP :  7.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `data`
--

-- --------------------------------------------------------

--
-- Structure de la table `movies`
--

DROP TABLE IF EXISTS `movies`;
CREATE TABLE IF NOT EXISTS `movies` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Title` varchar(200) NOT NULL,
  `ReleaseYear` varchar(50) NOT NULL,
  `Rank` varchar(10) NOT NULL,
  `Rating` varchar(10) NOT NULL,
  `Url` varchar(10) NOT NULL,
  `Image` varchar(500) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

--
-- Déchargement des données de la table `movies`
--

INSERT INTO `movies` (`id`, `Title`, `ReleaseYear`, `Rank`, `Rating`, `Url`, `Image`) VALUES
(6, 'Les évadés', '(1994)', ' ', '9,2', ' ', ''),
(5, 'iron', '2018', '7', '8', 'okok', 'wiii'),
(7, 'Le parrain', '(1972)', ' ', '9,1', ' ', ''),
(8, 'Le parrain, 2ème partie', '(1974)', ' ', '9,0', ' ', ''),
(9, 'The Dark Knight: Le chevalier noir', '(2008)', ' ', '9,0', ' ', ''),
(10, 'Douze hommes en colère', '(1957)', ' ', '8,9', ' ', ''),
(11, 'La liste de Schindler', '(1993)', ' ', '8,9', ' ', ''),
(12, 'Le seigneur des anneaux: Le retour du roi', '(2003)', ' ', '8,9', ' ', ''),
(13, 'Pulp Fiction', '(1994)', ' ', '8,9', ' ', ''),
(14, 'Le bon, la brute et le truand', '(1966)', ' ', '8,8', ' ', ''),
(15, 'iron', '2018', '7', '8', 'oooo', 'eee');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

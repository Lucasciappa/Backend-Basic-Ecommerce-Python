-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.4.14-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.1.0.6116
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para ecommerce
CREATE DATABASE IF NOT EXISTS `ecommerce` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `ecommerce`;

-- Volcando estructura para tabla ecommerce.bancos
CREATE TABLE IF NOT EXISTS `bancos` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(40) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla ecommerce.bancos: ~7 rows (aproximadamente)
/*!40000 ALTER TABLE `bancos` DISABLE KEYS */;
INSERT INTO `bancos` (`ID`, `nombre`) VALUES
	(1, 'Banco Galicia'),
	(2, 'Banco Frances'),
	(3, 'Banco Ciudad'),
	(4, 'Banco Itau'),
	(5, 'Banco Macro'),
	(6, 'Banco ICBC'),
	(7, 'Banco HSBC');
/*!40000 ALTER TABLE `bancos` ENABLE KEYS */;

-- Volcando estructura para vista ecommerce.banco_clientes
-- Creando tabla temporal para superar errores de dependencia de VIEW
CREATE TABLE `banco_clientes` (
	`apellido` VARCHAR(40) NOT NULL COLLATE 'utf8mb4_general_ci',
	`nombre` VARCHAR(40) NOT NULL COLLATE 'utf8mb4_general_ci'
) ENGINE=MyISAM;

-- Volcando estructura para tabla ecommerce.categorias
CREATE TABLE IF NOT EXISTS `categorias` (
  `ID` int(10) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla ecommerce.categorias: ~11 rows (aproximadamente)
/*!40000 ALTER TABLE `categorias` DISABLE KEYS */;
INSERT INTO `categorias` (`ID`, `nombre`) VALUES
	(1, 'Microprocesadores'),
	(2, 'Motherboards'),
	(3, 'Placas graficas'),
	(4, 'Fuentes'),
	(5, 'Discos'),
	(6, 'Memorias'),
	(7, 'Gabinetes'),
	(8, 'Monitores'),
	(9, 'Teclados'),
	(10, 'Mouses');
/*!40000 ALTER TABLE `categorias` ENABLE KEYS */;

-- Volcando estructura para tabla ecommerce.ciudades
CREATE TABLE IF NOT EXISTS `ciudades` (
  `ID` int(10) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(40) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=214 DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla ecommerce.ciudades: ~11 rows (aproximadamente)
/*!40000 ALTER TABLE `ciudades` DISABLE KEYS */;
INSERT INTO `ciudades` (`ID`, `nombre`) VALUES
	(1, 'CABA'),
	(2, 'Rosario'),
	(3, 'Santa Rosa'),
	(12, 'Carmelo'),
	(15, 'Montevideo'),
	(71, 'Barcelona'),
	(190, 'Valencia'),
	(209, 'Tres Arroyos'),
	(210, 'Chascomus'),
	(211, 'Marcos Paz'),
	(212, 'Villa Adelina'),
	(213, 'Villa Celina');
/*!40000 ALTER TABLE `ciudades` ENABLE KEYS */;

-- Volcando estructura para tabla ecommerce.compras
CREATE TABLE IF NOT EXISTS `compras` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `fecha_compra` date NOT NULL,
  `id_usuario` int(10) DEFAULT NULL,
  `precio_final` int(11) NOT NULL DEFAULT 0,
  `nombre` varchar(30) NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `usuario` (`id_usuario`),
  CONSTRAINT `usuario` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=68 DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla ecommerce.compras: ~31 rows (aproximadamente)
/*!40000 ALTER TABLE `compras` DISABLE KEYS */;
INSERT INTO `compras` (`ID`, `fecha_compra`, `id_usuario`, `precio_final`, `nombre`) VALUES
	(3, '2020-11-30', 4, 17999, 'Placa de video Asus Nvidia GTX'),
	(35, '2020-11-30', 4, 3900, 'Disco SSD 240 GB Kingston '),
	(36, '2020-11-30', 4, 899, 'Teclado Logitech USB'),
	(37, '2020-11-30', 4, 9399, 'Fuente Alimentacion Sentey 850'),
	(38, '2020-12-01', 4, 2330, 'Memoria RAM 4GB Kingston'),
	(39, '2020-12-01', 4, 22999, 'Placa de video Gigabyte Nvidia'),
	(40, '2020-12-01', 4, 2299, 'Fuente Alimentacion Casio 550w'),
	(41, '2020-12-01', 4, 2900, 'Disco SSD 120 GB Kingston'),
	(42, '2020-12-01', 4, 2299, 'Fuente Alimentacion Casio 550w'),
	(43, '2020-12-01', 4, 4999, 'Gabinete Oficina Dell'),
	(44, '2020-12-01', 32, 2299, 'Fuente Alimentacion Casio 550w'),
	(45, '2020-12-01', 32, 899, 'Teclado Logitech USB'),
	(46, '2020-12-01', 4, 9399, 'Fuente Alimentacion Sentey 850'),
	(47, '2020-12-01', 4, 699, 'Mouse Genius Oficina'),
	(48, '2020-12-01', 32, 68999, 'Placa de video Radeon 5700 ser'),
	(49, '2020-12-01', 32, 5400, 'Disco SSD 480 GB Kingston '),
	(50, '2020-12-01', 32, 40000, 'Microprocesador Intel Core I7 '),
	(51, '2020-12-01', 15, 3900, 'Disco SSD 240 GB Kingston '),
	(52, '2020-12-01', 15, 4999, 'Gabinete Oficina Dell'),
	(53, '2020-12-01', 15, 20999, 'Motherboard Asrock x570 am4'),
	(54, '2020-12-01', 4, 2299, 'Fuente Alimentacion Casio 550w'),
	(55, '2020-12-01', 4, 7499, 'Gabinete Gamer Acer Vidrio tem'),
	(56, '2020-12-01', 4, 15650, 'Microprocesador gamer AMD Ryze'),
	(57, '2020-12-01', 33, 2299, 'Fuente Alimentacion Casio 550w'),
	(58, '2020-12-01', 4, 56999, 'Monitor 24\'\' Asus Curvo '),
	(59, '2020-12-01', 32, 68999, 'Placa de video Radeon 5700 ser'),
	(60, '2020-12-01', 32, 3699, 'Fuente Alimentacion Sentey 550'),
	(61, '2020-12-01', 32, 7499, 'Gabinete Gamer Acer Vidrio tem'),
	(62, '2020-12-01', 15, 17999, 'Placa de video Asus Nvidia GTX'),
	(63, '2020-12-01', 15, 3699, 'Fuente Alimentacion Sentey 550'),
	(64, '2020-12-01', 15, 7699, 'Motherboard Asrock amd a320m'),
	(65, '2020-12-01', 15, 7699, 'Motherboard Asrock amd a320m'),
	(66, '2020-12-02', 6, 5099, 'Placa de video Asus Nvidia GT '),
	(67, '2020-12-02', 6, 2330, 'Memoria RAM 4GB Kingston');
/*!40000 ALTER TABLE `compras` ENABLE KEYS */;

-- Volcando estructura para vista ecommerce.listaprecios
-- Creando tabla temporal para superar errores de dependencia de VIEW
CREATE TABLE `listaprecios` (
	`nombre` VARCHAR(40) NOT NULL COLLATE 'utf8mb4_general_ci',
	`precio` VARCHAR(24) NOT NULL COLLATE 'utf8mb4_general_ci',
	`marca` VARCHAR(20) NULL COLLATE 'utf8mb4_general_ci'
) ENGINE=MyISAM;

-- Volcando estructura para tabla ecommerce.marcas
CREATE TABLE IF NOT EXISTS `marcas` (
  `ID` int(10) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla ecommerce.marcas: ~24 rows (aproximadamente)
/*!40000 ALTER TABLE `marcas` DISABLE KEYS */;
INSERT INTO `marcas` (`ID`, `nombre`) VALUES
	(1, 'Acer'),
	(2, 'Razer'),
	(3, 'Asus'),
	(4, 'HP'),
	(5, 'Lenovo'),
	(6, 'Dell'),
	(7, 'Genius'),
	(8, 'Gigabyte'),
	(9, 'ASRock'),
	(10, 'Radeon'),
	(12, 'Genius'),
	(13, 'Casio'),
	(14, 'Logitech'),
	(15, 'Panasonic'),
	(16, 'Samsung'),
	(17, 'ViewSonic'),
	(18, 'Intel'),
	(19, 'AMD'),
	(20, 'Corsair'),
	(21, 'Kingston'),
	(22, 'HyperX'),
	(23, 'Sentey'),
	(24, 'Seagate'),
	(27, 'Reddragon');
/*!40000 ALTER TABLE `marcas` ENABLE KEYS */;

-- Volcando estructura para tabla ecommerce.productos
CREATE TABLE IF NOT EXISTS `productos` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(40) NOT NULL,
  `precio` double NOT NULL,
  `id_categoria` int(11) NOT NULL,
  `id_marca` int(11) NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `categoria` (`id_categoria`),
  KEY `marca` (`id_marca`),
  CONSTRAINT `categoria` FOREIGN KEY (`id_categoria`) REFERENCES `categorias` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `marca` FOREIGN KEY (`id_marca`) REFERENCES `marcas` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla ecommerce.productos: ~46 rows (aproximadamente)
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
INSERT INTO `productos` (`ID`, `nombre`, `precio`, `id_categoria`, `id_marca`) VALUES
	(1, 'Microprocesador gamer AMD Ryzen 5 2600', 15650, 1, 19),
	(2, 'Memoria RAM 8GB HyperX ddr4', 3790, 6, 22),
	(3, 'Gabinete Gamer Sentey k20', 15300, 7, 23),
	(4, 'Mouse Razer Deathadder', 6780, 10, 2),
	(5, 'Microprocesador Intel Core I7 10800', 40000, 1, 18),
	(6, 'Memoria RAM 4GB Hyperx ddr4', 2740, 6, 22),
	(7, 'Memoria RAM 4GB Kingston', 2330, 6, 21),
	(8, 'Memoria RAM 16GB Corsair', 13650, 6, 20),
	(9, 'Memoria RAM 8GB Corsair', 8450, 6, 20),
	(10, 'Disco Duro 1TB Seagate', 4200, 5, 24),
	(11, 'Disco Duro 2TB Seagate', 6400, 6, 24),
	(13, 'Disco SSD 120 GB Kingston', 2900, 5, 21),
	(14, 'Disco SSD 240 GB Kingston ', 3900, 5, 21),
	(15, 'Disco SSD 480 GB Kingston ', 5400, 5, 21),
	(16, 'Disco SSD 240 GB Gigabyte', 3499, 5, 8),
	(17, 'Gabinete Pc Gamer Sentey x10', 9499, 7, 23),
	(18, 'Gabinete Pc Gamer Sentey j20', 15999, 7, 23),
	(19, 'Monitor 24\'\' Asus Curvo ', 56999, 8, 3),
	(20, 'Monitor 19\'\' Samsumg ', 13999, 8, 16),
	(21, 'Monitor 24\'\' Samsung Curvo', 25999, 8, 16),
	(22, 'Monitor 19\'\' HP ', 12999, 8, 4),
	(23, 'Fuente Alimentacion Casio 550w', 2299, 4, 13),
	(24, 'Fuente Alimentacion Sentey 550w', 3699, 4, 23),
	(25, 'Fuente Alimentacion Sentey 850w', 9399, 4, 23),
	(26, 'Microprocesador Intel Core i5 9400', 16299, 1, 18),
	(27, 'Microprocesador Intel Core i3 9100', 8999, 1, 18),
	(30, 'Microprocesador AMD A10 9700', 11999, 1, 19),
	(31, 'Memoria RAM 4GB Hyperx ddr3', 3299, 6, 22),
	(32, 'Mouse Genius Oficina', 699, 10, 7),
	(33, 'Mouse Asus Gamer', 1999, 10, 3),
	(34, 'Mouse Gamer Logitech', 4799, 10, 14),
	(35, 'Motherboard Gigabyte b356m ', 13899, 2, 8),
	(36, 'Motherboard Gigabyte Amd a320m', 7299, 2, 8),
	(37, 'Motherboard Asus b450m', 9399, 2, 8),
	(38, 'Motherboard Asrock x570 am4', 20999, 2, 9),
	(39, 'Motherboard Asrock amd a320m', 7699, 2, 9),
	(40, 'Placa de video Asus Nvidia GT 700 1GB', 5099, 3, 3),
	(41, 'Placa de video Asus Nvidia GTX 1050', 17999, 3, 3),
	(42, 'Placa de video Radeon 5700 series RX', 68999, 3, 10),
	(43, 'Placa de video Gigabyte Nvidia GTX 1650', 22999, 3, 8),
	(44, 'Gabinete Gamer Acer Vidrio templado', 7499, 7, 1),
	(46, 'Gabinete Lenovo Oficina', 3999, 7, 5),
	(48, 'Gabinete Oficina Dell', 4999, 7, 6),
	(49, 'Teclado Logitech USB', 899, 9, 14),
	(50, 'Teclado Genius Oficina', 999, 9, 12),
	(51, 'Monitor 21\'\' ViewSonic', 15999, 8, 17),
	(52, 'Monitor ViewSonic Gamer 24\'\'', 36999, 8, 17),
	(56, 'Mouse Gamer Reddragon', 4599, 10, 27);
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;

-- Volcando estructura para tabla ecommerce.usuarios
CREATE TABLE IF NOT EXISTS `usuarios` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(40) NOT NULL,
  `apellido` varchar(40) NOT NULL,
  `fecha_nac` date NOT NULL,
  `interes` varchar(100) NOT NULL,
  `celular` varchar(30) NOT NULL,
  `email` varchar(40) NOT NULL,
  `contraseña` varchar(40) NOT NULL,
  `genero` char(1) NOT NULL,
  `id_ciudad` int(10) DEFAULT NULL,
  `id_banco` int(10) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `ciudad` (`id_ciudad`),
  KEY `banco` (`id_banco`),
  CONSTRAINT `banco` FOREIGN KEY (`id_banco`) REFERENCES `bancos` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `ciudad` FOREIGN KEY (`id_ciudad`) REFERENCES `ciudades` (`ID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb4;

-- Volcando datos para la tabla ecommerce.usuarios: ~20 rows (aproximadamente)
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` (`ID`, `nombre`, `apellido`, `fecha_nac`, `interes`, `celular`, `email`, `contraseña`, `genero`, `id_ciudad`, `id_banco`) VALUES
	(4, 'Lucas', 'Ciapparelli', '1997-07-04', 'Monitor Samsung 24"', '1531063791', 'lucasciappa97@gmail.com', 'U2FubG9yZW56by4x\n', 'M', 1, 4),
	(5, 'Mariana', 'Collado', '1995-03-11', 'Monitor 19\'\' con entrada HDMI', '1535424321', 'maricollado@gmail.com', 'Uml2ZXIuMTIz\n', 'F', 15, 1),
	(6, 'Martin', 'Gorriti', '1996-03-05', 'Microprocesador I7 y Mother compatible', '1524312142', 'martinggorra@gmail.com', 'U2FubG9yZW56by4x\n', 'M', 71, 2),
	(7, 'Maria Elena', 'Fuceneco', '1975-09-02', 'Teclado y mouse genius', '1560773356', 'mariaelenafuce@hotmail.com', 'Uml2ZXIuMTIz\n', 'F', 15, 6),
	(8, 'Valeria', 'Comizzo', '1994-11-21', 'Fuente de alimentacion de 550w', '1520266399', 'valecomizzo@gmail.com', 'QmFuZmllbGQuMTIz\n', 'F', 2, 7),
	(9, 'Lucio', 'Lagrott', '1998-04-13', 'Memoria RAM 8GB', '1512321514', 'luciolagrott@gmail.com', 'Uml2ZXIuMTIz\n', 'M', 213, 5),
	(10, 'Lorena', 'Fazio', '1977-05-12', 'Monitor ViewSonic 21\'\'', '1556748890', 'lorefazio@gmail.com', 'Qm9jYS4xMjM=\n', 'F', 1, 5),
	(11, 'Marcos', 'Oliva', '1997-10-25', 'Disco SSD 240gb y teclado logitech', '1553679932', 'marcosoliva@hotmail.com', 'Qm9rZS4xMjM=\n', 'M', 3, 3),
	(13, 'Valeria', 'Rivero', '1986-11-15', 'Placa Madre compatible con Intel i5', '1532943245', 'valerivero@gmail.com', 'UG9sbGl0by4xMjM=\n', 'F', 2, 3),
	(14, 'Victor', 'Ciappa', '1951-03-10', 'motherboard compatible con i3', '1541026596', 'jvicotr51@hotmail.com', 'UGF0aXRvLjEyMw==\n', 'M', 1, 7),
	(15, 'Diego', 'Maradona', '1960-10-30', 'Disco Duro 1TB', '15425903412', 'diegote@gmail.com', 'dkFNT1NCT0NBMTIz\n', 'M', 71, 1),
	(16, 'Pablo', 'Michellini', '1989-07-17', 'Disco SSD 480gb cualquiera', '1560243322', 'pablomiche@gmail.com', 'RHVwaWEuMTIz\n', 'M', 12, 4),
	(30, 'Jose', 'Tarragona', '1976-04-02', 'Placa grafica 4gb', '1590324566', 'jose76@gmail.com', 'U2FubG9yZW56by4x\n', 'M', 190, 5),
	(31, 'Valentina', 'Vila', '1998-02-28', 'Memoria RAM 4gb', '1552679923', 'valenvila@gmail.com', 'Qm9jYS4xMjM=\n', 'F', 15, 6),
	(32, 'Maria', 'Krzisnik', '1965-04-11', 'Mouse y Teclado de oficina', '1531073456', 'retnecinu@hotmail.com', 'Uml2ZXIuMTIz\n', 'F', 209, 2),
	(33, 'Felix', 'Orode', '1989-09-02', 'Memoria RAM 8gb', '1155784335', 'felixorode@gmail.com', 'U2FubG9yZW56by4x\n', 'M', 210, 3),
	(34, 'Luciano', 'Castro', '1979-09-10', 'Monitor ViewSonic 20"', '1552432266', 'castrolu@gmail.com', 'Qm9jYS4xMjM=\n', 'M', 211, 1),
	(35, 'Graciela', 'Alfano', '1951-09-21', 'Disco SSD 480gb', '1527789435', 'grace@gmail.com', 'R3JhY2UuMTIz\n', 'F', 1, 6),
	(36, 'Ricardo', 'Fort', '1977-09-02', 'Monitor samsung curvo', '15324232141', 'riki@gmail.com', 'U2FubG9yZW56by4x\n', 'M', 211, 4);
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;

-- Volcando estructura para vista ecommerce.banco_clientes
-- Eliminando tabla temporal y crear estructura final de VIEW
DROP TABLE IF EXISTS `banco_clientes`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `banco_clientes` AS SELECT usuarios.apellido,bancos.nombre FROM usuarios 
INNER JOIN bancos ON usuarios.id_banco = bancos.ID ;

-- Volcando estructura para vista ecommerce.listaprecios
-- Eliminando tabla temporal y crear estructura final de VIEW
DROP TABLE IF EXISTS `listaprecios`;
CREATE ALGORITHM=UNDEFINED SQL SECURITY DEFINER VIEW `listaprecios` AS SELECT (productos.nombre) nombre , CONCAT('$',SPACE(1),productos.precio) AS precio , (marcas.nombre) marca FROM productos
INNER JOIN marcas ON productos.id_marca=marcas.ID
ORDER BY marca ;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

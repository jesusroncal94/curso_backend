-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 15-10-2019 a las 10:19:05
-- Versión del servidor: 10.4.6-MariaDB
-- Versión de PHP: 7.3.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `mydb`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `areas`
--

CREATE TABLE `areas` (
  `idarea` int(11) NOT NULL,
  `descripcion` varchar(45) DEFAULT NULL,
  `relacion` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `areas`
--

INSERT INTO `areas` (`idarea`, `descripcion`, `relacion`) VALUES
(1, 'GERENCIA GENERAL', 0),
(2, 'GERENCIA TÉCNICA', 1),
(3, 'GERENCIA ADM Y FINANZAS', 1),
(4, 'TECNOLOGÍA DE LA INFORMACIÓN Y COMUNICACIONES', 2),
(5, 'COMPRAS', 2),
(6, 'CONTABILIDAD', 3),
(7, 'GESTIÓN HUMANA', 3),
(8, 'DESARROLLO', 4),
(9, 'HELPDESK', 4),
(10, 'RECEPCIÓN FACTURAS', 6),
(11, 'REGISTRO FACTURAS', 6);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cargos`
--

CREATE TABLE `cargos` (
  `idcargo` int(11) NOT NULL,
  `descripcion` varchar(45) DEFAULT NULL,
  `idarea` int(11) NOT NULL,
  `relacion` int(11) NOT NULL,
  `nivel` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `cargos`
--

INSERT INTO `cargos` (`idcargo`, `descripcion`, `idarea`, `relacion`, `nivel`) VALUES
(1, 'GERENTE GENERAL', 1, 0, 0),
(2, 'ASISTENTE DE GERENCIA', 1, 1, 1),
(3, 'GERENTE TÉCNICO', 2, 0, 0),
(4, 'SUB-GERENTE TÉCNICO', 2, 3, 1),
(5, 'COORDINADOR TÉCNICO', 2, 4, 2),
(6, 'GERENTE ADM Y FINANZAS', 3, 0, 0),
(7, 'SUB-GERENTE ADM Y FINANZAS', 3, 6, 1),
(8, 'COORDINADOR ADM Y FINANZAS', 3, 7, 2),
(9, 'JEFE TIC', 4, 0, 0),
(10, 'RESPONSABLE TIC', 4, 9, 1),
(11, 'JEFE COMPRAS', 5, 0, 0),
(12, 'RESPONSABLE COMPRAS', 5, 11, 1),
(13, 'ASISTENTE COMPRAS I', 5, 12, 2),
(14, 'ASISTENTE COMPRAS II', 5, 12, 2),
(15, 'ASISTENTE COMPRAS III', 5, 12, 2),
(16, 'JEFE CONTABILIDAD', 6, 0, 0),
(17, 'RESPONSABLE CONTABILIDAD', 6, 16, 1),
(18, 'JEFE GESTIÓN HUMANA', 7, 0, 0),
(19, 'RESPONSABLE GESTIÓN HUMANA', 7, 18, 1),
(20, 'ASISTENTE GESTIÓN HUMANA I', 7, 19, 2),
(21, 'ASISTENTE GESTIÓN HUMANA II', 7, 19, 2),
(22, 'ASISTENTE GESTIÓN HUMANA III', 7, 19, 2),
(23, 'RESPONSABLE DESARROLLO', 8, 0, 2),
(24, 'DESARROLLADOR I', 8, 23, 3),
(25, 'DESARROLLADOR II', 8, 23, 3),
(26, 'DESARROLLADOR III', 8, 23, 3),
(27, 'RESPONSABLE HELPDESK', 9, 0, 2),
(28, 'ASISTENTE HELPDESK I', 9, 27, 3),
(29, 'ASISTENTE HELPDESK II', 9, 27, 3),
(30, 'ASISTENTE HELPDESK III', 9, 27, 3),
(31, 'RESPONSABLE RECEPCIÓN FACTURAS', 10, 0, 2),
(32, 'ASISTENTE RECEPCIÓN FACTURAS I', 10, 31, 3),
(33, 'ASISTENTE RECEPCIÓN FACTURAS II', 10, 31, 3),
(34, 'RESPONSABLE REGISTRO FACTURAS', 11, 0, 2),
(35, 'ASISTENTE REGISTRO FACTURAS I', 11, 34, 3),
(36, 'ASISTENTE REGISTRO FACTURAS II', 11, 34, 3),
(37, 'ASISTENTE REGISTRO FACTURAS III', 11, 34, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cargos_empleado`
--

CREATE TABLE `cargos_empleado` (
  `idcargo_empleado` int(11) NOT NULL,
  `idempleado` int(11) NOT NULL,
  `idcargo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `cargos_empleado`
--

INSERT INTO `cargos_empleado` (`idcargo_empleado`, `idempleado`, `idcargo`) VALUES
(1, 1, 1),
(2, 2, 2),
(3, 3, 3),
(4, 4, 4),
(5, 5, 5),
(6, 6, 6),
(7, 7, 7),
(8, 8, 8),
(9, 9, 9),
(10, 10, 10),
(11, 11, 11),
(12, 12, 12),
(13, 13, 13),
(14, 14, 14),
(15, 15, 15),
(16, 16, 16),
(17, 17, 17),
(18, 18, 18),
(19, 19, 19),
(20, 20, 20),
(21, 21, 21),
(22, 22, 22),
(23, 23, 23),
(24, 24, 24),
(25, 25, 25),
(26, 26, 26),
(27, 27, 27),
(28, 28, 28),
(29, 29, 29),
(30, 30, 30),
(31, 31, 31),
(32, 32, 32),
(33, 33, 33),
(34, 34, 34),
(35, 35, 35),
(36, 36, 36),
(37, 37, 37);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleados`
--

CREATE TABLE `empleados` (
  `idempleado` int(11) NOT NULL,
  `nombres` varchar(45) DEFAULT NULL,
  `apellidos` varchar(45) DEFAULT NULL,
  `dni` char(8) DEFAULT NULL,
  `edad` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `empleados`
--

INSERT INTO `empleados` (`idempleado`, `nombres`, `apellidos`, `dni`, `edad`) VALUES
(1, 'GUSTAVO', 'VILCAPOMA', '12345678', 30),
(2, 'JAZMIN', 'COPO', '12345678', 30),
(3, 'MARCIO', 'VILCAPOMA', '12345678', 30),
(4, 'ISA', 'ZUMAETA', '12345678', 30),
(5, 'MIGUEL', 'MENDOZA', '12345678', 30),
(6, 'ELIZABETH', 'BRAVO', '12345678', 30),
(7, 'IVAN', 'MONTES', '12345678', 30),
(8, 'AZUCENA', 'CRISOSTOMO', '12345678', 30),
(9, 'JOSE', 'ADRIAN', '12345678', 30),
(10, 'MARCO', 'GARCIA', '12345678', 30),
(11, 'MAURO', 'VILCAPOMA', '12345678', 30),
(12, 'PAMELA', 'VILCAPOMA', '12345678', 30),
(13, 'KELLY', 'AMAUT', '12345678', 30),
(14, 'CARLOS', 'ARIAS', '12345678', 30),
(15, 'AMY', 'GARCIA', '12345678', 30),
(16, 'LILY', 'MAURICIO', '12345678', 30),
(17, 'OFELIA', 'MONTAÑO', '12345678', 30),
(18, 'JULIO', 'QUISPE', '12345678', 30),
(19, 'MAXIMINA', 'VEGA', '12345678', 30),
(20, 'MARISOL', 'RIVERA', '12345678', 30),
(21, 'PATRICIA', 'LOPEZ', '12345678', 30),
(22, 'LIZ', 'DEL CASTILLO', '12345678', 30),
(23, 'WILLIAM', 'LOPEZ', '12345678', 30),
(24, 'JESUS E.', 'RONCAL H.', '12345678', 25),
(25, 'OMAR', 'MORI', '12345678', 30),
(26, 'ALEXANDER', 'CARRASCO', '12345678', 30),
(27, 'JORGE', 'TURPO', '12345678', 30),
(28, 'FERNANDO', 'AGUIRRE', '12345678', 30),
(29, 'PEDRO', 'ROMERO', '12345678', 30),
(30, 'CATALINA', 'BUEN DIA', '12345678', 30),
(31, 'VERONICA', 'VARGAS', '12345678', 30),
(32, 'BRICK', 'ENRICO', '12345678', 30),
(33, 'ROCIO', 'LIMACO', '12345678', 30),
(34, 'JOSE', 'PUCA', '12345678', 30),
(35, 'JEAN', 'SALAS', '12345678', 30),
(36, 'DANIEL', 'ASMAD', '12345678', 30),
(37, 'SMITH', 'TORRES', '12345678', 30);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `areas`
--
ALTER TABLE `areas`
  ADD PRIMARY KEY (`idarea`);

--
-- Indices de la tabla `cargos`
--
ALTER TABLE `cargos`
  ADD PRIMARY KEY (`idcargo`);

--
-- Indices de la tabla `cargos_empleado`
--
ALTER TABLE `cargos_empleado`
  ADD PRIMARY KEY (`idcargo_empleado`);

--
-- Indices de la tabla `empleados`
--
ALTER TABLE `empleados`
  ADD PRIMARY KEY (`idempleado`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `areas`
--
ALTER TABLE `areas`
  MODIFY `idarea` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `cargos`
--
ALTER TABLE `cargos`
  MODIFY `idcargo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;

--
-- AUTO_INCREMENT de la tabla `cargos_empleado`
--
ALTER TABLE `cargos_empleado`
  MODIFY `idcargo_empleado` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;

--
-- AUTO_INCREMENT de la tabla `empleados`
--
ALTER TABLE `empleados`
  MODIFY `idempleado` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

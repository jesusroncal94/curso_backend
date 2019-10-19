-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 20-10-2019 a las 00:03:32
-- Versión del servidor: 10.4.8-MariaDB
-- Versión de PHP: 7.3.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `reto`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `business`
--

CREATE TABLE `business` (
  `business_id` int(10) UNSIGNED NOT NULL,
  `ruc` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `business`
--

INSERT INTO `business` (`business_id`, `ruc`, `name`, `address`, `created_at`, `updated_at`) VALUES
(1, '11111111111', 'Empresa 1', 'Av. 1', '2019-10-19 19:44:46', '2019-10-19 19:44:46'),
(2, '22222222222', 'Empresa 2', 'Av. 2', '2019-10-19 19:45:12', '2019-10-19 19:45:12'),
(3, '33333333333', 'Empresa 3', 'Av. 3', '2019-10-19 21:30:22', '2019-10-19 21:30:22');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `migrations`
--

CREATE TABLE `migrations` (
  `migration` varchar(255) NOT NULL,
  `batch` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `migrations`
--

INSERT INTO `migrations` (`migration`, `batch`) VALUES
('2019_10_19_155016_create_business_table', 1),
('2019_10_19_192953_create_users_table', 1),
('2019_10_19_193001_create_roles_table', 1),
('2019_10_19_193008_create_user_roles_table', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `roles`
--

CREATE TABLE `roles` (
  `role_id` int(10) UNSIGNED NOT NULL,
  `name` varchar(255) NOT NULL,
  `status` int(11) NOT NULL,
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `roles`
--

INSERT INTO `roles` (`role_id`, `name`, `status`, `created_at`, `updated_at`) VALUES
(1, 'Gerente', 0, '2019-10-19 19:52:17', '2019-10-19 19:52:17'),
(2, 'Supervisor', 0, '2019-10-19 19:52:24', '2019-10-19 19:52:24'),
(3, 'Cajero', 0, '2019-10-19 19:52:28', '2019-10-19 19:52:28');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `user_id` int(10) UNSIGNED NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `age` int(11) NOT NULL,
  `gender` varchar(255) NOT NULL,
  `status` int(11) NOT NULL,
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`user_id`, `username`, `password`, `name`, `last_name`, `age`, `gender`, `status`, `created_at`, `updated_at`) VALUES
(1, 'jesusroncal94', '$2b$12$tG18LyjFyPG2TaPfBSfSueMvth6qEubpqxEEwBYKvrO/NkNHz9Uja', 'Jesus', 'Roncal', 25, 'M', 0, '2019-10-19 19:46:28', '2019-10-19 19:46:28'),
(2, 'mariaroncal99', '$2b$12$ItTNMeLxq8iKfO5GK25DxORFgeqR4fhVEmYut0pfPJ5EJmbd3lcWu', 'Maria', 'Roncal', 20, 'F', 0, '2019-10-19 19:50:22', '2019-10-19 19:50:22'),
(3, 'andresaybar03', '$2b$12$AMyZPrB8xvTMH3leEgqYZeCGeptpztLWg/lbUfbhkWUcU6XJzVmoK', 'Andres', 'Aybar', 13, 'M', 0, '2019-10-19 19:51:04', '2019-10-19 19:51:04'),
(4, 'joseroncal97', '$2b$12$DG/zM2cUh1Jc9my9EqowAeZKJASNpQVGkNa.jtD.kzLJgocMGY3iC', 'Jose', 'Roncal', 22, 'M', 0, '2019-10-19 19:51:41', '2019-10-19 19:51:41'),
(5, 'jesustuesta123', '$2b$12$.qXKMcKbFOUzWsXIELSuoegB/PTEmqpdKrsJ.r9L76FXrzYhtmpNu', 'Jesus', 'Tuesta', 28, 'M', 0, '2019-10-19 20:31:01', '2019-10-19 20:31:01');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user_roles`
--

CREATE TABLE `user_roles` (
  `user_role_id` int(10) UNSIGNED NOT NULL,
  `business_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `role_id` int(11) NOT NULL,
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `user_roles`
--

INSERT INTO `user_roles` (`user_role_id`, `business_id`, `user_id`, `role_id`, `created_at`, `updated_at`) VALUES
(1, 1, 1, 1, '2019-10-19 19:54:11', '2019-10-19 19:54:11'),
(2, 1, 2, 2, '2019-10-19 19:54:35', '2019-10-19 19:54:35'),
(3, 2, 3, 1, '2019-10-19 19:54:51', '2019-10-19 19:54:51'),
(4, 2, 4, 2, '2019-10-19 19:54:58', '2019-10-19 19:54:58');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `business`
--
ALTER TABLE `business`
  ADD PRIMARY KEY (`business_id`);

--
-- Indices de la tabla `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`role_id`);

--
-- Indices de la tabla `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- Indices de la tabla `user_roles`
--
ALTER TABLE `user_roles`
  ADD PRIMARY KEY (`user_role_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `business`
--
ALTER TABLE `business`
  MODIFY `business_id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `roles`
--
ALTER TABLE `roles`
  MODIFY `role_id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `user_roles`
--
ALTER TABLE `user_roles`
  MODIFY `user_role_id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

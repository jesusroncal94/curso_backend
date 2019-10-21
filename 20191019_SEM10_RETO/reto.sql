-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 21-10-2019 a las 22:55:04
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
(3, '33333333333', 'Empresa 3', 'Av. 3', '2019-10-19 21:30:22', '2019-10-19 21:30:22'),
(4, '44444444444', 'Empresa 4', 'Av. 4', '2019-10-20 22:36:31', '2019-10-20 22:36:31');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `invoices`
--

CREATE TABLE `invoices` (
  `invoice_id` int(10) UNSIGNED NOT NULL,
  `user_role_id` int(11) NOT NULL,
  `subtotal` double(8,2) NOT NULL,
  `igv` double(8,2) NOT NULL,
  `total` double(8,2) NOT NULL,
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `invoices`
--

INSERT INTO `invoices` (`invoice_id`, `user_role_id`, `subtotal`, `igv`, `total`, `created_at`, `updated_at`) VALUES
(1, 4, 1500.00, 270.00, 1770.00, '2019-10-21 20:32:07', '2019-10-22 01:32:07'),
(2, 4, 3500.00, 630.00, 4130.00, '2019-10-21 20:34:16', '2019-10-22 01:34:16'),
(3, 4, 5500.00, 990.00, 6490.00, '2019-10-21 20:34:48', '2019-10-22 01:34:48'),
(4, 8, 7500.00, 1350.00, 8850.00, '2019-10-21 20:40:30', '2019-10-22 01:40:31'),
(5, 8, 9500.00, 1710.00, 11210.00, '2019-10-21 20:41:12', '2019-10-22 01:41:13'),
(6, 8, 11500.00, 2070.00, 13570.00, '2019-10-21 20:42:02', '2019-10-22 01:42:02'),
(7, 8, 13500.00, 2430.00, 15930.00, '2019-10-21 20:53:35', '2019-10-22 01:53:35');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `invoice_details`
--

CREATE TABLE `invoice_details` (
  `invoice_detail_id` int(10) UNSIGNED NOT NULL,
  `invoice_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `price` double(8,2) NOT NULL,
  `quantity` int(11) NOT NULL,
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `invoice_details`
--

INSERT INTO `invoice_details` (`invoice_detail_id`, `invoice_id`, `product_id`, `price`, `quantity`, `created_at`, `updated_at`) VALUES
(1, 1, 1, 10.00, 5, '2019-10-21 20:32:07', '2019-10-21 20:32:07'),
(2, 1, 2, 20.00, 10, '2019-10-21 20:32:07', '2019-10-21 20:32:07'),
(3, 1, 3, 30.00, 15, '2019-10-21 20:32:07', '2019-10-21 20:32:07'),
(4, 1, 4, 40.00, 20, '2019-10-21 20:32:07', '2019-10-21 20:32:07'),
(5, 2, 5, 50.00, 5, '2019-10-21 20:34:16', '2019-10-21 20:34:16'),
(6, 2, 6, 60.00, 10, '2019-10-21 20:34:16', '2019-10-21 20:34:16'),
(7, 2, 7, 70.00, 15, '2019-10-21 20:34:16', '2019-10-21 20:34:16'),
(8, 2, 8, 80.00, 20, '2019-10-21 20:34:16', '2019-10-21 20:34:16'),
(9, 3, 9, 90.00, 5, '2019-10-21 20:34:48', '2019-10-21 20:34:48'),
(10, 3, 10, 100.00, 10, '2019-10-21 20:34:48', '2019-10-21 20:34:48'),
(11, 3, 11, 110.00, 15, '2019-10-21 20:34:48', '2019-10-21 20:34:48'),
(12, 3, 12, 120.00, 20, '2019-10-21 20:34:48', '2019-10-21 20:34:48'),
(13, 4, 13, 130.00, 5, '2019-10-21 20:40:30', '2019-10-21 20:40:30'),
(14, 4, 14, 140.00, 10, '2019-10-21 20:40:31', '2019-10-21 20:40:31'),
(15, 4, 15, 150.00, 15, '2019-10-21 20:40:31', '2019-10-21 20:40:31'),
(16, 4, 16, 160.00, 20, '2019-10-21 20:40:31', '2019-10-21 20:40:31'),
(17, 5, 17, 170.00, 5, '2019-10-21 20:41:13', '2019-10-21 20:41:13'),
(18, 5, 18, 180.00, 10, '2019-10-21 20:41:13', '2019-10-21 20:41:13'),
(19, 5, 19, 190.00, 15, '2019-10-21 20:41:13', '2019-10-21 20:41:13'),
(20, 5, 20, 200.00, 20, '2019-10-21 20:41:13', '2019-10-21 20:41:13'),
(21, 6, 21, 210.00, 5, '2019-10-21 20:42:02', '2019-10-21 20:42:02'),
(22, 6, 22, 220.00, 10, '2019-10-21 20:42:02', '2019-10-21 20:42:02'),
(23, 6, 23, 230.00, 15, '2019-10-21 20:42:02', '2019-10-21 20:42:02'),
(24, 6, 24, 240.00, 20, '2019-10-21 20:42:02', '2019-10-21 20:42:02'),
(25, 7, 25, 250.00, 5, '2019-10-21 20:53:35', '2019-10-21 20:53:35'),
(26, 7, 26, 260.00, 10, '2019-10-21 20:53:35', '2019-10-21 20:53:35'),
(27, 7, 27, 270.00, 15, '2019-10-21 20:53:35', '2019-10-21 20:53:35'),
(28, 7, 28, 280.00, 20, '2019-10-21 20:53:35', '2019-10-21 20:53:35');

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
('2019_10_19_193008_create_user_roles_table', 1),
('2019_10_20_230746_create_products_table', 2),
('2019_10_21_001358_create_invoices_table', 3),
('2019_10_21_001415_create_invoice_details_table', 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `products`
--

CREATE TABLE `products` (
  `product_id` int(10) UNSIGNED NOT NULL,
  `name` varchar(255) NOT NULL,
  `price` double(8,2) NOT NULL,
  `quantity` int(11) NOT NULL,
  `created_at` timestamp NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `products`
--

INSERT INTO `products` (`product_id`, `name`, `price`, `quantity`, `created_at`, `updated_at`) VALUES
(1, 'Producto 1', 10.00, 5, '2019-10-21 02:03:48', '2019-10-22 01:32:07'),
(2, 'Producto 2', 20.00, 10, '2019-10-21 02:03:48', '2019-10-22 01:32:07'),
(3, 'Producto 3', 30.00, 15, '2019-10-21 02:04:12', '2019-10-22 01:32:07'),
(4, 'Producto 4', 40.00, 15, '2019-10-21 02:04:12', '2019-10-22 01:32:07'),
(5, 'Producto 5', 50.00, 45, '2019-10-21 02:04:33', '2019-10-22 01:34:16'),
(6, 'Producto 6', 60.00, 50, '2019-10-21 02:04:33', '2019-10-22 01:34:16'),
(7, 'Producto 7', 70.00, 55, '2019-10-21 02:04:45', '2019-10-22 01:34:16'),
(8, 'Producto 8', 80.00, 60, '2019-10-21 02:04:45', '2019-10-22 01:34:16'),
(9, 'Producto 9', 90.00, 85, '2019-10-21 02:05:20', '2019-10-22 01:34:48'),
(10, 'Producto 10', 100.00, 90, '2019-10-21 02:05:20', '2019-10-22 01:34:48'),
(11, 'Producto 11', 110.00, 95, '2019-10-21 02:05:52', '2019-10-22 01:34:48'),
(12, 'Producto 12', 120.00, 100, '2019-10-21 02:05:52', '2019-10-22 01:34:48'),
(13, 'Producto 13', 130.00, 125, '2019-10-21 02:06:11', '2019-10-22 01:40:30'),
(14, 'Producto 14', 140.00, 130, '2019-10-21 02:06:11', '2019-10-22 01:40:31'),
(15, 'Producto 15', 150.00, 135, '2019-10-21 02:07:13', '2019-10-22 01:40:31'),
(16, 'Producto 16', 160.00, 140, '2019-10-21 02:07:13', '2019-10-22 01:40:31'),
(17, 'Producto 17', 170.00, 165, '2019-10-21 02:07:50', '2019-10-22 01:41:13'),
(18, 'Producto 18', 180.00, 170, '2019-10-21 02:07:50', '2019-10-22 01:41:13'),
(19, 'Producto 19', 190.00, 175, '2019-10-21 02:08:05', '2019-10-22 01:41:13'),
(20, 'Producto 20', 200.00, 180, '2019-10-21 02:08:05', '2019-10-22 01:41:13'),
(21, 'Producto 21', 210.00, 205, '2019-10-21 02:08:23', '2019-10-22 01:42:02'),
(22, 'Producto 22', 220.00, 210, '2019-10-21 02:08:23', '2019-10-22 01:42:02'),
(23, 'Producto 23', 230.00, 215, '2019-10-21 02:08:42', '2019-10-22 01:42:02'),
(24, 'Producto 24', 240.00, 220, '2019-10-21 02:08:42', '2019-10-22 01:42:02'),
(25, 'Producto 25', 250.00, 245, '2019-10-21 02:09:02', '2019-10-22 01:53:35'),
(26, 'Producto 26', 260.00, 250, '2019-10-21 02:09:02', '2019-10-22 01:53:35'),
(27, 'Producto 27', 270.00, 255, '2019-10-21 02:09:21', '2019-10-22 01:53:35'),
(28, 'Producto 28', 280.00, 260, '2019-10-21 02:09:21', '2019-10-22 01:53:35'),
(29, 'Producto 29', 290.00, 290, '2019-10-21 02:09:39', '2019-10-21 02:09:39'),
(30, 'Producto 30', 300.00, 300, '2019-10-21 02:09:39', '2019-10-21 02:09:39');

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
(1, 'Super Administrador', 0, '2019-10-20 22:44:24', '2019-10-20 22:44:24'),
(2, 'Gerente', 0, '2019-10-20 22:45:14', '2019-10-20 22:45:14'),
(3, 'Supervisor', 0, '2019-10-20 22:45:14', '2019-10-20 22:45:14'),
(4, 'Cajero', 0, '2019-10-20 22:45:31', '2019-10-20 22:45:31');

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
(5, 'jesustuesta123', '$2b$12$.qXKMcKbFOUzWsXIELSuoegB/PTEmqpdKrsJ.r9L76FXrzYhtmpNu', 'Jesus', 'Tuesta', 28, 'M', 0, '2019-10-19 20:31:01', '2019-10-19 20:31:01'),
(6, 'cinthyafuentes', '$2b$12$4K1A8WMcwZWTMsR2QJWu4uHibTkF5rUyZg0TokOnNftL86a6P3vJK', 'Cinthya', 'Fuentes', 22, 'F', 0, '2019-10-21 20:37:44', '2019-10-21 20:37:44'),
(7, 'elizabethhuamani', '$2b$12$2Dbnd5GrLPXcqo5RERuTdu7QsjOOak0BFXPf/iNBs1vHpwxgJxXxG', 'Elizabeth', 'Huamani', 23, 'F', 0, '2019-10-21 20:38:16', '2019-10-21 20:38:16'),
(8, 'danielcotaquispe', '$2b$12$EiiXECpugY23lcVYiuWJHOR2C6JWgV3ukC/kc7G7UxUiLMMkPnnmq', 'Daniel', 'Cotaquispe', 24, 'M', 0, '2019-10-21 20:38:48', '2019-10-21 20:38:48');

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
(1, 1, 1, 1, '2019-10-21 02:17:07', '2019-10-21 02:17:07'),
(2, 1, 2, 2, '2019-10-21 02:17:07', '2019-10-21 02:17:07'),
(3, 1, 3, 3, '2019-10-21 02:17:34', '2019-10-21 02:17:34'),
(4, 1, 4, 4, '2019-10-21 02:17:34', '2019-10-21 02:17:34'),
(5, 2, 5, 1, '2019-10-21 02:18:07', '2019-10-21 02:18:07'),
(6, 2, 6, 2, '2019-10-21 02:18:07', '2019-10-21 02:18:07'),
(7, 2, 7, 3, '2019-10-21 02:18:22', '2019-10-21 02:18:22'),
(8, 2, 8, 4, '2019-10-21 02:18:22', '2019-10-21 02:18:22');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `business`
--
ALTER TABLE `business`
  ADD PRIMARY KEY (`business_id`);

--
-- Indices de la tabla `invoices`
--
ALTER TABLE `invoices`
  ADD PRIMARY KEY (`invoice_id`);

--
-- Indices de la tabla `invoice_details`
--
ALTER TABLE `invoice_details`
  ADD PRIMARY KEY (`invoice_detail_id`);

--
-- Indices de la tabla `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`product_id`);

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
  MODIFY `business_id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `invoices`
--
ALTER TABLE `invoices`
  MODIFY `invoice_id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `invoice_details`
--
ALTER TABLE `invoice_details`
  MODIFY `invoice_detail_id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT de la tabla `products`
--
ALTER TABLE `products`
  MODIFY `product_id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT de la tabla `roles`
--
ALTER TABLE `roles`
  MODIFY `role_id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `user_roles`
--
ALTER TABLE `user_roles`
  MODIFY `user_role_id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

-- MySQL Script generated by MySQL Workbench
-- Sat Oct  5 17:00:04 2019
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema colegio
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema colegio
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `colegio` DEFAULT CHARACTER SET latin1 ;
USE `colegio` ;

-- -----------------------------------------------------
-- Table `colegio`.`alumnos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `colegio`.`alumnos` (
  `idAlumno` INT NOT NULL AUTO_INCREMENT,
  `dni` VARCHAR(8) NOT NULL,
  `nombres` VARCHAR(50) NOT NULL,
  `apellidos` VARCHAR(50) NOT NULL,
  `edad` INT NOT NULL,
  PRIMARY KEY (`idAlumno`),
  UNIQUE INDEX `dni_UNIQUE` (`dni` ASC) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `colegio`.`docentes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `colegio`.`docentes` (
  `idDocente` INT NOT NULL AUTO_INCREMENT,
  `dni` VARCHAR(8) NOT NULL,
  `nombres` VARCHAR(50) NOT NULL,
  `apellidos` VARCHAR(50) NOT NULL,
  `edad` INT NOT NULL,
  PRIMARY KEY (`idDocente`),
  UNIQUE INDEX `dni_UNIQUE` (`dni` ASC) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `colegio`.`periodos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `colegio`.`periodos` (
  `idPeriodo` INT NOT NULL AUTO_INCREMENT,
  `periodo` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`idPeriodo`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `colegio`.`grados`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `colegio`.`grados` (
  `idGrado` INT NOT NULL AUTO_INCREMENT,
  `grado` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`idGrado`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `colegio`.`secciones`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `colegio`.`secciones` (
  `idSeccion` INT NOT NULL AUTO_INCREMENT,
  `seccion` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`idSeccion`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `colegio`.`aulas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `colegio`.`aulas` (
  `idAula` INT NOT NULL AUTO_INCREMENT,
  `aula` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`idAula`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `colegio`.`niveles`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `colegio`.`niveles` (
  `idNivel` INT NOT NULL AUTO_INCREMENT,
  `nivel` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`idNivel`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `colegio`.`cursos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `colegio`.`cursos` (
  `idCurso` INT NOT NULL AUTO_INCREMENT,
  `curso` VARCHAR(8) NOT NULL,
  PRIMARY KEY (`idCurso`),
  UNIQUE INDEX `dni_UNIQUE` (`curso` ASC) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `colegio`.`horarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `colegio`.`horarios` (
  `idHorario` INT NOT NULL AUTO_INCREMENT,
  `horario` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`idHorario`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `colegio`.`gradoseccion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `colegio`.`gradoseccion` (
  `idGradoSeccion` INT NOT NULL AUTO_INCREMENT,
  `vacantes` INT NOT NULL,
  `turnos` CHAR(1) NOT NULL,
  `grados_idGrado` INT NOT NULL,
  `secciones_idSeccion` INT NOT NULL,
  `niveles_idNivel` INT NOT NULL,
  `aulas_idAula` INT NOT NULL,
  PRIMARY KEY (`idGradoSeccion`),
  INDEX `fk_gradoseccion_grados_idx` (`grados_idGrado` ASC) ,
  INDEX `fk_gradoseccion_secciones1_idx` (`secciones_idSeccion` ASC) ,
  INDEX `fk_gradoseccion_niveles1_idx` (`niveles_idNivel` ASC) ,
  INDEX `fk_gradoseccion_aulas1_idx` (`aulas_idAula` ASC) ,
  CONSTRAINT `fk_gradoseccion_grados`
    FOREIGN KEY (`grados_idGrado`)
    REFERENCES `colegio`.`grados` (`idGrado`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_gradoseccion_secciones1`
    FOREIGN KEY (`secciones_idSeccion`)
    REFERENCES `colegio`.`secciones` (`idSeccion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_gradoseccion_niveles1`
    FOREIGN KEY (`niveles_idNivel`)
    REFERENCES `colegio`.`niveles` (`idNivel`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_gradoseccion_aulas1`
    FOREIGN KEY (`aulas_idAula`)
    REFERENCES `colegio`.`aulas` (`idAula`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `colegio`.`matricula`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `colegio`.`matricula` (
  `idMatricula` INT NOT NULL AUTO_INCREMENT,
  `descripcion` VARCHAR(45) NULL,
  `alumnos_idAlumno` INT NOT NULL,
  `gradoseccion_idGradoSeccion` INT NOT NULL,
  PRIMARY KEY (`idMatricula`),
  INDEX `fk_matricula_alumnos1_idx` (`alumnos_idAlumno` ASC) ,
  INDEX `fk_matricula_gradoseccion1_idx` (`gradoseccion_idGradoSeccion` ASC) ,
  CONSTRAINT `fk_matricula_alumnos1`
    FOREIGN KEY (`alumnos_idAlumno`)
    REFERENCES `colegio`.`alumnos` (`idAlumno`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_matricula_gradoseccion1`
    FOREIGN KEY (`gradoseccion_idGradoSeccion`)
    REFERENCES `colegio`.`gradoseccion` (`idGradoSeccion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `colegio`.`cursogradoseccion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `colegio`.`cursogradoseccion` (
  `idCursoGradoSeccion` INT NOT NULL AUTO_INCREMENT,
  `descripcion` VARCHAR(45) NULL,
  `gradoseccion_idGradoSeccion` INT NOT NULL,
  `cursos_idCurso` INT NOT NULL,
  `docentes_idDocente` INT NOT NULL,
  `horarios_idHorario` INT NOT NULL,
  PRIMARY KEY (`idCursoGradoSeccion`),
  INDEX `fk_cursogradoseccion_gradoseccion1_idx` (`gradoseccion_idGradoSeccion` ASC) ,
  INDEX `fk_cursogradoseccion_cursos1_idx` (`cursos_idCurso` ASC) ,
  INDEX `fk_cursogradoseccion_docentes1_idx` (`docentes_idDocente` ASC) ,
  INDEX `fk_cursogradoseccion_horarios1_idx` (`horarios_idHorario` ASC) ,
  CONSTRAINT `fk_cursogradoseccion_gradoseccion1`
    FOREIGN KEY (`gradoseccion_idGradoSeccion`)
    REFERENCES `colegio`.`gradoseccion` (`idGradoSeccion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_cursogradoseccion_cursos1`
    FOREIGN KEY (`cursos_idCurso`)
    REFERENCES `colegio`.`cursos` (`idCurso`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_cursogradoseccion_docentes1`
    FOREIGN KEY (`docentes_idDocente`)
    REFERENCES `colegio`.`docentes` (`idDocente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_cursogradoseccion_horarios1`
    FOREIGN KEY (`horarios_idHorario`)
    REFERENCES `colegio`.`horarios` (`idHorario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `colegio`.`notasperiodo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `colegio`.`notasperiodo` (
  `idNota` INT NOT NULL AUTO_INCREMENT,
  `nota` FLOAT NOT NULL,
  `descripcion` VARCHAR(20) NULL,
  `periodos_idPeriodo` INT NOT NULL,
  `cursogradoseccion_idCursoGradoSeccion` INT NOT NULL,
  `alumnos_idAlumno` INT NOT NULL,
  PRIMARY KEY (`idNota`),
  INDEX `fk_notasperiodo_periodos1_idx` (`periodos_idPeriodo` ASC) ,
  INDEX `fk_notasperiodo_cursogradoseccion1_idx` (`cursogradoseccion_idCursoGradoSeccion` ASC) ,
  INDEX `fk_notasperiodo_alumnos1_idx` (`alumnos_idAlumno` ASC) ,
  CONSTRAINT `fk_notasperiodo_periodos1`
    FOREIGN KEY (`periodos_idPeriodo`)
    REFERENCES `colegio`.`periodos` (`idPeriodo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_notasperiodo_cursogradoseccion1`
    FOREIGN KEY (`cursogradoseccion_idCursoGradoSeccion`)
    REFERENCES `colegio`.`cursogradoseccion` (`idCursoGradoSeccion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_notasperiodo_alumnos1`
    FOREIGN KEY (`alumnos_idAlumno`)
    REFERENCES `colegio`.`alumnos` (`idAlumno`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

USE `colegio` ;

-- -----------------------------------------------------
-- Placeholder table for view `colegio`.`view1`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `colegio`.`view1` (`id` INT);

-- -----------------------------------------------------
-- View `colegio`.`view1`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `colegio`.`view1`;
USE `colegio`;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

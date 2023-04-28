-- Schema: World_bank

CREATE DATABASE World_bank;

USE World_bank;

﻿-- Table: international_debt

CREATE TABLE international_debt
(
  country_name varcharacter(50),
  country_code varcharacter(50),
  indicator_name text,
  indicator_code text,
  debt int
);
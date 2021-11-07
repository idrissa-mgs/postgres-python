CREATE SCHEMA IF NOT EXISTS `test_schema`;

CREATE TABLE IF NOT EXISTS `test_schema`.`players` (
    `name`        VARCHAR(30),
    `age`       INTEGER,
    `club`     VARCHAR(30),
    `nationality` VARCHAR(30)
    CONSTRAINT pk_name PRIMARY KEY(`name`)
);

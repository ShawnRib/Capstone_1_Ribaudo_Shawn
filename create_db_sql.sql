/*** Initial Setup - only change lastname to your last name ***/ 
Select @@autocommit; -- 1 by default, all commands COMMIT immediately (no ROLLBACK)
Set @@autocommit = 0; -- ROLLBACK may be used to reverse DML changes not yet COMMIT.
Select @@SQL_SAFE_UPDATES; -- 1 by default
Set @@SQL_SAFE_UPDATES = 0; -- Lifts Warning on DELETE


DROP SCHEMA IF EXISTS TractorTEK; 
CREATE SCHEMA IF NOT EXISTS TractorTEK;
Use TractorTEK;

DROP TABLE IF EXISTS product_codes;
CREATE TABLE IF NOT EXISTS product_codes (
	prod_code VARCHAR(10) PRIMARY KEY,
    prod_name VARCHAR(64),
    URL VARCHAR(255),
    manufacturer varchar(64),
    ext_service_plan VARCHAR (7),
    warranty_price INT
);
/* 
CREATE TABLE IF NOT EXISTS service_plans (
	ext_service_plan VARCHAR (7) PRIMARY KEY,
    warranty_price INT,
    FOREIGN KEY (prod_code) REFERENCES product_code(prod_code)
);
*/
DROP TABLE IF EXISTS employers;
CREATE TABLE IF NOT EXISTS employers (
	emp_id VARCHAR(64) PRIMARY KEY,
    region VARCHAR(2),
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    pay_grade varchar(3)
);

DROP TABLE IF EXISTS dates;
CREATE TABLE IF NOT EXISTS dates (
	id INT AUTO_INCREMENT PRIMARY KEY,
	week0 INT,
    week1 INT,
    when_date DATE,
    sales_period INT,
    sales_year INT,
    quarter_number INT
);


DROP TABLE IF EXISTS sales_quantities;
CREATE TABLE IF NOT EXISTS sales_quantities(
	id INT AUTO_INCREMENT PRIMARY KEY,
    item_code VARCHAR(10),
    emp_id VARCHAR(64),
    FOREIGN KEY (emp_id) REFERENCES employers(emp_id),
    years INT,
    w0 INT,
	w1 INT,
	w2 INT,
	w3 INT,
	w4 INT,
	w5 INT,
	w6 INT,
	w7 INT,
	w8 INT,
	w9 INT,
	w10 INT,
	w11 INT,
	w12 INT,
	w13 INT,
	w14 INT,
	w15 INT,
	w16 INT,
	w17 INT,
	w18 INT,
	w19 INT,
	w20 INT,
	w21 INT,
	w22 INT,
	w23 INT,
	w24 INT,
	w25 INT,
	w26 INT,
	w27 INT,
	w28 INT,
	w29 INT,
	w30 INT,
	w31 INT,
	w32 INT,
	w33 INT,
	w34 INT,
	w35 INT,
	w36 INT,
	w37 INT,
	w38 INT,
	w39 INT,
	w40 INT,
	w41 INT,
	w42 INT,
	w43 INT,
	w44 INT,
	w45 INT,
	w46 INT,
	w47 INT,
	w48 INT,
	w49 INT,
	w50 INT,
	w51 INT
);


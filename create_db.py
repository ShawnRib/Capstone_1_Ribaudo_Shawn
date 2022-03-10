import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user='root',
    passwd = "SQL5Data",

)

my_cursor = mydb.cursor()
#Reset TractorTEK database
my_cursor. execute("DROP DATABASE TractorTEK;")
my_cursor. execute("CREATE DATABASE TractorTEK;")

#create prod_codes table
my_cursor. execute("CREATE TABLE `TractorTEK`.`product_codes`(`prod_code` VARCHAR(10) PRIMARY KEY, `prod_name` VARCHAR(64), `url` VARCHAR(255), `manufacturer` varchar(64), `ext_service_plan` VARCHAR (7), `warranty_price` INT);")
#create employers table
my_cursor. execute("CREATE TABLE `TractorTEK`.`employers`(`emp_id` VARCHAR(64) PRIMARY KEY, `region` VARCHAR(2), `first_name` VARCHAR(50), `last_name` VARCHAR(50), `pay_grade` VARCHAR(3));")
#create dates table
my_cursor. execute("CREATE TABLE `TractorTEK`.`dates`(id INT AUTO_INCREMENT PRIMARY KEY, week0 INT, week1 INT, when_date DATE, sales_period INT, sales_year INT, quarter_number INT);")
#create sales quantities
my_cursor.execute("CREATE TABLE `TractorTEK`.`sales_quantities`(id INT AUTO_INCREMENT PRIMARY KEY,    item_code VARCHAR(10),    emp_id VARCHAR(64),    FOREIGN KEY (emp_id) REFERENCES employers(emp_id),    years INT,    w0 INT,	w1 INT,	w2 INT,	w3 INT,	w4 INT,	w5 INT,	w6 INT,	w7 INT,	w8 INT,	w9 INT,	w10 INT,	w11 INT,	w12 INT,	w13 INT,	w14 INT,	w15 INT,	w16 INT,	w17 INT,	w18 INT,	w19 INT,	w20 INT,	w21 INT,	w22 INT,	w23 INT,	w24 INT,	w25 INT,	w26 INT,	w27 INT,	w28 INT,	w29 INT,	w30 INT,	w31 INT,	w32 INT,	w33 INT,	w34 INT,	w35 INT,	w36 INT,	w37 INT,	w38 INT,	w39 INT,	w40 INT,	w41 INT,	w42 INT,	w43 INT,	w44 INT,	w45 INT,	w46 INT,	w47 INT,	w48 INT,	w49 INT,	w50 INT,	w51 INT);")

#my_cursor. execute("CREATE TABLE `puppies`.`product_codes` (`id` INT NOT NULL AUTO_INCREMENT,`name` VARCHAR(45) NULL,`color_fur` VARCHAR(45) NULL, `owner` INT NULL,PRIMARY KEY (`id`));")
#my_cursor. execute("CREATE TABLE `puppies`.`owners` (`id` INT NOT NULL AUTO_INCREMENT,`name` VARCHAR(45) NULL, `puppy_id` INT NULL,PRIMARY KEY (`id`));")

'''
CREATE TABLE `puppies`.`puppies` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `owner` INT NULL,
  PRIMARY KEY (`id`));
  
  CREATE TABLE `puppies`.`owners` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `owner` INT NULL,
  PRIMARY KEY (`id`));
'''
#my_cursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
#my_cursor. execute("DROP DATABASE owners")
#my_cursor. execute("CREATE DATABASE owners")
#insert table!!!!

#add dummy information

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)

DROP TABLE IF EXISTS delivery;
DROP TABLE IF EXISTS supplier;
DROP TABLE IF EXISTS ean_product;
DROP TABLE IF EXISTS contains;
DROP TABLE IF EXISTS product;
DROP TABLE IF EXISTS pay;
DROP TABLE IF EXISTS sale;
DROP TABLE IF EXISTS process;
DROP TABLE IF EXISTS order_;
DROP TABLE IF EXISTS customer;
DROP TABLE IF EXISTS works ;
DROP TABLE IF EXISTS employee;
DROP TABLE IF EXISTS warehouse;
DROP TABLE IF EXISTS office;
DROP TABLE IF EXISTS workplace;
DROP TABLE IF EXISTS department;

CREATE TABLE department(
                           name VARCHAR(80),
                           PRIMARY KEY (name)
);
CREATE TABLE workplace(
                          address VARCHAR(255),
                          lat NUMERIC(8, 6) NOT NULL,
                          long NUMERIC(9, 6) NOT NULL,
                          UNIQUE (lat, long),
                          CHECK (lat >= -90 AND lat <= 90),
                          CHECK (long >= -180 AND long <= 180),
                          PRIMARY KEY (address)

);
CREATE TABLE office(
                       address VARCHAR(255),
                       PRIMARY KEY (address),
                       FOREIGN KEY (address) REFERENCES workplace(address)
);
CREATE TABLE warehouse(
                          address VARCHAR(255),
                          PRIMARY KEY (address),
                          FOREIGN KEY (address) REFERENCES workplace(address)
);

CREATE TABLE employee(
                         ssn BIGINT,
                         TIN BIGINT NOT NULL,
                         bdate DATE NOT NULL,
                         name VARCHAR(80) NOT NULL,
                         CHECK (ssn > 0),
                         CHECK (TIN > 0),
                         UNIQUE(TIN),
                         PRIMARY KEY(ssn)
    --every employee (ssn) must participate in the “works” association–
);


CREATE TABLE works (
                       address VARCHAR(255),
                       ssn BIGINT,
                       name VARCHAR(80),
                       PRIMARY KEY(address,ssn,name),
                       FOREIGN KEY (address) REFERENCES workplace(address),
                       FOREIGN KEY (ssn) REFERENCES employee(ssn),
                       FOREIGN KEY (name) REFERENCES department(name)
);


CREATE TABLE customer(
                         cust_no BIGINT,
                         name VARCHAR(80) NOT NULL,
                         email VARCHAR(254) NOT NULL,
                         phone VARCHAR(15) NOT NULL, --for different countries–
                         address VARCHAR(80) NOT NULL,
                         PRIMARY KEY(cust_no),
                         UNIQUE(email),
                         CHECK( cust_no > 0)

);

CREATE TABLE order_(
                       order_no BIGINT,
                       date DATE NOT NULL,
                       placed_by_cust_no BIGINT NOT NULL,
                       PRIMARY KEY (order_no),
                       FOREIGN KEY (placed_by_cust_no) REFERENCES customer(cust_no)
    --every order_no must exist in the table contains
);

CREATE TABLE process(
                        ssn BIGINT,
                        order_no BIGINT,
                        PRIMARY KEY (ssn, order_no),
                        FOREIGN KEY (ssn) REFERENCES employee(ssn),
                        FOREIGN KEY (order_no) REFERENCES order_(order_no)
);

CREATE TABLE sale(
                     order_no BIGINT,
                     PRIMARY KEY (order_no),
                     FOREIGN KEY (order_no) REFERENCES order_(order_no)
);

CREATE TABLE pay(
                    cust_no BIGINT NOT NULL,
                    order_no BIGINT,
                    PRIMARY KEY (order_no),
                    FOREIGN KEY (order_no) REFERENCES sale (order_no),
                    FOREIGN KEY (cust_no) REFERENCES customer (cust_no)
    -- the pair (cust_no, order_no) must exist in order
);

CREATE TABLE product(
                        sku VARCHAR(80),
                        name VARCHAR(80) NOT NULL,
                        description VARCHAR(400) NOT NULL,
                        price NUMERIC(16,4) NOT NULL,
                        PRIMARY KEY(sku),
                        CHECK (price > 0)
    --Every product sku must exist in table supplier–
);



CREATE TABLE ean_product(
                            sku VARCHAR(80),
                            ean NUMERIC (13) NOT NULL,
                            PRIMARY KEY(sku),
                            FOREIGN KEY(sku) REFERENCES product(sku),
                            CHECK (ean > 0)

);

CREATE TABLE contains(
                         order_no BIGINT,
                         sku VARCHAR(80),
                         qty INTEGER NOT NULL,
                         PRIMARY KEY(order_no, sku),
                         FOREIGN KEY(order_no) REFERENCES order_ (order_no),
                         FOREIGN KEY(sku) REFERENCES product(sku),
                         CHECK (qty > 0)
);

CREATE TABLE supplier(
                         TIN BIGINT,
                         name VARCHAR(80) NOT NULL,
                         address VARCHAR(255) NOT NULL,
                         supply_contract_sku VARCHAR(80) NOT NULL,
                         date DATE NOT NULL,
                         PRIMARY KEY(TIN),
                         FOREIGN KEY(supply_contract_sku) REFERENCES product(sku),
                         CHECK (TIN > 0)
);

CREATE TABLE delivery (
                          TIN BIGINT,
                          address VARCHAR(255),
                          PRIMARY KEY (TIN, address),
                          FOREIGN KEY(TIN) REFERENCES supplier(TIN),
                          FOREIGN KEY(address) REFERENCES warehouse(address)
);
--
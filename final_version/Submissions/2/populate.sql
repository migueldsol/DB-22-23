INSERT INTO department (name) VALUES ('Sales');
INSERT INTO department (name) VALUES ('Marketing');
INSERT INTO department (name) VALUES ('Engineering');
INSERT INTO department (name) VALUES ('Finances');

-- Insert data into workplace table
--warehouse workplaces
INSERT INTO workplace (address, lat, long) VALUES ('123 Main St', 40.7128, -74.0060);
INSERT INTO workplace (address, lat, long) VALUES ('234 Cedar Drive St', 43.2109, -77.8901);
INSERT INTO workplace (address, lat, long) VALUES ('345 Walnut Lane', 36.7890, -94.3487);
INSERT INTO workplace (address, lat, long) VALUES ('456 Elm St', 42.3601, -71.0589);
INSERT INTO workplace (address, lat, long) VALUES ('567 Maple lane', 39.1234, -75.6789);
--not used
INSERT INTO workplace (address, lat, long) VALUES ('891 Oak St', 37.7749, -122.4194);
INSERT INTO workplace (address, lat, long) VALUES ('912 Chestnut Road', 40.8765, -83.2109);

--office workplaces
INSERT INTO workplace (address, lat, long) VALUES ('111 Pine St', 37.7924, -122.4037);
INSERT INTO workplace (address, lat, long) VALUES ('222 Market St', 37.7950, -122.3986);
INSERT INTO workplace (address, lat, long) VALUES ('333 Battery St', 37.7955, -122.4009);
INSERT INTO workplace (address, lat, long) VALUES ('444 5th Ave', 40.7549, -73.9840);
INSERT INTO workplace (address, lat, long) VALUES ('555 10th Ave', 1.3214, -73.9840);
--not used
INSERT INTO workplace (address, lat, long) VALUES ('666 Broadway', 40.7294, -73.9933);
INSERT INTO workplace (address, lat, long) VALUES ('777 Birch Street', 42.3456, -80.4352);


-- Insert data into office table
INSERT INTO office (address) VALUES ('111 Pine St');
INSERT INTO office (address) VALUES ('222 Market St');
INSERT INTO office (address) VALUES ('333 Battery St');
INSERT INTO office (address) VALUES ('444 5th Ave');
--not used
INSERT INTO office (address) VALUES ('555 10th Ave');

-- Insert data into warehouse table
INSERT INTO warehouse (address) VALUES ('123 Main St');
INSERT INTO warehouse (address) VALUES ('234 Cedar Drive St');
INSERT INTO warehouse (address) VALUES ('345 Walnut Lane');
INSERT INTO warehouse (address) VALUES ('456 Elm St');
--not used
INSERT INTO warehouse (address) VALUES ('567 Maple lane');

-- Insert data into employee table

--works in warehouse
    --process delivery in 2022
INSERT INTO employee (ssn, TIN, bdate, name) VALUES (123456789, 987654321, '1990-01-01', 'John Smith');
    --process delivery in 2023
INSERT INTO employee (ssn, TIN, bdate, name) VALUES (234567890, 876543210, '1995-02-02', 'Jane Doe');

--works in warehouse and office
    --process delivery in 2022
INSERT INTO employee (ssn, TIN, bdate, name) VALUES (345678901, 765432109, '2000-03-03', 'Bob Johnson');
    --process delivery in 2023
INSERT INTO employee (ssn, TIN, bdate, name) VALUES (456789012, 654321098, '1995-04-04', 'Sarah Lee');

--works in office
    --process delivery in 2022
INSERT INTO employee (ssn, TIN, bdate, name) VALUES (567890123, 543210987, '2000-05-05', 'David Kim');
    --process delivery in 2023
INSERT INTO employee (ssn, TIN, bdate, name) VALUES (678901234, 972489657, '1998-07-13', 'Jimmy Oliver');

--works in the same as Bob
INSERT INTO employee (ssn, TIN, bdate, name) VALUES (789012345, 922489657, '1988-07-13', 'Alexander Hamilton');

--doesn't work anywhere
INSERT INTO employee (ssn, TIN, bdate, name) VALUES (890123456, 932489657, '1999-07-13', 'Caroline Amber');


-- Insert data into works table

--works in warehouse
INSERT INTO works (address, ssn, name) VALUES ('123 Main St', 123456789, 'Sales');
INSERT INTO works (address, ssn, name) VALUES ('234 Cedar Drive St', 234567890, 'Sales');

--works in warehouse and office
INSERT INTO works (address, ssn, name) VALUES ('456 Elm St', 345678901, 'Marketing');
INSERT INTO works (address, ssn, name) VALUES ('111 Pine St', 345678901, 'Finances');

INSERT INTO works (address, ssn, name) VALUES ('345 Walnut Lane', 456789012, 'Engineering');
INSERT INTO works (address, ssn, name) VALUES ('222 Market St', 456789012, 'Marketing');

--works in office
INSERT INTO works (address, ssn, name) VALUES ('333 Battery St', 567890123, 'Engineering');
INSERT INTO works (address, ssn, name) VALUES ('444 5th Ave', 678901234, 'Marketing');

--works in the same as bob (345678901)
INSERT INTO works (address, ssn, name) VALUES ('456 Elm St', 789012345, 'Finances');
INSERT INTO works (address, ssn, name) VALUES ('111 Pine St', 789012345, 'Marketing');

--Insert data into customer table

--Customer that made orders in 2022

    --with product price inferior to 50$
INSERT INTO customer (cust_no, name, email, phone, address) VALUES (1, 'Alice Smith', 'alice@example.com', 1234567890, 'Home1');

    --with product price equal to 50$
INSERT INTO customer (cust_no, name, email, phone, address) VALUES (2, 'Bob Johnson', 'bob@example.com', 2345678901, 'Home2');

    --with product price superior to 50$
INSERT INTO customer (cust_no, name, email, phone, address) VALUES (3, 'Charlie Brown', 'charlie@example.com', 3456789012, 'Home3');

--Customer that made orders in 2023
    --with product price inferior to 50$
INSERT INTO customer (cust_no, name, email, phone, address) VALUES (4, 'David Lee', 'david@example.com', 4567890123, 'Home4');

    --with product price equal to 50$
INSERT INTO customer (cust_no, name, email, phone, address) VALUES (5, 'Emily Kim', 'emily@example.com', 5678901234, 'Home5');

    --with product price superior to 50$
INSERT INTO customer (cust_no, name, email, phone, address) VALUES (6, 'James Bond', 'james@example.com', 6789012345, 'Home6');
INSERT INTO customer (cust_no, name, email, phone, address) VALUES (7, 'Gustavo Rodriguez', 'gustavo@example.com', 7890123456, 'Home7');

--with no orders
INSERT INTO customer (cust_no, name, email, phone, address) VALUES (8, 'Tiago Santos', 'tiago@example.com', 8901234567, 'Home8');

-- Insert data into order_ table

--order in 2022
    --price inferior to 50
INSERT INTO order_ (order_no, date, placed_by_cust_no) VALUES (1, '2022-01-01', 1);
INSERT INTO order_ (order_no, date, placed_by_cust_no) VALUES (2, '2022-01-02', 1);

    --price equal to 50
INSERT INTO order_ (order_no, date, placed_by_cust_no) VALUES (3, '2022-01-03', 2);
INSERT INTO order_ (order_no, date, placed_by_cust_no) VALUES (4, '2022-01-04', 2);

    --price superior to 50
INSERT INTO order_ (order_no, date, placed_by_cust_no) VALUES (5, '2022-01-05', 3);
INSERT INTO order_ (order_no, date, placed_by_cust_no) VALUES (6, '2022-01-06', 3);

--orders in 2023

    --price inferior to 50
INSERT INTO order_ (order_no, date, placed_by_cust_no) VALUES (7, '2023-01-07', 4);
INSERT INTO order_ (order_no, date, placed_by_cust_no) VALUES (8, '2023-01-08', 4);

    --price equal to 50
INSERT INTO order_ (order_no, date, placed_by_cust_no) VALUES (9, '2023-01-09', 5);
INSERT INTO order_ (order_no, date, placed_by_cust_no) VALUES (10, '2023-01-10', 5);

    --price superior to 50
INSERT INTO order_ (order_no, date, placed_by_cust_no) VALUES (11, '2023-01-11', 6);
INSERT INTO order_ (order_no, date, placed_by_cust_no) VALUES (12, '2023-01-12', 6);

INSERT INTO order_ (order_no, date, placed_by_cust_no) VALUES (13, '2023-01-13', 7);
INSERT INTO order_ (order_no, date, placed_by_cust_no) VALUES (14, '2023-01-14', 7);

-- Insert data into process table
--only first per client of each order becomes sale
INSERT INTO process (ssn, order_no) VALUES (123456789, 1);--2022
INSERT INTO process (ssn, order_no) VALUES (234567890, 7);--2023
INSERT INTO process (ssn, order_no) VALUES (345678901, 3);--2022
INSERT INTO process (ssn, order_no) VALUES (456789012, 9);--2023
INSERT INTO process (ssn, order_no) VALUES (567890123, 5);--2022
INSERT INTO process (ssn, order_no) VALUES (678901234, 11);--2023
INSERT INTO process (ssn, order_no) VALUES (678901234, 13);--2023


-- Insert data into sale table
INSERT INTO sale (order_no) VALUES (1);
INSERT INTO sale (order_no) VALUES (3);
INSERT INTO sale (order_no) VALUES (5);
INSERT INTO sale (order_no) VALUES (7);
INSERT INTO sale (order_no) VALUES (9);
INSERT INTO sale (order_no) VALUES (11);
INSERT INTO sale (order_no) VALUES (13);


-- Insert data into pay table
INSERT INTO pay (cust_no, order_no) VALUES (1, 1);
INSERT INTO pay (cust_no, order_no) VALUES (2, 3);
INSERT INTO pay (cust_no, order_no) VALUES (3, 5);
INSERT INTO pay (cust_no, order_no) VALUES (4, 7);
INSERT INTO pay (cust_no, order_no) VALUES (5, 9);
INSERT INTO pay (cust_no, order_no) VALUES (6, 11);
INSERT INTO pay (cust_no, order_no) VALUES (7, 13);


-- Insert data into product table
INSERT INTO product (sku, name, description, price) VALUES ('SKU001', 'Product 1', 'Description 1', 10.00);
INSERT INTO product (sku, name, description, price) VALUES ('SKU002', 'Product 2', 'Description 2', 20.00);
INSERT INTO product (sku, name, description, price) VALUES ('SKU003', 'Product 3', 'Description 3', 30.00);
INSERT INTO product (sku, name, description, price) VALUES ('SKU004', 'Product 4', 'Description 4', 40.00);
INSERT INTO product (sku, name, description, price) VALUES ('SKU005', 'Product 5', 'Description 5', 50.00);
INSERT INTO product (sku, name, description, price) VALUES ('SKU006', 'Product 6', 'Description 6', 60.00);
INSERT INTO product (sku, name, description, price) VALUES ('SKU007', 'Product 7', 'Description 7', 70.00);
INSERT INTO product (sku, name, description, price) VALUES ('SKU008', 'Product 8', 'Description 8', 80.00);
INSERT INTO product (sku, name, description, price) VALUES ('SKU009', 'Product 9', 'Description 9', 90.00);

--not used
INSERT INTO product (sku, name, description, price) VALUES ('SKU010', 'Product 10', 'Description 10', 100.00);
INSERT INTO product (sku, name, description, price) VALUES ('SKU011', 'Product 11', 'Description 11', 110.00);
INSERT INTO product (sku, name, description, price) VALUES ('SKU012', 'Product 12', 'Description 12', 120.00);
INSERT INTO product (sku, name, description, price) VALUES ('SKU013', 'Product 13', 'Description 13', 130.00);
INSERT INTO product (sku, name, description, price) VALUES ('SKU014', 'Product 14', 'Description 14', 140.00);
INSERT INTO product (sku, name, description, price) VALUES ('SKU015', 'Product 15', 'Description 15', 150.00);
INSERT INTO product (sku, name, description, price) VALUES ('SKU016', 'Product 16', 'Description 16', 160.00);
INSERT INTO product (sku, name, description, price) VALUES ('SKU017', 'Product 17', 'Description 17', 170.00);
INSERT INTO product (sku, name, description, price) VALUES ('SKU018', 'Product 18', 'Description 18', 180.00);
INSERT INTO product (sku, name, description, price) VALUES ('SKU019', 'Product 19', 'Description 19', 190.00);

-- Insert data into ean_product table
INSERT INTO ean_product (sku, ean) VALUES ('SKU001', 1234567890123);
INSERT INTO ean_product (sku, ean) VALUES ('SKU004', 1234567890124);
INSERT INTO ean_product (sku, ean) VALUES ('SKU005', 1234567890125);
INSERT INTO ean_product (sku, ean) VALUES ('SKU006', 1234567890126);
INSERT INTO ean_product (sku, ean) VALUES ('SKU007', 1234567890127);
INSERT INTO ean_product (sku, ean) VALUES ('SKU008', 1234567890128);
INSERT INTO ean_product (sku, ean) VALUES ('SKU009', 1234567890129);
INSERT INTO ean_product (sku, ean) VALUES ('SKU010', 1234567890130);
INSERT INTO ean_product (sku, ean) VALUES ('SKU011', 1234567890131);
INSERT INTO ean_product (sku, ean) VALUES ('SKU012', 1234567890132);
INSERT INTO ean_product (sku, ean) VALUES ('SKU013', 1234567890133);
INSERT INTO ean_product (sku, ean) VALUES ('SKU014', 1234567890134);
INSERT INTO ean_product (sku, ean) VALUES ('SKU015', 1234567890135);


-- Insert data into contains table
--BIGGEST QUANTITY is 10 and there is 2 products SKU005 and SKU009

    --product price inferior to 50
INSERT INTO contains (order_no, sku, qty) VALUES (1, 'SKU001', 1);
INSERT INTO contains (order_no, sku, qty) VALUES (2, 'SKU002', 2);

INSERT INTO contains (order_no, sku, qty) VALUES (7, 'SKU001', 1);
INSERT INTO contains (order_no, sku, qty) VALUES (7, 'SKU002', 2);
INSERT INTO contains (order_no, sku, qty) VALUES (7, 'SKU003', 1);
INSERT INTO contains (order_no, sku, qty) VALUES (8, 'SKU004', 3);
INSERT INTO contains (order_no, sku, qty) VALUES (8, 'SKU003', 2);
INSERT INTO contains (order_no, sku, qty) VALUES (8, 'SKU002', 1);

    --product price equal to 50
INSERT INTO contains (order_no, sku, qty) VALUES (3, 'SKU005', 10);
INSERT INTO contains (order_no, sku, qty) VALUES (3, 'SKU002', 5);

INSERT INTO contains (order_no, sku, qty) VALUES (4, 'SKU004', 7);
INSERT INTO contains (order_no, sku, qty) VALUES (4, 'SKU005', 1);

INSERT INTO contains (order_no, sku, qty) VALUES (9, 'SKU003', 1);
INSERT INTO contains (order_no, sku, qty) VALUES (9, 'SKU005', 1);

INSERT INTO contains (order_no, sku, qty) VALUES (10, 'SKU004', 5);
INSERT INTO contains (order_no, sku, qty) VALUES (10, 'SKU005', 5);



    --product price superior to 50
INSERT INTO contains (order_no, sku, qty) VALUES (5, 'SKU006', 1);
INSERT INTO contains (order_no, sku, qty) VALUES (5, 'SKU009', 10);

INSERT INTO contains (order_no, sku, qty) VALUES (6, 'SKU007', 3);
INSERT INTO contains (order_no, sku, qty) VALUES (6, 'SKU008', 6);

INSERT INTO contains (order_no, sku, qty) VALUES (11, 'SKU001', 1);
INSERT INTO contains (order_no, sku, qty) VALUES (11, 'SKU004', 1);
INSERT INTO contains (order_no, sku, qty) VALUES (11, 'SKU009', 1);

INSERT INTO contains (order_no, sku, qty) VALUES (12, 'SKU008', 4);

INSERT INTO contains (order_no, sku, qty) VALUES (13, 'SKU006', 2);

INSERT INTO contains (order_no, sku, qty) VALUES (14, 'SKU007', 7);



-- Insert data into supplier table
INSERT INTO supplier (TIN, name, address, supply_contract_sku, date) VALUES (987654321, 'Supplier 1', '123 Main St', 'SKU001', '2021-01-01');
INSERT INTO supplier (TIN, name, address, supply_contract_sku, date) VALUES (876543210, 'Supplier 2', '456 Elm St', 'SKU002', '2021-02-02');
INSERT INTO supplier (TIN, name, address, supply_contract_sku, date) VALUES (765432109, 'Supplier 3', '789 Oak St', 'SKU003', '2021-03-03');
INSERT INTO supplier (TIN, name, address, supply_contract_sku, date) VALUES (109876543, 'Supplier 9', '444 5th Ave', 'SKU013', '2021-09-09');
INSERT INTO supplier (TIN, name, address, supply_contract_sku, date) VALUES (938954321, 'Supplier 10', '777 Broadway', 'SKU014', '2021-10-10');
INSERT INTO supplier (TIN, name, address, supply_contract_sku, date) VALUES (896543530, 'Supplier 11', '123 Main St', 'SKU015', '2021-11-11');
INSERT INTO supplier (TIN, name, address, supply_contract_sku, date) VALUES (776452109, 'Supplier 12', '456 Elm St', 'SKU016', '2021-12-12');
INSERT INTO supplier (TIN, name, address, supply_contract_sku, date) VALUES (654321098, 'Supplier 13', '789 Oak St', 'SKU017', '2022-01-01');
INSERT INTO supplier (TIN, name, address, supply_contract_sku, date) VALUES (543210987, 'Supplier 14', '444 5th Ave', 'SKU018', '2022-02-02');
INSERT INTO supplier (TIN, name, address, supply_contract_sku, date) VALUES (432109876, 'Supplier 15', '777 Broadway', 'SKU019', '2022-03-03');

-- Insert data into delivery table
INSERT INTO delivery (TIN, address) VALUES (987654321, '123 Main St');
INSERT INTO delivery (TIN, address) VALUES (876543210, '234 Cedar Drive St');
INSERT INTO delivery (TIN, address) VALUES (987654321, '345 Walnut Lane');
INSERT INTO delivery (TIN, address) VALUES (876543210, '123 Main St');
INSERT INTO delivery (TIN, address) VALUES (765432109, '456 Elm St');
INSERT INTO delivery (TIN, address) VALUES (654321098, '456 Elm St');


--

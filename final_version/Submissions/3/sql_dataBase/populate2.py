from datetime import date, timedelta
import random

numbers_of_customers = 1000

number_of_products = 1000

number_of_employees = 100

number_of_orders = 10000

number_of_orders_per_customer = 28

number_of_dates_per_order = 10

number_of_payments_per_customer = 5

number_of_products_per_order = 2

number_of_suppliers = 100

number_of_workplaces = 90

city = ["Lisboa", "Porto", "Faro", "Coimbra", "Braga", "Aveiro", "Evora", "Funchal", "Gimaraes", "Vila Nova de Gaia"]

print("\t--customers")
for i in range(numbers_of_customers):
    print("INSERT INTO customer (name, email, phone, address, cust_no) VALUES ({}, {}, {}, {}, {});".format("\'cust_name_" + str(i) + "\'", "\'cust_email_" + str(i) +"@gmail.com\'", str(i), "\'watever_street_" + str(i) + " 1234-123 " + city[i % 10] + "\'", i))

print("\t--products")
counter = 0
for i in range(number_of_products):
    if (counter == 26):
        counter = 0
    if (i == 0):
        print("INSERT INTO product (name, description, price, ean, sku) VALUES ({}, {}, 1, {}, {});".format("\'A_Product_name_" + str(i) + "\'", "\'Description for product" + str(i) + "\'", 100000000 + i, "\'" + str(i) + "\'"))
    else:
        print("INSERT INTO product (name, description, price, ean, sku) VALUES ({}, {}, {}, {}, {});".format("\'" + chr(65 + counter) + "_Product_name_" + str(i) + "\'", "\'Description for product" + str(i) + "\'", i* 2, 100000000 + i, "\'" + str(i) + "\'"))
    counter += 1

counter = 0
customer_id = 0 
date_counter = 0
date_ = date(2022, 1, 1)

print()
print("\t--orders, payments and contains")
print("--customer_0")
print("--date 2022/1/1")
for i in range(number_of_orders):
    if (counter == number_of_orders_per_customer):
        customer_id += 1
        counter = 0
        print("--customer_" + str(customer_id))
        
    if (date_counter == number_of_dates_per_order):
        date_counter = 0
        date_ = date_ + timedelta(days=1)
        print("--date ",date_)
    
    counter += 1
    date_counter += 1

    increment = number_of_products / number_of_products_per_order
    start_interval = 0

    """
    for j in range(number_of_products_per_order):
        random_product = random.randint(start_interval,start_interval + increment)
        random_qty = random.randint(1,10)

        if (j == 0):
            print("START TRANSACTION;")
            print("SET CONSTRAINTS ALL DEFERRED;")
            print("INSERT INTO \"order\" (cust_no, date, order_no) VALUES ({}, {}, {});".format(customer_id, "\'" + date_.strftime("%Y/%m/%d") + "\'", i))
            print("INSERT INTO contains (order_no, sku, qty) VALUES ({}, {}, {});".format(i, "\'" + str(random_product) + "\'", random_qty))
            print("COMMIT;")
        else:
            print("INSERT INTO contains (order_no, sku, qty) VALUES ({}, {}, {});".format(i, "\'" + str(random_product) + "\'", random_qty))
        
        start_interval += increment
    """
    if (i < 0.99 * number_of_orders):
        print("START TRANSACTION;")
        print("SET CONSTRAINTS ALL DEFERRED;")
        print("INSERT INTO \"order\" (cust_no, date, order_no) VALUES ({}, {}, {});".format(customer_id, "\'" + date_.strftime("%Y/%m/%d") + "\'", i))
        print("INSERT INTO contains (order_no, sku, qty) VALUES ({}, {}, {});".format(i, "\'" + str(1) + "\'", 1))
        print("INSERT INTO contains (order_no, sku, qty) VALUES ({}, {}, {});".format(i, "\'" + str(2) + "\'", 1))
        print("COMMIT;")
    else:
        print("START TRANSACTION;")
        print("SET CONSTRAINTS ALL DEFERRED;")
        print("INSERT INTO \"order\" (cust_no, date, order_no) VALUES ({}, {}, {});".format(customer_id, "\'" + date_.strftime("%Y/%m/%d") + "\'", i))
        print("INSERT INTO contains (order_no, sku, qty) VALUES ({}, {}, {});".format(i, "\'" + str(98) + "\'", 1))
        print("INSERT INTO contains (order_no, sku, qty) VALUES ({}, {}, {});".format(i, "\'" + str(99) + "\'", 1))
        print("COMMIT;")

    if counter <= 5:
        print("INSERT INTO pay (cust_no, order_no) VALUES ({}, {});".format(customer_id, i))

print("\t--supplier")
counter = 0
supplier_id = 0
for i in range(number_of_suppliers):
    print("INSERT INTO supplier (name, address, sku, date, tin) VALUES ({}, {}, {}, {}, {});".format("\'supplier_" + str(i) + "\'", "\'supplier_address_" + str(i) + " \'", i, "\'2022/01/01\'", i))

print("\t--employee")
bdate = date(2000, 1, 1)
for i in range(number_of_employees):
    print("INSERT INTO employee (ssn, tin, bdate, name) VALUES ({}, {}, {}, {});".format(i, 364 + i, "\'" + bdate.strftime("%Y/%m/%d") + "\'", "\'employee_" + str(i) + "\'"))
    bdate = bdate + timedelta(days=1)

departments = [
    "\'Recursos Humanos\'",
    "\'Financas\'",
    "\'Marketing\'",
    "\'Vendas\'",
    "\'Desenvolvimento de Produto\'",
    "\'Atendimento ao Cliente\'",
    "\'Logistica\'",
    "\'TI (Tecnologia da Informacao)\'",
    "\'Operacoes\'",
    "\'Pesquisa e Desenvolvimento\'"
]
print("\t--departments")
for i in departments:
    print("INSERT INTO department (name) VALUES ({});".format(i))

print("\t--workplace, office, warehouse")
workplace_especialization = ["warehouse","office"]
for i in range(90):
    print("START TRANSACTION;")
    print("SET CONSTRAINTS ALL DEFERRED;")
    print("INSERT INTO workplace (address, lat, long) VALUES ({}, {}, {});".format("\'workplace_" + str(i) + "\'", i, i*2))
    print("INSERT INTO ",workplace_especialization[i%2]," (address) VALUES ({});".format("\'workplace_" + str(i) + "\'"))
    print("COMMIT;")

print("\t--delivery")
for i in range(number_of_workplaces):
    if (i < 45):
        print("INSERT INTO delivery (address, tin) VALUES ({}, {});".format("\'workplace_" + str(i*2) + "\'", i))
    elif (i < 90):
        print("INSERT INTO delivery (address, tin) VALUES ({}, {});".format("\'workplace_" + str((i - 45)*2) + "\'", i))
    else:
        print("INSERT INTO delivery (address, tin) VALUES ({}, {});".format("\'workplace_" + str((i - 90)*2) + "\'", i))

print("\t--works")
for i in range(number_of_employees):
    if (i < 90):
        print("INSERT INTO works (ssn, name, address) VALUES ({}, {}, {});".format(i, departments[i%10], "\'workplace_" + str(i) + "\'"))
    else:
        print("INSERT INTO works (ssn, name, address) VALUES ({}, {}, {});".format(i, departments[i%10], "\'workplace_" + str(i - 90) + "\'"))
    
print("\t--process")
print("--employee 0 and 1 processe all days")
print("--employee 2 processes all but 2022/12/31")
print("--employee 3 processes all but 2022/12/31 and 2022/12/30")
print("--employee 4 processes all but 31,30 and 29")
for i in range(365):
    print("INSERT INTO process (ssn, order_no) VALUES (0, {});".format(i * 10))
    print("INSERT INTO process (ssn, order_no) VALUES (1, {});".format(i* 10 + 1))
    if (i != 364):
        print("INSERT INTO process (ssn, order_no) VALUES (2, {});".format(10 * i + 2))
    if (i != 363):
        print("INSERT INTO process (ssn, order_no) VALUES (3, {});".format(10 * i + 3))
    if (i != 362):
        print("INSERT INTO process (ssn, order_no) VALUES (4, {});".format(10 * i + 4))

#!/usr/bin/python3

import psycopg2, cgi
import login

print("Content-Type: text/html\n\n")

print("<html>")
print("<head>")
print("<title>My Web Page</title>")
print(
    "<link href='https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css' rel='stylesheet' integrity='sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM' crossorigin='anonymous' />"
)
print("<link rel='stylesheet' href='./styles2.css' />")
print("</head>")
print("<body>")
print("<div class='sidebar'>")
print("      <a href='Home.html'>Home</a>")
print("      <a href='ManageProducts.html'>Products</a>")
print("      <a href='ManageSuppliers.html'>Suppliers</a>")
print("      <a href='ManageCustomers.html' class='white-link'>Customers</a>")
print("    </div>")
print("    <div class='content'>")

form = cgi.FieldStorage()

product_sku = form.getvalue("product_sku")
product_name = form.getvalue("product_name")
product_price = form.getvalue("product_price")
product_ean = form.getvalue("product_ean")
product_description = form.getvalue("product_description")

supplier_tin = form.getvalue("supplier_tin")
supplier_name = form.getvalue("supplier_name")
supplier_address = form.getvalue("supplier_address")
supplier_sku = form.getvalue("supplier_sku")
supplier_date = form.getvalue("supplier_date")


connection = None
try:
    # connect to the database
    connection = psycopg2.connect(login.credentials)
    cursor = connection.cursor()

    add_product = (
        "INSERT INTO product "
        "(sku, name, description, price, ean) "
        "VALUES (%(sku)s, %(name)s, %(description)s, %(price)s, %(ean)s)"
    )

    data_product = {
        "sku": product_sku,
        "name": product_name,
        "description": product_description,
        "ean": product_ean,
        "price": product_price,
    }

    add_supplier = """
        INSERT INTO supplier
        (tin, name, address, sku, date)
        VALUES (%(tin)s, %(name)s, %(address)s, %(sku)s, %(date)s)
        """

    data_supplier = {
        "tin": supplier_tin,
        "name": supplier_name,
        "address": supplier_address,
        "sku": supplier_sku,
        "date": supplier_date,
    }

    # Insert new product
    cursor.execute(add_product, data_product)

    # Insert new supplier
    cursor.execute(add_supplier, data_supplier)

    # commit the changes
    connection.commit()

    cursor.close()
    print("<h1>Product Added!</h1>")
except Exception as e:
    # Print errors on the webpage if they occur
    print("<h1>An error occurred.</h1>")
    print("<p>{}</p>".format(e))
finally:
    if connection is not None:
        connection.close()

print("<div>")
print("  </body>")
print("</html>")
